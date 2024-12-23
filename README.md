# Smart-Task-Manager

Use terminal for all of the steps except 3

Step 1: Create a Virtual Environment
python -m venv venv

Step 2:
pip install -r requirements.txt

Step 3:
Create a .env file in the project root with the following variables
OPENAI_API_KEY=your_openai_api_key

step 4:
uvicorn main:app --reload
