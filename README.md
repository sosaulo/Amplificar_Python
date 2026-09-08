# Emulação de Amplificador: Distorção de Frequência e Amplitude

Este repositório contém a simulação computacional em Python desenvolvida para a disciplina de **Circuitos Eletrônicos** do Departamento de Engenharia em Teleinformática (DETI) da Universidade Federal do Ceará (UFC).

O objetivo do projeto é analisar e visualizar o comportamento de um sinal elétrico ao passar por um amplificador, considerando dois tipos fundamentais de distorção: **distorção de frequência** (com e sem seletividade) e **distorção não linear de amplitude** (utilizando a função tangente hiperbólica).

---

## 📌 Conteúdo do Repositório

* `Amplif_Python.py`: Script principal em Python contendo a lógica das simulações e a geração dos gráficos.
* `parte_1.png`: Gráfico gerado para a análise de distorção de frequência.
* `parte_2.png`: Gráfico gerado para a análise da característica de transferência e distorção de amplitude ($\\tanh$).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **NumPy**: Manipulação de vetores numéricos e geração dos sinais senoidais.
* **Matplotlib**: Plotagem dos gráficos e saídas do sistema.

---

## 🚀 Como Executar o Código

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
   cd NOME_DO_REPOSITORIO
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install numpy matplotlib
   ```
4. Execute o script:
   ```bash
   python Amplif_Python.py
   ```
---

## ✒️ Autor

* **Saulo Gomes Pinto** - *Engenharia de Computação / DETI - UFC*
