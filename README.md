# day2

## ENVIRONMENT SETUP

## 建立文件 touch/mkdir
>touch ....
>touch file.py
>mkdir folder

## create virtual environment
1. create virtual environment
>python -m venv .venv
2. make sure the .venv file was created, active virtual environment
>source .venv/bin/activate

## install independencies / python libraries
1. create a requirements.txt file
2. add, each new line, open ai, streamlit, python-dotenv
3. run:
>pip install -r requirements.txt

## Step 3 create a .env file to store our secrets (including OpenAI API Key)
1. create .env file
>touch .env file
2. add the OPENAI_API_KEY to the .env file
email / openai plantform==>API key==>copy the key
>OPENAI_API_KEY = "xxxxxxxxxxxxx"

