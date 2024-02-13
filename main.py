from src.utili import get_response
from src.dataLoader import dataLoad
import re
from langchain_community.vectorstores import Chroma

dl = dataLoad()
db3 = Chroma(persist_directory="./chroma_db", embedding_function=dl.embbading_fucn)

def main(que):
    response = get_response(db3,que)
    pattern = r"Question: (.*?)\n\n\s*Helpful Answer: (.*?)\n"

    # Using regex to find the first question and helpful answer
    match = re.search(pattern, response)

    # Extracting the first question and its helpful answer
    if match:
        first_question = match.group(1).strip()
        helpful_answer = match.group(2).strip()


        print("First Question:", first_question)
        print("Helpful Answer:", helpful_answer)
    else:
        print("No match found.")
        helpful_answer = response
        response.split()

    return helpful_answer


# if __name__ == '__main__':
#     print(main("What are Recent profit Margin of TCS?"))
