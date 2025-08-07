def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)
    print(f"Arquivo criado: {path}")

def read_file(path):
    with open(path, 'r') as f:
        return f.read()
