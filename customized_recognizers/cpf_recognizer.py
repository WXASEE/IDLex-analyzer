import re
from presidio_analyzer import PatternRecognizer, Pattern

class CPFRecognizer(PatternRecognizer):
    def __init__(self):
        # aceita CPF com ou sem pontos/traço: 123.456.789-09 ou 12345678909
        cpf_pattern = Pattern(
            name="CPF Flexível",
            regex=r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b",
            score=0.5  # score base baixo, ajustado após validação 0.0 para cpf invalido e 1.0 para cpf valido.
        )
        super().__init__(
            supported_entity="CPF",
            patterns=[cpf_pattern],
            name="CPF Recognizer",
            supported_language="pt"
        )