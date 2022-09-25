from random import sample

lst = sample(range(1, 51), 50)

print('Unsorted list: ', lst)

def bubble_sort(l):
    check = sorted(l)
    while l != check:
        x = len(l)
        for i in range(x-1):
            if l[0+i] > l[1+i]:
                l[0+i], l[1+i] = l[1+i], l[0+i]


    print('Sorted list: ', l)



bubble_sort(lst)