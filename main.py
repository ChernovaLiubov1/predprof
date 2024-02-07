import sqlite3
con = sqlite3.connect('clienr_city.db')
cursor = con.cursor()
sql = 'SELECT client.id, client.name,client.surname, client.phone, client.email,city.name FROM client, city WHERE client.city_id=city.id'
out = cursor.execute(sql).fetchall()

for id, name, surname, phone, email, city_id in out:
    print(id, name, surname, phone, email, city_id)

name = input('Введите имя клиента: ')
surname = input('Введите фамилию клиента: ')
phone = input('Введите тел клиент: ')
email = input('Введите емейл клиента: ')
city_id = input('Введите город клиента: ')
sql = f'INSERT INTO client (name, surname, phone, email, city_id) VALUES ("{name}", "{surname}","{phone}","{email}", {city_id})'
cursor.execute(sql)
con.commit()

id=input('удаление')
sql = f'DELETE FROM client WHERE id = {id}'
cursor.execute(sql)
con.commit()

id=input('id клиента, почту которого вы хотите изменить')
email = input('почта клиента, на которую хотите измененить')
sql = f'UPDATE client SET email = "{email}" WHERE id={id}'
cursor.execute(sql)
con.commit()
def select_client():
    print('список клиентов')
    sql='SELECT * FROM clients'
    out=cursor.execute(sql).fetchall()
    for id in out:
        print(*id)
def add_client():
    name=input('введите имя клиента')
    sql=f'INSERT INTO clients (name) VALUES("{name}")'
    cursor.execute(sql)
    con.commit()
    print('клиент добавлен')

def add_city():
    name=input('введите название города')
    sql=f'INSERT INTO city (name) VALUES ("{name}")'
    cursor.execute(sql)
    con.commit()
    print('город добавлен')

def change_client():
    id = input('введите id client')
    sql = f'UPDATE client SET name = ("{name}") WHERE id=({id}))'
    cursor.execute(sql)
    con.commit()
    print('данные обновлены')

def delete_client():
    id=input('введите айди клиента')
    sql=f'DELETE FROM clients WHERE id = ("{id}")'
    cursor.execute(sql)
    con.commit()
    print('клиент удален')

def menu():
    print('''
меню:
1)просмотреть список клиента
2)добавить клиента
3)удалить клиента
4)добавить город
5)изменить данные клиента''')
    select_menu=int(input('Введите пункт меню'))
    print()
    if select_menu == 1:
        select_client()
    elif select_menu == 2:
        add_client()
    elif select_menu == 3:
        delete_client()
    elif select_menu == 4:
        add_city()
    elif select_menu == 5:
        delete_client()
    else:
        exit()
    menu()

menu()