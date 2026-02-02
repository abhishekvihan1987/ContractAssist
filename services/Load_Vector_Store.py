from cred.Create_Embeddings import createEmbeddings
from services.loader import splitted_documents as chunks
from langchain_core.vectorstores import InMemoryVectorStore

embeddings = createEmbeddings()
# vectors = []
# #Create vectors from chunks
# texts=[str(chunk) for chunk in chunks]
# vector = embeddings.embed_documents(texts)
# vectors.append(vector)
# print(vectors)

# Create vector store
texts=[chunk.page_content for chunk in chunks]
vector_db=InMemoryVectorStore.from_texts(texts,embedding=embeddings)

#Create retreiver
retreiver = vector_db.as_retriever(search_kwargs={"k":3})

# Find sample result
result = retreiver.invoke("The rent shall be paid before which date of month ?")
final_result = "\n\n".join(doc.page_content for doc in result)
print(final_result)