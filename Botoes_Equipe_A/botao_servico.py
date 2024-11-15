# botao_servico.py

# Dicionários para decodificar a pontuação de pedido de tempo
pontuacao_vigessimo_terceiro = {
    b'\xb0': "SEM SERVIÇO",
    b'\x38': "SEM SERVIÇO",
    b'\x31': "SERVIÇO EQUIPE A",
    b'\xb9': "SERVIÇO EQUIPE A",
    b'\x32': "SERVIÇO EQUIPE B",
    b'\xba': "SERVIÇO EQUIPE B",
}

# Formata o pacote em hexadecimal
def formatar_em_hexa(pacote):
    return " ".join(f"{byte:02x}" for byte in pacote)

# Função para decodificar o valor de pedido de tempo
def decodificar_vigessimo_terceiro(pacote):
    try:
        vigessimo_terceiro_byte = pacote[22:23]  # 18º byte

        # Decodifica o valor do 18º byte
        servico = pontuacao_vigessimo_terceiro.get(vigessimo_terceiro_byte, "Desconhecido")
        
        # Retorna o valor do pedido de tempo (simplesmente o valor do byte)
        return servico
    except IndexError:
        return "Desconhecido"
