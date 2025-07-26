import argparse
from utils.wrapper_presidio_analyzer import (
    create_model, 
    create_analyzer
)
from utils.const import *
from presidio_analyzer import RecognizerResult
from customized_recognizers.cpf_recognizer import is_valid_cpf

from presidio_analyzer import RecognizerResult
from customized_recognizers.cpf_recognizer import is_valid_cpf

def pos_processamento(texto: str, resultados: list[RecognizerResult]) -> list[RecognizerResult]:
    novos_resultados = []
    for res in resultados:
        tipo = res.entity_type
        start = res.start
        end = res.end

        if tipo == "CPF" and start is not None and end is not None:
            trecho = texto[start:end]
            valido = is_valid_cpf(trecho)
            score = 1.0 if valido else 0.0

            novo_res = RecognizerResult(
                entity_type=res.entity_type,
                start=res.start,
                end=res.end,
                score=score,
                analysis_explanation=f"CPF {'válido' if valido else 'inválido'}"
            )
        else:
            novo_res = res

        novos_resultados.append(novo_res)

    return novos_resultados


def main():
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
        help="Entidades a buscar (ex: CPF RG EMAIL)"
    )

    parser.add_argument(
        "--nlp",
        type=str,
        choices=["spacy", "transformers"],
        default="spacy",
        help="Engine NLP a ser usada"
    )

    parser.add_argument(
        "--model-name",
        type=str,
        default="pt_core_news_lg",
        help="Nome do modelo SpaCy ou Transformers (padrão: pt_core_news_lg)"
    )

    args = parser.parse_args()

    # Cria o NLP engine
    nlp_engine = create_model(
        nlp_engine_name=args.nlp,
        models=[{"lang_code": args.language, "model_name": args.model_name}]
    )

    # Cria o analyzer com os recognizers customizados
    analyzer = create_analyzer(nlp_engine, supported_languages=[args.language])

    # Executa a análise
    results = analyzer.analyze(
        text=args.text,
        language=args.language,
        entities=args.entities
    )

    # Mostra os resultados
    resultado_processado = pos_processamento(args.text, results)

    print(resultado_processado)

if __name__ == "__main__":
    main()
