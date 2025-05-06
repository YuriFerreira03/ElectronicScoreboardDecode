# botao_set_faltas_b.py

# Dicionários para decodificar a pontuação de Set/Faltas
pontuacao_decimo_sexto_byte = {
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
pontuacao_decimo_oitavo_byte = {
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
def decodificar_set_faltas_b(pacote):
    try:
        decimo_sexto_byte = pacote[15:16]   # 16º byte
        decimo_setimo_byte = pacote[16:17]  # 17º byte
        
        
        # print(f"Byte 16 (dezenas): {decimo_sexto_byte.hex()}, Byte 17 (unidades): {decimo_setimo_byte.hex()}")

        pontos_decimo_sexto_byte = pontuacao_decimo_sexto_byte.get(decimo_sexto_byte, "Desconhecido")
        pontos_decimo_setimo_byte = pontuacao_decimo_oitavo_byte.get(decimo_setimo_byte, "Desconhecido")

        if "Desconhecido" in (pontos_decimo_sexto_byte, pontos_decimo_setimo_byte):
            return "Desconhecido"
        
        # Calcula o valor total de Set/Faltas
        set_faltas_b = pontos_decimo_sexto_byte * 10 + pontos_decimo_setimo_byte
        return set_faltas_b
    except IndexError:
        return "Desconhecido"
