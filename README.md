# Aurora_Singer

# 🚀 Sistema de Verificação de Decolagem

## 📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de um sistema de verificação de condições para decolagem de um veículo (ex: foguete), com base em dados de telemetria.

O sistema analisa parâmetros críticos em tempo real e decide automaticamente se o veículo está:

* ✅ **PRONTO PARA DECOLAR**
* ❌ **DECOLAGEM ABORTADA**

Além disso, o sistema inclui uma **análise energética**, que calcula a autonomia com base na energia disponível, perdas e consumo na decolagem.

---

## 📊 Parâmetros analisados

O sistema verifica os seguintes dados:

* 🌡️ **Temperatura interna** (18ºC a 27ºC)
* 🌍 **Temperatura externa** (40ºC a 50ºC)
* 🏗️ **Integridade estrutural** (1 = OK, 0 = Falha)
* 🔋 **Nível de energia** (mínimo 85%)
* ⛽ **Pressão dos tanques** (90% a 110%)
* 🧠 **Status dos módulos críticos** (1 = OK, 0 = Falha)

---

## ⚙️ Funcionamento

O programa:

1. Solicita os dados ao utilizador
2. Verifica cada condição
3. Retorna o estado da decolagem
4. Calcula a autonomia energética

---

## 🖥️ Prints da Execução

### ✔ Exemplo de execução com sucesso

```
Temperatura interna: 20
Temperatura externa: 42
Integridade estrutural (1=OK,0=Falha): 1
Nível de energia (%): 90
Pressão dos tanques (%): 105
Status módulos críticos (1=OK,0=Falha): 1

PRONTO PARA DECOLAR

Capacidade total (kWh): 1000
Consumo na decolagem (kWh): 250
Taxa de perdas (ex: 0.1 para 10%): 0.1

--- ANÁLISE ENERGÉTICA ---
Energia disponível: 900.00 kWh
Perdas: 90.00 kWh
Energia útil: 810.00 kWh
Autonomia: 3.24 ciclos de decolagem
✔ Energia suficiente para a missão inicial
```

---

### ❌ Exemplo de falha

```
Temperatura interna: 30

DECOLAGEM ABORTADA - Temperatura interna fora do limite
```

---

## ▶️ Instruções de Execução

### 📌 Requisitos

* Python 3 instalado

### 📌 Como executar

1. Guardar o código em um ficheiro:

```
decolagem.py
```

2. Abrir o terminal ou prompt de comando

3. Executar o programa:

```
python decolagem.py
```

4. Inserir os valores solicitados

---

## 🧠 Observações

* O sistema segue limites de segurança predefinidos
* Caso qualquer parâmetro esteja fora do intervalo, a decolagem é automaticamente abortada
* A análise energética ajuda a prever a viabilidade da missão

---

## 👨‍💻 Autor

Trabalho académico desenvolvido para a disciplina de programação.
