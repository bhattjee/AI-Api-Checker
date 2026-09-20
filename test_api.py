import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()

try:
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # Use current model
    model_name = 'gemini-pro-latest'
    response = client.models.generate_content(
        model=model_name,
        contents="Hello, how are you?"
    )
    print("Response:", response.text)
    print("Success! API is working.")
    
except Exception as e:
    print(f"Error: {e}")
    print("\nTrying to list available models...")
    
    try:
        for m in client.models.list():
            print(f"Available model: {m.name}")
    except Exception as list_error:
        print(f"Cannot list models: {list_error}")
        print("Please check your API key in the .env file")