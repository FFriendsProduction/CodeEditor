import code

python_interpreter = code.InteractiveInterpreter()

def run_code(code_to_run, file_name):
    python_interpreter.runsource(code_to_run, file_name, symbol = "exec")