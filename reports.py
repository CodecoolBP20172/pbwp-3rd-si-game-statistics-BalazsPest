import csv
import sys
file_name = "game_stat.txt"
year = 2007
genre = 'First-person shooter'
title = 'Half-Life'


"""
#for dictionary
def game_list(file_name):

    results = []
    with open(sys.path[0] + '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))

    print(results)
    for i in results:
        i.insert(0,"title")
        i.insert(2,"copies")
        i.insert(4,"year")
        i.insert(6,"genre")
        i.insert(8,"publisher")
"""


def count_games(file_name):
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
    return(len(results))


def decide(file_name, year):
    x = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
    for i in results:
        for n in i:
            if str(year) == n:
                x += 1
    if x > 0:
        return True
    else:
        return False


def get_latest(file_name):
    t = 0
    latest = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
        for i in results:
            if int(results[t][2]) > int(latest):
                latest = results[t][2]
                name = results[t][0]
            t += 1
        return(name)


def count_by_genre(file_name, genre):
    x = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
    for i in results:
        if genre in i:
            x += 1
    return x


def get_line_number_by_title(file_name, title):
    x = 0
    results = []
    with open(sys.path[0] + '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
    for i in results:
        x += 1
        if title in i:
            break
    return x


get_line_number_by_title(file_name, title)
count_by_genre(file_name, genre)
get_latest(file_name)
decide(file_name, year)
count_games(file_name)
