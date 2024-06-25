# API para tradução HTML - Projeto Pessoal

## Descrição

API para tradução de HTML para o inglês e português. A API foi desenvolvida em Python, utilizando a biblioteca Argos-Translate para realizar a tradução e a biblioteca FastAPI para criar a API.

Ela possui duas rotas:

- `/translate`: recebe um HTML e retorna o HTML traduzido.
- `/helloworld`: retorna uma mensagem 'Hello World!'.

## Como rodar a aplicação

Para rodar a aplicação, é necessário ter o Python instalado e instalar as dependências do projeto. Para instalar as dependências, execute o comando:

```bash
pip install -r requirements.txt
```

Depois de instalar as dependências, descomente as linhas abaixo no arquivo `main.py`:

```python
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="localhost", port=8080)
```

e depois execute o comando:

```bash
python3 main.py
```

A aplicação estará rodando em `http://localhost:8080`.
Tem outras formas de rodar a aplicação, mas a forma acima é a mais simples.

## Dependências

- Argos-Translate
- FastAPI
- Uvicorn - Para rodar a aplicação
