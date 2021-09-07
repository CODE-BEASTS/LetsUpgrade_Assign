#Write a program to implement insertion sort
def insertion_sort(e_list):
    for i in range(1, len(e_list)):
        temp = e_list[i]
        x = i - 1
        while (x >= 0 and temp < e_list[x]):
            e_list[x + 1] = e_list[x]
            x = x - 1
        e_list[x + 1] = temp
 
 
e_list = input('Enter the numbers: ')
e_list = [int(x) for x in e_list]
insertion_sort(e_list)
print('Sorted list: ', end='')
print(e_list)