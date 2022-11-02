try:
    n_bilet=int(input('Введите количество билетов:\n'))    #запрос на ввод количества билетов
    n=0
    spisok_biletov=[]
    while n!=n_bilet:
        for i in range(1,n_bilet+1,1):
            n += 1
            age=(int((input("Введите возраст,для каждого билета")))) #Возраст для каждого билета

            if 0<age<18: #стоимость билета 0
                spisok_biletov.append(int(0))
            elif 18<age<25: #стоимость билета 990
                spisok_biletov.append(int(990))
            elif 100>=age>=25: #стоимость билета 1390
                spisok_biletov.append(int(1390))
            elif age<0 or age>100: #Вызвать ошибку если возраст меньше 0 или больше 100
                raise ValueError
    sum=sum(spisok_biletov)
    if n>3: #скидка 10%
        sum=sum*0.90
        print("Стоимость билетов составляет:",sum,"рублей,с учетом 10% скидки.")
    else: #без скидки
        print("Стоимость билетов составляет:",sum,"рублей")
except ValueError as e: #Введено некоректное значение
    print("Для ввода доступны только положительные числа от 0 до 100 включительно ")