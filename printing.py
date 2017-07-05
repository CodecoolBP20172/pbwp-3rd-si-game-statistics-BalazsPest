import sys
import pprint
from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title


file_name = "game_stat.txt"
year = 1998
genre = 'First-person shooter'
title = 'Half-Life 2'

a = count_games(file_name)
b = decide(file_name, year)
c = get_latest(file_name)
d = count_by_genre(file_name, genre)
e = get_line_number_by_title(file_name, title)

the_list = [a, b, c, d, e]

pprint.pprint(the_list)
