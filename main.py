
from ofxparse import OfxParser
from decimal import Decimal

# 1. Ler o arquivo OFX
with open("extrato.ofx", "rb") as arquivo:
    ofx = OfxParser.parse(arquivo)

# 2. Obter as movimentações bancárias
transacoes = ofx.account.statement.transactions

# 3. Inicializar os totais
entradas = Decimal("0.00")
saidas = Decimal("0.00")

print("=" * 60)
print("                 EXTRATO BANCÁRIO")
print("=" * 60)

# 4. Percorrer e exibir cada movimentação
for t in transacoes:
    data = t.date.strftime("%d/%m/%Y")
    valor = Decimal(str(t.amount))
    descricao = t.memo or "Sem descrição"

    print(f"Data      : {data}")
    print(f"Valor     : R$ {valor:.2f}")
    print(f"Descrição : {descricao}")
    print("-" * 60)

    # 5. Calcular entradas e saídas
    if valor > 0:
        entradas += valor
    elif valor < 0:
        saidas += valor

# 6. Calcular o saldo das movimentações
saldo = entradas + saidas

# 7. Exibir o resumo financeiro
print("\nRESUMO FINANCEIRO")
print("=" * 60)
print(f"Quantidade de movimentações: {len(transacoes)}")
print(f"Total de entradas: R$ {entradas:.2f}")
print(f"Total de saídas: R$ {abs(saidas):.2f}")
print(f"Saldo calculado: R$ {saldo:.2f}")
print("=" * 60)