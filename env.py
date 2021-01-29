from dotenv import load_dotenv
import os
load_dotenv()
usr = os.getenv("username")
pswd = os.getenv("password")

print(f"User: {usr}\nPassword: {pswd}")
