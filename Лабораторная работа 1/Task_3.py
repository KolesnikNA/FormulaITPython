list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
quantity_of_players = len(list_players)
to_equal_team = int(quantity_of_players/2)

first_team = list_players[:to_equal_team:]
second_team = list_players[to_equal_team::]

print(first_team)
print(second_team)
# TODO Разделите участников на две команды
