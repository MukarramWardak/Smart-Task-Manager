import os
from openai import OpenAI
import yaml

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def load_config(file_path):
    with open(file_path,'r') as file:
        return yaml.safe_load(file)

config=load_config('config.yaml')
tools=config['openai_tool']

def generate_category(title: str, description: str):
    tool1_user_message = tools["tool1"]["messages"][1]["content"].format(title=title, description=description)
    response = client.chat.completions.create(
        model=tools["tool1"]["model"],
    messages=[
        {"role": "system", "content": tools["tool1"]["messages"][0]["content"]},
        {"role": "user", "content": tool1_user_message}
    ],
    temperature=tools["tool1"]["temperature"],
    max_tokens=tools["tool1"]["max_tokens"]
    )
    answer = response.choices[0].message.content.strip()
    category = answer.replace("Category: ", "").strip()
    return category

def generate_summary(description):
    response = client.chat.completions.create(
        model=tools["tool2"]["model"],
    messages=[
        {"role": "system", "content": tools["tool2"]["messages"][0]["content"]},
        {"role": "user", "content": description}
    ],
    temperature=tools["tool2"]["temperature"],
    max_tokens=tools["tool2"]["max_tokens"]
    )
    summary = response.choices[0].message.content.strip()
    return summary