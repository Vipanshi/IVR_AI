from langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_llm_response(user_text: str) -> str:

    llm = ChatOpenAI(model="gpt-4.1-nano-2025-04-14", temperature=0.2)

    prompt = PromptTemplate(
    template="""You are a helpfull assistant of online food delivery company.
    Answer question humbly and try to use provided information regarding status of the order.

    {context}
    {question}
    """,
    input_variables=["context", "question"]
    )

    context_text="order id: 1234567890, status: out for delivery, rider name: Nacho, rider number: 1234567890, Order created At date:June 2 2025 12:00pm, Order estimated delivery date: June 2 2025 1:30pm, initial delivery time: 30 minutes"
    final_prompt = prompt.invoke({"context":context_text, "question": "I haven't received my order yet."})
    response_text=llm.invoke(final_prompt)
    print(response_text.content)
    
    return response_text.content
  
