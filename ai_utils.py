# ai_utils.py
import openai
import os

# Use environment variable for security
openai.api_key = os.getenv("OPENAI_API_KEY")

def transform_text(text, universe):
    prompt = f"Rewrite the following text in the style of a {universe}:\n\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content
