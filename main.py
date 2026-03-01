import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-course!")
    print(f"Your OPENAI_API_KEY is: {os.getenv('OPENAI_API_KEY')}")
    print(f"Your GOOGLE_API_KEY is: {os.getenv('GOOGLE_API_KEY')}")


if __name__ == "__main__":
    main()
