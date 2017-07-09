import sys
import pprint
from reports import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game



file_name = "game_stat.txt"
title = 'Half-Life 2'

a = get_most_played(file_name)
b = sum_sold(file_name)
c = get_selling_avg(file_name)
d = count_longest_title(file_name)
e = get_date_avg(file_name)
f = get_game(file_name, title)

the_list =[a,b,c,d,e,f]

pprint.pprint(the_list)