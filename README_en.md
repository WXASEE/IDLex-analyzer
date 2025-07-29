# = Identification of Sensitive Data in Brazilian Legal Documents with Microsoft Presidio Analyzer

Python project that uses [Microsoft Presidio](https://github.com/microsoft/presidio) with **custom recognizers** for Brazilian entities such as **CPF** and **RG**, allowing the identification and classification of sensitive information in text with real data validation (like checking if a CPF is valid).

---

## > Recognized Entities

### In progress!

## = Requirements

- Python version ! [**3.12.x**](https://peps.python.org/pep-0693/#bugfix-releases)
- Dependencies listed in `requirements.txt`

> You can use a virtual environment with `venv`:
```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

---

## = How to use

Run the command below passing the text directly as an argument via the `--text` flag:
```bash
py main.py --text "TERMO DE CONSENTIMENTO PARA TRATAMENTO DE DADOS PESSOAISDeclaro, na qualidade de titular dos dados:Nome completo: Marcelo Augusto Vieira  Data de nascimento: 15/02/1985  CPF: 456.789.012-33  RG: 33.221.445-0 SSP/RJ  Endereço: Rua da Liberdade, nº 789, Bairro Centro Histórico, CEP 20000-000, Rio de Janeiro/RJ  Telefone: (21) 98765-4321  E-mail: marcelo.vieira@email.com..."
```

---

## > What this project does

* Uses `Presidio Analyzer` with NLP in Portuguese via `spaCy`.
* Adds custom recognizers for:
  * **CPF** (with check digit validation)
  * **RG** (with or without dashes/dots)
* Post-processes the results:
  * For valid CPFs, sets `score = 1.0`
  * For invalid CPFs, sets `score = 0.0`

---

---

## = Useful commands

### Run with specific entities:
```bash
py main.py --text "..." --entities CPF RG EMAIL
```

### Use a different NLP model:
```bash
py main.py --text "..." --nlp spacy --model-name pt_core_news_md
```

---

## = Example of expected output
```text
type: CPF, start: 175, end: 189, score: 1.0
type: RG, start: 195, end: 207, score: 0.75
type: EMAIL_ADDRESS, start: 346, end: 370, score: 1.0
...
```
