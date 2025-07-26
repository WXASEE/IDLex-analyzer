import re
from presidio_analyzer import PatternRecognizer, Pattern

class CPFRecognizer(PatternRecognizer):
    def __init__(self):
        # aceita CPF com ou sem pontos/traço: 123.456.789-09 ou 12345678909
        cpf_pattern = Pattern(
            name="CPF Flexível",
            regex=r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b",
            score=0.01  # score base baixo, ajustado após validação
        )
        super().__init__(
            supported_entity="CPF",
            patterns=[cpf_pattern],
            name="CPF Recognizer",
            supported_language="pt"
        )

@staticmethod
def is_valid_cpf(cpf: str) -> bool:
    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False

    return True