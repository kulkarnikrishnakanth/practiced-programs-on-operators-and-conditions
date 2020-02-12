subject1 = int(input("enter subject1 marks: "))
subject2 = int(input("enter subject2 marks: "))
subject3 = int(input("enter subject3 marks: "))
subject4 = int(input("enter subject4 marks: "))
subject5 = int(input("enter subject5 marks: "))
sum_of_all_subjects = subject1 + subject2 + subject3 + subject4 + subject5
total_marks = 500
average = (sum_of_all_subjects/total_marks)*100

if average < 40:
    print("total marks=",sum_of_all_subjects, "grade is F")
elif average > 40 and average < 50:
    print("total marks= ",sum_of_all_subjects,"grade is C")
elif average > 50 and average < 60:
    print("total marks=",sum_of_all_subjects,"grade is C+")
elif average > 60 and average < 70:
    print("total marks=",sum_of_all_subjects,"grade is B")
elif average > 70 and average < 80:
    print("total marks=",sum_of_all_subjects,"grade is B+")
elif average > 80 and average < 90:
    print("total marks=",sum_of_all_subjects,"grade is A")
else:
    print("total marks=",sum_of_all_subjects,"grade is A+")

        
