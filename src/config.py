from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")