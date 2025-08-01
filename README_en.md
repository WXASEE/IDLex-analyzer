# 📚 Identification of Sensitive Data in Brazilian Legal Documents using Microsoft Presidio Analyzer

This Python project leverages [Microsoft Presidio](https://github.com/microsoft/presidio) with **custom recognizers** for Brazilian entities such as **CPF** and **RG**, enabling the identification and classification of sensitive information with real data validation (for example, verifying whether a CPF is valid).

---

## 🧾 Recognized Entities

### ✅ Presidio's Built-in Entities

| Entity | Description |
| --- | --- |
| `EMAIL_ADDRESS` | Email addresses |
| `AGE` | Ages represented as numbers with or without the word "anos" (years) |
| `URL` | Website links and addresses |
| `PHONE_NUMBER` | Phone numbers with or without area code |
| `DATE_TIME` | Dates and times in various formats |

---

### 🛠️ Custom Entities in this Project

| Entity | Description |
| --- | --- |
| `CPF` | CPF number with check digit validation |
| `RG` | RG number with or without separators such as hyphens or dots |
| `CEP` | Brazilian postal code (CEP) with optional validation |
| `ENDERECO` | Complete or partial addresses |
| `PESSOA` | Full names of individuals |

#### ⚠️ Note

When changing the **Transformers** model, you might need to adjust how the entities are mapped to the `Recognizer`. Each `Recognizer` has a corresponding file in the `customized_recognizers` folder where you can update this logic for compatibility with the chosen model.

---

## 📦 Requirements

* Python → [**3.12.x**](https://peps.python.org/pep-0693/#bugfix-releases)
* Dependencies listed in `requirements.txt`

Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

---

## 🚀 How to Use

Run the main script providing the text through the `--text` flag. Example:

```bash
python main.py --text "TERMO DE CONSENTIMENTO PARA TRATAMENTO DE DADOS PESSOAIS... CPF: 456.789.012-33 RG: 33.221.445-0 ..."
```

Other optional arguments:

* `--language` → text language (default: `pt`)
* `--entities` → list of entities to search for (e.g., `CPF RG EMAIL_ADDRESS`)
* `--nlp` → NLP engine (`spacy` or `transformers`) — default: `spacy`
* `--spacy_model` → name of the SpaCy model (default: `pt_core_news_lg`)
* `--transformer_model` → name of the Transformers model (default: `pierreguillou/ner-bert-base-cased-pt-lenerbr`)

---

## 🧠 What This Project Does

* Uses `Presidio Analyzer` with NLP in Portuguese via `spaCy` or `Transformers`.
* Adds custom recognizers for:
  * ✅ **CPF** (with check digit validation)
  * ✅ **RG** (with or without hyphens/dots)
* Post-processes the results:
  * Assigns `score = 1.0` for valid CPFs
  * Assigns `score = 0.0` for invalid CPFs

---

## 🛠️ Command Examples

### Run with specific entities:

```bash
python main.py --text "..." --entities CPF RG EMAIL_ADDRESS
```

### Use SpaCy with a specific model:

```bash
python main.py --text "..." --nlp spacy --spacy_model pt_core_news_md
```

### Use a Transformers model:

```bash
python main.py --text "..." --nlp transformers --transformer_model pierreguillou/ner-bert-base-cased-pt-lenerbr
```

---

## 📜 Example Output

```text
type: CPF, start: 175, end: 189, score: 1.0
type: RG, start: 195, end: 207, score: 0.75
type: EMAIL_ADDRESS, start: 346, end: 370, score: 1.0
...
```

---

