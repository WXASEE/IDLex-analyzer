import argparse
from utils.wrapper_presidio_analyzer import (
    create_model_spacy, 
    create_model_transformers,
    create_analyzer
)
from utils.const import *
from utils.pos_processamento import (
    pos_processamento_cpf,
    pos_processamento_cep
)
FUNCOES_POS_PROCESSAMENTO = [
    pos_processamento_cpf,
    pos_processamento_cep,
]

def main():
    ## parser
    parser = argparse.ArgumentParser(description="Executa o analisador com reconhecedores customizados (CPF e RG)")

    parser.add_argument(
        "--text",
        type=str,
        required=True,
        help="Texto a ser analisado"
    )

    parser.add_argument(
        "--language",
        type=str,
        default="pt",
        help="Idioma do texto (padrão: pt)"
    )

    parser.add_argument(
        "--entities",
        type=str,
        nargs="+",
        default=ENTIDADES_SUPORTADAS + ENTIDADES_CRIADAS,
        help="Entidades a buscar (ex: --entities PERSON EMAIL_ADDRESS CPF RG)"
    )

    parser.add_argument(
        "--nlp",
        type=str,
        choices=["spacy", "transformers"],
        default="spacy",
        help="Engine NLP a ser usada (spacy ou transformers)"
    )

    parser.add_argument(
        "--transformer_model",
        type=str,
        default="pierreguillou/ner-bert-base-cased-pt-lenerbr",
        help="Nome do modelo Transformers (padrão: pierreguillou/ner-bert-base-cased-pt-lenerbr)"
    )
    parser.add_argument(
        "--spacy_model",
        type=str,
        default="pt_core_news_lg",
        help="Nome do modelo SpaCy(padrão: pt_core_news_lg)"
    )
    ## parser

    args = parser.parse_args()

    if args.nlp == 'spacy':
        nlp_engine = create_model_spacy(
            nlp_engine_name=args.nlp,
            language=args.language,
            spacy_model=args.spacy_model
            #models=[{"lang_code": args.language, "model_name": args.model_name}]
        )

    elif args.nlp == 'transformers':
       nlp_engine = create_model_transformers(
            language=args.language,
            spacy_model=args.spacy_model,
            transformers_model=args.transformer_model
       )

    analyzer = create_analyzer(nlp_engine, supported_languages=[args.language])
    #--------------------------------------------------------------------------------
    # Executa a análise
    results = analyzer.analyze(
        text=args.text,
        language=args.language,
        entities=args.entities if isinstance(args.entities, list) else [e.strip() for e in args.entities.split(' ') if e.strip()]

    )

    resultado_processado = results
    for func in FUNCOES_POS_PROCESSAMENTO:
        resultado_processado = func(args.text, resultado_processado)
    
    if DEBUG:
        print(args.entities if isinstance(args.entities, list) else [e.strip() for e in args.entities.split(' ') if e.strip()])
        print(resultado_processado)
        #teste
        from presidio_anonymizer import AnonymizerEngine
        anonymizer = AnonymizerEngine()
        anonymized_text = anonymizer.anonymize(text=args.text, analyzer_results=resultado_processado)
        print(args.text)
        print(anonymized_text)

    ## TODO criar logica de guarda dados criptografados

if __name__ == "__main__":
    main()
