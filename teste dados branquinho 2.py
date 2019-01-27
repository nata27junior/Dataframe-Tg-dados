
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_excel('Dados de consumo.xlsx',parse_dates=['Data e Hora'])


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df['Data e Hora'] = pd.to_datetime(df['Data e Hora'])
df['Data'] = df['Data e Hora'].dt.strftime('%d-%m-%Y')
df['Hora'] = df['Data e Hora'].dt.strftime('%H:%M:%S')
df['Semana'] = df['Data e Hora'].dt.strftime('%A')


# In[6]:


df.head()


# In[7]:


df.describe()


# In[8]:


df.mean()


# In[9]:


del df['Data e Hora']


# In[10]:


df.head()


# In[11]:


df.tail()


# In[12]:


df.describe()


# In[13]:


df=df[['Data','Hora','Semana','Consumo(litros)','Valor Acumulado']]


# In[14]:


df.index


# In[15]:


df.head()


# In[16]:


df2=df.drop([1])


# In[17]:


df2.head()


# In[18]:


df.tail(15)


# In[19]:


df=df.drop([0,1,2,3,4021,4022,4023,4024,4025,4026,4027,4028,4029,4030,4031,4032])


# In[20]:


df.head()


# In[21]:


df.describe()


# In[22]:


for i in df['Consumo(litros)']:
    if i >= 300:
        print(i)


# In[23]:


df['Data'][df['Consumo(litros)']>=300]


# In[24]:


df['Consumo(litros)'][df['Data']=='16-01-2018'].mean()


# In[25]:


df['Consumo(litros)'][df['Data']=='16-01-2018'].sum()


# plt.figure(figsize=(20,10))
# dataunicas=df['Data'].unique()
# lista=[]
# for i in dataunicas:
#     medias=float(df['Consumo(litros)'][df['Data']==i].mean())
#     lista.append((i,medias))
# plt.plot(lista)
# plt.grid(True)
# plt.xticks(rotation=45,fontsize='15')
# plt.yticks(fontsize='15')
#     
#     

# In[26]:


dataunicas=df['Data'].unique()
lista=[]
for i in dataunicas:
    medias=float(df['Consumo(litros)'][df['Data']==i].mean())
    lista.append((i,medias))
df2 = pd.DataFrame(lista)
df2.columns = ['Data', 'Médias (Litros)']


# In[27]:


df2.head()


# In[28]:


df2['Data'][df2['Data']=='01-09-2017']


# In[29]:


df2['Data'][df2['Data']=='30-09-2017']


# In[30]:


df2['Data'][df2['Data']=='01-10-2017']


# In[31]:


df2['Data'][df2['Data']=='27-10-2017']


# In[32]:


df2.loc[10:39,'Data']


# In[33]:


a= df2.loc[10:36,'Médias (Litros)']#total consumo 01-09; 30/09
b= df2.loc[40:66,'Médias (Litros)']#consumo 01-10; 27/10

def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)
lista_distancia=[]
for i in range(len(a)):
    sub = dist_euclidiana_np(a[10+i], b[40+i])
    lista_distancia.append(sub)
#print(lista)
#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(a, b)))
print(len(a))
print(len(b))
print(len(lista_distancia))


# In[34]:


import datetime
tempo=df2.loc[10:39,'Data']
a= df2.loc[10:39,'Médias (Litros)']#media consumo 01-09; 30/09
b= df2.loc[40:66,'Médias (Litros)']#consumo 01-10; 27/10
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[10+i])
    i+=1
while l< len(b) :
    d.append(b[40+l])
    l+=1

for i in tempo:
    tempo1.append(i)


plt.figure(figsize=(20,10))
plt.plot(c,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(tempo1)), rotation=90,fontsize='15')
plt.yticks(fontsize='15')
plt.legend(('Setembro','Outubro','Distancia E'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação medias entre setembro e outubro consumo",fontsize='20')
plt.savefig('comparação medias entre dois meses consumo com distancia e.png')


# In[35]:


dataunicas=df['Data'].unique()
lista=[]
for i in dataunicas:
    somas=float(df['Consumo(litros)'][df['Data']==i].sum())
    lista.append((i,somas))
df3 = pd.DataFrame(lista)
df3.columns = ['Data', 'Soma (Litros)']


# In[36]:


df3.head()


# In[37]:


a= df3.loc[10:36,'Soma (Litros)']#total consumo 01-09; 30/09
a


# In[38]:


b= df3.loc[40:66,'Soma (Litros)']#consumo 01-10; 27/10
b


# a= df3.loc[10:36,'Soma (Litros)']#total consumo 01-09; 30/09
# lista=[]
# for i in range(len(a)):
#     #sub = dist_euclidiana_np(a[10+i], b[40+i])
#     #lista.append(sub)
#     print(i)

# In[39]:


a= df3.loc[10:36,'Soma (Litros)']#total consumo 01-09; 30/09
b= df3.loc[40:66,'Soma (Litros)']#consumo 01-10; 27/10

def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)
lista_distancia=[]
for i in range(len(a)):
    sub = dist_euclidiana_np(a[10+i], b[40+i])
    lista_distancia.append(sub)
#print(lista)
#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(a, b)))
print(len(a))
print(len(b))
print(len(lista_distancia))


# In[40]:


import datetime
tempo=df3.loc[10:39,'Data']
a= df3.loc[10:39,'Soma (Litros)']#media consumo 01-09; 30/09
b= df3.loc[40:66,'Soma (Litros)']#consumo 01-10; 27/10
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[10+i])
    i+=1
while l< len(b) :
    d.append(b[40+l])
    l+=1

for i in tempo:
    tempo1.append(i)




plt.figure(figsize=(20,10))
plt.plot(c,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(tempo1)), rotation=90,fontsize='15')
plt.yticks(fontsize='15')
plt.legend(('Setembro','Outubro','Distancia E'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação total diario entre setembro e outubro consumo",fontsize='20')
plt.savefig('comparação total diario entre dois meses consumo com distancia e.png')


# In[41]:


df2.tail()


# In[42]:


df2.to_excel('medias.xlsx')
df3.to_excel('somas.xlsx')


# In[43]:


df2['Data'].head()


# In[44]:


len(df2)


# In[45]:


len(df3)


# In[46]:


df2['Data'].tail()


# In[47]:


df2.loc[:17]


# In[48]:


data=df2.loc[:80,'Data']
a=[]
for i in df2.loc[:80,'Data']:
    a.append(i)
df2.loc[:80].plot.line(marker='o',style='r--', figsize=(20,10))
plt.title('Grafico Médias Diárias Detalhado',fontsize='20') #adicionando o título
plt.xlabel('Datas',fontsize='20')
plt.ylabel('Médias (Litros)',fontsize='20')
plt.xticks(np.arange(len(data)),data,rotation=90,fontsize='10')
plt.yticks(fontsize='20')
plt.legend('Médias (Litros)',loc='upper center', fontsize='15')

plt.grid(True)
plt.savefig('Grafico Médias Diárias(este com zoom).png')


# In[49]:


data=df3.loc[:80,'Data']
a=[]
for i in df3.loc[:80,'Data']:
    a.append(i)
df3.loc[:80].plot.line(marker='o',style='g--', figsize=(20,10))
plt.title('Grafico Soma Diárias Detalhado',fontsize='20') #adicionando o título
plt.xlabel('Datas',fontsize='20')
plt.ylabel('Soma (Litros)',fontsize='20')
plt.xticks(np.arange(len(data)),data,rotation=90,fontsize='10')
plt.yticks(fontsize='20')
plt.legend('Soma (Litros)',loc='upper center', fontsize='15')

plt.grid(True)
plt.savefig('Grafico Soma Diárias(este com zoom).png')


# In[50]:


data=df2['Data']
a=[]
for i in df2['Data']:
    a.append(i)
df2.plot.line(marker='o',style='r--', figsize=(30,10))
plt.title('Grafico Médias Diárias',fontsize='20') #adicionando o título
plt.xlabel('Datas',fontsize='20')
plt.ylabel('Médias (Litros)',fontsize='20')
plt.xticks(np.arange(len(data)),data,rotation=90,fontsize='10')
plt.yticks(fontsize='20')
plt.legend('Médias (Litros)',loc='upper center', fontsize='15')

plt.grid(True)
plt.savefig('Grafico Médias Diárias(este).png')


# In[51]:


data=df3['Data']
a=[]
for i in df3['Data']:
    a.append(i)
df3.plot.line(marker='o',style='g--', figsize=(30,10))
plt.title('Grafico Somas Diárias',fontsize='20') #adicionando o título
plt.xlabel('Datas',fontsize='20')
plt.ylabel('Somas (Litros)',fontsize='20')
plt.xticks(np.arange(len(data)),data,rotation=90,fontsize='10')
plt.yticks(fontsize='20')
plt.legend(('Somas (Litros)'),loc='upper center', fontsize='15')

plt.grid(True)
plt.savefig('Grafico Somas Diárias(este).png')


# In[52]:


df_merge=pd.merge(df2,df3)


# In[53]:


df_merge.head()


# In[54]:


data=df_merge['Data']
a=[]
for i in df_merge['Data']:
    a.append(i)
df_merge.plot.line(marker='o',figsize=(30,10))
plt.title('Grafico Somas e Medias Diárias',fontsize='20') #adicionando o título
plt.xlabel('Datas',fontsize='20')
#plt.ylabel('Somas (Litros)',fontsize='20')
plt.xticks(np.arange(len(data)),data,rotation=90,fontsize='10')
plt.yticks(fontsize='20')
plt.legend(('Media','Soma'),loc='best', fontsize='15')

plt.grid(True)
plt.savefig('Grafico Somas e Medias Diárias(este).png')


# x=df2['Data']
# y=df2['Médias (Litros)']
# #sns.lineplot(x,y, color="coral", label="Médias")
# sns.lineplot(x="Data", y="Médias (Litros)", data=df2, label="Médias",sizes=(20,10))

# In[55]:


a=df2['Data']
b=df2['Médias (Litros)']
plt.figure(figsize=(40,10))#largura e altura
plt.grid(True)
plt.plot(a,b,'r',marker='s')

plt.xticks(rotation=90,fontsize='18')
plt.yticks(fontsize='20')
plt.title("Grafico Médias Diárias",fontsize='25')
plt.savefig('Grafico Médias Diárias.png')


# In[56]:


a=df3['Data']
b=df3['Soma (Litros)']
plt.figure(figsize=(40,10))#largura e altura
plt.grid(True)
plt.plot(a,b,'g',marker='s')

plt.xticks(rotation=90,fontsize='18')
plt.yticks(fontsize='20')
plt.title("Grafico Total de Consumo Diário",fontsize='25')
plt.savefig('Grafico Total Diário.png')


# In[57]:


a=df2['Data']
b=df2['Médias (Litros)']
plt.scatter(a,b)


# In[58]:


df['Consumo(litros)'][df['Data']].mean()


# In[59]:


from datetime import datetime
plt.figure(figsize=(20,10))
#data = input('data  [d-m-Y]: ')
data = ['16-05-2018','15-05-2018']
marque = ['s','p','*','D']
for i in range(len(data)):
    data1 = datetime.strptime(data[i], "%d-%m-%Y").strftime('%d-%m-%Y')
    plt.plot(df['Hora'][df['Data']==data1], df['Consumo(litros)'][df['Data']==data1],marker=marque[i])
plt.legend(data,loc='upper center', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.xticks(rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title("Grafico comparação entre os dias com maior consumo",fontsize='20')
plt.savefig('comparação entre os dias com maior consumo.png')


# In[60]:


df[df['Data']=='16-01-2018']


# In[61]:


df[df['Data']=='14-01-2018']


# In[62]:


df[df['Data']=='15-05-2018']


# In[63]:


df[df['Data']=='16-05-2018']


# In[64]:


df['Consumo(litros)'][df['Data']=='15-05-2018']


# In[65]:


import datetime
tempo=df.loc[3973:3993,'Hora']
a= df.loc[3967:3972,'Consumo(litros)']#consumo 03-09; 09/09
b= df.loc[3973:3993,'Consumo(litros)']#consumo 10-09; 16/09
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[3967+i])
    i+=1
while l< len(b) :
    d.append(b[3973+l])
    l+=1
for i in range(len(a)):
    sub = abs(c[i]-d[i])
    sub1.append(sub)
for i in tempo:
    tempo1.append(i)
#print(tempo1)
#print('Distancia Numpy {:.2f}' .format(dst))
#print(c)
#print(d)
#print(sub1)
#print(len(c))
#print(len(d))
#print(len(a))
#print(len(b))

plt.figure(figsize=(20,10))
plt.plot(c,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=3, markersize=12)
#plt.plot(sub1,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(tempo1)),tempo1, rotation=90,fontsize='15')
plt.yticks(fontsize='15')
plt.title('Comparação entre max',fontsize='20')
plt.grid(True)
#plt.legend(["semana 03/09/2017 a 09/09/2017", "semana 10/09/2017 a 16/09/2017",'diferença entre as duas semanas'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='12').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
#plt.savefig('comparação entre semana 03 a 09-09 a semana 10 a 16-09.png')


# In[66]:


df['Data'][df['Consumo(litros)']==550]


# In[67]:


df.max()


# In[68]:


from datetime import datetime
plt.figure(figsize=(20,10))
#data = input('data  [d-m-Y]: ')
data = ['17-01-2018','16-01-2018','15-01-2018']#14-01 nao tem dados
marque = ['s','p','*','D']
for i in range(len(data)):
    data1 = datetime.strptime(data[i], "%d-%m-%Y").strftime('%d-%m-%Y')
    plt.plot(df['Hora'][df['Data']==data1], df['Consumo(litros)'][df['Data']==data1],marker=marque[i])
plt.legend(data,loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.xticks(rotation=45,fontsize='13')
plt.yticks(fontsize='13')
plt.title("Grafico dos dias com max",fontsize='15')


# In[69]:


df.min()


# In[70]:


df.mean()


# In[71]:


df['Data'][df['Consumo(litros)'].max()]


# In[72]:


df['Consumo(litros)'].max()


# In[73]:


df['Data'][df['Consumo(litros)'].max()]


# In[74]:


df['Consumo(litros)'][df['Data']=='13-09-2017']


# In[75]:


df['Data'][df['Consumo(litros)'].max()]


# In[76]:


df['Consumo(litros)'][df['Data']=='16-01-2018']


# In[77]:


df['Consumo(litros)'][df['Data']=='17-01-2018']


# In[78]:


df['Consumo(litros)'][df['Data']=='13-09-2017']


# In[79]:


df.tail()


# In[80]:


g = sns.FacetGrid(df, col='Hora',col_wrap=4, height=2)
g.map(plt.plot, 'Consumo(litros)')
#g.grid(True)
sns.set(style="whitegrid", font_scale=0.25)
g.savefig('tentativa')


# In[81]:


g = sns.FacetGrid(df, col='Semana',col_wrap=3, height=3)
g.map(plt.plot, 'Hora','Consumo(litros)')
sns.set(style="whitegrid", font_scale=0.75)
g.set_xticklabels(rotation=90)
g.savefig('tentativa1')


# correlação

# In[82]:


df.corr()


# In[83]:


df[['Consumo(litros)','Valor Acumulado']].corr().plot()


# correlação não linear

# In[84]:


df.corr('spearman')


# In[85]:


sns.pairplot(df,hue='Hora',palette="Dark2")


# In[86]:


sns.pairplot(df,hue='Semana',palette="Dark2")


# sns.pairplot(df,vars=["Semana", "Hora"])

# In[87]:


sns.pairplot(df, diag_kind="kde")


# In[88]:


sns.pairplot(df, diag_kind="reg")


# In[89]:


df_pivot_table=df.pivot_table(df,index=['Data','Semana'])
df_pivot_table.head()


# plt.figure(figsize=(15,5))
# plt.plot()

# plt.figure(figsize=(15,5))
# plt.plot(df['Semana']=='Monday', df['Consumo(litros)'])

# plt.figure(figsize=(15,5))
# plt.plot( df['Consumo(litros)'])

# In[90]:


horaunicas=df['Hora'].unique()
lista=[]
for i in horaunicas:
    media=float(df['Consumo(litros)'][df['Hora']==i].mean())
    lista.append((i,media))
df_hora_media = pd.DataFrame(lista)
df_hora_media.columns = ['Hora', 'Media (Litros)']


# In[91]:


df_hora_media


# In[92]:


df_hora_media['Hora']


# In[230]:


data=df_hora_media['Hora']
df_hora_media.plot.line(marker='o',style='r-.', figsize=(15,10))
plt.title('Grafico Médias por hora',fontsize='15') #adicionando o título
plt.xlabel('Horas',fontsize='15')
plt.ylabel('Médias (Litros)',fontsize='15')
plt.xticks(np.arange(len(data)),data,rotation=90,fontsize='15')
plt.yticks(fontsize='15')
plt.legend(('Médias'),loc='best',  shadow=True, fancybox=True, fontsize='15')

plt.grid(True)
plt.savefig('Grafico Médias Por Hora(este).png')


# In[94]:


df['Consumo(litros)'][df['Hora']=='07:00:00'].head()


# In[95]:


df.loc[1951:2599,'Consumo(litros)'][df['Hora']=='07:00:00']
df.loc[2600:3224,'Consumo(litros)'][df['Hora']=='07:00:00']


# In[96]:


df[df['Data']=='28-04-2018']


# In[97]:


a=df.loc[1951:2599,'Consumo(litros)']
b=df.loc[2600:3224,'Consumo(litros)']
horaunicas=df['Hora'].unique()
lista=[]
lista1=[]
for i in horaunicas:
    media=float(df.loc[1951:2599,'Consumo(litros)'][df['Hora']==i].mean())
    lista.append((i,media))
df_hora_media1 = pd.DataFrame(lista)
df_hora_media1.columns = ['Hora', 'Media (Litros)1']


# In[98]:


a=df.loc[1951:2599,'Consumo(litros)']
b=df.loc[2600:3224,'Consumo(litros)']
horaunicas=df['Hora'].unique()
lista=[]
lista1=[]

for i in horaunicas:
    media=float(df.loc[2600:3224,'Consumo(litros)'][df['Hora']==i].mean())
    lista.append((i,media))
df_hora_media2 = pd.DataFrame(lista)
df_hora_media2.columns = ['Hora', 'Media (Litros)2']


# In[99]:


a=df.loc[1951:2599,'Consumo(litros)']
b=df.loc[3295:3920,'Consumo(litros)']
horaunicas=df['Hora'].unique()
lista=[]
lista1=[]

for i in horaunicas:
    media=float(df.loc[3295:3920,'Consumo(litros)'][df['Hora']==i].mean())
    lista.append((i,media))
df_hora_media3 = pd.DataFrame(lista)
df_hora_media3.columns = ['Hora', 'Media (Litros)3']


# In[100]:


df_hora_media3


# In[101]:


df_hora_media1


# In[102]:


df_hora_media2


# In[103]:


df_merge_media_horaria = pd.merge(df_hora_media1,df_hora_media2)


# In[104]:


df_merge_media_horaria.head()


# In[105]:


df_merge_media_horaria = pd.merge(df_merge_media_horaria,df_hora_media3)


# In[106]:


df_merge_media_horaria.head()


# In[107]:


data=df_merge_media_horaria['Hora']
plt.figure(figsize=(20,10))
plt.plot(df_merge_media_horaria['Hora'],df_merge_media_horaria['Media (Litros)1'],marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(df_merge_media_horaria['Hora'],df_merge_media_horaria['Media (Litros)2'],marker='D',ls='--',linewidth=3, markersize=12)
#plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(data, rotation=90,fontsize='20')
plt.yticks(fontsize='15')
plt.legend(('Fevereiro','Março'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação média por hora entre Fevereiro e Março",fontsize='20')
plt.savefig('comparação media horari entre dois meses consumo.png')


# In[108]:


#df_hora_media
data=df_merge_media_horaria['Hora']
plt.figure(figsize=(20,10))
plt.plot(df_merge_media_horaria['Hora'],df_merge_media_horaria['Media (Litros)1'],marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(df_merge_media_horaria['Hora'],df_merge_media_horaria['Media (Litros)2'],marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(df_hora_media['Hora'],df_hora_media['Media (Litros)'],marker='*',ls='-.',linewidth=3, markersize=12)
#plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(data, rotation=90,fontsize='20')
plt.yticks(fontsize='15')
plt.legend(('Fevereiro','Março','Media Geral'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação média por hora entre Fevereiro e Março consumo com média geral",fontsize='20')
plt.savefig('comparação media horari entre dois meses consumo.png')


# In[109]:


#df_hora_media
data=df_merge_media_horaria['Hora']
plt.figure(figsize=(20,10))
plt.plot(df_merge_media_horaria['Hora'],df_merge_media_horaria['Media (Litros)1'],marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(df_merge_media_horaria['Hora'],df_merge_media_horaria['Media (Litros)2'],marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(df_merge_media_horaria['Hora'],df_merge_media_horaria['Media (Litros)3'],marker='*',ls='-.',linewidth=3, markersize=12)
plt.plot(df_hora_media['Hora'],df_hora_media['Media (Litros)'],marker='D',ls=':',linewidth=3, markersize=12)
#plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(data, rotation=90,fontsize='20')
plt.yticks(fontsize='15')
plt.legend(('Fevereiro','Março','Abril','Media Geral'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação média por hora entre Fevereiro, Março e Abril com consumo de média geral",fontsize='20')
plt.savefig('comparação media horari entre tres meses consumo.png')


# In[110]:



plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Semana']=='Monday'], df['Consumo(litros)'][df['Semana']=='Monday'],'ro')
plt.plot(df['Hora'][df['Semana']=='Monday'], df['Consumo(litros)'][df['Semana']=='Monday'],'b--')
plt.grid(True)
plt.xticks(rotation=45,fontsize='13')
plt.yticks(fontsize='13')
plt.title('Grafico consumo Segundas feiras',fontsize='15')
plt.legend(loc='best', ncol=2, shadow=True, fancybox=True,fontsize='13').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico consumo Segundas feiras.png')


# In[111]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Semana']=='Tuesday'], df['Consumo(litros)'][df['Semana']=='Tuesday'],'ro')
plt.plot(df['Hora'][df['Semana']=='Tuesday'], df['Consumo(litros)'][df['Semana']=='Tuesday'],'b--')
plt.grid(True)
plt.xticks(rotation=45,fontsize='13')
plt.yticks(fontsize='13')
plt.title('Grafico consumo  Terças feiras',fontsize='15')
plt.legend(loc='best', ncol=2, shadow=True, fancybox=True,fontsize='13').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico consumo  Terças feiras.png')


# In[112]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Semana']=='Wednesday'], df['Consumo(litros)'][df['Semana']=='Wednesday'],'ro')
plt.plot(df['Hora'][df['Semana']=='Wednesday'], df['Consumo(litros)'][df['Semana']=='Wednesday'],'b--')
plt.grid(True)
plt.xticks(rotation=45,fontsize='13')
plt.yticks(fontsize='13')
plt.title('Grafico consumo  Quartas Feiras',fontsize='15')
plt.legend(loc='best', ncol=2, shadow=True, fancybox=True,fontsize='13').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico consumo  Quartas Feiras.png')


# In[113]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Semana']=='Thursday'], df['Consumo(litros)'][df['Semana']=='Thursday'],'ro')
plt.plot(df['Hora'][df['Semana']=='Thursday'], df['Consumo(litros)'][df['Semana']=='Thursday'],'b--')
plt.grid(True)
plt.xticks(rotation=45,fontsize='13')
plt.yticks(fontsize='13')
plt.title('Grafico consumo  Quintas Feiras',fontsize='15')
plt.legend(loc='best', ncol=2, shadow=True, fancybox=True,fontsize='13').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico consumo  Quintas Feiras.png')


# In[114]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Semana']=='Friday'], df['Consumo(litros)'][df['Semana']=='Friday'],'ro')
plt.plot(df['Hora'][df['Semana']=='Friday'], df['Consumo(litros)'][df['Semana']=='Friday'],'b--')
plt.grid(True)
plt.xticks(rotation=45,fontsize='13')
plt.yticks(fontsize='13')
plt.title('Grafico consumo  Sextas Feiras',fontsize='15')
plt.legend(loc='best', ncol=2, shadow=True, fancybox=True,fontsize='13').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico consumo  Sextas Feiras.png')


# In[115]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Semana']=='Saturday'], df['Consumo(litros)'][df['Semana']=='Saturday'],'ro')
plt.plot(df['Hora'][df['Semana']=='Saturday'], df['Consumo(litros)'][df['Semana']=='Saturday'],'b--')

plt.grid(True)
plt.xticks(rotation=45,fontsize='13')
plt.yticks(fontsize='13')
plt.title('Grafico consumo  Sabados',fontsize='15')
plt.legend(loc='best', ncol=2, shadow=True, fancybox=True,fontsize='13').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico consumo  Sabados.png')


# In[116]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Semana']=='Monday'], df['Consumo(litros)'][df['Semana']=='Monday'],'ro')
plt.plot(df['Hora'][df['Semana']=='Monday'], df['Consumo(litros)'][df['Semana']=='Monday'],'b--')

plt.grid(True)
plt.xticks(rotation=45,fontsize='13')
plt.yticks(fontsize='13')
plt.title('Grafico consumo  Domingos',fontsize='15')
plt.legend(loc='best', ncol=2, shadow=True, fancybox=True,fontsize='13').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico consumo  Domingos.png')


# In[117]:


df['Data'][df['Semana']=='Monday'].head()


# In[118]:


df['Data'][df['Semana']=='Tuesday'].head()


# In[119]:


df['Data'][df['Semana']=='Tuesday'].tail()


# In[120]:


df[df['Data']=='13-09-2017']


# In[121]:


df_simula=df[527:647]


# In[122]:


df_simula.head()


# In[123]:


df_simula.tail()


# In[124]:


df_simula['Consumo(litros)Simulação']= df_simula['Consumo(litros)']


# In[125]:


df_simula


# In[126]:


df_simula['Consumo(litros)Simulação'].sum()


# In[127]:


df_simula['Consumo(litros)'].sum()


# In[128]:


simular= df_simula.loc[540:620,'Consumo(litros)Simulação']


# In[129]:


len(df_simula.loc[540:620,'Consumo(litros)Simulação'])


# In[130]:


x=50
i=0
while i <= len(simular):
    df_simula.loc[539+i,'Consumo(litros)Simulação']=df_simula.loc[539+i,'Consumo(litros)Simulação']+x
    #x=x+5
    i=i+1


# In[131]:


df_simula.loc[540:540+1,'Consumo(litros)']


# In[132]:


df_simula


# In[133]:


df_simula['Consumo(litros)Simulação'].sum()


# In[134]:


df_simula['Consumo(litros)'].sum()


# In[135]:


df_simula['Consumo(litros)Simulação'].sum() - df_simula['Consumo(litros)'].sum()


# In[136]:


tempo=df_simula.loc[531:650,'Hora']
a= df_simula.loc[531:650,'Consumo(litros)']#consumo 13-09; 14/09
b= df_simula.loc[531:650,'Consumo(litros)Simulação']#consumo 13-09; 14/09

def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)
lista_distancia=[]
for i in range(len(a)):
    sub = dist_euclidiana_np(a[531+i], b[531+i])
    lista_distancia.append(sub)
print(lista)
#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(a, b)))
print(len(a))
print(len(b))
print(len(lista_distancia))


# In[137]:


tempo=df_simula.loc[531:650,'Hora']
a= df_simula.loc[531:650,'Consumo(litros)']#consumo 13-09; 14/09
b= df_simula.loc[531:650,'Consumo(litros)Simulação']#consumo 13-09; 14/09
tempo1=[]
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[531+i])
    i+=1
while l< len(b) :
    d.append(b[531+l])
    l+=1
for i in tempo:
    tempo1.append(i)
plt.figure(figsize=(30,15))
plt.plot(c,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(tempo1)),tempo1, rotation=90,fontsize='18')
plt.yticks(fontsize='20')
plt.title('Simulação de vazamento nos dias 13 a 17-09 com Distancia Euclidiana',fontsize='25')
plt.legend(["normal", "Simulação de vazamento",'Distancia E'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='20').get_frame().set_alpha(0.8)
plt.grid(True)
plt.savefig('Simulação de vazamento nos dias 13 a 17-09 com Distancia Euclidiana.png')


# In[138]:



tempo=df_simula.loc[531:650,'Hora']
a= df_simula.loc[531:650,'Consumo(litros)']#consumo 13-09; 14/09
b= df_simula.loc[531:650,'Consumo(litros)Simulação']#consumo 13-09; 14/09

tempo1=[]
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[531+i])
    i+=1
while l< len(b) :
    d.append(b[531+l])
    l+=1

for i in tempo:
    tempo1.append(i)
#print(tempo1)
#print('Distancia Numpy {:.2f}' .format(dst))
#print(c)
#print(d)
#print(sub1)
#print(len(c))
#print(len(d))
#print(len(a))
#print(len(b))
plt.figure(figsize=(30,15))
plt.plot(c,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=3, markersize=12)

plt.xticks(np.arange(len(tempo1)),tempo1, rotation=90,fontsize='18')
plt.yticks(fontsize='20')
plt.title('Simulação de vazamento nos dias 13 a 17-09',fontsize='25')
plt.legend(["normal", "Simulação de vazamento"],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='20').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.grid(True)
plt.savefig('Simulação de vazamento nos dias 13 a 17-09.png')


# In[139]:


from datetime import datetime
plt.figure(figsize=(20,10))
#data = input('data  [d-m-Y]: ')
data = ['28-08-2017',"04-09-2017",'11-09-2017','18-09-2017']
marque = ['s','p','*','D']
for i in range(len(data)):
    data1 = datetime.strptime(data[i], "%d-%m-%Y").strftime('%d-%m-%Y')
    plt.plot(df['Hora'][df['Data']==data1], df['Consumo(litros)'][df['Data']==data1],marker=marque[i])
plt.legend(data,loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)

plt.grid(True)
plt.xticks(rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title("Grafico comparando os dias (Segundas-feiras)",fontsize='20')


# In[140]:


from datetime import datetime
plt.figure(figsize=(20,10))
#data = input('data  [d/m/Y]: ')
data = ['28-08-2017',"04-09-2017",'11-09-2017','18-09-2017']
marque = ['s','p','*','D']
for i in range(len(data)):
    data1 = datetime.strptime(data[i], "%d-%m-%Y").strftime('%d-%m-%Y')
    plt.plot(df['Hora'][df['Data']==data1], df['Consumo(litros)'][df['Data']==data1],marker=marque[i])
plt.legend(data,loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
#plt.plot(df['Hora'][df['Data']=='04-09-2017'], df['Consumo(litros)'][df['Data']=='04-09-2017'],marker='p')
#plt.plot(df['Hora'][df['Data']=='11-09-2017'], df['Consumo(litros)'][df['Data']=='11-09-2017'],marker='*')
#plt.plot(df['Hora'][df['Data']=='18-09-2017'], df['Consumo(litros)'][df['Data']=='18-09-2017'],marker='D')
#plt.legend( ["2017-08-28", "2017-09-04",'2017-09-11','2017-09-18'])
plt.xticks(rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title("Grafico comparando os dias (Segundas-feiras)",fontsize='20')
plt.grid(True)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
#plt.savefig('Grafico comparando os dias 28-08, 04-09, 11-09, 18-09 de 2017  (Segundas-feiras).png')


# In[141]:


plt.figure(figsize=(20,10))
#plt.plot(df['Hora'][df['Data']=='2017-08-21'], df['Consumo(litros)'][df['Data']=='2017-08-21'])
plt.plot(df['Hora'][df['Data']=='28-08-2017'], df['Consumo(litros)'][df['Data']=='28-08-2017'],marker='s')
plt.plot(df['Hora'][df['Data']=='04-09-2017'], df['Consumo(litros)'][df['Data']=='04-09-2017'],marker='p')
plt.plot(df['Hora'][df['Data']=='11-09-2017'], df['Consumo(litros)'][df['Data']=='11-09-2017'],marker='*')
plt.plot(df['Hora'][df['Data']=='18-09-2017'], df['Consumo(litros)'][df['Data']=='18-09-2017'],marker='D')
#plt.legend(loc='upper left')
plt.grid(True)
plt.legend(["28-08-2017", "04-09-2017",'11-09-2017','18-09-2017'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='14').get_frame().set_alpha(0.8)
#plt.legend( ["2017-08-28", "2017-09-04",'2017-09-11','2017-09-18'])
plt.xticks(rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title('Grafico comparando os dias 28/08, 04/09, 11/09, 18/09 de 2017 (Segundas-feiras)',fontsize='20')
plt.grid(True)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico comparando os dias 28-08, 04-09, 11-09, 18-09 de 2017  (Segundas-feiras).png')


# In[142]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Data']=='22-08-2017'], df['Consumo(litros)'][df['Data']=='22-08-2017'],marker='s')
plt.plot(df['Hora'][df['Data']=='29-08-2017'], df['Consumo(litros)'][df['Data']=='29-08-2017'],marker='p')
plt.plot(df['Hora'][df['Data']=='05-09-2017'], df['Consumo(litros)'][df['Data']=='05-09-2017'],marker='*')
plt.plot(df['Hora'][df['Data']=='12-09-2017'], df['Consumo(litros)'][df['Data']=='12-09-2017'],marker='D')

plt.grid(True)
plt.xticks(rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title('Grafico comparando os dias 22/08, 29/08, 05/09, 12/09 de 2017 (Terças-feiras)',fontsize='20')
plt.legend(["22-08-2017", "29-08-2017",'05-09-2017','12-09-2017'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='14').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.grid(True)
plt.savefig('Grafico comparando os dias 22-08, 29-08, 05-09, 12-09 de 2017 (Terças-feiras).png')


# plt.figure(figsize=(20,5))
# for i in df['Data']:
#     for e in df['Semana']:
#         if e == 'Monday':
#             plt.plot(df['Hora'][df['Data']==i], df['Consumo(litros)'][df['Data']==i])

# In[143]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Data']=='23-08-2017'], df['Consumo(litros)'][df['Data']=='23-08-2017'],marker='s')
plt.plot(df['Hora'][df['Data']=='30-08-2017'], df['Consumo(litros)'][df['Data']=='30-08-2017'],marker='p')
plt.plot(df['Hora'][df['Data']=='06-09-2017'], df['Consumo(litros)'][df['Data']=='06-09-2017'],marker='*')
plt.plot(df['Hora'][df['Data']=='13-09-2017'], df['Consumo(litros)'][df['Data']=='13-09-2017'],marker='D')
#plt.legend(loc='upper left')
plt.grid(True)
plt.xticks(rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title('Grafico comparando os dias 23/08, 30/08, 06/09, 13/09 de 2017 (Quartas-feiras)',fontsize='20')
plt.legend(["23-08-2017", "30-08-2017",'06-09-2017','13-09-2017'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='14').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico comparando os dias 23-08, 30-08, 06-09, 13-09 de 2017 (Quartas-feiras.png')


# In[144]:


plt.figure(figsize=(20,10))
#ver esse dia 24/08
#plt.plot(df['Hora'][df['Data']=='24-08-2017'], df['Consumo(litros)'][df['Data']=='24-08-2017'],marker='s')
plt.plot(df['Hora'][df['Data']=='31-08-2017'], df['Consumo(litros)'][df['Data']=='31-08-2017'],marker='p')
plt.plot(df['Hora'][df['Data']=='07-09-2017'], df['Consumo(litros)'][df['Data']=='07-09-2017'],marker='*')
plt.plot(df['Hora'][df['Data']=='14-09-2017'], df['Consumo(litros)'][df['Data']=='14-09-2017'],marker='D')
plt.plot(df['Hora'][df['Data']=='21-09-2017'], df['Consumo(litros)'][df['Data']=='21-09-2017'],marker='s')
#plt.legend(loc='upper left')
plt.grid(True)
plt.xticks(rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title('Grafico comparando os dias  31/08, 07/09, 14/09, 21/09 de 2017 (Quintas-feiras)',fontsize='20')
plt.legend(["31-08-2017", "07-09-2017",'14-09-2017','21-09-2017'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='14').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico comparando os dias  31-08, 07-09, 14-09, 21-09 de 2017 (Quintas-feiras).png')


# In[145]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Data']=='25-08-2017'], df['Consumo(litros)'][df['Data']=='25-08-2017'],marker='s')
plt.plot(df['Hora'][df['Data']=='01-09-2017'], df['Consumo(litros)'][df['Data']=='01-09-2017'],marker='p')
plt.plot(df['Hora'][df['Data']=='08-09-2017'], df['Consumo(litros)'][df['Data']=='08-09-2017'],marker='*')
plt.plot(df['Hora'][df['Data']=='15-09-2017'], df['Consumo(litros)'][df['Data']=='15-09-2017'],marker='D')
#plt.legend(loc='upper left')
plt.grid(True)
plt.xticks(rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title('Grafico comparando os dias 25/08, 01/09, 08/09, 15/09 de 2017 (Sextas-feiras)',fontsize='20')
plt.legend(["25-08-2017", "01-09-2017",'08-09-2017','15-09-2017'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='14').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico comparando os dias 25-08, 01-09, 08-09, 15-09 de 2017 (Sextas-feiras).png')


# In[146]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Data']=='26-08-2017'], df['Consumo(litros)'][df['Data']=='26-08-2017'],marker='s')
plt.plot(df['Hora'][df['Data']=='02-09-2017'], df['Consumo(litros)'][df['Data']=='02-09-2017'],marker='p')
plt.plot(df['Hora'][df['Data']=='09-09-2017'], df['Consumo(litros)'][df['Data']=='09-09-2017'],marker='*')
plt.plot(df['Hora'][df['Data']=='16-09-2017'], df['Consumo(litros)'][df['Data']=='16-09-2017'],marker='D')
#plt.legend(loc='upper left')
plt.grid(True)
plt.xticks( rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title('Grafico comparando os dias 26/08, 02/09, 09/09, 16/09 de 2017 (Sabados)',fontsize='20')
plt.legend(["26-08-2017", "02-09-2017",'09-09-2017','16-09-2017'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='14').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico comparando os dias 26-08, 02-09, 09-09, 16-09 de 2017 (Sabados).png')


# In[147]:


plt.figure(figsize=(20,10))
plt.plot(df['Hora'][df['Data']=='27-08-2017'], df['Consumo(litros)'][df['Data']=='27-08-2017'],marker='s')
plt.plot(df['Hora'][df['Data']=='03-09-2017'], df['Consumo(litros)'][df['Data']=='03-09-2017'],marker='p')
plt.plot(df['Hora'][df['Data']=='10-09-2017'], df['Consumo(litros)'][df['Data']=='10-09-2017'],marker='*')
plt.plot(df['Hora'][df['Data']=='17-09-2017'], df['Consumo(litros)'][df['Data']=='17-09-2017'],marker='D')
#plt.legend(loc='upper left')
plt.grid(True)
plt.xticks( rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.title('Grafico comparando os dias 27/08, 03/09, 10/09, 17/09 de 2017 (Domingos)',fontsize='20')
plt.legend(["27-08-2017", "03-09-2017",'10-09-2017','17-09-2017'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='14').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('Grafico comparando os dias 27-08, 03-09, 10-09, 17-09 de 2017 (Domingos).png')


# In[148]:


a=df.loc[291:458,'Hora']#03-09; 06/09


# a=[]
# for i in df.loc[291:458,'Hora']:
#     a.append(i)
# print (a)
# 

# In[149]:


a=[]
for i in df.loc[291:458,'Hora']:
    a.append(i)
b=[]
for di in df.loc[291:458,'Consumo(litros)']:
    b.append(di)

plt.figure(figsize=(20,5))
plt.plot( b,marker='s')
#plt.plot(df.loc[459:626,'Hora'], df.loc[459:626,'Consumo(litros)'],marker='p')

plt.grid(True)
plt.xticks( np.arange(len(a)),a,rotation=45,fontsize='13')
plt.yticks(fontsize='13')
#plt.title('Grafico comparando os dias 26/08, 02/09, 09/09, 16/09 de 2017 (Sabados)',fontsize='15')
#plt.legend(["26-08-2017", "02-09-2017",'09-09-2017','16-09-2017'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='14').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('S.png')


# In[150]:


from scipy.spatial import distance
a= df.loc[291:458,'Consumo(litros)']
b= df.loc[459:626,'Consumo(litros)']


dst = distance.euclidean(a, b)
print('Distancia Euclidiana: {:.2f}' .format(dst))


# In[151]:


df.loc[458,'Consumo(litros)']
df.loc[626,'Consumo(litros)']


# a= df.loc[291:458,'Consumo(litros)']
# b= df.loc[459:626,'Consumo(litros)']
# i=0
# c=[]
# while i< len(a) :
#     c.append(a[291+i])
#     i+=1
# print(c)

# a= df.loc[291:458,'Consumo(litros)']
# b= df.loc[459:626,'Consumo(litros)']
# i=0
# c=[]
# while i< len(b) :
#     c.append(b[459+i])
#     i+=1
# print(c)

# In[152]:


import datetime
tempo=df.loc[291:458,'Hora']
a= df.loc[291:458,'Consumo(litros)']#consumo 03-09; 09/09
b= df.loc[459:626,'Consumo(litros)']#consumo 10-09; 16/09
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[291+i])
    i+=1
while l< len(b) :
    d.append(b[459+l])
    l+=1
for i in range(len(a)):
    sub = abs(c[i]-d[i])
    sub1.append(sub)
for i in tempo:
    tempo1.append(i)
#print(tempo1)
#print('Distancia Numpy {:.2f}' .format(dst))
#print(c)
#print(d)
#print(sub1)
#print(len(c))
#print(len(d))
#print(len(a))
#print(len(b))
plt.figure(figsize=(30,15))
plt.plot(c,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(sub1,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(tempo1)),tempo1, rotation=90,fontsize='20')
plt.yticks(fontsize='20')
plt.title('Comparação entre semana 03 a 09-09 a semana 10 a 16-09',fontsize='25')
plt.legend(["semana 03/09/2017 a 09/09/2017", "semana 10/09/2017 a 16/09/2017",'diferença entre as duas semanas'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='20').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.grid(True)
plt.savefig('comparação entre semana 03 a 09-09 a semana 10 a 16-09.png')


# Distancia euclidiana entre as duas semanas 03/09/2017 a 09/09/2017 e 10/09/2017 a 16/09/2017

# In[153]:


v1= df.loc[291:458,'Consumo(litros)']#consumo 03-09; 09/09
v2= df.loc[459:626,'Consumo(litros)']#consumo 10-09; 16/09
from scipy.spatial import distance
dst = distance.euclidean(v1,v2)
print('Distancia Euclidiana {:.2f}'.format(dst))
def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)


print('Distancia Numpy %.2f' % dist_euclidiana_np(v1, v2))

#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(v1, v2)))


# In[154]:


import datetime
tempo=df.loc[435:458,'Hora']
a= df.loc[435:458,'Consumo(litros)']#consumo 09/09
b= df.loc[603:626,'Consumo(litros)']#consumo 16/09
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[435+i])
    i+=1
while l< len(b) :
    d.append(b[603+l])
    l+=1
for i in range(len(a)):
    sub = abs(c[i]-d[i])
    sub1.append(sub)
for i in tempo:
    tempo1.append(i)
#print(tempo1)
#print('Distancia Numpy {:.2f}' .format(dst))
#print(c)
#print(d)
#print(sub1)
#print(len(c))
#print(len(d))
#print(len(a))
#print(len(b))
plt.figure(figsize=(30,15))
plt.plot(c,marker='p',ls='-',linewidth=4, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=4, markersize=12)
plt.plot(sub1,marker='s',ls='-.',linewidth=4, markersize=12)
plt.xticks(np.arange(len(tempo1)),tempo1, rotation=90,fontsize='20')
plt.yticks(fontsize='20')
plt.title('Comparação entre 09-09 e 16-09',fontsize='20')
plt.legend(["dia 09/09 ","dia 16/09 ",'diferença entre as dois dias'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='20').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.grid(True)
plt.savefig('zoom da comparação entre semana 03 a 09-09 a semana 10 a 16-09.png')


# In[155]:


import datetime
tempo=df.loc[627:793,'Hora']
a= df.loc[627:793,'Consumo(litros)']#consumo 17-09; 23/09
b= df.loc[794:960,'Consumo(litros)']#consumo 24-09; 30/09
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[627+i])
    i+=1
while l< len(b) :
    d.append(b[794+l])
    l+=1
for i in range(len(a)):
    sub = abs(c[i]-d[i])
    sub1.append(sub)
for i in tempo:
    tempo1.append(i)
#print(tempo1)
#print('Distancia Numpy {:.2f}' .format(dst))
#print(c)
#print(d)
#print(sub1)
#print(len(c))
#print(len(d))
#print(len(a))
#print(len(b))
plt.figure(figsize=(30,15))
plt.plot(c,marker='p',ls='-',linewidth=4, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=4, markersize=12)
plt.plot(sub1,marker='s',ls='-.',linewidth=4, markersize=12)
plt.xticks(np.arange(len(tempo1)),tempo1, rotation=90,fontsize='20')
plt.yticks(fontsize='20')
plt.title('Comparação entre semana 17 a 23-09 a semana 24 a 30-09',fontsize='25')
plt.legend(["semana 17/09/2017 a 23/09/2017", "semana 24/09/2017 a 30/09/2017",'diferença entre as duas semanas'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='20').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.grid(True)
plt.savefig('comparação entre semana 17 a 23-09 a semana 24 a 30-09.png')


# In[156]:


import datetime
tempo=df.loc[771:793,'Hora']
a= df.loc[771:793,'Consumo(litros)']#consumo 23/09
b= df.loc[938:960,'Consumo(litros)']#consumo 30/09
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[771+i])
    i+=1
while l< len(b) :
    d.append(b[938+l])
    l+=1
for i in range(len(a)):
    sub = abs(c[i]-d[i])
    sub1.append(sub)
for i in tempo:
    tempo1.append(i)
#print(tempo1)
#print('Distancia Numpy {:.2f}' .format(dst))
#print(c)
#print(d)
#print(sub1)
#print(len(c))
#print(len(d))
#print(len(a))
#print(len(b))
plt.figure(figsize=(30,15))
plt.plot(c,marker='p',ls='-',linewidth=4, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=4, markersize=12)
plt.plot(sub1,marker='s',ls='-.',linewidth=4, markersize=12)
plt.xticks(np.arange(len(tempo1)),tempo1, rotation=90,fontsize='20')
plt.yticks(fontsize='15')
plt.title('Comparação entre 23-09 e 30-09',fontsize='20')
plt.legend(["dia 23/09 ","dia 30/09 ",'diferença entre as dois dias'],loc='upper left', ncol=2, shadow=True, fancybox=True,fontsize='20').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.grid(True)
plt.savefig('zoom da comparação entre semana 17 a 23-09 a semana 24 a 30-09.png')


# In[157]:


a= df.loc[794:960,'Data']
#print(a)
print((626-459)+626)
print(a.loc[960])


# In[158]:



plt.figure(figsize=(20,10))
tempo=df.loc[627:793,'Hora']
tempo1=[]
for i in tempo:
    tempo1.append(i)
a=[]
b=[]
for i in df.loc[459:626,'Consumo(litros)']:
     a.append(i)
for di in df.loc[291:458,'Consumo(litros)']:
    b.append(di)

#a= df.loc[627:793,'Consumo(litros)']#consumo 03-09; 09/09
#b= df.loc[794:960,'Consumo(litros)']#consumo 10-09; 16/09
plt.plot(b,marker='p')
plt.plot(a,marker='s')


#plt.plot(df.loc[459:626,'Hora'], df.loc[459:626,'Consumo(litros)'],marker='p')

plt.grid(True)
plt.xticks(np.arange(len(tempo1)),tempo1, rotation=90,fontsize='12')
plt.yticks(fontsize='13')
#plt.title('Grafico comparando os dias 26/08, 02/09, 09/09, 16/09 de 2017 (Sabados)',fontsize='15')
#plt.legend(["26-08-2017", "02-09-2017",'09-09-2017','16-09-2017'],loc='best', ncol=2, shadow=True, fancybox=True,fontsize='14').get_frame().set_alpha(0.8)
#fig = plt.figure()
#fig=figura_resultado.get_figure()
plt.savefig('S1.png')


# plt.figure(figsize=(20,10))
# x1=df.loc[291:458,'Hora']# hora 03-09; 09/09
# y1=df.loc[291:458,'Consumo(litros)']# consumo 03-09; 09/09
# x2=df.loc[459:626,'Hora']# hora 03-09; 09/09
# y2=df.loc[459:626,'Consumo(litros)']# consumo 03-09; 09/09
# plt.grid(True)
# plt.xticks( rotation=45,fontsize='13')
# plt.yticks(fontsize='13')
# plt.plot(x1,y1,marker='s')
# plt.plot(x2,y2,marker='p')

# In[159]:


#(df['Consumo(litros)'][df['Data']=='03-09-2017']).plot(figsize=(22,10),grid=True ,marker='s')
tempo=df.loc[627:793,'Hora']
tempo1=[]
for i in tempo:
    tempo1.append(i)
df.loc[291:458,'Consumo(litros)'].plot(figsize=(22,10),grid=True ,marker='s')
#df.loc[459:626,'Consumo(litros)'].plot(figsize=(22,10),grid=True ,marker='p')
#plt.xticks(np.arange(len(tempo1)),tempo1, rotation=90,fontsize='12')


# lm=sns.lineplot(x=df.loc[291:458,'Hora'], y=df.loc[291:458,'Consumo(litros)'],   data=df,marker='s')
# lm.grid(True)
# 
# xticks=( rotation(45),fontsize(13)
# #lm.yticks(fontsize='13')
# #fig = lm.get_figure()
# #fig.savefig('grafico_semana.png')

# In[160]:


df.loc[291:458,'Consumo(litros)'].plot(figsize=(20, 5), linewidth=4,grid=True,marker='s')
df.loc[459:626,'Consumo(litros)'].plot(figsize=(20, 5), linewidth=4,grid=True,marker='p')
plt.legend(loc='upper right');


# In[161]:


#sns.lineplot(x=df.loc[291:458,'Hora'], y=df.loc[291:458,'Consumo(litros)'],   data=df,marker='s')
fig, ax = plt.subplots(1,1, figsize=(12, 10))
lm2=sns.lineplot(data=df.loc[291:458,'Consumo(litros)'])
lm3=sns.lineplot(data=df.loc[459:626,'Consumo(litros)'])
lm2.grid(True)
lm2.legend(loc='best')
#lm2.title('Exemplo')


# In[162]:


df[df['Data']=='16-09-2017']


# Distancia euclidiana entre dois dias  09/09/2017 e 16/09/2017

# In[163]:


v1= df.loc[435:458,'Consumo(litros)']#consumo 09/09
v2= df.loc[603:626,'Consumo(litros)']#consumo 16/09
from scipy.spatial import distance
dst = distance.euclidean(v1,v2)
print('Distancia Euclidiana {:.2f}'.format(dst))
def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)


print('Distancia Numpy %.2f' % dist_euclidiana_np(v1, v2))

#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(v1, v2)))


# dataunicas09=df.loc[435:458,'Data']
# dataunicas16=df.loc[603:626,'Data']
# lista1=[]
# lista2=[]
# for i in dataunicas09:
#     somas=df['Consumo(litros)'][df['Data']==i]
#     lista1.append(somas)
# for l in dataunicas16:
#     somas1=df['Consumo(litros)'][df['Data']==l]
#     lista2.append(somas1)
# df09 = pd.DataFrame(lista1)
# df16 = pd.DataFrame(lista2)
# #df09.columns = ['Dia1']
# #df16.columns = ['Dia2']

# In[164]:


a=df.loc[435:458,'Consumo(litros)']
b=df.loc[603:626,'Consumo(litros)']


b

def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)
lista_distancia=[]
for i in range(len(a)):
    sub = dist_euclidiana_np(a[435+i], b[603+i])
    lista_distancia.append(sub)
#print(lista)
#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(a, b)))
print(len(a))
print(len(b))
print(len(lista_distancia))


# Distancia euclidiana entre as dois dias 23/09/2017 e  30/09/2017

# In[165]:


a=df.loc[435:458,'Consumo(litros)']
b=df.loc[603:626,'Consumo(litros)']
tempo=df.loc[435:458,'Hora']
i=0
l=0
c=[]
d=[]


while i< len(a) :
    c.append(a[435+i])
    i+=1
while l< len(b) :
    d.append(b[603+l])
    l+=1

plt.figure(figsize=(20,10))
plt.plot(c,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(tempo)),tempo, rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.legend(('Dia 09/09','Dia 16/09','Distancia E'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação de consumo entre dias 09/09 de 16/09 com distância Euclidiana",fontsize='20')
plt.savefig('Comparação de dias 09-09 e 16-09 com distância.png')


# Distancia euclidiana entre as dois dias 23/09/2017 e  30/09/2017

# In[166]:


v1= df.loc[771:793,'Consumo(litros)']#consumo 23/09
v2= df.loc[938:960,'Consumo(litros)']#consumo 30/09
from scipy.spatial import distance
dst = distance.euclidean(v1,v2)
print('Distancia Euclidiana {:.2f}'.format(dst))
def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)


print('Distancia Numpy %.2f' % dist_euclidiana_np(v1, v2))

#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(v1, v2)))


# Distancia euclidiana entre as duas semanas 17/09/2017 a 23/09/2017 e 24/09/2017 a 30/09/2017

# In[167]:


v1= df.loc[627:793,'Consumo(litros)']#consumo 17-09; 23/09
v2= df.loc[794:960,'Consumo(litros)']#consumo 24-09; 30/09
from scipy.spatial import distance
dst = distance.euclidean(v1,v2)
print('Distancia Euclidiana {:.2f}'.format(dst))
def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)


print('Distancia Numpy %.2f' % dist_euclidiana_np(v1, v2))

#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(v1, v2)))


# In[168]:


dataunicas17=df.loc[627:793,'Data'].unique()
dataunicas24=df.loc[794:960,'Data'].unique()
lista1=[]
lista2=[]
for i in dataunicas17:
    somas=float(df['Consumo(litros)'][df['Data']==i].sum())
    lista1.append(somas)
for l in dataunicas24:
    somas1=float(df['Consumo(litros)'][df['Data']==l].sum())
    lista2.append(somas1)
df17 = pd.DataFrame(lista1)
df24 = pd.DataFrame(lista2)
df17.columns = ['Semana1']
df24.columns = ['Semana2']


# In[169]:


df17.head()


# In[170]:


a= df17 #consumo semana1
b= df24 #consumo semana2

def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)
lista_distancia=[]
for i in range(len(a)):
    sub = dist_euclidiana_np(a.loc[i], b.loc[i])
    lista_distancia.append(sub)
#print(lista)
#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(a, b)))
print(len(a))
print(len(b))
print(len(lista_distancia))


# Distancia euclidiana entre as duas semanas 17/09/2017 a 23/09/2017 e 24/09/2017 a 30/09/2017

# In[171]:


a= df17 #consumo 17/09/2017 a 23/09/2017 
b= df24 #consumo e 24/09/2017 a 30/09/2017



plt.figure(figsize=(20,10))
plt.plot(a,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(b,marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(a)), rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.legend(('Semana 17-23/09','Semana 24-30/09','Distancia E'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação de consumo semanas 17/09/2017 a 23/09/2017 e 24/09/2017 a 30/09/2017 com distância Euclidiana",fontsize='20')
plt.savefig('Comparação de semanas 17 a 23-09 e 24 a 30-09 com distância.png')


# In[172]:


a=df.loc[627:793,'Consumo(litros)']
b=df.loc[794:960,'Consumo(litros)']

b

def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)
lista_distancia=[]
for i in range(len(a)):
    sub = dist_euclidiana_np(a[627+i], b[794+i])
    lista_distancia.append(sub)
#print(lista)
#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(a, b)))
print(len(a))
print(len(b))
print(len(lista_distancia))


# In[173]:



a=df.loc[627:793,'Consumo(litros)']
b=df.loc[794:960,'Consumo(litros)']
tempo=df.loc[627:793,'Hora']
i=0
l=0
c=[]
d=[]


while i< len(a) :
    c.append(a[627+i])
    i+=1
while l< len(b) :
    d.append(b[794+l])
    l+=1

plt.figure(figsize=(20,10))
plt.plot(c,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(tempo)),tempo, rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.legend(('Semana 17-23/09','Semana 24-30/09','Distancia E'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação de consumo semanas 17/09/2017 a 23/09/2017 e 24/09/2017 a 30/09/2017 com distância Euclidiana completo",fontsize='20')
plt.savefig('Comparação de semanas 17 a 23-09 e 24 a 30-09 com distância completo.png')


# In[174]:


df.loc[555:578,'Consumo(litros)']


# Distancia euclidiana entre dados de duas datas 22/08/2017 e 29/08/2017

# In[175]:


v1= df['Consumo(litros)'][df['Data']=='22-08-2017']
v2=df['Consumo(litros)'][df['Data']=='29-08-2017']

def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)


print('Distancia Numpy %.2f' % dist_euclidiana_np(v1, v2))

print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(v1, v2)))


# In[176]:


a= df['Consumo(litros)'][df['Data']=='22-08-2017']
b= df['Consumo(litros)'][df['Data']=='29-08-2017']
dista = np.linalg.norm(a-b)
print('Distancia Numpy {:.2f}' .format(dista))
print('-*'*15)
from scipy.spatial import distance
dst = distance.euclidean(a, b)
print('Distancia Numpy {:.2f}' .format(dst))


# Distancia euclidiana entre dados de duas datas 29/08/2017 e 05/09/2017

# Distancia euclidiana entre as duas datas 29/08/2017 e 05/09/2017 (terças-feiras)

# In[177]:


v1= df['Consumo(litros)'][df['Data']=='29-08-2017']
v2=df['Consumo(litros)'][df['Data']=='05-09-2017']
def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)


print('Distancia Numpy %.2f' % dist_euclidiana_np(v1, v2))


# In[178]:


v1= df['Consumo(litros)'][df['Data']=='29-08-2017']
v2=df['Consumo(litros)'][df['Data']=='05-09-2017']
from scipy.spatial import distance
dst = distance.euclidean(v1,v2)
print('Distancia Euclidiana {:.2f}'.format(dst))


# df.loc[0:170,'Consumo(litros)']

# Distancia euclidiana entre as semanas 22/08/2017 - 28/08/2017 e 29/08/2017 - 04/09/2017

# In[179]:


v1=df.loc[3:170,'Consumo(litros)']
v2=df.loc[171:337,'Consumo(litros)']
from scipy.spatial import distance
#print(f'distanci euclidiana\n{v1}')
dst = distance.euclidean(v1,v2)
print('Distancia Euclidiana {:.2f}'.format(dst))


# In[180]:


v1=df.loc[3:170,'Consumo(litros)']
v2=df.loc[171:337,'Consumo(litros)']
def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)


print('Distancia Numpy %.2f' % dist_euclidiana_np(v1, v2))
print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(v1, v2)))


# In[181]:


df.loc[3296,'Data']


# Distancia euclidiana entre as semanas 01/03/2018 - 30/03/2018 e 01/04/2018 - 30/04/2018

# In[182]:


v1=df.loc[2600:3272,'Consumo(litros)']
v2=df.loc[3295:3967,'Consumo(litros)']
def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)


print('Distancia Numpy %.2f' % dist_euclidiana_np(v1, v2))
print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(v1, v2)))


# In[183]:


dataunicas1=df.loc[2600:3272,'Data'].unique()
dataunicas2=df.loc[3295:3967,'Data'].unique()
lista1=[]
lista2=[]
for i in dataunicas1:
    somas=float(df['Consumo(litros)'][df['Data']==i].sum())
    lista1.append(somas)
for l in dataunicas2:
    somas1=float(df['Consumo(litros)'][df['Data']==l].sum())
    lista2.append(somas1)
df4 = pd.DataFrame(lista1)
df5 = pd.DataFrame(lista2)
df4.columns = ['Março']
df5.columns = ['Abril']


# In[184]:


df4.head()


# In[185]:


df5.head()


# In[186]:


len(df5)


# In[187]:


a= df4 #consumo 01-03; 30/03
a.loc[1]


# In[206]:


a= df4 #consumo 01-03; 30/03
b= df5 #consumo 01-04; 30/04

def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)
lista_distancia=[]
for i in range(len(a)):
    sub = dist_euclidiana_np(a.loc[i], b.loc[i])
    lista_distancia.append(sub)
print(lista)
#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(a, b)))
print(len(a))
print(len(b))
print(len(lista_distancia))


# In[207]:


a= df4 #consumo 01-03; 30/03
b= df5 #consumo 01-04; 30/04



plt.figure(figsize=(20,10))
plt.plot(a,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(b,marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(a)), rotation=45,fontsize='15')
plt.yticks(fontsize='15')
plt.legend(('Março','Abril','Distancia E'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação de Março e Abril com distância Euclidiana",fontsize='20')
plt.savefig('Comparação de Março e Abril com distância Euclidiana.png')


# In[190]:


tempo=df.loc[2600:3272,'Hora']
a= df.loc[2600:3272,'Consumo(litros)']#consumo 01-03; 30/03
b= df.loc[3295:3967,'Consumo(litros)']#consumo 01-04; 30/04

def dist_euclidiana_np(v1, v2):
    # v1= np.array(v1)
    # v2 = np.array(v2)
	#variavel v1 recebe vetor v1
    v1, v2 = np.array(v1), np.array(v2)
	#diferenca entre os elementos 
    dif = v1 - v2
	#multiplicaçao entre os elementos
    quad_dist = np.dot(dif, dif)
    return math.sqrt(quad_dist)
lista_distancia=[]
for i in range(len(a)):
    sub = dist_euclidiana_np(a[2600+i], b[3295+i])
    lista_distancia.append(sub)
print(lista)
#print('Distancia Numpy {:.2f}' .format(dist_euclidiana_np(a, b)))
print(len(a))
print(len(b))
print(len(lista_distancia))


# In[191]:


import datetime
tempo=df.loc[2600:3272,'Data']
a= df.loc[2600:3272,'Consumo(litros)']#consumo 01-03; 30/03
b= df.loc[3295:3967,'Consumo(litros)']#consumo 01-04; 30/04
i=0
l=0
c=[]
d=[]
sub1=[]
tempo1=[]
while i< len(a) :
    c.append(a[2600+i])
    i+=1
while l< len(b) :
    d.append(b[3295+l])
    l+=1

for i in tempo:
    tempo1.append(i)




plt.figure(figsize=(20,10))
plt.plot(c,marker='p',ls='-',linewidth=3, markersize=12)
plt.plot(d,marker='D',ls='--',linewidth=3, markersize=12)
plt.plot(lista_distancia,marker='s',ls='-.',linewidth=3, markersize=12)
plt.xticks(np.arange(len(tempo1)), rotation=90,fontsize='15')
plt.yticks(fontsize='15')
plt.legend(('Março','Abril','Distancia E'),loc='best', ncol=2, shadow=True, fancybox=True,fontsize='15').get_frame().set_alpha(0.8)
plt.grid(True)
plt.title("Grafico comparação de Março e Abril com distância Euclidiana",fontsize='20')
plt.savefig('comparação de Março e Abril com distância Euclidiana ruim.png')


# In[192]:



from scipy.spatial import distance
#print(f'distanci euclidiana\n{v1}')
dst = distance.euclidean(v1,v2)
print('Distancia Euclidiana {:.2f}'.format(dst))


# In[193]:


df.loc[3967,'Consumo(litros)']
df.loc[3967,'Data']


# In[194]:


df['Data'][df['Data']=='01-03-2018'].head()


# In[195]:


df['Data'][df['Data']=='30-03-2018'].tail()


# In[196]:


df['Data'][df['Data']=='01-04-2018'].head()


# In[197]:


df['Data'][df['Data']=='30-04-2018'].tail()


# In[198]:


df['Consumo(litros)'][df['Data']=='26-08-2017'].count()


# df['Consumo(litros)'][[df['Data'][df['Semana']=='Monday']]]

# In[199]:


df['Data'][df['Semana']=='Monday'].head()


# In[200]:


df_teste=df['Consumo(litros)'][df['Semana']=='Monday']==df['Data'][df['Semana']=='Monday']


# In[201]:


df_teste.head()


# In[202]:


df['Data'][df['Semana']=='Monday']==df['Data'][df['Semana']=='Monday']

