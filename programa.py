# -----------------------------------------------------------------------------
# Estrutura de Dados
# Aula 03
#
# Neste script, abordamos um projeto básico para criar um módulo de funções
# estatísticas, baseado nas seguintes referências:
# SILVA, Marcos Noé Pedro da. Estatística.
# Disponível em <https://brasilescola.uol.com.br/matematica/estatistica-1.htm>.
# Acesso em 31 de julho de 2018.
#
# Portal Action. Estatística Básica.
# Disponível em <http://www.portalaction.com.br/estatistica-basica>.
# Acesso em 31 de julho de 2018.
#
# -----------------------------------------------------------------------------
# Utilize um ambiente de desenvolvimento (IDE ou editor de texto), para
# digitar o trecho de código a seguir. Salve o arquivo com a extensão '.py',
# e em seguida execute-o, verificando a saída obtida.
# Como exemplo de IDEs, temos: IDLE, PyCharm, Spyder...
# Como exemplo de editores de texto, temos: Notepad++, Sublime, Atom...
# *****************************************************************************
# 1. Cria as funções para cálculo das medidas estatísticas
# *****************************************************************************
# Importa os módulos utilizados neste programa
import math
import os
# -----------------------------------------------------------------------------
# Entrada dos dados
# -----------------------------------------------------------------------------
def entrada_dados():
    """Realiza a entrada do conjunto de dados."""
    # Lista para armazenar os valore do conjunto de dados
    dados = []
    # Entrada da quantidade de valores
    total_valores = int(input("\n>>> Informe a quantidade de valores: "))
    # Pula uma linha
    print()
    # Loop para a entrada de dados
    for i in range(total_valores):
        dados.append(int(input(">>> Informe o valor %d -> " %(i + 1))))
    # Retorna a lista com os valores
    return dados
# -----------------------------------------------------------------------------
# Frequência absoluta
# -----------------------------------------------------------------------------
def freq_absoluta(dados):
    """Cálculo da frequência absoluta de um conjunto de dados."""
    # Dicionário para armazenar a frequência absoluta de cada valor
    freq = {}
    # Calcula a frequência absoluta de cada valor
    for valor in dados:
        freq[valor] = dados.count(valor)
    # Retorna o dicionário contendo a frequência absoluta de cada valor
    return freq
# -----------------------------------------------------------------------------
# Frequência relativa
# -----------------------------------------------------------------------------
def freq_relativa(dados):
    """Cálculo da frequência relativa de um conjunto de dados."""
    freq = {}
    for valor in dados:
        freq[valor] = '{:.1%}'.format(dados.count(valor) / len(dados))
    return freq
# -----------------------------------------------------------------------------
# Média aritmética
# -----------------------------------------------------------------------------
def media_aritmetica(dados):
    """Cálculo da média aritmética de um conjunto de dados."""
    return sum(dados)/len(dados)
# -----------------------------------------------------------------------------
# Moda
# -----------------------------------------------------------------------------
def moda(dados):
    """Cálculo da moda de um conjunto de dados."""
    frequencia = freq_absoluta(dados)
    moda = [num for num, tamanho in frequencia.items() if tamanho == max(list(frequencia.values()))]
    if len(moda) == len(dados):
        return "Não existe moda para esse conjunto de dados"
    else:
        return " A moda é/são: " + ', '.join(map(str, moda))
# -----------------------------------------------------------------------------
# Mediana
# -----------------------------------------------------------------------------
def mediana(dados):
    """Cálculo da mediana de um conjunto de dados."""
    if len(dados) % 2 == 0:
        mediana1 = dados[len(dados)//2]
        mediana2 = dados[len(dados)//2-1]
        mediana = (mediana1 + mediana2)/2
    else:
        mediana = dados[len(dados)//2]
    return mediana
# -----------------------------------------------------------------------------
# Amplitude
# -----------------------------------------------------------------------------
def amplitude(dados):
    """Cálculo da amplitude de um conjunto de dados."""
    return max(dados) - min(dados)
# -----------------------------------------------------------------------------
# Variância populacional
# -----------------------------------------------------------------------------
def variancia_populacional(dados):
    """Cálculo da variância populacional de um conjunto de dados."""
    return sum((valor - media_aritmetica(dados)) ** 2 for valor in dados) / len(dados)
# -----------------------------------------------------------------------------
# Variância amostral
# -----------------------------------------------------------------------------
def variancia_amostral(dados):
    """Cálculo da variância amostral de um conjunto de dados."""
    return sum((valor - media_aritmetica(dados)) ** 2 for valor in dados) / (len(dados) - 1)
# -----------------------------------------------------------------------------
# Desvio padrão populacional
# -----------------------------------------------------------------------------
def desvio_populacional(dados):
    """Cálculo do desvio padrão populacional de um conjunto de dados."""
    return math.sqrt(variancia_populacional(dados))
# -----------------------------------------------------------------------------
# Desvio padrão amostral
# -----------------------------------------------------------------------------
def desvio_amostral(dados):
    """Cálculo do desvio padrão amostral de um conjunto de dados."""
    return math.sqrt(variancia_amostral(dados))
# -----------------------------------------------------------------------------
# Exibe os dados originais
# -----------------------------------------------------------------------------
def exibir_dados(dados):
    """Exibe os valores originais do conjunto de dados."""
    print("\n>>> Dados: %s" %(dados))
# -----------------------------------------------------------------------------
# Menu de opções
# -----------------------------------------------------------------------------
def menu():
    """Menu de opções. Retorna a opção escolhida pelo usuário."""
    print('-' * 40)
    print("Estatística Básica")
    print('-' * 40)
    print()
    print("1. Entrada do conjunto de dados")
    print("2. Exibir conjunto de dados")
    print("3. Frequência absoluta")
    print("4. Frequência relativa")
    print("5. Média aritmética")
    print("6. Moda")
    print("7. Mediana")
    print("8. Amplitude")
    print("9. Variância populacional")
    print("10. Variância amostral")
    print("11. Desvio padrão populacional")
    print("12. Desvio padrão amostral")
    print("13. Limpar o terminal")
    print("0. Encerrar o programa\n")
    return (int(input("Informe sua opção -> ")))
# *****************************************************************************
# 2. Exemplo de utilização das funções
# *****************************************************************************
# Define uma lista inicial para armazenar o conjunto de dados
dados = []
dados_ordenados = []
# Loop infinito, que permite a execução do programa até o usuário digitar 0
while True:
    # Exibe um menu de opções para o usuário escolher o que deseja fazer
    escolha = menu()
    # Entrada do conjunto de dados
    if escolha == 1:
        dados = entrada_dados()
        dados_ordenados = sorted(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
    # Exibe o conjunto de dados
    elif escolha == 2:
        exibir_dados(dados)
        input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula a frequência absoluta
    elif escolha == 3:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n")
        else:
            print("\n-- A frequência absoluta é: %s\n" %(freq_absoluta(dados_ordenados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula a frequência relativa
    elif escolha == 4:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n")
        else:
            print("\n-- A frequência relativa é: %s\n" %(freq_relativa(dados_ordenados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula a média aritmética
    elif escolha == 5:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n")
        else:
            print("\n-- A média aritmética é: %s\n" %(media_aritmetica(dados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula a moda
    elif escolha == 6:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n")
        else:
            print("\n-- %s\n" %(moda(dados_ordenados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula a mediana
    elif escolha == 7:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n") 
        else:
            print("\n-- A mediana é: %s\n" %(mediana(dados_ordenados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula a amplitude
    elif escolha == 8:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n") 
        else:
            print("\n-- A amplitude é: %s\n" %(amplitude(dados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula a variância populacional
    elif escolha == 9:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n") 
        else:
            print("\n-- A variância populacional é: %s\n" %(variancia_populacional(dados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula a variância amostral
    elif escolha == 10:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n") 
        else:
            print("\n-- A variância amostral é: %s\n" %(variancia_amostral(dados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula o desvio padrão populacional
    elif escolha == 11:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n") 
        else:
            print("\n-- O desvio padrão populacional é: %s\n" %(desvio_populacional(dados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Calcula o desvio padrão amostral
    elif escolha == 12:
        if not dados:
            print("\n-- Entre um conjunto de dados para executar esta função! --\n")
            input("\n>>> Pressione <ENTER> para continuar...\n") 
        else:
            print("\n-- O desvio padrão amostral é: %s\n" %(desvio_amostral(dados)))
            input("\n>>> Pressione <ENTER> para continuar...\n")
    # Limpa a tela do terminal
    elif escolha == 13:
    # Verifica o sistema operacional utilizado pelo usuário e
    # utiliza o comando adequado para limpar a tela do terminal
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    # Encerra o programa
    elif escolha == 0:
        print("\n>>> Programa encerrado com sucesso!\n")
        break