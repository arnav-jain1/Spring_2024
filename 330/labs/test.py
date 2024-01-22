import random as r

def main():
    elements = insertsort([r.randint(0, 100) for i in range(100)])
    print(elements)

def insertsort(unsorted):
    for i in range(1, len(unsorted)):
        value = unsorted[i]

        j = i - 1
        while j >= 0 and unsorted[j] > value:
            unsorted[j + 1] = unsorted[j]
            j -= 1
        
        unsorted[j + 1] = value
    return unsorted

main()