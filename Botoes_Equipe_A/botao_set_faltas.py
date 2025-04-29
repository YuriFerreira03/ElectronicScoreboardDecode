# botao_set_faltas.py

# Dicionários para decodificar a pontuação de Set/Faltas
pontuacao_decimo_byte = {
    b'\xbf': 0,  # zero tens
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
pontuacao_decimo_primeiro_byte = {
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

# Função para decodificar o valor de Set/Faltas
def decodificar_set_faltas(pacote):
    try:
        decimo_byte = pacote[9:10]           # 10º byte
        decimo_primeiro_byte = pacote[10:11]  # 11º byte

        pontos_decimo = pontuacao_decimo_byte.get(decimo_byte, "Desconhecido")
        pontos_decimo_primeiro = pontuacao_decimo_primeiro_byte.get(decimo_primeiro_byte, "Desconhecido")

        if "Desconhecido" in (pontos_decimo, pontos_decimo_primeiro):
            return "Desconhecido"
        
        # Calcula o valor total de Set/Faltas
        pontos = pontos_decimo * 10 + pontos_decimo_primeiro
        return pontos
    except IndexError:
        return "Desconhecido"
