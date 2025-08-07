import os

def init_git_repo(path="."):
    os.system(f"cd {path} && git init")
    print("Repositório Git inicializado.")
