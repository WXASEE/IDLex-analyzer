from presidio_analyzer import RecognizerResult
from utils.funcoes_validacao import (
    is_valid_cpf,
    validar_formato_cep,
    consultar_cep_api,
)
def pos_processamento_cpf(texto: str, resultados: list[RecognizerResult]) -> list[RecognizerResult]:
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

def pos_processamento_cep(texto : str, resultados : list[RecognizerResult]) -> list[RecognizerResult]:
    novos_resultados = []
    for res in resultados:
        tipo = res.entity_type
        start = res.start
        end = res.end

        if tipo == "CEP" and start is not None and end is not None:
            trecho = texto[start:end]

            if validar_formato_cep(trecho):
                valido = consultar_cep_api(trecho)
            else:
                valido = False

            score = 1.0 if valido else 0.0

            novo_res = RecognizerResult(
                entity_type=res.entity_type,
                start=res.start,
                end=res.end,
                score=score,
                analysis_explanation=f"CEP {'válido' if valido else 'inválido'} via API"
            )
        else:
            novo_res = res

        novos_resultados.append(novo_res)

    return novos_resultados