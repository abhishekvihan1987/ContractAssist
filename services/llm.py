from langchain_google_vertexai import ChatVertexAI
from utils.config import settings
from cred.create_credentials import initVertexai,credentials
from langchain_core.prompts import ChatPromptTemplate 
from services.retreival import get_retreived_document

#create LLM Instance
llm1 = ChatVertexAI(model_name="gemini-2.5-flash",project=settings.PROJECT_ID,
    location=settings.LOCATION,
    credentials=credentials)

#create Prompt Template

# Define a template with placeholders 
template = """ You are a highly accurate and helpful PDF Assistant.

Your role is to answer user questions ONLY using the information provided in the retrieved PDF content.
The PDF content will be passed to you as context.

Rules you must strictly follow:
1. Use only the provided PDF content to answer the question.
2. Do NOT use prior knowledge or make assumptions beyond the PDF.
3. If the answer is not present in the PDF, clearly say:
   "The requested information is not available in the provided document."
4. Be concise, clear, and factual.
5. Preserve the original meaning and terminology used in the PDF.
6. If relevant, mention section names, headings, or page numbers from the PDF.
7. If the question is ambiguous, ask for clarification based on the document context.

Output Guidelines:
- Provide a direct answer first.
- Use bullet points or numbered lists if it improves clarity.
- Do not hallucinate or add extra explanations.
- Do not repeat the question.

Context:
{retrieved_pdf_chunks}

User Question:
{user_query}
 """
# Create a PromptTemplate instance 
prompt = ChatPromptTemplate.from_template(template) 
#create chain
chain = prompt | llm1
# Format the prompt with actual input
user_query = "before which date of month the rent needs to be submitted"
retreived_document = get_retreived_document(user_query)
response = chain.invoke({"user_query":user_query,"retrieved_pdf_chunks":retreived_document})
print(response.content.strip())