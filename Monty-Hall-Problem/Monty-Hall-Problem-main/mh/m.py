import random

cnt=0
carGuess_cnt=0

while cnt != 1000:

    #2 kapıda keçi, 1 kapıda araba olma durumu sağlandı:
    gate1 = random.randint(0,1)
    if gate1==0:
        gate2=1
        gate3=1
    else:   #gate=1 durumu
        gate2 = random.randint(0,1)

        if gate2 == 0:
            gate3=1
        else:   #gate2=1 durumu
            gate3=0

    user_guess = random.randint(1,3) #1,2,3 kapılarından birisi random olarak tahmin alındı.

    #tahmini kapının arkasında 'araba var mı?' durumu kontrolleri:
    if user_guess == 1:
        if gate1 == 0:
            carGuess_cnt+=1
    
    elif user_guess == 2:
        if gate2 == 0:
            carGuess_cnt+=1

    else:
        if gate3 == 0:
            carGuess_cnt+=1  
    
    cnt+=1
    

print("probability in case of no gate change: ",carGuess_cnt/1000)


#kapı değişikliği yapılması durumunda:

cnt2=0
carGuess_cnt2=0

while cnt2 != 1000:

    #2 kapıda keçi, 1 kapıda araba olma durumu sağlandı: 
    gate_1 = random.randint(0,1)
    if gate_1==0:
        gate_2=1
        gate_3=1
    else:   #gate=1 durumu
        gate_2 = random.randint(0,1)

        if gate_2 == 0:
            gate_3=1
        else:   #gate2=1 durumu
            gate_3=0

    user_guess2 = random.randint(1,3) #1,2,3 kapılarından birisi random olarak tahmin alındı.


    #kapı değişikliği yapıldı:
    if user_guess2 == 1:    #tahmini kapı 1  ise 
        if gate_2 == 1:  # 2 kapısında keçi var ise 2 kapısı elenir ve 3 kapısı seçilir.
            user_guess2 = 3
        elif gate_3 == 1:  # 3 kapısında keçi var ise 3 kapısı elenir ve 2 kapısı seçilir.
            user_guess2 = 2

    elif user_guess2 ==2:
        if gate_1 == 1:  # 1 kapısında keçi var ise 1 kapısı elenir ve 3 kapısı seçilir.
            user_guess2 = 3
        elif gate_3 == 1:  # 3 kapısında keçi var ise 3 kapısı elenir ve 1 kapısı seçilir.
            user_guess2 = 1
    
    else:
        if gate_1 == 1:  # 1 kapısında keçi var ise 1 kapısı elenir ve 2 kapısı seçilir.
            user_guess2 = 2
        elif gate_2 == 1:  # 2 kapısında keçi var ise 2 kapısı elenir ve 1 kapısı seçilir.
            user_guess2 = 1


    #kapı seçimi değişikliğinden sonra kapının arkasında 'araba var mı?' durumu kontrolleri:
    if user_guess2 == 1:
        if gate_1 == 0:
            carGuess_cnt2+=1
    
    elif user_guess2 == 2:
        if gate_2 == 0:
            carGuess_cnt2+=1

    else:
        if gate_3 == 0:
            carGuess_cnt2+=1  
    
    cnt2+=1

print("probability after gate change: ",carGuess_cnt2/1000)