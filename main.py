from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_ollama import ChatOllama




load_dotenv()


def main():
  information = """
  Vijaya Lakshmi kaja is a software craftmen With over eight years of experience in AI-related roles, I am currently a Prompt Engineer at Elevance Health, a company that provides data-driven solutions for cancer care. I hold a master's degree in computer engineering and multiple certifications in big data, automation, and spark.

My core competencies include natural language processing, text generation, and large language models. I develop and deploy generative AI models that produce insights on oncology data, helping clinicians and patients make better decisions and improve outcomes. Previously, I built and implemented a neural NER model for clinical trial design, drug design, and discovery at Natsoft, and contributed to a large language model project at IBM. I am passionate about creating positive impact in the world with AI, and I thrive in a fast-paced and challenging environment. """
  
  summary_template = """ given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them   """

  summary_prompt_template = PromptTemplate(
    input_variables=["information"],template=summary_template
  )
  llm = ChatOpenAI(model="gpt-5", temperature=0)
  #llm = ChatOllama(model="gemma3:270m",temperature=0)
  chain = summary_prompt_template | llm
  
  response = chain.invoke({"information": information})
  print(response.content)
  
    #print("Hello from langchain-practice!")
    #print(os.environ.get("ANTHROPIC_API_KEY"))


if __name__ == "__main__":
    main()
