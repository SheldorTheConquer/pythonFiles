#!/usr/bin/env python
# -*- encoding: utf-8 -*-


#GERADOR DE SENHAS ALEATÓRIAS
#Jhonatas Albuquerque
#albuquerquejhonatas@gmail.com
#sheldortheconquer@protonmail.com
#v0.1


import random

tamanhoDaSenha = int(input("Digite o tamanho da senha: "))
while tamanhoDaSenha < 6:
        tamanhoDaSenha = int(input("\nDigite novamente o tamanho da senha, é necessário ser mais que 5: "))

numeros = str(input("\nDigite 'S' - Sim ou 'N' - Não para números na senha: "))
numeros = numeros.upper()

while numeros != "S" and numeros !="N":
        numeros = str(input("Digite 'S' - Sim ou 'N' - Não para números na senha: "))


caractereEspecial = str(input("\nDigite 'S' - Sim ou 'N' - Não para caracteres especiais na senha: "))
caractereEspecial = caractereEspecial.upper()

while caractereEspecial != "S" and caractereEspecial !="N":
                caractereEspecial = str(input("Digite 'S' - Sim ou 'N' - Não para caracteres especiais na senha: "))


#'numeros' e 'caractereEspecial' como parametros pra que a função posssa trabalhar internamente com as estruturas de condição
def gerarSenha(tamanhoDaSenha, numeros, caractereEspecial):
        letter = 'abcdefghijlmnopqrstuwvxz'
        number = '0123456789'
        especial = '!()-.?[]`~'
        password = ''
        aux = 0

        #só letras 
        if numeros == "N" and caractereEspecial == "N":
                for aux in range(tamanhoDaSenha):
                        password +=str(random.choice(letter))

        #só numeros e letras
        if numeros == "S" and caractereEspecial == "N":
                for aux in range(tamanhoDaSenha):
                        password += str(random.choice(letter+number))

        #só caracteres especiais e letras
        if numeros == "N" and caractereEspecial == "S":
                for aux in range(tamanhoDaSenha):
                        password += str(random.choice(letter+especial))

        #todas as opções
        if numeros == "S" and caractereEspecial == "S":
                for aux in range(tamanhoDaSenha):
                        password += str(random.choice(letter+number+especial))
        
        return password


print(gerarSenha(tamanhoDaSenha, numeros, caractereEspecial))
