
min_value = int(input("enter min value: "))
max_value = int(input("enter max value: "))
start_value = int(input("enter min value again: "))
while min_value <= start_value <= max_value:
    if start_value % 7 == 0 and start_value % 5 == 0:
        print(start_value)
    start_value = start_value + 1

    
