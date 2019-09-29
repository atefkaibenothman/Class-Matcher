# main.py
#
# Atef Kai Benothman
# 09/28/2019

from collections import defaultdict

def get_num_people():
    return int(input('Enter number of people: '))


def get_all_courses(n):
    all_course_list = []
    for i in range(n):
        courses = input('Enter courses: ').split()
        all_course_list.append(organize(i+1, courses))
    return all_course_list


def organize(n, course_list):
    organizer = defaultdict()
    for course in course_list:
        if n not in organizer:
            organizer[n] = [course]
        else:
            organizer[n].append(course)
    return dict(organizer)


def get_similarity(l):
    for person in l:
        return


def run():
    num_people = get_num_people()
    master_list = get_all_courses(num_people)
    get_similarity(master_list)

if __name__ == '__main__':
    run()