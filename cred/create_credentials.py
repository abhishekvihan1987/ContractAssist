from google.oauth2 import service_account
from utils.config import settings
from google.cloud import storage
import os
from pathlib import Path
from langchain_google_vertexai import ChatVertexAI
import vertexai
from langchain_core.output_parsers import StrOutputParser
from langchain_google_vertexai import VertexAIEmbeddings






#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = settings.GCS_KEY_PATH


credentials = service_account.Credentials.from_service_account_file(settings.GCS_KEY_PATH,
scopes=["https://www.googleapis.com/auth/cloud-platform"])
 
 

storage_client = storage.Client(credentials=credentials)  

# Now you can use storage_client to interact with Google Cloud Storage
# buckets = list(storage_client.list_buckets())

# for bucket in buckets:
#     print(bucket.name)
# # List of all methods for the storage client
# # print(dir(storage_client)) 
# gcs_folder = "legaldocuments10"
# bucket123 = storage_client.bucket('legaldocuments10')
# # pdf_filepath = Path("C:\Users\hp\Downloads\contract.pdf")
# #object_path = f"{gcs_folder}/{pdf_filepath.name}"
# blob = bucket123.blob(object_path)
# blob.upload_from_filename(pdf_filepath)

def initVertexai():
    vertexai.init(project="erudite-creek-457304-p9", location="us-east1", credentials=credentials)   

def create_llm():
    llm = ChatVertexAI(model_name="models/gemini-2.0-flash", temperature=0.1,top_p=0.8,credentials=credentials, max_output_tokens=1024,top_k=40 )
    return llm
    
    
    # Example usage of the llm
    # chain = llm | StrOutputParser()
    # response = chain.invoke("write 100 word poem on vikings sieze of paris")
    # print(response)

# chunk1 = None
# chunks = llm.stream("write a short story of 50 words on London ?")
# for chunk in chunks:
#     print(chunk.text)



# for chunk in llm.stream("what is the colour of sky ?"):
#     chunk1=chunk if chunk1 is None else chunk1 + chunk
#     print(chunk1.text)
   





# crrate embeddings

#embeddings =  VertexAIEmbeddings(model_name="models/embedding-gecko-001", credentials=credentials)





