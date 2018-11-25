#Задание 1

print('Введите операцию и числа в формате "+ 2 2",\nоперанды должны располагаться через пробел\nДопустимые операнды + - / *')
user_notation = input()
notation_list = user_notation.split(' ')
assert ((int(notation_list[1]) >= 0) and (int(notation_list[2]) >= 0)),"Операции возможны только с положительными числами"
#print(notation_list)
if notation_list[0] == '+':
    print(int(notation_list[1]) + int(notation_list[2]))
elif notation_list[0] == '-':
    print(int(notation_list[1]) - int(notation_list[2]))
elif notation_list[0] == '/':
    try:
        result = int(notation_list[1]) / int(notation_list[2])
    except ZeroDivisionError:
        result = 0
    print(result)
elif notation_list[0] == '*':
    print(int(notation_list[1]) * int(notation_list[2]))
else:
    print('Вы ввели неверный операнд')    


#Задание 2
documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
  ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

#Напишите функцию, выводящей имена всех владельцев документов. С помощью исключения KeyError проверяйте, если поле "name" и документа.

def all_names(x):
    try:
        for data in documents:
      #if document_number == data['number']:
            #name_person = data['name']            
            #- 2break         
        print(data["name"])
    except KeyError:
        print('Нет имени в строке')
    return


com = input('Введите команду. Наберите одну из букв латинского алфавита: n ')

if com == 'n':
    all_names(com)