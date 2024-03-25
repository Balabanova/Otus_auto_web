import csv
import json

result_json = []
user_number = 0


with open("users.json", "r") as jsonFile:
    users = json.load(jsonFile)
    users_count = len(users)
    for user in users:
        result_json.append(
            {
                'name': user.get('name'),
                'gender': user.get('gender'),
                'address': user.get('address'),
                'age': user.get('age'),
                'books': []
            }
        )

with open('books.csv', newline='') as csvFile:
    books = csv.reader(csvFile, delimiter=',')
    next(books, None)  # пропускаю строку с заголовками
    for book in books:
        if user_number == users_count:
            user_number = 0
        result_json[user_number]['books'].append(
            {
                'title': book[0],
                'author': book[1],
                'pages': book[3],
                'genre': book[2]
            }
        )
        user_number += 1

with open('result.json', 'w') as out_json:
    json.dump(result_json, out_json, indent=2)


