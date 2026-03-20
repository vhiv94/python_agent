import os
import argparse
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()

    ## gemini api variables
    api_key: str = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("please provide a valid gemini api key in .env")

    client = genai.Client(api_key=api_key)
    model: str = "gemini-2.5-flash"

    ## argparse variables
    parser = argparse.ArgumentParser(prog="Agentic Dev", description="Toy Agent from Boot.Dev module")
    # parser.add_help = True
    parser.add_argument("user_prompt", type=str, help="The prompt to be passed to the LLM")
    args = parser.parse_args()

    prompt: str = args.user_prompt
    if prompt is not None:
        response = client.models.generate_content(model=model, contents=prompt)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)


if __name__ == "__main__":
    main()


