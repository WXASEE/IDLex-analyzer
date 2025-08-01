from presidio_analyzer import PatternRecognizer, Pattern, EntityRecognizer, RecognizerResult
from presidio_analyzer.nlp_engine import NlpArtifacts


class ThaiNationalIDRecognizer(PatternRecognizer):
    """Recognize Thai national ID numbers (13 digits)."""

    def __init__(self) -> None:
        pattern = Pattern(
            name="Thai National ID",
            regex=r"\b\d{13}\b",
            score=0.6,
        )
        super().__init__(
            supported_entity="TH_ID",
            patterns=[pattern],
            name="ThaiNationalIDRecognizer",
            supported_language="th",
            context=["บัตรประชาชน"],
        )


class ThaiPhoneRecognizer(PatternRecognizer):
    """Recognize Thai phone numbers in formats 0X-XXXX-XXXX or 0X XXXX XXXX."""

    def __init__(self) -> None:
        phone_pattern = Pattern(
            name="Thai Phone Number",
            regex=r"\b0\d[- ]\d{4}[- ]\d{4}\b",
            score=0.6,
        )
        super().__init__(
            supported_entity="TH_PHONE",
            patterns=[phone_pattern],
            name="ThaiPhoneRecognizer",
            supported_language="th",
            context=["โทรศัพท์"],
        )


class ThaiPersonNameRecognizer(EntityRecognizer):
    """Recognize Thai person names using NER results from the NLP engine."""

    def __init__(self) -> None:
        super().__init__(
            supported_entities=["TH_PERSON"],
            name="ThaiPersonNameRecognizer",
            supported_language="th",
            context=["ชื่อ"],
        )

    def load(self) -> None:
        """No external resources needed."""
        return None

    def analyze(
        self, text: str, entities: list[str], nlp_artifacts: NlpArtifacts
    ) -> list[RecognizerResult]:
        results: list[RecognizerResult] = []
        for ent in nlp_artifacts.entities:
            if ent.label_.upper() in {"PERSON", "PER", "B-PERSON", "I-PERSON"}:
                results.append(
                    RecognizerResult(
                        entity_type="TH_PERSON",
                        start=ent.start_char,
                        end=ent.end_char,
                        score=0.85,
                    )
                )
        return results
