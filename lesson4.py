# Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()


# done
# text = "a a a b c a a d c d d"
# text_lst = text.split()
# new_lst = []
# for i in range(len(text_lst)):
#     if text_lst[i] in text_lst[:i]:
#         new_lst.append(text_lst[i]+"_"+str(text_lst[:i].count(text_lst[i])))
#     else:
#         new_lst.append(text_lst[i])
# print(', '.join(new_lst))



# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, 
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she 
# sells are sea shells I'm sure So if she sells sea shells on the sea 
# shore I'm sure that the shells are sea shore shells

# Output: 13


# done
# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower()
# print(len(set(text.split())))



# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать 
# это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.

# Примечание: Программные коды на следующих слайдах
# HZ




# *доп. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и вывести его в терминал.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# значение выражения можно записать в виде:
# 2*x^2+5=0
# (если коэффициент равен 0 - значение не пишется,)



# *доп2
# Реализуйте RLE алгоритм: реализуйте модуль 
# сжатия и восстановления данных.
# Сжатие:
# 111222334 -> 31322414
# aaabbbbbccd -> 3a3b2c1d

# Восстановление:
# 31322414 ->111222334
# 3a3b2c1d->aaabbbbbccd

# done
# def shifr(number):
#     lst = []
#     for i in range(len(number)-1):
#         if number[i] != number[i+1]:
#             lst.append(str(number[:i+1].count(number[i]))+str(number[i]))
#     lst.append(str(number.count(number[-1]))+str(number[-1]))
#     return ''.join(lst)

# def deshifr(number):
#     lst = []
#     i = 0
#     j = 1
#     while i < len(number)-1:
#         lst.append(int(number[i])*number[j])
#         i += 2
#         j +=2
#     return ''.join(lst)


# num = input("Enter the number: ")
# print(deshifr(num))
