# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Lojistik Regresyon, SVM gibi algoritmalar ikili sınıflandırma için tasarlanmıştır ve ikiden fazla sınıfa 
sahip sınıflandırma (multiclass classification) görevleri için doğrudan kullanılamazlar.
Birden çok ikili sınıflandırıcı kullanarak multiclass classification gerçekleştirmek için kullanabileceğimiz
stratejiler vardır:
    1. One-versus-All (OvA)
    2. One-versus-One (OvO)
Bu stratejiler ile, çok sınıflı sınıflandırma veri kümesi birden çok ikili sınıflandırma veri kümesine 
bölünür ve her birine bir ikili sınıflandırma modeli sığdırılır. 
Kısaca bahsedelim:
1. One-versus-All (OvA): Öncelikle bir diğer adının One-vs-Rest(OvR) olduğunu belirtelim. Bu yaklaşımda,
her bir sınıf için bir model oluşturulur. Bir sınıfı bir kutuya koyduğunuzu ve geri kalan tüm sınıflarıda bir
başka kutuya koyduğunuzu düşünün. Bu işlem her bir sınıf için yapılır ve  böylece çok sınıflı bir 
sınıflandırma problemini ikili sınıflandırma şekline getirmiş oluruz. 
Örneğin pamuk, keten, yün şeklinde 3 adet sınıfımız olsun. İki adetten fazla sayıda sınıf olduğuna göre bu 
bir multiclass classification problemidir. Sınıf sayısı kadar sınıflandırıcı oluşturmamız gerek. 3 adet 
sınıf olduğu için 3 adet sınıflandırıcı oluşturmalıyız. 
Sınıflandırıcı-1 : [pamuk]vs[keten,yün]
Sınıflandırıcı-2:  [keten]vs[pamuk,yün]
Sınıflandırıcı-3:  [yün]vs[pamuk,keten]
Bu üç sınıflandırıcıyı eğitmek için üç adet eğitim veri seti oluşturmamız gerek. Mesela birinci veri setinde
özellik değerlerine karşılık gelen sınıf pamuk ise, pamuk değerinin yer aldığı satırlara 1 yazılır. Ve sınıf
değeri pamuk olmayan satırlara 0 yazılır. Böylece sınıfı pamuk olan özellikler belirtilir. Her bir sınıf için
bu işlem yapılarak, eğitim veri seti oluşturulmuş olur. 
Sonrasında bir algoritma ile model eğitilir. Burada Logistic Regression kullandık. 
Ve sonrasında olasılık puanları analiz edilir. Sonuç maksimum olasılık puanına sahip sınıfa aittir.

2. One-versus-One (OvO): Burada ise OvA yaklaşımındaki 'bir sınıfı bir kutuya koymak ve geri kalan tüm 
sınıflarıda bir başka kutuya koymak' mantığından farklı olarak, her sınıf için diğer tüm sınıflara karşı 
bölme işlemi gerçekleştirilir. Dolayısıyla N adet sınıfımız var ise, Nx(N-1)/2 adet sınıflandırıcıyı 
eğitmemiz gerekir.
pamuk, keten, yün şeklindeki 3 adet sınıfımız için OvO stratejisini uygulayalım:
Nx(N-1)/2  ->  3x(3-1)/2 = 3 adet ikili sınıflandırıcıya ayrılır.
Sınıflandırıcı-1 : pamuk ve keten
Sınıflandırıcı-2:  pamuk ve yün
Sınıflandırıcı-3:  keten ve yün
Her ikili sınıflandırıcı bir sınıf etiketini tahmin eder. Test verilerini sınıflandırıcıya girdiğimizde,
en fazla tahmin alan model sonuç olarak kabul edilir.
Aşağıdaki kodda OvO stratejisinde model eğitimi için SVM algoritmasını kullandık.
"""

#One-versus-All (OvA):
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

#Rastgele bir 3 sınıflı sınıflandırma problemi oluşturalım:
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)

#OvR (OvA) tekniği kullanılarak Logistic Regression modeli:
m = LogisticRegression(multi_class='ovr')

m.fit(X, y)

pred = m.predict(X)

print(pred)

#One-versus-One (OvO)
from sklearn.datasets import make_classification
from sklearn.svm import SVC

X2, y2 = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, n_classes=3, random_state=1)

#OvO tekniği kullanılarak SVM modeli:
m2 = SVC(decision_function_shape='ovo')

m2.fit(X2, y2)

pred2 = m2.predict(X2)
print(pred2)