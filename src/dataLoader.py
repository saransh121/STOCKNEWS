from langchain_community.document_loaders import WhatsAppChatLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os

class dataLoad():
    def __init__(self):
        chart_path_text = os.getenv('chart_path')

        print(chart_path_text)
        loader = WhatsAppChatLoader(chart_path_text)
        data = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=250, chunk_overlap=0
        )
        self.embbading_fucn = HuggingFaceEmbeddings()
        self.splitted_doc = splitter.split_documents(data)
    def getVectorStor(self):
        print("into vectorization")
        vectorstore = Chroma.from_documents(documents=self.splitted_doc, 
                                            embedding=self.embbading_fucn,
                                            persist_directory="./chroma_db")
        return vectorstore
    def __len__(self):
        return len(self.splitted_doc)

