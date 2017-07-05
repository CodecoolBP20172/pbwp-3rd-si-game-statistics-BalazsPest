import sys
from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title


def print_out():
    file_name = "game_stat.txt"
    year = 1998
    genre = 'First-person shooter'
    title = 'Half-Life 2'

    a = count_games(file_name)
    b = decide(file_name, year)
    c = get_latest(file_name)
    d = count_by_genre(file_name, genre)
    e = get_line_number_by_title(file_name, title)

    with open(sys.path[0] + '/' + "answers.txt", "w+") as outputfile:
        outputfile.write(str(a) + "\n" + str(b) + "\n" + str(c) + "\n" + str(d) + "\n" + str(e) + "\n")
        outputfile.close()


print_out()
