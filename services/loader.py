from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
# code for implementing recursive text splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter



loader = DirectoryLoader(path="Contract/",glob="**/*.pdf",loader_cls=PyPDFLoader)
documents = loader.load()
#print(documents)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200, 
    chunk_overlap=20,) 

splitted_documents = text_splitter.split_documents(documents)
print(splitted_documents)






