# Ambiente Python + VS Code 2025

## Gerenciando tudo com o uv

[uv](https://docs.astral.sh/uv/getting-started/) é uma ferramenta para ambiente moderno em python. Sua intenção é substituir praticamente todas as outras ferramentas: pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, e outras... Até agora tem cumprido tudo com perfeição. Além disso, é uma ferramenta extremamente rápida, escrita em Rust.

```sh
# Instalação do uv (Windows, Linux, Mac)
# Windows PowerShell:
iwr https://astral.sh/uv/install.ps1 -useb | iex

# Linux/macOS (curl)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```sh
# Cria o projeto completo
diretório: uv init nome-do-projeto

# Ou inicializa dentro de um projeto existente:
uv init
```

```sh
# Instala Python, cria venv e instala dependências em 1 comando
uv sync
```

```sh
# Instala pacotes
uv add requests ruff pyright

# Remove pacotes
uv remove requests

# Requerimentos via requirements.txt
uv add -r requirements.txt
```

```sh
# Executa scripts Python sem ativar venv
uv run src/main.py

# Instala ferramentas como ruff ou pyright globalmente
uv tool install ruff
uvx ruff
uv tool uninstall ruff
```

---

## Configuração do Git

```bash
# Inicia o repositório
git init # Não precisa fazer isso se a uv já fez

# Configura usuário global
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# Padroniza branches para 'main'
git config --global init.defaultBranch main
git branch -m main

# Padroniza finais de linha para multiplataforma
git config --global core.autocrlf input
git config --global core.eol lf

git config --list --global

# Primeiro commit
git add .
git commit -m "initial"

# Configurar o repositório
git remote add origin URL_REPO_SSH
git push origin main -u

# Nos próximos
git add .
git commit -m "MENSAGEM"
git push
```

---

## `.env` e `.env-example`

É extremamente comum precisarmos de variáveis de ambiente em nossos projetos. Sabendo
disso, já adicionei o `python-dotenv` como dependência do projeto.

Para instalar escolha uma das opções abaixo:

```bash
# Opção 1: pip
pip install python-dotenv
# Opção 2: uv pip
uv pip install python-dotenv
# Opção 3: uv
uv sync
```

Copie o arquivo `.env-example` para outro arquivo chamado de `.env` para ativar as
variáveis de ambiente. Já deixei um teste na função principal que pode responder duas coisas:

- `Check dotenv: dotenv is working fine`
- `Check dotenv: Not working. Read the README.md`

As mensagens são auto explicativas. Se você receber `Not working`, provavelmente não copiou o arquivo `.env-example` para `.env`.

## Configurando o Docker

```bash
# Construindo a imagem
 docker build -f ./Dockerfile . -t nome_da_imagem

```

```bash
# Entrando dentro do container
 docker run --rm -it nome_da_imagem bash

# Esse comando significa: Cria um container depois que eu sair desse 
# container apague ele e me permita usar esse container de forma interativa
# usando essa imagem "nome_da_imagem"

```