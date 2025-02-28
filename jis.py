from openai import OpenAI # type: ignore
from langchain_openai import ChatOpenAI  # type: ignore
from langchain_core.messages import HumanMessage, SystemMessage   # type: ignore

OPENAI_API_KEY = 'Your_api_key_here'

model = ChatOpenAI(model="gpt-4", api_key = OPENAI_API_KEY)

messages = [
    SystemMessage(content="you are an expert in assisting users as a job interview simulator."),
    HumanMessage(content="I am preparing for a job interview for role Machine Learning Engineer and I have an experience of around 2 years. Can you help me with some tips?"),
]

res = model.invoke(messages)

print(res.content)