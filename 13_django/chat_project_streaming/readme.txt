uv pip install django 
uv pip install python-dotenv langchain langchain-openai

python manage.py makemigrations
python manage.py migrate

langchain - .env 파일을 root 아래 복사

python manage.py runserver

http://127.0.0.1:8000/chat

디렉토리 구조
- chatbot_project: 프로젝트 설정파일 디렉토리
- chat: App