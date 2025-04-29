# para rodar o programa coloque : python3 -m venv support/venv, source support/venv/bin/activate, ./run.sh

import serial  # type: ignore
import time

# Equipe A
from Botoes_Equipe_A.botao_mais_pontos import decodificar_pontuacao, formatar_em_hexa
from Botoes_Equipe_A.botao_set_faltas import decodificar_set_faltas
from Botoes_Equipe_A.botao_pedido_tempo import decodificar_pedido_tempo
from Botoes_Equipe_A.botao_servico import decodificar_vigessimo_terceiro

# Equipe B
from Botoes_Equipe_B.botao_mais_pontos_b import decodificar_pontuacao_b
from Botoes_Equipe_B.botao_set_faltas_b import decodificar_set_faltas_b
from Botoes_Equipe_B.botao_pedido_tempo_b import decodificar_pedido_tempo_b

#cronometro
from Botoes_Cronometro.cronometro import decodificar_cronometro, valores_preset, formatar_em_hexa
from Botoes_Cronometro.botao_prog_reset import decodificar_reset_rapido

# Botões de alarme e período
from Botoes_Alarme_Periodo.botao_alarme import decodificar_vigessimo_segundo
from Botoes_Alarme_Periodo.botao_periodo import decodificar_sexto

# def crc8(data, poly=0x01, init=0x80, width=8):
#     crc = init
    
#     for byte in data:
#         crc ^= byte
        
#         for _ in range(width):
#             if crc & 0x80:  # Se o bit mais significativo for 1
#                 crc = (crc << 1) ^ poly  # Shift e XOR com o polinômio
#             else:
#                 crc <<= 1  # Caso contrário, apenas shift
#             crc &= 0xFF  # Garante que o CRC permanece dentro de 8 bits

#     return crc

# Configuração da porta serial
ser = serial.Serial('/dev/cu.usbserial-58BA1184401', 9600)
#ser = serial.Serial('/dev/ttyACM0', 9600)
#ser = serial.Serial('/dev/ttyUSB0', 9600)

print("Pegando um padrão de pacotes")

# Parâmetros de configuração
tamanho_pacote = 28
num_linhas_para_verificar = 100  # Número de pacotes para verificar o padrão
linhas_armazenadas = []

# Verifica se todas as linhas armazenadas são iguais
def verificar_padroes():
    return all(linha == linhas_armazenadas[0] for linha in linhas_armazenadas)

# Sincroniza com o padrão inicial
while True:
    while True:
        dado = ser.read(1)
        if dado == b'\x02':
            break
    dado = ser.read(1)
    if dado == b'\x92':
        break

ser.read(26)

# Loop de captura contínua
while True:
    # Captura 28 bytes de dados
    pacote = ser.read(28)

    # Decodifica os valores
    pontos = decodificar_pontuacao(pacote)
    set_faltas = decodificar_set_faltas(pacote)
    pedido_tempo = decodificar_pedido_tempo(pacote)
    servico = decodificar_vigessimo_terceiro(pacote)
    pontosb = decodificar_pontuacao_b(pacote)
    set_faltas_b = decodificar_set_faltas_b(pacote)
    pedido_tempo_b = decodificar_pedido_tempo_b(pacote)
    botao_cronometro = decodificar_cronometro(pacote)
    reset_rapido = decodificar_reset_rapido(pacote)
    alarme = decodificar_vigessimo_segundo(pacote)
    periodo = decodificar_sexto(pacote)
    
    if pontos != "Desconhecido" and set_faltas != "Desconhecido" and pedido_tempo != "Desconhecido":
        print(
            f"========== Placar Eletrônico ==========\n"
            f"Equipe A:\n"
            f"  Pontos: {pontos}\n"
            f"  Set/Faltas: {set_faltas}\n"
            f"  Pedido de Tempo: {pedido_tempo}\n"
            f"  Serviço: {servico}\n"
            f"----------------------------------------\n"
            f"Equipe B:\n"
            f"  Pontos: {pontosb}\n"
            f"  Set/Faltas: {set_faltas_b}\n"
            f"  Pedido de Tempo: {pedido_tempo_b}\n"
            f"  Serviço: {servico}\n"
            f"----------------------------------------\n"
            f"Cronômetro: {botao_cronometro}\n"
            f"Reset Rápido: {reset_rapido}\n"
            f"----------------------------------------\n"
            f"Alarme: {alarme}\n"
            f"Período: {periodo}\n"
            f"----------------------------------------\n"
            f"Pacote: {formatar_em_hexa(pacote)}\n"
            f"========================================\n"
        )
        # crc_result = crc8(pacote[0:24])
        # print(f" medido {pacote[24]:02X}")
    else:
        print(f"Pacote normal: {formatar_em_hexa(pacote)}\n")
        
    if botao_cronometro in valores_preset:
        print(f"Botão Preset Apertado, passou ou está nos valores predefinidos: {botao_cronometro}")

    time.sleep(0.0)  # delay se precisar