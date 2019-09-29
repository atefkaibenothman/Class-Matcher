# class-matcher

### Creates a graph showing the similarity of courses between any number of people.

#### Tools:
1. PrettyTable
```
sudo pip3 install PTable
```

#### Steps:
1. Ask each person for a list of their courses
2. Iterate through each course and check if it is in the database.
3. If the course is in the db, add the person to the corresponding course. If not, add the course to the database and add the person to the corresponding course.
4. Iterate through the database and create graph.

#### Example:
```
Person1: classA   classB    classC
Person2: classB   classD    classC
```
#### Result:

|   | classA  | classB  | classC  | classD  |
|---|---|---|---|---|
| 1  | x  | x  | x  |   |
| 2  |   | x  | x  | x  |
