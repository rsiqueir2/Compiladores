#Bibliotecas
import string #Para operações com strings string.ascii_letters , punctuations

class Analisa:
    #Passando o arquivo de teste
    def __init__(self):
        self.arquivo_entrada = "Ex-04-incorreto.ptg"

    #Metodo para mudar arquivo de entrada
    def arq_entrada(self, string):
        self.arquivo_entrada = string

    def getEntrada(self):
        return self.arquivo_entrada

    #Verifica se é um delimitador a entrada (; , ou espaço)
    def Delimitador(self, caracter):
        #Delimitdores tk_delimitador
        delimitadores = "; , "
        if caracter in delimitadores:
            return True
        return False

    #Exibe qual dos delimitadores foi usado
    def Token_delimitador(self, entrada):
        #Delimitdores tk_delimitador
        delimitadores = "; , "
        posicao = delimitadores.find(entrada)

    #Manda pra tabela o token e exibe qual deles é
        return "| TOKEN: tk_delimitador | CODIGO: "+str(posicao)

    #Verifica se é alguma letra do alfabeto
    def Letra(self, caracter):
        #Alfabeto de (a..z|A..Z)
        letra = string.ascii_letters
        if caracter in letra:
            return True
        return False

    #Verifica se é um número
    def Numero(self, caracter):
        #Números de 0-9
        digito = string.digits
        if caracter in digito:
            return True
        return False

    #Verifica se é um simbolo da tabela ASCII
    def Simbolo(self, caracter):
        #!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHJKLMNOPQRSTUVXWYZ[\]^_`abcdefghijklmnopqrstuvxwyz{|}~
        simbolos = string.printable
        if (caracter in simbolos):
            return True
        return False

    #Verifica se é um operador Binário, Unario
    def Operador(self, entrada):
        #Operadores
        operadores = ' + - * / = e ou <> > >= < <= := : ( ) nao '.split()
        if entrada in operadores:
            return True
        return False

    #Verifica qual tk_operador é a entrada
    def Token_operador(self, entrada): #Operadores
        operadores = ' + - * / = e ou <> > >= < <= := : ( ) nao '.split()
        posicao = 0
        for x in operadores:
            if x == entrada:
              break
            posicao += 1
        if (posicao == 0):
            return "| TOKEN: tk_mais  | CODIGO: " + str(posicao)# +
        elif (posicao == 1):
            return "| TOKEN: tk_menos  | CODIGO: " + str(posicao)# -
        elif (posicao == 2):
            return "| TOKEN: tk_vezes  | CODIGO: " + str(posicao)# *
        elif (posicao == 3):
            return "| TOKEN: tk_divisao  | CODIGO: " + str(posicao)# /
        elif (posicao == 4):
            return "| TOKEN: tk_igual  | CODIGO: " + str(posicao)# =
        elif (posicao == 5):
            return "| TOKEN: tk_e  | CODIGO: " + str(posicao)# e
        elif (posicao == 6):
            return "| TOKEN: tk_ou | CODIGO: " + str(posicao)# ou
        elif (posicao == 7):
            return "| TOKEN: tk_diferente  | CODIGO: " + str(posicao)# <>
        elif (posicao == 8):
            return "| TOKEN: tk_maior  | CODIGO: " + str(posicao)# >
        elif (posicao == 9):
            return "| TOKEN: tk_maior_igual  | CODIGO: " + str(posicao)# >=
        elif (posicao == 10):
            return "| TOKEN: tk_menor  | CODIGO: " + str(posicao)# <
        elif (posicao == 11):
            return "| TOKEN: tk_menor_igual  | CODIGO: " + str(posicao)# <=
        elif (posicao == 12):
            return "| TOKEN: tk_atribuicao  | CODIGO: " + str(posicao)# :=
        elif (posicao == 13):
            return "| TOKEN: tk_dois_pontos | CODIGO: " + str(posicao)# :
        elif (posicao == 14):
            return "| TOKEN: tk_abre_par  | CODIGO: " + str(posicao)# (
        elif (posicao == 15):
            return "| TOKEN: tk_fecha_par | CODIGO: " + str(posicao)# )
        elif (posicao == 16):
            return "| TOKEN: tk_nao  | CODIGO: " + str(posicao)# nao

    #Verifica se é uma palavra reservada da linguagem
    def Reservada(self, entrada):
        #Plavras reservadas
        palavra_reservada = "programa fim_programa caso fim_caso entao senao para de ate fim_para passo leia imprima " \
        "inteiro decimal cadeia".split()
        if entrada in palavra_reservada:
          return True
        return False

    #Verifica qual tk_palavra_reservada é a entrada
    def Token_reservada(self, entrada): 
      #Palavras reservadas
        palavra_reservada = '''programa fim_programa caso fim_caso entao senao para de ate fim_para passo leia 
        imprima inteiro decimal cadeia'''.split()
        posicao = 0
        for x in palavra_reservada:
            if x == entrada:
              break
            posicao += 1
        if (posicao == 0):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #programa
        elif (posicao == 1):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #fim progrma
        elif (posicao == 2):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #caso
        elif (posicao == 3):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #fim caso
        elif (posicao == 4):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #entao
        elif (posicao == 5):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #senao
        elif (posicao == 6):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #para
        elif (posicao == 7):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #de
        elif (posicao == 8):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #ate
        elif (posicao == 9):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #fim para
        elif (posicao == 10):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #passo
        elif (posicao == 11):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #leia
        elif (posicao == 12):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #imprima
        elif (posicao == 13):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #inteiro
        elif (posicao == 14):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #decimal
        elif (posicao == 15):
          return "| TOKEN: tk_palavra_reservada | CODIGO: "+ str(posicao) #cadeia
        
    #################ANALISADOR######################
    def analisa(self):
        #Abre o arquivo de entrada
        arquivo = open(self.arquivo_entrada, 'r')
        print('######LISTA DE TOKENS RECONHECIDOS######\n')
       
        #Le a primeira linha
        linha = arquivo.readline()

        #Variavel que indica a linha do caracter
        linha_atual = 1

        #Contador de erros
        errolexico = 0

        while linha:
            i = 0
            tamanho_linha = len(linha)
            while i < tamanho_linha: 
              #Verifica os caracteres por caracteres
                caracter = linha[i]
                caractere_seguinte = None
              #Se existe caracter exibe
                if (i + 1) < tamanho_linha:
                    caractere_seguinte = linha[i + 1]

                #Verifica se é delimitador
                if self.Delimitador(caracter):
                        print(self.Token_delimitador(caracter) + ' | ITEM: ' + caracter + ' | LINHA: ' + str(
                            linha_atual) + '\n')
                
                #verifica comentários //COMENTARIO
                elif (caracter == '/' and caractere_seguinte == '/'):
                    # Fazendo o programa pular para a proxima linha
                    i = tamanho_linha
                
                #Comentario de bloco /*COMENTARIO*/
                elif (caracter == '/' and caractere_seguinte == '*'):
                    cont = True  
                    linha_comeco = linha_atual  
                    while cont and not (caracter == '*' and caractere_seguinte == '/'):
                        #Se existe na linha exibe
                        if ((i + 2) < tamanho_linha):
                            i += 1
                            caracter = linha[i]
                            caractere_seguinte = linha[i + 1]
                        else:
                            linha = arquivo.readline()  
                            #Le a proxima linha
                            tamanho_linha = len(linha)
                            linha_atual += 1
                            i = -1
                            if (not linha):
                                print("| ERRO COMENTARIO DE BLOCO NAO FECHADO | LINHA: %d\n" % linha_comeco)
                                errolexico += 1
                                cont = False
                    i += 1 
                  # Verificando se é um operador
                elif caractere_seguinte != None and self.Operador(caracter + caractere_seguinte):
                    print(self.Token_operador(
                        caracter + caractere_seguinte) + ' | CODIGO:' + caracter + caractere_seguinte + ' | LINHA:' + str(
                        linha_atual) + '\n')
                    i += 1
                elif self.Operador(caracter):
                    print(
                        self.Token_operador(caracter) + ' | ITEM: ' + caracter + ' | LINHA: ' + str(
                            linha_atual) + '\n')
                
                # Verificando se o elemento é caractere constante  
                elif (caracter == string.punctuation[6]):

                    if (linha[i + 1] == '\n') or (not (string.punctuation[6] in linha[i + 1:])):
                        print('ERRO LEXICO CARACTER NAO FECHADO | LINHA: %d\n' % linha_atual)
                        errolexico += 1
                        i = tamanho_linha
                    elif linha[i + 1] == string.punctuation[6] and linha[i + 2] == string.punctuation[
                        6]:
                        print(
                            'ERRO LEXICO CARACTER NAO PODE SER ASPAS SIMPLES | LINHA: %d\n' % linha_atual)
                        errolexico += 1
                        i += 2
                    elif linha[i + 1] == string.punctuation[6]:
                        print('ERRO LEXICO CARACTER NAO PODE SER VAZIO | LINHA: %d\n' % linha_atual)
                        errolexico += 1
                        i += 1
                    else:
                        print(
                            'ERRO LEXICO TAMANHO OU SIMBOLO INVALIDO | LINHA: %d\n' % linha_atual)
                        errolexico += 1
                        i = linha[i + 1:].find(string.punctuation[6]) + 1

                elif (caracter == string.punctuation[1]):
                    i += 1  #Para passar a primeira ocorrencia do caractere "
                    Valido = True

                    # Se a linha possui somente ", significa que a string nao foi fechada
                    if linha[i:].find(string.punctuation[1]) == -1:
                        print('| ERRO STRING NAO FECHADA | LINHA: %d\n' % linha_atual)
                        errolexico += 1
                        i = tamanho_linha
                    else:
                        fim_cadeia = i + linha[i:].find(string.punctuation[1])
                        nova_cadeia = linha[i:fim_cadeia]
                        i = fim_cadeia
                        for x in nova_cadeia:
                            if not self.Simbolo(x):
                                Valido = False
                                print(
                                    '| ERRO STRING INVALIDA FORA DA TABELA ASCII: '+ caracter + ' | LINHA: %d\n' % linha_atual)
                                errolexico += 1
                                break
                        if Valido:
                            print(
                                '| TOKEN: tk_cadeia | LEXEMA: ' + nova_cadeia + ' | LINHA: ' + str(linha_atual) + '\n')
                
                #Verifica se é número 0-9
                elif self.Numero(caracter):
                    string_temp = caracter
                    i += 1
                    j = 0  # Conta se o numero tem pelo menos 1 digito depois do '.'
                    caracter = linha[i]
                    while self.Numero(caracter) and (i + 1 < tamanho_linha):
                        string_temp += caracter
                        i += 1
                        caracter = linha[i]

                    if (caracter == '.'):
                        if ((i + 1) < tamanho_linha):
                            string_temp += caracter
                            i += 1
                            caracter = linha[i]
                            while self.Numero(caracter) and i + 1 < tamanho_linha:
                                j += 1
                                string_temp += caracter
                                i += 1
                                caracter = linha[i]

                            if (caracter == '.'):
                                j = 0
                                while (i + 1 < tamanho_linha):
                                    i += 1
                                    caracter = linha[i]
                                    if self.Delimitador(caracter) or caracter == ' ':
                                        i -= 1  
                                        break
                        else:
                            print('| ERRO LEXICO NUMERO EM FORMATO INCORRETO | LINHA: %d\n' % linha_atual)
                            errolexico += 1

                        if (j > 0):
                            print('| TOKEN: tk_decimal | CODIGO: ' + string_temp + '| LINHA: ' + str(linha_atual) + '\n')
                        else:
                            print('| ERRO LEXICO NUMERO EM FORMATO INCORRETO | LINHA: %d\n' % linha_atual)
                            errolexico += 1
                    else:
                        print('| TOKEN: tk_inteiro | ITEM: ' + string_temp + ' | LINHA: ' + str(linha_atual) + '\n')
                        if (not self.Numero(caracter)):
                            i -= 1
                # Verifica palavras reservadas e identificadores
                elif (self.Letra(caracter)):
                    #Se for letra segue até achar algo que não seja letra entre o meio e fim
                    string_temp = caracter
                    i += 1
                    algum_erro = False
                    while i < tamanho_linha:
                        caractere_seguinte = None
                        caracter = linha[i]
                        if (i + 1 < tamanho_linha):
                            caractere_seguinte = linha[i + 1]
                        if (self.Letra(caracter) or self.Numero(caracter) or caracter == '_'):
                            string_temp += caracter
                        elif (self.Delimitador(
                                caracter) or caracter == ' ' or caracter == '\t' or caracter == '\r'):
                            i -= 1 
                            break
                        elif (caractere_seguinte != None and self.Operador(
                                caracter + caractere_seguinte)) or self.Operador(caracter):
                            i -= 1
                            break
                        elif caracter != '\n':
                            print(
                                "| ERRO LEXICO IDENTIFICADOR COM CARACTER NAO PERMITIDO: " + caracter + " | LINHA: %d\n" % linha_atual)
                            errolexico += 1
                            algum_erro = True
                            break
                        i += 1  #Verificando arquivo ate identificador/palavra reservada

                    if (algum_erro):
                        while (i + 1 < tamanho_linha):
                            i += 1
                            caracter = linha[i]
                            if self.Delimitador(
                                    caracter) or caracter == ' ' or caracter == '\t' or caracter == '\r' or caracter == '/':
                                i -= 1  
                                break
                    else:  # Se não existir erros só verificar se é palavra reservada
                        if (self.Reservada(string_temp)):
                            print(self.Token_reservada(
                                string_temp) + ' | PALAVRA RESERVADA: ' + string_temp + ' | LINHA: ' + str(
                                linha_atual) + '\n')
                        else:
                            print(
                                '| TOKEN: tk_identificador | LEXEMA: ' + string_temp + '  | LINHA: ' + str(
                                    linha_atual) + '\n')
                #Caracter Invalido
                elif caracter != '\n' and caracter != " " and caracter != '\t':
                    print('| ERRO LEXICO CARACTER INVALIDO: ' + caracter + ' | LINHA: %d\n' % linha_atual)
                    errolexico += 1
   
                i += 1  #Incrementando a leitura dos caracteres da linha lida no momento
       
            linha = arquivo.readline()  #Le a proxima linha
            linha_atual += 1

        ##########ERROS LEXICOSSSS###########  
        print ("########LISTA DE ERROS LEXICOS########\n")

        #Abrindo o arquivo de origem
        arquivo_entrada = open('Ex-04-incorreto.ptg', 'r')
        conteudo = arquivo_entrada.readlines()

        #inserindo o rodapé de conteúdo
        conteudo.append('\n\nTOTAL DE ERROS:')

        #Escrevendo o conteudo da origem em um novo arquivo que exibe os erros
        arquivo_saida = open('Ex-04-incorreto-Erros.ptg', 'a')
        arquivo_saida.writelines("LISTA DE ERROS LEXICOS\n\n")
        arquivo_saida.writelines(conteudo)
        arquivo_saida.close()

        #Exibir no console
        f = open("Ex-04-incorreto-Erros.ptg", "r")
        print(f.read())
        print (errolexico)

        ##########Erros TABELA DE SIMBOLOS###########  
        print ("\n########TABELA DE SIMBOLOS########\n")
        

#Inicia
lexico = Analisa()
lexico.analisa()