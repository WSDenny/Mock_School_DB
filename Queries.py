import sqlite3

conn = conn = sqlite3.connect('Cosc_386_Project.db')
cur = conn.cursor()

#Which courses are offered in 2023
cur.execute('SELECT courseID, section, year \
            From Courses \
            Where year = 2023;')
for row in cur:
    print(row)
print('\n')
conn.commit()

#How many courses are offered in 2023
cur.execute('SELECT Count(Distinct section) \
            From Courses \
            Where year = 2023;')
for row in cur:
    print(row)
print('\n')
conn.commit()

#Names of Students which begin with "Sam"
cur.execute('SELECT first, last \
            From Students Where \
            first like "Sam%";')
for row in cur:
    print(row)
print('\n')
conn.commit()

#Highest Grade from the 386-001 class in FALL 2022
cur.execute('SELECT MAX(grade) \
            From Enrolled, Courses \
            Where Enrolled.courseID = Courses.courseID and year = 2022 \
            and semester like "FALL" and section = "386-001";')
for row in cur:
    print(row)
print('\n')
conn.commit()

#Average grade from 386-001 in year 2022
cur.execute('SELECT AVG(DISTINCT grade) \
            From Enrolled, Courses \
            Where Enrolled.courseID = Courses.courseID and year = 2022 \
            and section = "386-001";')
for row in cur:
    print(row)
print('\n')
conn.commit()

#Number of students in the 386-001 course during fall 2022 with a grade less than 70
cur.execute('SELECT COUNT(*) \
            From Enrolled e, Courses \
            Where e.courseID = Courses.courseID and year = 2022 \
            and section = "386-001" and semester = "FALL" and e.grade < 70;')
for row in cur:
    print(row)
print('\n')
conn.commit()

#The faculty ID of a faculty member teaching a course with more than 10 students enrolled
cur.execute('SELECT facultyID \
            From Courses \
            Where courseID = (SELECT courseID \
                                From Enrolled \
                                GROUP BY courseID \
                                HAVING COUNT(studentID) > 10);')
for row in cur:
    print(row)
print('\n')
conn.commit()

#Number of proffessors who are teaching more than 2 courses or were born in the 1980's
cur.execute('SELECT count(*) \
            From Professors \
            Where facultyID IN (SELECT facultyID \
                                From Courses \
                                GROUP BY facultyID \
                                HAVING COUNT(facultyID) > 2) OR facultyID IN (SELECT facultyID \
                                                                                From Professors \
                                                                                Where dateofbirth like "198%");')
for row in cur:
    print(row)
print('\n')
conn.commit()

conn.close()