import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

## gemini api variables
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("please provide a valid gemini api key in .env")

client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"


def main():
    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(model=model, contents=prompt)
    print(response.text)


if __name__ == "__main__":
    main()


