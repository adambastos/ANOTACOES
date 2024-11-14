"""
Comentário de múltiplas linhas
"""
#Comentário de uma linha

#Importando um arquivo dentro do outro
import tipo.variaveis            #Tenho o arquivo index.py e importei dentro dele o arquivo variáveis que está dentro da pasta tipo
from tipo import variaveis       #Outra forma de fazer o mesmo import


#Concatenando variável com String utilizando o método "String" + str(...variável) + "String"
idade = 26
print("Adam tem " + str(idade) + " anos")
Adam tem 26 anos

#Concatenando utilizando o método f-strings. Tudo que estiver entre {} será interpretado como código python
idade = 26
print(f'{idade}')

