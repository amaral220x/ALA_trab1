# Gabriel Amaral - 121069963
# Mariana Furriel da Silva Siqueira - 121088886
# Rafaela 

# Rode o código para visualizar o passo a passo da fatoração

import numpy as np

def troca(b,c,i,j): #i e j são linhas para c e colunas para b
    c[[i,j]] = c[[j,i]] #trocando linha
    b[:,[i,j]] = b[:,[j,i]] #trocando coluna

def encol_estica(b,c,i,alfa): 
    b_linhas,_ = b.shape
    _,c_colunas = c.shape

    for j in range(b_linhas):
      b[j][i] = b[j][i]*alfa
    for j in range(c_colunas):
      c[i][j] = c[i][j]/alfa

def soma_subtrai(b,c,i,j,alfa): #faz l_i<-l_i - alfa* l_j em c e c_j<-c_j+ alfa*c_i
	b_linhas,_ = b.shape
	_,c_colunas = c.shape
	for k in range(b_linhas):
		b[k][i] =  b[k][i] + b[k][j]*alfa
	for k in range(c_colunas):
		c[j][k] = c[j][k]-c[i][k]*alfa

#Inicialização do processo de fatoração, atribuindo b como identidade e c como a
matrizA = np.array([[2.0,4.0,1.0,8.0,11.0,101.0],[2.0,4.0,2.0,8.0,12.0,102.0],[2.0,4.0,3.0,8.0,13.0,103.0],[2.0,4.0,4.0,8.0,14.0,104.0]])
matrizB = np.array(np.matrix(np.identity(4)))
matrizC = matrizA

encol_estica(matrizB,matrizC,0,2) #Dividindo a linha 1 (ou 0) por 2 (nossa "janela")
print("Matriz B e C pos encolhe estica")
print(matrizB)
print("----")
print(matrizC)

#Diminuindo as linhas dos seus 
for x in range(1,4):
  soma_subtrai(matrizB, matrizC, 0, x, matrizC[x][0])
print("Matriz C pós subtração")
print(matrizC)

#Trocamos e de linha e avistamos uma sequencia nula na coluna 2. Então nossa "Janela" foi para a coluna 3 onde temos um 1
#É preciso forçar o aparecimento de 1 e zerar o restante. 
encol_estica(matrizB,matrizC,1,1) 
print("Matriz C pos encolhe estica")
print(matrizC)
for x in range(4):
  if x!=1:
    soma_subtrai(matrizB, matrizC, 1, x, matrizC[x][2])

print("Matriz C pos subtração")
print(matrizC)

#Fatoração completa, pois as "Janelas" restantes possiveis são nulas
print("___________________________________________")
print("MatrizB e C resultantes da fatoração")
print(matrizB,"\n")
print(matrizC)



#Testes 
#matriz1 = np.arange(12.0).reshape(4,3)
#print("Matriz1 de exemplo")
#print(matriz1)
#print("\n")

#matriz2 = np.arange(12.0).reshape(4,3)
#print(matriz2)

# troca(matriz1,matriz2,1,2)
# print(matriz1)
# print(matriz2)

#encol_estica(matriz1,matriz2, 0,3)
#print(matriz1)
#print(matriz2)

# soma_subtrai(matriz1,matriz2,1,2,2)
# print("\n")
# print(matriz1)
# print("\n")
# print(matriz2)


