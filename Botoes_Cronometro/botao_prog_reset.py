# botao_prog_reset.py

# Dicionário para decodificar os valores dos segundos
pontuacao_segundos = {
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

# Função para decodificar o reset rápido
def decodificar_reset_rapido(pacote):
    try:
        byte_segundos_dezena = pacote[19:20]  # Byte 20
        byte_segundos_unidade = pacote[20:21]  # Byte 21

        # Decodifica os valores usando o dicionário
        segundos_dezena = pontuacao_segundos.get(byte_segundos_dezena, "Desconhecido")
        segundos_unidade = pontuacao_segundos.get(byte_segundos_unidade, "Desconhecido")

        # Verifica se algum byte é desconhecido
        if "Desconhecido" in (segundos_dezena, segundos_unidade):
            return "Desconhecido"

        # Calcula os segundos no formato 00:SS
        segundos = segundos_dezena * 10 + segundos_unidade
        return f"00:{segundos:02}"
    except IndexError:
        return "Desconhecido"
