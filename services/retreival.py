from services.Load_Vector_Store import retreiver

def get_retreived_document(user_query:str):
    result = retreiver.invoke(user_query)
    final_result = "\n\n".join(doc.page_content for doc in result)
    return final_result