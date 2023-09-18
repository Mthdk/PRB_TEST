import os
import csv

# Diretório que deseja percorrer
diretorio_base = '/caminho/do/diretorio/base'

# Lista de pastas a serem excluídas da busca
pastas_a_excluir = ['pasta1', 'pasta2']

# Função para verificar se um arquivo é uma imagem (você pode adicionar mais extensões, se necessário)
def is_imagem(arquivo):
    extensoes_imagens = ['.jpg', '.jpeg', '.png', '.gif']
    return any(arquivo.lower().endswith(ext) for ext in extensoes_imagens)

# Função para contar imagens em uma pasta e listar os nomes dos arquivos
def contar_imagens_em_pasta(pasta):
    contador = 0
    nomes_arquivos = []
    for item in os.listdir(pasta):
        item_caminho = os.path.join(pasta, item)
        if os.path.isfile(item_caminho) and is_imagem(item):
            contador += 1
            nomes_arquivos.append(item)
    return contador, nomes_arquivos

# Abrir um arquivo CSV para escrever as informações
with open('relatorio.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Pasta', 'Quantidade de Imagens', 'Nomes dos Arquivos'])

    # Percorrer o diretório base
    for pasta_raiz, subpastas, arquivos in os.walk(diretorio_base):
        for pasta in subpastas[:]:
            if pasta in pastas_a_excluir:
                subpastas.remove(pasta)
        if any(is_imagem(arquivo) for arquivo in arquivos):
            quantidade_imagens, nomes_arquivos = contar_imagens_em_pasta(pasta_raiz)
            escritor_csv.writerow([pasta_raiz, quantidade_imagens, ', '.join(nomes_arquivos)])

print("Relatório gerado com sucesso em 'relatorio.csv'")
