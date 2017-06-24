#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#GERADOR DE SENHAS ALEATÓRIAS
#Jhonatas Albuquerque
#albuquerquejhonatas@gmail.com
#sheldortheconquer@protonmail.com
#v0.1

import random

#define tamanho da senha
tamanhoDaSenha = int(input("Digite o tamanho da senha: "))
while tamanhoDaSenha < 6:
        tamanhoDaSenha = int(input("\nDigite novamente o tamanho da senha, é necessário ser mais que 5: "))

#opções de senha       
numeros = str(input("\nDigite 'S' - Sim ou 'N' - Não para números na senha: "))
numeros = numeros.upper()
while numeros != "S" and numeros !="N":
        numeros = str(input("\nDigite 'S' - Sim ou 'N' - Não para números na senha: \n"))


#opções de senha
caractereEspecial = str(input("\nDigite 'S' - Sim ou 'N' - Não para caracteres especiais na senha: \n"))
caractereEspecial = caractereEspecial.upper()
while caractereEspecial != "S" and caractereEspecial !="N":
                caractereEspecial = str(input("\nDigite 'S' - Sim ou 'N' - Não para caracteres especiais na senha: \n"))


#'numeros' e 'caractereEspecial' como parametros pra que a função posssa trabalhar internamente com as estruturas de condição
def gerarSenha(tamanhoDaSenha, numeros, caractereEspecial):
        letter = 'abcdefghijlmnopqrstuwvxz'
        number = '0123456789'
        especial = '!()-.?[]~'
        password = ''
        aux = 0

        #somente letras 
        if numeros == "N" and caractereEspecial == "N":
                for aux in range(tamanhoDaSenha):
                        password +=str(random.choice(letter))

        #somente numeros e letras
        if numeros == "S" and caractereEspecial == "N":
                for aux in range(tamanhoDaSenha):
                        password += str(random.choice(letter+number))

        #somente caracteres especiais e letras
        if numeros == "N" and caractereEspecial == "S":
                for aux in range(tamanhoDaSenha):
                        password += str(random.choice(letter+especial))

        #todas as opções
        if numeros == "S" and caractereEspecial == "S":
                for aux in range(tamanhoDaSenha):
                        password += str(random.choice(letter+number+especial))
        
        return password

#mostra mais de uma senha pra que o usuário possa escolher dentre as possibilidades
i = 0
log = open('log.txt', 'a+') #abre o arquivo para a gravação no final
while i<10: 
        senhas = gerarSenha(tamanhoDaSenha, numeros, caractereEspecial)
        log.writelines(senhas+'\n')#esreve uma senha, linha por linha. além de listar as que já foram utilizadas
        print(senhas)
        i+=1

log.close()
