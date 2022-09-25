from random import sample

lst = sample(range(1, 51), 50)
seeking = int(input('Target: '))
res = False


def binary_search(lst, seeking):
    global res
    lst.sort()
    first = lst[0]
    last = lst[-1]
    while first < last:
        middle = (first+last)//2
        if middle == seeking:
            first = middle
            last = first
            seeking = middle
            res = True
        elif seeking > middle:
            first = middle +1
        elif seeking < middle:
            last = middle -1
        if res == True:
            print('found!!')
            break

    if res == False:
        print('failed')


binary_search(lst, seeking)









