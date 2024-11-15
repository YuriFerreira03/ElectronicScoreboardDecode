#crometro.py

# Dicionário para decodificar os valores do cronômetro
pontuacao_cronometro = {
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

# Valores predefinidos do botão "preset"
valores_preset = ["00:00", "05:00", "07:00", "10:00", "12:00", "20:00", "30:00"]

# Formata o pacote em hexadecimal
def formatar_em_hexa(pacote):
    return " ".join(f"{byte:02x}" for byte in pacote)

# Função para decodificar o cronômetro
def decodificar_cronometro(pacote):
    try:
        byte_minutos_dezena = pacote[11:12]  # Byte 12
        byte_minutos_unidade = pacote[12:13]  # Byte 13
        byte_segundos_dezena = pacote[13:14]  # Byte 14
        byte_segundos_unidade = pacote[14:15]  # Byte 15

        # Decodifica os valores usando o dicionário
        minutos_dezena = pontuacao_cronometro.get(byte_minutos_dezena, "Desconhecido")
        minutos_unidade = pontuacao_cronometro.get(byte_minutos_unidade, "Desconhecido")
        segundos_dezena = pontuacao_cronometro.get(byte_segundos_dezena, "Desconhecido")
        segundos_unidade = pontuacao_cronometro.get(byte_segundos_unidade, "Desconhecido")

        # Verifica se algum byte é desconhecido
        if "Desconhecido" in (minutos_dezena, minutos_unidade, segundos_dezena, segundos_unidade):
            return "Desconhecido"

        # Calcula o cronômetro no formato MM:SS
        minutos = minutos_dezena * 10 + minutos_unidade
        segundos = segundos_dezena * 10 + segundos_unidade
        cronometro = f"{minutos:02}:{segundos:02}"

        return cronometro
    except IndexError:
        return "Desconhecido"
