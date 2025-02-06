numbers = [2,4,6,7,1,300,30,20,45]
i = 0
largest_number = 0
for items in numbers:
    if items > largest_number:
        largest_number = items
    elif items<= largest_number:
        largest_number = largest_number
    i +=1
print(largest_number)