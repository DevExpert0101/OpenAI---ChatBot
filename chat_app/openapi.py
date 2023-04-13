import os
import openai
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

def chatResponse(text):
    try: 
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt='''The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: {} '''.format(text),
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:"]
        )
        
        text1 = response['choices'][0]['text']
        if text1[1:3]=="AI":
            return text1[5:]
        return text1
    except Exception as e:
        return f"Error {e}"