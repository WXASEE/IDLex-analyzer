import re
import requests
from utils.const import API_VIA_CEP_RETURN_TYPE, API_VIA_CEP

def validar_formato_cep(cep: str) -> bool:
    cep = cep.replace("-", "")
    return bool(re.fullmatch(r"\d{8}", cep))

def consultar_cep_api(cep: str) -> bool:
    url = API_VIA_CEP.format(cep, API_VIA_CEP_RETURN_TYPE)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 400:
            # CEP com formato inválido segundo API
            return False
        if response.status_code == 200:
            dados = response.json()
            # Se a API retornar erro: true, CEP não existe
            return not dados.get("erro", False)
    except Exception:
        # Em caso de erro de rede, considere inválido (ou adaptar)
        return False
    return False

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