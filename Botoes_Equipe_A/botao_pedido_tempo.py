# botao_pedido_tempo.py

# Dicionários para decodificar a pontuação de pedido de tempo
pontuacao_decimo_oitavo_byte = {
    b'\xb0': 0,
    b'\x31': 1,
    b'\x32': 2,
}

# Formata o pacote em hexadecimal
def formatar_em_hexa(pacote):
    return " ".join(f"{byte:02x}" for byte in pacote)

# Função para decodificar o valor de pedido de tempo
def decodificar_pedido_tempo(pacote):
    try:
        decimo_oitavo_byte = pacote[17:18]  # 18º byte

        # Decodifica o valor do 18º byte
        pontos_decimo_oitavo = pontuacao_decimo_oitavo_byte.get(decimo_oitavo_byte, "Desconhecido")

        if pontos_decimo_oitavo == "Desconhecido":
            return "Desconhecido"
        
        # Retorna o valor do pedido de tempo (simplesmente o valor do byte)
        return pontos_decimo_oitavo
    except IndexError:
        return "Desconhecido"
