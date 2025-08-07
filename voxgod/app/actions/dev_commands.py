def generate_code_snippet(prompt):
    return f"# TODO: implementar geração de código para: {prompt}"

def run_code_snippet(snippet):
    print("Executando código...")
    exec(snippet)
