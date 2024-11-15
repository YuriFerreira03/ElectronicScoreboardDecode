# botao_periodo.py

# Dicionários para decodificar a pontuação de pedido de tempo
pontuacao_sexto = {
    b'\x31': 1,
    b'\x32': 2,
    b'\xb3': 3,
    b'\x34': 4,
    b'\xb5': 5,
    b'\x45': "TEMPO EXTRA",
    B'\xd0': "PENALTIS",
}

# Formata o pacote em hexadecimal
def formatar_em_hexa(pacote):
    return " ".join(f"{byte:02x}" for byte in pacote)

# Função para decodificar o valor de pedido de tempo
def decodificar_sexto(pacote):
    try:
        sexto_byte = pacote[5:6]  # 22º byte

        # Decodifica o valor do 18º byte
        periodo = pontuacao_sexto.get(sexto_byte, "Desconhecido")
        
        # Retorna o valor do pedido de tempo (simplesmente o valor do byte)
        return periodo
    except IndexError:
        return "Desconhecido"
