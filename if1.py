age = int(input("Введите ваш возраст "))
def selection(age):
    if age < 0:
        raise ValueError("Введите корректный возраст")
    if age <= 0 and age < 7:
        return("Вы в детском саду")
    if age >= 7 and age <= 18:
        return("Вы в школе")
    if age >= 18 and age <= 24:
        return("Вы в ВУЗе")
    if age >24 and age <=65:
        return("Вы работаете")
    else:
        return("Вы скорее всего умерли")
escape = selection(age)
print(escape)

    


