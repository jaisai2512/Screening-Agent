from prompts import generate_question_prompt
from dotenv import load_dotenv
from groq import Groq
import os
import json
load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
class LlmAgent:
    def __init__(self):
        pass
    def question_generation(self,data):
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "assistant", "content":generate_question_prompt(data)},
                {"role":"assistant","content":''}
            ],
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""
        return response


