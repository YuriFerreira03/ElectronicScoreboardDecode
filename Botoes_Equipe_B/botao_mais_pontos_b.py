# botao_mais_pontos_b.py

# Dicionários para decodificar a pontuação da Equipe B
pontuacao_setimo_byte = {
    b'\xbf': 0,
    b'\x31': 1,
}
pontuacao_oitavo_byte = {
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
pontuacao_nono_byte = {
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

# Função para decodificar a pontuação da Equipe B
def decodificar_pontuacao_b(pacote):
    try:
        setimo_byte = pacote[6:7]   # Sétimo byte
        oitavo_byte = pacote[7:8]  # Oitavo byte
        nono_byte = pacote[8:9]    # Nono byte

        pontos_setimo = pontuacao_setimo_byte.get(setimo_byte, "Desconhecido")
        pontos_oitavo = pontuacao_oitavo_byte.get(oitavo_byte, "Desconhecido")
        pontos_nono = pontuacao_nono_byte.get(nono_byte, "Desconhecido")

        if "Desconhecido" in (pontos_setimo, pontos_oitavo, pontos_nono):
            return "Desconhecido"
        
        # Calcula a pontuação total
        pontosb = pontos_setimo * 100 + pontos_oitavo * 10 + pontos_nono
        return pontosb
    except IndexError:
        return "Desconhecido"
