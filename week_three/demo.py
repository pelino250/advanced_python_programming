import os
from dotenv import load_dotenv

# os.environ.get('DB_NAME')

load_dotenv()

print(os.environ.get('DB_NAME'))
