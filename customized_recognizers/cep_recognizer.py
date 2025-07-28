from presidio_analyzer import PatternRecognizer, Pattern

class CEPRecognizer(PatternRecognizer):
    def __init__(self):
        # aceita CEP com ou sem hífen: 12345-678 ou 12345678
        cep_pattern = Pattern(
            name="CEP Flexível",
            regex=r"\b\d{5}-?\d{3}\b",
            score=0.5  # score base médio, pode ajustar conforme validação
        )
        super().__init__(
            supported_entity="CEP",
            patterns=[cep_pattern],
            name="CEP Recognizer",
            supported_language="pt"
        )
