import pandas as pd
from sklearn.datasets import make_classification, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import warnings
import numpy as np
warnings.filterwarnings('ignore')

#Sentetik veri seti oluşturalım:
#Ekrana basılan tabloları daha iyi inceleyebilmek amacıyla tabloların daha geniş gösterimi için:
pd.set_option('display.max_columns', None)

# 2 etiketli sınıflandırma veri seti
x, y = make_blobs(n_samples=1000    #satır sayısı
                  ,n_features = 7   #özellik sayısı
                  ,centers = 2  #hedef değişkeni 2 sınıflı olarak tanımladık
                  ,cluster_std = 5) # verideki gürültü


# Dataframe objesine dönüştürelim:
df = pd.DataFrame({"x1":x[:,0],
                   "x2":x[:,1],
                   "x3":x[:,2],
                   "x4":x[:,3],
                   "x5":x[:,4],
                   "x6":x[:,5],
                   "target":y})

# değişkenlerin float değerlerini küçültelim:
df = round(df ,3)

# ilk beş satırı yazdıralım:
print(df.head())

# Scatter plot ile veri setimizi görselleştirelim:
colors = {0:'red', 1:'blue'}
fig, ax = plt.subplots()
grouped = df.groupby('target')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter'
               ,x='x1', y='x6', label=key
               ,color=colors[key])
plt.show()

#describe() metodu sayısal verilere sahip olan sütunların max, min , std gibi
#istatiksel değerlerini döndürür. Bu metod ile X değişkenlerindeki ortalama ve
#medyan (ortanca) değerlerin birbirine yakın ve normal dağılım gösterdiğini gözlemleyebiliriz:
print(df.describe())

#sentetik veri setimizde kim hedef değişken kimler bağımsız değişken belirleyelim.
#Sonrasında test ve train olarak veri setini bölelim:

target = df.target
predictors = df.drop(columns = "target", axis = 1)

# Train and test splitting
x_train, x_test, y_train, y_test = train_test_split(predictors
                                                    ,target
                                                    ,test_size=0.25
                                                    ,random_state=0)

#Logistic regression uygulayalım:

logreg = LogisticRegression()   #logistic regression nesnesinin çağrılması
logreg.fit(x_train,y_train)  #veri setine fit etme işlemi. Yani tanımlanan sınıfı train veri seti üzerinden çalıştırdık.
y_pred = logreg.predict(x_test)  #öğrenilen modelin test verisine uygulanması

#test verisinde ayırdığımız y_test ile y_pred sonuçlarını karşılaştırarak modelin doğruluğunu değerlendirelim:

#Karmaşıklık Matrisi (confusion matrix) :
print(metrics.confusion_matrix(y_test, y_pred))

#Confusion matrix'i görselleştirelim:
import scikitplot.metrics as splt
splt.plot_confusion_matrix(y_test, y_pred)
