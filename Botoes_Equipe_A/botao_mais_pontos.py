# botao_mais_pontos.py

# Dicionários para decodificar a pontuação
pontuacao_terceiro_byte = {
    b'\xbf': 0,
    b'\x31': 1,
}
pontuacao_quarto_byte = {
    b'\xb0': 0,
    b'\x31': 1,
    b'\x32': 2,
    b'\xb3': 3,
    b'\x34': 4,
    b'\xb5': 5,
    b'\xb6': 6,
    b'\x37': 7,
    b'\x38': 8,
    b'\xb9': 9,
}
pontuacao_quinto_byte = {
    b'\xb0': 0,
    b'\x31': 1,
    b'\x32': 2,
    b'\xb3': 3,
    b'\x34': 4,
    b'\xb5': 5,
    b'\xb6': 6,
    b'\x37': 7,
    b'\x38': 8,
    b'\xb9': 9,
}

# Formata o pacote em hexadecimal
def formatar_em_hexa(pacote):
    return " ".join(f"{byte:02x}" for byte in pacote)

# Função para decodificar a pontuação da equipe A
def decodificar_pontuacao(pacote):
    try:
        terceiro_byte = pacote[2:3]  # Terceiro byte
        quarto_byte = pacote[3:4]    # Quarto byte
        quinto_byte = pacote[4:5]   # Quinto byte

        pontos_terceiro = pontuacao_terceiro_byte.get(terceiro_byte, "Desconhecido")
        pontos_quarto = pontuacao_quarto_byte.get(quarto_byte, "Desconhecido")
        pontos_quinto = pontuacao_quinto_byte.get(quinto_byte, "Desconhecido")

        if "Desconhecido" in (pontos_terceiro, pontos_quarto, pontos_quinto):
            return "Desconhecido"
        
        # Calcula a pontuação total
        pontos = pontos_terceiro * 100 + pontos_quarto * 10 + pontos_quinto
        return pontos
    except IndexError:
        return "Desconhecido"
