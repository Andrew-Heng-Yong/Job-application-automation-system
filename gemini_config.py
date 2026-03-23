from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
API_KEY = os.getenv("GEMINI_API_KEY")
#API_KEY = "api_key_here" #you can hardcode it to save setting eviroment variable everytime
MODEL_NAME = "gemini-2.5-flash-lite"
OUTPUT_DIR = BASE_DIR / "generated_cover_letters"