# botao_alarme.py

# Dicionários para decodificar a pontuação de pedido de tempo
pontuacao_vigessimo_segundo = {
    b'\xb3': "ALARME APERTADO",
    b'\x37': "ALARME APERTADO",
    b'\x3b': "ALARME APERTADO",
    b'\xba': "ALARME NAO APERTADO",
    b'\x32': "ALARME NAO APERTADO",
    b'\xb6': "ALARME NAO APERTADO",
}

# Formata o pacote em hexadecimal
def formatar_em_hexa(pacote):
    return " ".join(f"{byte:02x}" for byte in pacote)

# Função para decodificar o valor de pedido de tempo
def decodificar_vigessimo_segundo(pacote):
    try:
        vigessimo_segundo_byte = pacote[21:22]  # 22º byte

        # Decodifica o valor do 18º byte
        alarme = pontuacao_vigessimo_segundo.get(vigessimo_segundo_byte, "Desconhecido")
        
        # Retorna o valor do pedido de tempo (simplesmente o valor do byte)
        return alarme
    except IndexError:
        return "Desconhecido"
