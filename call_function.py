from google.genai import types
from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.write_file import write_file, schema_write_file
from functions.run_python_file import run_python_file, schema_run_python_file


function_map: dict[str, types.FunctionCall] = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file,
}

def call_function(function_call: types.FunctionCall, verbose: bool = False) -> types.Content:
    function_name: str = function_call.name or ""

    def get_result(res_or_err: str, response: str) -> types.Content:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={res_or_err: response}
                )
            ]
        )
    
    
    ## call the function
    print(f"Calling function: {function_call.name}({function_call.args})" if verbose else f" - Calling function: {function_call.name}")
    if function_name not in function_map:
        return get_result("error", f"Unkown function: {function_name}")
    kwargs: dict[str, any] = function_call.args.copy() if function_call.args else {}
    kwargs["working_directory"] = "./calculator"
    function_result: str = function_map[function_name](**kwargs)
    return get_result("result", function_result)


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ],
) 