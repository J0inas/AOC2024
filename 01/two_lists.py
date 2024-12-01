# Plan
# sort both lists
# pair the numbers

list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

list1.sort()
list2.sort()

print(list1)
print(list2)

sum_of_lists = 0

for i in list1:
    sum_of_lists += abs(list1[i] - list2[i])

print(sum_of_lists)