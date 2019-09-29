# main.py
#
# Atef Kai Benothman
# 09/28/2019

from collections import defaultdict
from prettytable import PrettyTable

def get_num_people():
    return int(input('Enter number of people: '))


def get_all_courses(n):
    all_course_list = []
    db = defaultdict()
    for i in range(n):
        courses = input('Enter courses: ').split()
        for course in courses:
            if course not in db:
                db[course] = [i]
            else:
                db[course].append(i)
    return dict(db)


def setup_pt(n, d):
    l = [i for i in d.keys()]
    l.insert(0,'')
    table = PrettyTable()
    table.add_column('', [i for i in range(n)])

    num_rows = n

    for key,values in d.items():
        empty = ['']*num_rows
        for value in values:
            empty[value] = 'x'
        table.add_column(key, empty)
    return table

def run():
    num_people = get_num_people()
    master_list = get_all_courses(num_people)
    t = setup_pt(num_people, master_list)

    print(t)

if __name__ == '__main__':
    run()