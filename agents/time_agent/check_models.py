from google import genai
import os

try:
    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
    found = False
    print("Searching for Gemma models...")
    for m in client.models.list():
        if "gemma" in m.name.lower():
            print(f"Found: {m.name}")
            found = True
    if not found:
        print("No 'gemma' models found in list_models().")
        print("First 5 models for reference:")
        for i, m in enumerate(client.models.list()):
            if i < 5: print(m.name)
except Exception as e:
    print(f"Error: {e}")
