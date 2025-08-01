# 📚 Identificação de Dados Sensíveis em Documentos Jurídicos Brasileiros com Microsoft Presidio Analyzer
[English version](README_en.md)

Projeto em Python que utiliza o [Microsoft Presidio](https://github.com/microsoft/presidio) com **reconhecedores personalizados** para entidades brasileiras como **CPF** e **RG**, permitindo identificar e classificar informações sensíveis em textos, com validação real de dados (como verificação de CPF válido).

---

## 🧾 Entidades Reconhecidas

### ✅ Entidades padrão do Presidio

| Entidade        | Descrição                                                     |
| --------------- | ------------------------------------------------------------- |
| `EMAIL_ADDRESS` | Endereços de e-mail                                           |
| `AGE`           | Idades representadas como números com ou sem a palavra "anos" |
| `URL`           | Links e endereços de sites                                    |
| `PHONE_NUMBER`  | Números de telefone com ou sem DDD                            |
| `DATE_TIME`     | Datas e horários em vários formatos                           |

---

### 🛠️ Entidades personalizadas deste projeto

| Entidade   | Descrição                                                               |
| ---------- | ----------------------------------------------------------------------- |
| `CPF`      | Número de CPF (com validação dos dígitos verificadores)                 |
| `RG`       | Número de RG (com ou sem separadores como traços ou pontos)             |
| `CEP`      | Código de Endereçamento Postal brasileiro (CEP), com validação opcional |
| `ENDERECO` | Endereços completos ou parciais                                         |
| `PESSOA`   | Nomes completos de pessoas físicas                                      |

#### ⚠️ Atenção

Ao mudar o modelo **Transformers**, você pode precisar ajustar como as entidades são mapeadas para o `Recognizer`.
Cada `Recognizer` possui um arquivo correspondente na pasta `*customized_recognizers*`, onde essa lógica pode ser alterada para compatibilidade com o modelo escolhido.

---

## 📦 Requisitos

* Python → [**3.12.x**](https://peps.python.org/pep-0693/#bugfix-releases)
* Dependências no `requirements.txt`

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
```

---

## 🚀 Como usar

Você pode executar o script principal passando o texto via flag `--text`. Exemplo:

```bash
python main.py --text "TERMO DE CONSENTIMENTO PARA TRATAMENTO DE DADOS PESSOAIS... CPF: 456.789.012-33 RG: 33.221.445-0 ..."
```

Outros argumentos opcionais:

* `--language` → idioma do texto (padrão: `pt`)
* `--entities` → lista de entidades a buscar (ex: `CPF RG EMAIL_ADDRESS`)
* `--nlp` → engine de NLP (`spacy` ou `transformers`) — padrão: `spacy`
* `--spacy_model` → nome do modelo SpaCy (padrão: `pt_core_news_lg`)
* `--transformer_model` → nome do modelo Transformers (padrão: `pierreguillou/ner-bert-base-cased-pt-lenerbr`)

---

## 🧠 O que este projeto faz

* Utiliza o `Presidio Analyzer` com NLP em português via `spaCy` ou `Transformers`.
* Adiciona reconhecedores customizados para:

  * ✅ **CPF** (com validação dos dígitos verificadores)
  * ✅ **RG** (com ou sem traços/pontos)
* Pós-processa os resultados:

  * Para CPFs válidos, atribui `score = 1.0`
  * Para CPFs inválidos, atribui `score = 0.0`

---

## 🛠️ Exemplos de comandos

### Rodar com entidades específicas:

```bash
python main.py --text "..." --entities CPF RG EMAIL_ADDRESS
```

### Usar SpaCy com modelo específico:

```bash
python main.py --text "..." --nlp spacy --spacy_model pt_core_news_md
```

### Usar modelo Transformers:

```bash
python main.py --text "..." --nlp transformers --transformer_model pierreguillou/ner-bert-base-cased-pt-lenerbr
```

---

## 📜 Exemplo de saída esperada

```text
type: CPF, start: 175, end: 189, score: 1.0
type: RG, start: 195, end: 207, score: 0.75
type: EMAIL_ADDRESS, start: 346, end: 370, score: 1.0
...
```

---
