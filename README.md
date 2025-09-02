# langchain-practice
This repository created for LangChain Practice 
1. Initialize the project with below command in terminal
       uv init
2. add requried libraries
langchain, python-dotenv, black, isort, langchain-openai, langchain-tavily

3. for below error

NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'.

uv pip install "urllib3 < 2.0>"


