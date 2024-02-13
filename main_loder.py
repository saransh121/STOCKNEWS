from src.dataLoader import dataLoad
dataLoad_ = dataLoad()

if __name__ == '__main__':
    dataLoad_.getVectorStor()
    print("vector data loaded successfully")