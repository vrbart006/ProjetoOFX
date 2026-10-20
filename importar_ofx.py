
import psycopg2
from ofxparse import OfxParser

# Conectar ao PostgreSQL

conexao = psycopg2.connect(
    host="localhost",
    database="integradados",
    user="postgres",
    password="unifeob@123",
    port="5432",
    options="-c client_encoding=UTF8"
)


cursor = conexao.cursor()

# Ler o arquivo OFX
with open("extrato.ofx", "rb") as arquivo:
    extrato = OfxParser.parse(arquivo)

# Importar as movimentações
for transacao in extrato.account.statement.transactions:
    data = transacao.date.date()
    valor = transacao.amount
    descricao = transacao.memo or transacao.payee or "Sem descrição"
    fitid = transacao.id

    cursor.execute("""
        INSERT INTO public.movimentacoes
        (data_movimentacao, valor, descricao, fitid)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (fitid) DO NOTHING
    """, (data, valor, descricao[:255], fitid))

# Salvar no banco
conexao.commit()

cursor.close()
conexao.close()

print("Movimentações importadas com sucesso!")
