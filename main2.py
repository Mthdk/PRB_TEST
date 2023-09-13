import os

def coletar_nomes_de_arquivos(diretorio, lista_de_pastas):
    nomes_de_arquivos = []
    for pasta in lista_de_pastas:
        pasta_diretorio = os.path.join(diretorio, pasta)
        if os.path.exists(pasta_diretorio) and os.path.isdir(pasta_diretorio):
            for arquivo in os.listdir(pasta_diretorio):
                nomes_de_arquivos.append(arquivo)
    return nomes_de_arquivos

def verificar_nomes_em_arquivos(nomes_de_arquivos, arquivos_txt):
    resultados = {}
    for txt_file in arquivos_txt:
        with open(txt_file, "r") as file:
            conteudo = file.read()
            for nome in nomes_de_arquivos:
                if nome in conteudo:
                    if nome not in resultados:
                        resultados[nome] = []
                    resultados[nome].append(txt_file)
    return resultados

def main():
    diretorio_alvo = "/caminho/do/diretorio/alvo"  # Substitua pelo diretório que você deseja analisar
    lista_de_pastas = ["pasta1", "pasta2", "pasta3"]  # Substitua pelas pastas que você deseja acessar dentro do diretório alvo

    # Lista de arquivos .txt para comparação
    lista_de_arquivos_txt = [
        "/caminho/do/arquivo1.txt",
        "/caminho/do/arquivo2.txt",
        "/caminho/do/arquivo3.txt",
    ]

    nomes_de_arquivos = coletar_nomes_de_arquivos(diretorio_alvo, lista_de_pastas)
    resultados = verificar_nomes_em_arquivos(nomes_de_arquivos, lista_de_arquivos_txt)

    if resultados:
        with open("resultados.txt", "w") as output_file:
            for nome, arquivos_encontrados in resultados.items():
                output_file.write(f"Nome: {nome}\n")
                output_file.write(f"Encontrado nos arquivos:\n")
                for arquivo in arquivos_encontrados:
                    output_file.write(f"- {arquivo}\n")
                output_file.write("\n")

if __name__ == "__main__":
    main()
