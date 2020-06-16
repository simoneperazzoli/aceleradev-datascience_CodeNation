
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# Reading dataset .csv file
black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[3]:


# Checking dataset head
black_friday.head(10)


# In[4]:


# Checking dataset information
black_friday.info()


# In[5]:


# Getting info about dtypes, null values and its amount in dataset
dataset_characteristics = pd.DataFrame({'Data_Type': black_friday.dtypes,
                                     'Missing_Values': black_friday.isna().sum(),
                                     '%_Missing_Values': (black_friday.isna().sum() / black_friday.shape[0]) * 100})                          
dataset_characteristics


# In[6]:


#Checking some basic statistics by using describe method
black_friday.describe()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[7]:


def q1():
    return black_friday.shape
q1()


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[8]:


def q2():
    return len(black_friday[(black_friday['Gender'] == 'F') & (black_friday['Age'] == '26-35')])
q2()


# ## Questão 3
# 
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[9]:


def q3():
    q3 = len(black_friday.groupby('User_ID')['User_ID'])
    return int(q3)
q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[10]:


def q4():
    return black_friday.dtypes.nunique()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[11]:


def q5():
    return float(1 - len(black_friday.dropna()) / len(black_friday))
q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[12]:


def q6():
    na_values = black_friday.isna()
    na_count = na_values.apply(pd.Series.value_counts).loc[True]
    return int(na_count.max())
q6()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[13]:


def q7():
    return black_friday['Product_Category_3'].value_counts().idxmax()
q7()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[14]:


def q8():
    data = black_friday['Purchase']
    normalized_data=(data-data.min())/(data.max()-data.min())
    return float(normalized_data.mean())
q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[15]:


def q9():
    purchase = black_friday['Purchase']
    purchase_score = (purchase - purchase.mean())/purchase.std(ddof=0)
    return int(len(purchase_score[(purchase_score > -1) & (purchase_score < 1)]))
q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[16]:


def q10():
    compare = black_friday[['Product_Category_2', 'Product_Category_3']]
    compare = compare[compare['Product_Category_2'].isna()]
    return compare['Product_Category_2'].equals(compare['Product_Category_3'])
q10()

