from langchain_community.llms import HuggingFaceHub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os

chart_path_text = os.getenv('chart_path')

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv('HUGGINGFACEHUB_API_TOKEN')

def get_response(vectorstore,que: str) : 
    retriever = vectorstore.as_retriever()
    llm = HuggingFaceHub(
        repo_id=os.getenv('model_name'), 
        model_kwargs={"temperature": 0.5, "max_length": 64,"max_new_tokens":512}
    )

    from langchain_core.prompts import PromptTemplate

    template = """Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Use three sentences maximum and keep the answer as concise as possible.

    {context}

    Question: {question}

    Helpful Answer:"""
    custom_rag_prompt = PromptTemplate.from_template(template)
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | custom_rag_prompt
        | llm
        | StrOutputParser()
    )
    details = []
    for chunk in rag_chain.stream(que):
        details.append(chunk)
    return details[0]
