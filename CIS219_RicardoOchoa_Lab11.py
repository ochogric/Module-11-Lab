#9.1 (CLASS AVERAGE: WRITING GRADES TO A PLAIN TEXT FILE) 

print('Enter any number of grades (-1 to quit)')
#open the txt file in write mode
file = open("grades.txt",'w')
#input the grades till user wishes to exit
while True:
    grade = int(input())
    if grade==-1:
        break
    else:
        file.writelines(f'{grade}\n')
    
#close the text file
file.close()

#9.2 (CLASS AVERAGE: READING GRADES FROM A PLAIN TEXT FILE)

grades = None #to store the grades
#open the file and read the grades
with open('grades.txt','r') as file:
    grades = file.readlines()

total = 0 #to store the sum of grades

#iterate over the grades and print it
for grade in grades:
    grade = int(grade.strip())
    print(grade)
    total += int(grade)
    
#display the info as mentioned
print(f"Total: {total}")
print(f"Count: {len(grades)}")
print(f"Average: {total/len(grades) : .2f}")

#9.3 (CLASS AVERAGE: WRITING STUDENT RECORDS TO A CSV FILE)
import csv

# open the file for writing
outfile = open('grades.csv', 'w', newline='')

# create a file writer object
writer = csv.writer(outfile)

# write the header row
writer.writerow(['Name', 'Test 1', 'Test 2', 'Test 3'])

# get the number of students
num_students = int(input('Enter the number of students: '))

# get each student's name and three test scores
for student in range(num_students):
    # get the student's name
    name = input('Enter the student\'s name: ')

    # get the student's three test scores
    test1 = int(input('Enter the score for test 1: '))
    test2 = int(input('Enter the score for test 2: '))
    test3 = int(input('Enter the score for test 3: '))

    # write the student's record to the file
    writer.writerow([name, test1, test2, test3])

# close the file
outfile.close()
print('Data written to grades.csv')
