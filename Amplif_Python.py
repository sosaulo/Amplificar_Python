import numpy as np
import matplotlib.pyplot as plt

# pt 1: distorcao de freq

# vetor de tempo e freqs
t = np.linspace(0, 0.025, 10000) #intervalo de temp continuo 
w1 = 1000 # freq base
w = [w1, 1.5*w1, 0.5*w1, 2*w1, 2.5*w1]

#1. sinal de entrada Vi(t): SOma de 5 sen com ampl base = 10
vi_t = 10 * sum(np.sin(freq * t) for freq in w)

#2. caso sem seletividade: G = 2.5 para todas as freqs
G_const = 2.5
vo_sem = G_const * vi_t

#3. caso com seletividade: ganhos diferentes
G1, G2, G3 = 0.25, 5.0, 0.5
vo_com = (G1 * 10 * (np.sin(w[0]*t) + np.sin(w[1]*t) + np.sin(w[2]*t)) +
          G2 * 10 * np.sin(w[3]*t) +
          G3 * 10 * np.sin(w[4]*t))

# plot parte 1
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plot das 5 senoides individuais (linhas finas e transparentes)
for i, freq in enumerate(w, start=1):
    axs[0].plot(t, 10 * np.sin(freq * t), linewidth=1, alpha=0.5, label=f'Senoide {i} ($\\omega_{i}$)')

# Plot da entrada total e da saída
axs[0].plot(t, vi_t, label='$v_i(t)$ (Entrada Total)', color='blue', linewidth=1.8)
axs[0].plot(t, vo_sem, label='$v_o(t)$ (Saída Sem Seletividade)', color='black', alpha=0.8, linewidth=1.5)
axs[0].set_title("Distorção de Frequência: Sem Seletividade")
axs[0].set_xlabel("Tempo [s]")
axs[0].set_ylabel("Tensão [V]")
axs[0].grid(True)
axs[0].legend(loc='upper right', fontsize=8, ncol=2)

# --- GRÁFICO 2: COM SELETIVIDADE ---
# Plot das 5 senoides individuais
for i, freq in enumerate(w, start=1):
    axs[1].plot(t, 10 * np.sin(freq * t), linewidth=1, alpha=0.5, label=f'Senoide {i} ($\\omega_{i}$)')

# Plot da entrada total e da saída com ganhos seletivos
axs[1].plot(t, vi_t, label='$v_i(t)$ (Entrada Total)', color='blue', linewidth=1.8)
axs[1].plot(t, vo_com, label='$v_o(t)$ (Saída Com Seletividade)', color='black', alpha=0.8, linewidth=1.5)
axs[1].set_title("Distorção de Frequência: Com Seletividade")
axs[1].set_xlabel("Tempo [s]")
axs[1].set_ylabel("Tensão [V]")
axs[1].grid(True)
axs[1].legend(loc='upper right', fontsize=8, ncol=2)

plt.tight_layout()
plt.show()

# ==========================================
# PARTE 2: DISTORÇÃO DE AMPLITUDE (NÃO-LINEARIDADE)
# ==========================================

# Modelo de curva do amplificador: tanh(x) = (e^x - e^-x) / (e^x + e^-x)
def amplificador_tanh(v_in):
    return np.tanh(v_in)

t2 = np.linspace(-0.01, 0.01, 10000)

# Caso 1: Grande amplitude de entrada (Satura/Ceifa a onda -> Onda Quadrada)
vi_caso1 = 10 * np.sin(1000 * t2)
vo_caso1 = amplificador_tanh(vi_caso1)

# Caso 2: Pequena amplitude de entrada (Pequeno Sinal -> Operação Linear)
vi_caso2 = 1.0 * np.sin(1000 * t2)
vo_caso2 = amplificador_tanh(vi_caso2)

# Plotagem da Parte 2
fig2, axs2 = plt.subplots(2, 2, figsize=(12, 8))

# Curva de Transferência
v_sweep = np.linspace(-5, 5, 1000)
axs2[0, 1].plot(v_sweep, amplificador_tanh(v_sweep), color='blue')
axs2[0, 1].set_title("Característica de Transferência $v_o = \\tanh(v_i)$")
axs2[0, 1].set_xlabel("Tensão Entrada [V]")
axs2[0, 1].set_ylabel("Tensão Saída [V]")
axs2[0, 1].grid(True)

# Entrada do Caso 1
axs2[0, 0].plot(t2, vi_caso1, color='blue')
axs2[0, 0].set_title("Caso 1: Entrada de Grande Amplitude (A = 10)")
axs2[0, 0].set_xlabel("Tempo [s]")
axs2[0, 0].set_ylabel("Tensão [V]")
axs2[0, 0].grid(True)

# Saída do Caso 1 (Saturada / Ceifada)
axs2[1, 0].plot(t2, vo_caso1, color='blue')
axs2[1, 0].set_title("Caso 1: Saída Distorcida (Saturação em ±1V)")
axs2[1, 0].set_xlabel("Tempo [s]")
axs2[1, 0].set_ylabel("Tensão Saída [V]")
axs2[1, 0].grid(True)

# Saída do Caso 2 (Pequeno Sinal)
axs2[1, 1].plot(t2, vo_caso2, color='blue')
axs2[1, 1].set_title("Caso 2: Saída para Pequeno Sinal (Sem ceifamento crítico)")
axs2[1, 1].set_xlabel("Tempo [s]")
axs2[1, 1].set_ylabel("Tensão Saída [V]")
axs2[1, 1].grid(True)

plt.tight_layout()
plt.show()