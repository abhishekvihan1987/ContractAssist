from langchain_google_vertexai import VertexAIEmbeddings
from cred.create_credentials import initVertexai,credentials
from utils.config import settings


def createEmbeddings():
    initVertexai()
    embeddings = VertexAIEmbeddings(model_name='text-embedding-005',
    project=settings.PROJECT_ID,
    location=settings.LOCATION,
    credentials=credentials)

    return embeddings


