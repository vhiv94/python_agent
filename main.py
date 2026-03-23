import os
import argparse
from dotenv import load_dotenv
# from functools import reduce
from google.genai import Client, types

from prompts import system_prompt
from call_function import call_function, available_functions


def main():
    load_dotenv()

    ## argparse variables
    parser = argparse.ArgumentParser(prog="Agentic Dev", description="Toy Agent from Boot.Dev module")
    parser.add_argument("user_prompt", type=str, help="The prompt to be passed to the LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    # parser.add_help = True
    args = parser.parse_args()

    ## gemini api variables
    api_key: str = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("please provide a valid gemini api key in .env")
    client = Client(api_key=api_key)
    model: str = "gemini-2.5-flash"

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    config = types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0)

    if messages is not None:
        response = client.models.generate_content(model=model, contents=messages, config=config)

        ## print the response to the console
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        if response.function_calls:
            # print(reduce(lambda acc, call: f"{acc}\nCalling function: {call.name}({call.args})", response.function_calls, ""))
            # function_call_results: list[types.Content] = list(map(lambda call: call_function(call, args.verbose), response.function_calls))
            function_response_list: list[str] = []
            for function in response.function_calls:
                result: types.Content = call_function(function, args.verbose)
                if not result.parts:
                    raise Exception(f'Error: function call "{function.name}": resulting Content.parts is empty')
                if not result.parts[0].function_response:
                    raise Exception(f'Error: function call "{function.name}": resulting Content.parts.function_response is empty')
                if not result.parts[0].function_response.response:
                    raise Exception(f'Error: function call "{function.name}": resulting Content.parts.function_response.response is empty')
                if args.verbose:
                    print(f'{function.name} -> {result.parts[0].function_response.response}') 
                function_response_list.append(result.parts[0].function_response.response)

        else:
            print(response.text)


if __name__ == "__main__":
    main()


