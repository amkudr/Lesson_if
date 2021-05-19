age = int(input("Введите ваш возраст "))
def selection(age):
    if age < 0:
        raise ValueError("Введите корректный возраст")
    if age <= 0 and age < 7:
        print("Вы в детском саду")
    if age >= 7 and age <= 18:
        print("Вы в школе")
    if age >= 18 and age <= 24:
        print("Вы в ВУЗе")
    if age >24 and age <=65:
        print("Вы работаете")
    #else:
        #print("Вы скорее всего умерли")
escape = selection(age)
print(escape)

    


