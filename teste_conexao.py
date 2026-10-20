import psycopg2

try:
    conexao = psycopg2.connect(
        host="localhost",
        database="integradados",
        user="postgres",
        password="unifeob@123",
        port=5432
    )

    print("Conexão realizada com sucesso!")
    conexao.close()

except Exception as erro:
    print("Tipo:", type(erro).__name__)
    print("Erro:", repr(erro))