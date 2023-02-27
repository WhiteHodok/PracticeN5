import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import colorama

customers = pd.read_csv('customers.csv') # Считываем дата-сет

#print(customers.head(3)) я самостоятельно просмотрел тип данных в этом сете и решил закоммитить строчку
# Часть с циферками
#print("Краткое info о нашем дата-сете: \n")
#print(customers.info())
#print("")
#print(customers.describe())
#print('Средний возраст покупателей :',customers['Age'].mean())
#print('Среднее количество детей у покупателей',customers['Family Size'].mean())
#print('Самая часто-встречаемая профессия у покупателей:', customers['Profession'].mode())

#Часть с рисуночками
#sns.countplot(data=customers, x='Gender') # проанализируем покупателей по полу
#plt.show() # Если работать не в колабе и не в юпитере ,то для людей не знакомых с пайтоном будет проблематичено вызвать график и вообще понять почему matplot и seaborn связаны
#sns.histplot(data=customers, y='Age', color='blue', edgecolor='black', hue='Gender',bins=10) # histplot более гибок в настройке , в оф доке на 3 абзаце это сказано : https://seaborn.pydata.org/generated/seaborn.countplot.html
#plt.show()
#заработок по полу
#sns.histplot(data=customers, x='Annual Income ($)',hue='Gender',bins=30000)
#plt.show()
#Размер семьи
#sns.histplot(data=customers, x='Family Size', color='red', edgecolor='black')
#plt.show()
#Тепловая карта всех параметров
#sns.heatmap(data=customers.corr(), annot=True)
#plt.show()
#Возраст и очки
#plt.savefig('scatter.png', dpi=300, bbox_inches='tight') итог работы этой фуфнкции в картинках :)
#Корреляция профессии и зарплаты
#grid = sns.FacetGrid(data=customers,col = 'Profession', hue='Profession', col_wrap=3)
#grid.map(sns.scatterplot, "Profession", "Annual Income ($)")
#plt.show()
# Опыт работы и возраст
#sns.residplot(data=customers, x='Age', y='Work Experience',lowess=True,line_kws=dict(color="r"))
#plt.show()
# Возраст и потраченные очки
#sns.scatterplot(data=customers, x="Age", y="Spending Score (1-100)")
#sns.rugplot(data=customers, x="Age", y="Spending Score (1-100)")
#plt.show()












