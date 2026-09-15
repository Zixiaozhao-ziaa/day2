# day2

## DAY1 RECAP
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

## CREATE STREAMLIT APPLICATION
1. create python file entrypoint
>touch home.py
2. run streamlit web server
>streamlit run home.py

## saving code
1. On LHS of screen, go to "source control"
2. client to add files to the commit (i.e., stage changes)
3. Enter a commit message (anything)
4. click "Commit"
5. click "sync changes"
6. check GitHub repository to confirm

## THEORY
Zero Data Retention (零数据保留 / ZDR) —— 常见于 AI/API 服务的隐私设置,意思是服务商不会保存或记录你发送的数据,处理完就立刻删除,不会用来训练模型或留存日志。企业客户在意隐私合规时经常会要求这个。