import re
from datetime import date

CATEGORIAS = {
    "jantar": "alimentacao",
    "almoço": "alimentacao",
    "almoco": "alimentacao",
    "salário": "renda",
    "salario": "renda",
    "presente": "extra",
    "cofrinho": "poupanca",
}

def parse_message(message: str):
    text = message.lower()

    if "gastei" in text or "gasto" in text or "comprei" in text:
        tipo = "despesa"
    elif "ganhei" in text or "recebi" in text:
        tipo = "ganho"
    elif "guardei" in text:
        tipo = "poupanca"
    else:
        raise ValueError("Não entendi o tipo da transação")

    valor_match = re.search(r'(\d+)', text)
    if not valor_match:
        raise ValueError("Valor não encontrado")

    valor = float(valor_match.group(1))

    categoria = "outros"
    descricao = ""

    for palavra, cat in CATEGORIAS.items():
        if palavra in text:
            categoria = cat
            descricao = palavra
            break

    return {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
        "data": date.today()
    }
