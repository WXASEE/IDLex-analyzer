ENTIDADES_SUPORTADAS = ['EMAIL_ADDRESS', 'AGE', 'URL', 'PHONE_NUMBER', 'DATE_TIME']#, 'LOCATION', 'ORGANIZATION']
ENTIDADES_CRIADAS = ['CPF', 'RG', 'CEP', 'ENDERECO']
DEBUG = True
API_VIA_CEP = 'https://viacep.com.br/ws/{}/{}/'
API_VIA_CEP_RETURN_TYPE = 'json' # pode ser json, json/?callback=callback_name (final da url) e xml