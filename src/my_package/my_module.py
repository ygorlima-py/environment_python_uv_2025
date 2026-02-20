# Instale o pacote: python-dotenv
# Mostrei como no README.md
from dotenv import load_dotenv
import os

# Essa função DEVE ser carregada antes do import dos módulos
# que forem usar variáveis de ambiente
load_dotenv()

def my_function(x: int, y: int) -> int:
    return x + y

def run_from_script() -> None:
    greetings = os.getenv("TESTE_KEY", "Not working. Read the README.md")
    print("Check dotenv: ",greetings)
    
    