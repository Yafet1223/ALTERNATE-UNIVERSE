from openai import OpenAI
import os

# Option 1: Use Groq (FREE alternative - get API key from https://console.groq.com/)
# Option 2: Use OpenAI (requires paid credits)
# Option 3: Use Hugging Face (FREE - get API key from https://huggingface.co/settings/tokens)

# Choose which service to use
USE_GROQ = True  # Set to False to use OpenAI instead

# if USE_GROQ:
#     # Groq API (FREE - sign up at https://console.groq.com/)
#     API_KEY = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE")
    
#     if API_KEY == "YOUR_GROQ_API_KEY_HERE":
#         print("\n⚠️  Please set your Groq API key!")
#         print("1. Get a FREE API key at: https://console.groq.com/")
#         print("2. Set it as an environment variable:")
#         print("   PowerShell: $env:GROQ_API_KEY='your-key-here'")
#         print("   Or replace 'YOUR_GROQ_API_KEY_HERE' in this file with your actual key")
#         print("\nExiting...")
#         exit(1)
    
#     BASE_URL = "https://api.groq.com/openai/v1"
#     MODEL = "llama-3.1-8b-instant"  # Free model on Groq
#     client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
#     print("✅ Using Groq (FREE) - Model: llama-3.1-8b-instant\n")
# else:
#     # OpenAI API (requires paid credits)
#     API_KEY = ""
#     MODEL = "gpt-3.5-turbo"
#     client = OpenAI(api_key=API_KEY)

# def chat_with_gpt(prompt):
#     try:
#         response = client.chat.completions.create(
#             model=MODEL,
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"Error: {str(e)}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
