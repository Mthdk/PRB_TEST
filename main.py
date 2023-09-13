import os

# Diretório alvo
diretorio_alvo = '/caminho/do/seu/diretorio/alvo'

# Lista de strings para procurar nos nomes dos arquivos
strings_procuradas = ['string1', 'string2', 'string3']

# Função para encontrar e escrever as linhas dos arquivos correspondentes
def encontrar_e_escrever_arquivos_com_strings(diretorio, strings):
    for string in strings:
        nome_arquivo_saida = f'{string}_reprocessamento.txt'
        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            for pasta_raiz, _, arquivos in os.walk(diretorio):
                for arquivo in arquivos:
                    if arquivo.startswith(string):
                        caminho_arquivo = os.path.join(pasta_raiz, arquivo)
                        with open(caminho_arquivo, 'r') as arquivo_entrada:
                            for linha in arquivo_entrada:
                                arquivo_saida.write(linha)

# Chamada da função principal
encontrar_e_escrever_arquivos_com_strings(diretorio_alvo, strings_procuradas)
