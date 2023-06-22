import os
from dotenv import load_dotenv

load_dotenv()

SUPER_JOB_APP_KEY = os.environ.get("SUPER_JOB_APP_KEY")[::]
PATH_TO_JSON_FILE = os.environ.get("PATH_TO_JSON_FILE")[::]