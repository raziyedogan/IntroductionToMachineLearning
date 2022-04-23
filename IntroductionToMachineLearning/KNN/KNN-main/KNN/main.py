import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("column_2C_weka.csv")

X,y = data.loc[:,data.columns != 'class'], data.loc[:,'class']

# train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 1)

"""
KNN algoritması özellikle sınıflandırma işlemleri için kullanılmaktadır. Bu algoritma, bir veri noktasının
etrafındaki veri noktalarına bakarak o veri noktasının hangi sınıfa ait olduğunu belirler. 
Bunu şöyle yapar:
    -> Etrafındaki veri noktalarına öklid mesafesi bulunur. 
    -> Elde edilen mesafe değerleri bir listede saklanır.
    -> Liste içerisinden belirlenen k değeri adetinde en yakın mesafe değerleri seçilir.
    -> Seçilen değerlerden çoğunluk hangi sınıfta ise, sınıfını belirlemeye çalıştığımız veri noktamızda
       o sınıftadır.
"""
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 3) # n_neighbors, k değeridir. Yani değerlendirmeye alınacak komşu sayısını ifade eder.
knn.fit(X_train,y_train)
prediction = knn.predict(X_test)
print('With KNN (K=3) accuracy is: ',knn.score(X_test,y_test)) # accuracy

# k'ya 1 ile 25 (dahil değil) arasında değerler vererek, knn algoritması için en iyi k değerini bulalım:
neig = np.arange(1, 25)
train_accuracy = []
test_accuracy = []
# Loop over different values of k
for i, k in enumerate(neig):
    # k from 1 to 25(exclude)
    knn = KNeighborsClassifier(n_neighbors=k)
    # Fit with knn
    knn.fit(X_train,y_train)
    #train accuracy
    train_accuracy.append(knn.score(X_train, y_train))
    # test accuracy
    test_accuracy.append(knn.score(X_test, y_test))

# Plot
plt.figure(figsize=[13,8])
plt.plot(neig, test_accuracy, label = 'Testing Accuracy')
plt.plot(neig, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.title('-value VS Accuracy')
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.xticks(neig)
plt.savefig('graph.png')
plt.show()
print("Best accuracy is {} with K = {}".format(np.max(test_accuracy),1+test_accuracy.index(np.max(test_accuracy))))