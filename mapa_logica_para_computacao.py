# **MAPA - LÓGICA PARA COMPUTAÇÃO**


#Importando a bibliotecas para Análise de Dados
import pandas as pd
import numpy as np
from matplotlib_venn import venn3, venn3_circles
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# Definindo dataframe
mapa = pd.read_excel("/content/drive/MyDrive/datasets/MAPA - LÓGICA PARA COMPUTAÇÃO.xlsx")

# Exibindo as 5 primeiras linhas
mapa.head()

# Exibindo as 5 ultimas linhas
mapa.tail()

# Verificando as dimensões do dataset.
mapa.shape

# Verificando o número de registros duplicados.
mapa.duplicated().sum()

# Verificando o número de NAs existentes dentro do dataset.
mapa.isna().sum()

#Retorna o tipo de dados das colunas
mapa.dtypes

#Alterando tipo da coluna para Float
mapa["Valor mercado"] = mapa["Valor mercado"].astype(float)

# Atribuindo uma coluna (Area construida) a uma lista (ac). 
ac = mapa["Área construída"].tolist()

# Criando conjunto de dados para o quadrande A.
conjunto_A = [number for number in ac if number < 150]

# Criando conjunto de dados para o quadrande B.
conjunto_B = [number for number in ac if number >= 100 and number <250]

# Criando conjunto de dados para o quadrande C.
conjunto_C = [number for number in ac if number >= 200 and number <380]

#Valores entre o quadrante A^B
AintersecB = [x for x in conjunto_A if x in conjunto_B]
print (AintersecB)

#Valores que estão somente no quandrante A
AdifeB = [x for x in conjunto_A if x not in conjunto_B]
print (AdifeB)

#Valores que estão somente no quandrante B
vari1 = [x for x in conjunto_B if x not in conjunto_A]
vari2 = [x for x in conjunto_B if x in conjunto_C]
BdifeA = [x for x in vari1 if x not in vari2]
print (BdifeA)

#Valores entre o quadrante B^C
BintersecC = [x for x in conjunto_B if x in conjunto_C]
print (BintersecC)

#Valores que estão somente no quandrante C
CdifeB = [x for x in conjunto_C if x not in conjunto_B]
print (CdifeB)

# Quantidade de dados por lista.
print (len(conjunto_A)) #Todos os valores pertencentes a quandrante A [50;50[
    
print (len(conjunto_B)) #Todos os valores pertencentes a quandrante B [100;250[
    
print (len(conjunto_C)) #Todos os valores pertencentes a quandrante B [200;380]

AiB = (len(AintersecB)) #Valores entre o quadrante A^B

A = (len(AdifeB)) #Valores que estão somente no quandrante A

B = (len(BdifeA)) #Valores que estão somente no quandrante B

BiC = (len(BintersecC)) #Valores entre o quadrante B^C

C = (len(CdifeB)) #Valores que estão somente no quandrante C

"""# **Visualização de Dados**"""

#Diagrama de Venn dos Conjuntos
venn3(subsets = (A,B,AiB,C,0,BiC,0), 
      set_labels = ('Conjunto A', 'Conjunto B', 'Conjunto C'), 
      alpha = 0.5);

# Grafico de dispersão da Area Construida X Valor de mercado
plt.scatter(x=mapa["Área construída"], y=mapa["Valor mercado"])
plt.ticklabel_format(style='plain', axis='y');
plt.show()

