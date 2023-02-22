import os
import dotenv

def set_env(body):
    try:
        dotenv.load_dotenv()
        dict = {}
        for field in body:
            dict[field] = os.getenv(field)
            return dict
    except Exception as e:
        print(f'Grrrr, undefined error: {e}')

if __name__ == "__main__":
    body = ['openai.api_key']
    print(set_env(body))