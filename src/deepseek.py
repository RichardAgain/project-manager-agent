from openai import OpenAI
from .config import Config

def call_deepseek_api(prompt: str) -> str:
    client = OpenAI(api_key=Config.DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Eres un project manager experto en el tema"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    return response.choices[0].message.content