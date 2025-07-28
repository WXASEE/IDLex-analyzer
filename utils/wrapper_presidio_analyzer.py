from presidio_analyzer import AnalyzerEngine
from presidio_analyzer.nlp_engine import (
    NlpEngineProvider, 
    NlpEngine
)
from typing import Literal
from customized_recognizers.cpf_recognizer import CPFRecognizer
from customized_recognizers.rg_recognizer import RGRecognizer
from customized_recognizers.cep_recognizer import CEPRecognizer

def create_model(nlp_engine_name: Literal['spacy', 'transformers'], models: list[dict[str, str]]) -> NlpEngine:
    engine_pt = NlpEngineProvider(nlp_configuration={
        'nlp_engine_name': nlp_engine_name,
        'models': models
    })
    return engine_pt.create_engine()

def create_analyzer(nlp_engine: NlpEngine, supported_languages: list[str]) -> AnalyzerEngine:
    analyzer = AnalyzerEngine(
        nlp_engine=nlp_engine,
        supported_languages=supported_languages
    )

    analyzer.registry.add_recognizer(CPFRecognizer())
    analyzer.registry.add_recognizer(RGRecognizer())
    analyzer.registry.add_recognizer(CEPRecognizer())

    return analyzer
