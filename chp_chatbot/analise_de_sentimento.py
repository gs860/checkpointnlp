#Lucas Caspirro Gitti Alcaraz – RM551090
#Gabriel Silva- RM552397
#Victor Hugo de Souza Martins- RM99591
#Henzzo fonseca de morais- RM97917


pontuação_de_sentimento = 0
def tokenizar(frase):
    pontuacoes = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    for pontuacao in pontuacoes:
        frase = frase.replace(pontuacao, ' ')

    palavras = frase.split()

    return palavras

def adicionar_palavra_arquivo(palavra, arquivo):
    try:
        with open(arquivo, "r") as f:
            pass
    except FileNotFoundError:
        with open(arquivo, "w") as f:
            pass

    with open(arquivo, "a") as f:
        f.write(palavra + "\n")  
        f.write("\n") 

def verificar_palavra_arquivo(palavra, arquivo):
    with open(arquivo, "r") as f:
        for linha in f:
            if linha.strip().lower() == palavra.lower():
                return True
    return False

def analisar_sentimento(frase):
    global pontuação_de_sentimento

    tokens = tokenizar(frase)

    palavras_ausentes = []
    palavras_perguntadas = set()

    with open("palavras_positivas.txt", "r") as p:
        for linha in p:
            palavra = linha.lower().strip()
            if palavra in tokens:
                pontuação_de_sentimento += 1
                
    with open("palavras_negativas.txt", "r") as p:
        for linha in p:
            palavra = linha.lower().strip()
            if palavra in tokens:
                pontuação_de_sentimento -= 1

    for token in tokens:
        if not verificar_palavra_arquivo(token, "palavras_positivas.txt") and not verificar_palavra_arquivo(token, "palavras_negativas.txt") and token not in palavras_perguntadas:
            palavras_ausentes.append(token)
            palavras_perguntadas.add(token)

    if palavras_ausentes:
        print("Palavras ausentes na lista:")
        for palavra in palavras_ausentes:
            opcao = input(f"Deseja adicionar '{palavra}' a um dos arquivos? (s/n): ")
            if opcao.lower() == 's':
                arquivo = input("Em qual arquivo deseja adicionar (positivo/negativo): ").lower()
                if arquivo == "positivo":
                    adicionar_palavra_arquivo(palavra, "palavras_positivas.txt")
                elif arquivo == "negativo":
                    adicionar_palavra_arquivo(palavra, "palavras_negativas.txt")

    if pontuação_de_sentimento > 0:
        return "positivo"
    elif pontuação_de_sentimento < 0:
        return "negativo"
    else:
        return "neutro"

def entrada_usuario():
    frase = input("Digite a sua frase: ")
    sentimento = analisar_sentimento(frase)
    print("Sentimento da frase:", sentimento)
    print("caso voçê tenha adicionado palavras novoa é recomendado rodar o codigo do inicio para que os dados sejam atualizados")

entrada_usuario()