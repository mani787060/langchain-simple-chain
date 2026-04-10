from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI  # use to print string as an output from the model's response. 


load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

parser = StrOutputParser()

# so using only one line we can create a chain that connects the prompt, model and parser together. This allows us to easily execute the entire process of generating a response from the model and extracting the desired information in a single step.
  
chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)


# we use this line to visualize the chain and understand how the data flows through the chain. It will show us the structure of the chain and how the different components are connected. This is especially useful when we have complex chains with multiple components, as it helps us to debug and optimize the chain effectively.
chain.get_graph().print_ascii()