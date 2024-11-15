# botao_pedido_tempo_b.py

# Dicionários para decodificar a pontuação de pedido de tempo
pontuacao_decimo_nono_byte = {
    b'\xb0': 0,
    b'\x31': 1,
    b'\x32': 2,
}

# Formata o pacote em hexadecimal
def formatar_em_hexa(pacote):
    return " ".join(f"{byte:02x}" for byte in pacote)

# Função para decodificar o valor de pedido de tempo
def decodificar_pedido_tempo_b(pacote):
    try:
        decimo_nono_byte = pacote[18:19]  # 19º byte

        # Decodifica o valor do 18º byte
        pontos_decimo_nono = pontuacao_decimo_nono_byte.get(decimo_nono_byte, "Desconhecido")

        if pontos_decimo_nono == "Desconhecido":
            return "Desconhecido"
        
        # Retorna o valor do pedido de tempo (simplesmente o valor do byte)
        return pontos_decimo_nono
    except IndexError:
        return "Desconhecido"
