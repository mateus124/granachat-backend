import re
from datetime import date

VALOR_REGEX = r'(\d+[.,]?\d*)'

DESPESA_VERBOS = ["gastei", "gasto", "comprei", "paguei"]
GANHO_VERBOS = ["ganhei", "recebi"]
POUPANCA_VERBOS = ["guardei"]

CATEGORIAS = {
    "alimentacao": [
        "jantar", "almoço", "almoco", "salgado", "pastel",
        "cantina", "ifood", "lanche"
    ],
    "transporte": [
        "passagem", "topic", "ônibus", "onibus", "uber"
    ],
    "moradia": [
        "aluguel"
    ],
    "contas": [
        "energia", "luz", "água", "agua", "internet"
    ],
    "renda": [
        "salário", "salario"
    ],
    "poupanca": [
        "cofrinho"
    ]
}

def parse_message(message: str):
    text = message.lower()

    if any(v in text for v in DESPESA_VERBOS):
        tipo = "despesa"
    elif any(v in text for v in GANHO_VERBOS):
        tipo = "ganho"
    elif any(v in text for v in POUPANCA_VERBOS):
        tipo = "poupanca"
    else:
        raise ValueError("Não entendi o tipo da transação")

    valor_match = re.search(VALOR_REGEX, text)
    if not valor_match:
        raise ValueError("Valor não encontrado")

    valor_str = valor_match.group(1)
    valor = float(valor_str.replace(",", "."))

    categoria = "outros"
    for cat, palavras in CATEGORIAS.items():
        if any(p in text for p in palavras):
            categoria = cat
            break

    descricao = (
        text
        .replace(valor_str, "")
        .replace("reais", "")
        .replace("real", "")
        .strip()
    )

    return {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
        "data": date.today()
    }
