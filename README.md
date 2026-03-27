# 🚀 Sistema de Verificação de Decolagem 

## 📌 Descrição do Projeto

Este projeto simula um sistema básico de análise de telemetria para uma possível decolagem de uma nave. O objetivo é verificar, com base em dados técnicos, se a nave está **"PRONTO PARA DECOLAR"** ou se a missão deve ser **"DECOLAGEM ABORTADA"**.

O sistema utiliza dados como temperatura, energia, pressão e integridade estrutural para tomar decisões simples através de lógica condicional em Python.

---

## 📊 Estrutura dos Dados (CSV)

O arquivo `telemetria.csv` contém dados simulados com os seguintes campos:

* `tempo_s` → tempo em segundos
* `temperatura_interna_c` → temperatura interna da nave
* `temperatura_externa_c` → temperatura externa
* `integridade_estrutural` → 1 (OK) ou 0 (falha)
* `nivel_energia_pct` → nível de energia (%)
* `pressao_tanque_bar` → pressão do combustível
* `status_modulos` → estado dos sistemas (OK/FALHA)

---

## ⚙️ Funcionalidades

✔ Leitura de dados CSV
✔ Verificação de condições de segurança
✔ Decisão automática de decolagem
✔ Simulação de análise energética
✔ Identificação de anomalias e riscos

---

## 🧠 Lógica do Sistema

O sistema avalia:

* Temperatura interna segura (18°C a 30°C)
* Integridade estrutural
* Nível mínimo de energia (≥ 80%)
* Pressão do tanque (230 a 260 bar)
* Status dos módulos

Caso alguma condição não seja atendida:

```
DECOLAGEM ABORTADA
```

Caso contrário:

```
PRONTO PARA DECOLAR
```

---

## 🐍 Exemplo de Execução em Python

```python
import pandas as pd

# Ler dados
df = pd.read_csv("telemetria.csv")

# Pegar última leitura
dados = df.iloc[-1]

# Verificações
if dados["temperatura_interna_c"] < 18 or dados["temperatura_interna_c"] > 30:
    print("DECOLAGEM ABORTADA")
elif dados["integridade_estrutural"] == 0:
    print("DECOLAGEM ABORTADA")
elif dados["nivel_energia_pct"] < 80:
    print("DECOLAGEM ABORTADA")
elif dados["pressao_tanque_bar"] < 230 or dados["pressao_tanque_bar"] > 260:
    print("DECOLAGEM ABORTADA")
elif dados["status_modulos"] != "OK":
    print("DECOLAGEM ABORTADA")
else:
    print("PRONTO PARA DECOLAR")
```

---

## 🔋 Análise Energética

O sistema também calcula a autonomia inicial da nave com base em:

* Capacidade total da bateria (kWh)
* Percentual de carga atual
* Consumo na decolagem
* Perdas energéticas

### Exemplo:

* Capacidade: 1000 kWh
* Carga atual: 80%
* Consumo: 300 kWh
* Perdas: 10%

Resultado:

* Energia útil: 720 kWh
* Energia restante após decolagem: 420 kWh

---

## 🤖 Análise Assistida

O sistema permite identificar:

### Classificação:

* Dados normais
* Estados de atenção
* Condições críticas

### Anomalias:

* Queda de energia
* Redução de pressão
* Condições externas severas

### Riscos:

* Falha energética
* Problemas no tanque
* Impacto térmico nos sistemas

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Google Colab / VS Code

---

## ▶️ Como Executar

### No Google Colab:

1. Fazer upload do arquivo CSV
2. Executar o script Python

```python
from google.colab import files
files.upload()
```

---

### Localmente (VS Code):

1. Instalar dependências:

```
pip install pandas
```

2. Executar:

```
python script.py
```

---

## 📁 Estrutura do Projeto

```
📦 Aurora Siger
 ┣ 📄 Aurora_Singer.ipynb
 ┗ 📄 README.md
```

---

## 🎯 Objetivo Acadêmico

Este projeto foi desenvolvido como atividade introdutória para aplicar conceitos de:

* Lógica de programação
* Estruturas condicionais
* Manipulação de dados
* Simulação de sistemas reais

---

## 📌 Possíveis Melhorias Futuras

* Integração com inteligência artificial
* Visualização gráfica dos dados
* Monitoramento em tempo real
* Interface gráfica (dashboard)

---

## 📄 Licença

Este projeto é de uso acadêmico e livre para estudo.

---
ina de programação.
