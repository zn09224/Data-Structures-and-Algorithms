def bubble_sort(lst):
    if len(lst) == 1:
        print(lst)

    for i in range(len(lst)-1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1] 
                lst[j+1] = temp
        print(lst)



# #Function call
bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])

# #Printed on terminal
# [26, 54, 17, 77, 31, 44, 55, 20, 93]
# [26, 17, 54, 31, 44, 55, 20, 77, 93]
# [17, 26, 31, 44, 54, 20, 55, 77, 93]
# [17, 26, 31, 44, 20, 54, 55, 77, 93]
# [17, 26, 31, 20, 44, 54, 55, 77, 93]
# [17, 26, 20, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]