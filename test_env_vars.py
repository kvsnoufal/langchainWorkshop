from dotenv import load_dotenv

load_dotenv()
import os
print("SERPER_API_KEY")
print(os.environ.get("SERPER_API_KEY"))
print("OPENAI_API_KEY")
print(os.environ.get("OPENAI_API_KEY"))