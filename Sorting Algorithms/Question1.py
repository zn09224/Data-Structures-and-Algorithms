def selection_sort(list):
    for i in range(len(list)):
        min = list[i]
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min = list[j]
                min_index = j
        temp = list[i]
        list[i] = min
        list[min_index] = temp
        print(list)


# #function call
# selection_sort([54, 26, 93, 17, 77, 31, 44, 55, 20])
# #Printed on terminal
# [17, 26, 93, 54, 77, 31, 44, 55, 20]
# [17, 20, 93, 54, 77, 31, 44, 55, 26]
# [17, 20, 26, 54, 77, 31, 44, 55, 93]
# [17, 20, 26, 31, 77, 54, 44, 55, 93]
# [17, 20, 26, 31, 44, 54, 77, 55, 93]
# [17, 20, 26, 31, 44, 54, 77, 55, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
    