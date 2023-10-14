users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

dictionary = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}

uniq_users = set(users)
all_visits = len(users)

quantity_uniq_visits = len(uniq_users)

dictionary = {
    "Общее количество": all_visits,
    "Уникальные посещения": quantity_uniq_visits,
}

print(dictionary)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
