import time

def mergesort(A):
    if len(A) > 1:
        mid = len(A) // 2

        L = A[:mid]
        R = A[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

    return A

def bubblesort(A):
    n = len(A)
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if A[j] < A[j-1]:
                aux = A[j]
                A[j] = A[j-1]
                A[j-1] = aux
    return A

def heapify(A, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[i] < A[l]:
        largest = l

    if r < n and A[largest] < A[r]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

def build(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)

def heapsort(A):
    n = len(A)
    build(A)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

    return A


def insertion(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i -1
        A[i+1] = key
    return A

def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)

def quicksort(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(arr, l, h)

        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
    return array


ranges = ['big','few','med']
types = ['D','NS','R']
lengths = ['40000']

files = []
for i in range(len(ranges)):
    for j in range(len(types)):
        for k in range(len(lengths)):
            string = ranges[i] + types[j] + lengths[k] + '.txt'
            files.append(string)

startt = time.time()
with open("out.txt","w") as f1:
    for file_name in files:
        with open(file_name,"r") as f:
            array = f.read().split()
            for i in range(0, len(array)):
                array[i] = int(array[i])

            for i in range(5):
                start = time.time()
                if i == 0: mergesort(array); algorithm = "merge"
                if i == 1: heapsort(array); algorithm = "heap"
                if i == 2: quicksort(array,0,len(array)-1); algorithm = "quick"
                if i == 3: insertion(array); algorithm = "insertion"
                if i == 4: bubblesort(array); algorithm = "bubble"
                end = time.time()
                print(file_name, algorithm, end - start, file=f1)

endd = time.time()
print(endd-startt)
