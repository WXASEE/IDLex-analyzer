from presidio_analyzer import PatternRecognizer, Pattern

class RGRecognizer(PatternRecognizer):
    def __init__(self):
        rg_pattern = Pattern(
            name="RG",
            regex=r"\b\d{2}\.?\d{3}\.?\d{3}-?[0-9Xx]\b",
            score=0.75
        )
        super().__init__(
            supported_entity="RG",
            patterns=[rg_pattern],
            name="RG Recognizer",
            supported_language="pt"
        )
