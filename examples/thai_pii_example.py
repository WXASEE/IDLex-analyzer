"""Example usage of Thai custom PII recognizers with Presidio."""
from presidio_analyzer import AnalyzerEngine
from customized_recognizers.thai_recognizers import (
    ThaiNationalIDRecognizer,
    ThaiPhoneRecognizer,
    ThaiPersonNameRecognizer,
)
from utils.wrapper_presidio_analyzer import create_model_spacy


def main():
    text = (
        "นายสมชาย โทรศัพท์ 09-1234-5678 เลขบัตรประชาชน 1101700201234"
    )

    # Load Thai NLP model (replace with your Thai model)
    nlp_engine = create_model_spacy(language="th", spacy_model="th_core_news_sm")

    analyzer = AnalyzerEngine(nlp_engine=nlp_engine, supported_languages=["th"])

    analyzer.registry.add_recognizer(ThaiNationalIDRecognizer())
    analyzer.registry.add_recognizer(ThaiPhoneRecognizer())
    analyzer.registry.add_recognizer(ThaiPersonNameRecognizer())

    results = analyzer.analyze(text=text, language="th")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
