import csv
import sys
import math
file_name = "game_stat.txt"
title = "Doom 3"

def get_most_played(file_name):
    results = []
    t = 0
    most_played = 0
    with open(sys.path[0] + '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
        for i in results:
            if float(results[t][1]) > float(most_played):
                most_played = results[t][1]
                name = results[t][0]
            t += 1
        return(name)


def sum_sold(file_name):
    results = []
    sold_sum = []
    with open(sys.path[0]+ '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
        for i in results:
            sold_sum.append(float(i[1]))
        return sum(sold_sum)

def get_selling_avg(file_name):
    results = []
    sold_sum = []
    with open(sys.path[0]+ '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
        for i in results:
            sold_sum.append(float(i[1]))
        return sum(sold_sum)/len(sold_sum)

def count_longest_title(file_name):
    results = []
    t = 0
    len_name = " "
    with open(sys.path[0] + '/' +file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
        for i in results:
            if len(results[t][0]) > len(len_name):
                len_name = results[t][0]
                name = results[t][0]
            t += 1
        return len(name)

def get_date_avg(file_name):
    results = []
    years = []
    with open(sys.path[0]+ '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
        for i in results:
            years.append(int(i[2]))
        return math.ceil(sum(years)/len(years))  

def get_game(file_name, title):
    results = []
    with open(sys.path[0]+ '/' + file_name, "r") as inputfile:
        for line in inputfile:
            results.append(line.strip().split('\t'))
        for i in results:
            if title == i[0]:
                return i


get_most_played(file_name)
sum_sold(file_name)
get_selling_avg(file_name)
count_longest_title(file_name)
get_date_avg(file_name)
get_game(file_name, title)