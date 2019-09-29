# main.py
#
# Atef Kai Benothman
# 09/28/2019

from collections import defaultdict

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


def run():
    num_people = get_num_people()
   master_list = get_all_courses(num_people)




if __name__ == '__main__':
    run()