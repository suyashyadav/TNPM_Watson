import csv
import operator


sample = open('D:/Watson/Training_Data/problem_solution_likes.csv', 'r')
csv1 = csv.reader(sample, delimiter=',')
sort = sorted(csv1, key=operator.itemgetter(2),reverse=True)

for eachline in sort:
    print(eachline)
