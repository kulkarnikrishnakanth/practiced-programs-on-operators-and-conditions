num_of_cls_held = 200
num_of_cls_attended = int(input("enter number of classes attended: "))
average = (num_of_cls_attended/num_of_cls_held) * 100
if average >= 75:
    print("your attendence % is",average,"you can write exam")
elif average >= 60 and average <75:
    medical_cause = input("did you suffered with any health issue (yes/no): ")
    if medical_cause == "yes":
        print("your attendence % is",average,"you can write the exam")
    else:
        print("your attendence % is",average,"you are not allowed to write exam")
else:
    print("your attendence % is",average,"you are not allowed to write exam")