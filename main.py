import os
import argparse
from dotenv import load_dotenv
from google.genai import Client, types

from prompts import system_prompt


def main():
    load_dotenv()

    ## argparse variables
    parser = argparse.ArgumentParser(prog="Agentic Dev", description="Toy Agent from Boot.Dev module")
    # parser.add_help = True
    parser.add_argument("user_prompt", type=str, help="The prompt to be passed to the LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    ## gemini api variables
    api_key: str = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("please provide a valid gemini api key in .env")

    client = Client(api_key=api_key)
    model: str = "gemini-2.5-flash"
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    config = types.GenerateContentConfig(system_instruction=system_prompt, temperature=0)

    if messages is not None:
        response = client.models.generate_content(model=model, contents=messages, config=config)
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)


if __name__ == "__main__":
    main()


