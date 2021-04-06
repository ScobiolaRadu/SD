import time
import random
import itertools

def test_sort(arr):
    if sorted(arr) == arr:
        return True
    return False

def BubbleSort(arr):
    n = len(arr)
    verificat = False
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                verificat = True
        if verificat == False:
            break

def CountSort(arr):
    maxim = max(arr)+2
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(maxim)]
    for element in arr:
        count[element] += 1
    for i in range(maxim):
        count[i] += count[i - 1]
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

def get_num(x):
    m = 0
    for element in x:
        m = max(m, element)
    return len(str(m))

from functools import reduce
def flatten(arr):
    return reduce(lambda x, y: x + y, arr)

def RadixSort(arr, nr):
    for cifra in range(0, nr):
        B = [[]for i in range(10)]
        for item in arr:
            num = item // 10 ** (cifra) % 10
            B[num].append(item)
        arr = flatten(B)
    return arr

def MergeSort(arr):
    if len(arr) > 1:
        mij = len(arr) // 2
        st = arr[:mij]
        dr = arr[mij:]
        MergeSort(st)
        MergeSort(dr)
        i = j = k = 0
        while i < len(st) and j < len(dr):
            if st[i] < dr[j]:
                arr[k] = st[i]
                i += 1
            else:
                arr[k] = dr[j]
                j += 1
            k += 1
        while i < len(st):
            arr[k] = st[i]
            i += 1
            k += 1

        while j < len(dr):
            arr[k] = dr[j]
            j += 1
            k += 1

def Mediana_3(arr,st,dr):
    mij = (st+dr)//2
    a = arr[st]
    b = arr[mij]
    c = arr[dr]
    if a <= b and b <= c:
        return b, mij
    elif c <= b and b <= a:
        return b, mij
    elif b <= c and c <= a:
        return c, dr
    elif a <= c and c <= b:
        return c, dr
    else:
        return a, st

def Partitie(arr,st,dr):
    pivot, poz = Mediana_3(arr, st, dr)
    arr[dr], arr[poz] = arr[poz], arr[dr]
    i = st
    j = dr-1
    while True:
        while arr[i] <= pivot and i <= j:
            i += 1
        while arr[j] >= pivot and i <= j:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[i], arr[dr] = arr[dr], arr[i]
    return i

def QuickSort(arr, st, dr):
    while st < dr:
        poz = Partitie(arr, st, dr)
        if poz - st < dr - poz:
            QuickSort(arr, st, poz-1)
            st = poz + 1
        else:
            QuickSort(arr, poz+1, dr)
            dr = poz - 1

sorts = [BubbleSort, CountSort, RadixSort, MergeSort, QuickSort]
sortnames = {BubbleSort:"Bubblesort", CountSort:"Countsort", RadixSort:"Radixsort", MergeSort:"Mergesort", QuickSort:"Quicksort"}
f = open("teste")
numar_teste = int(f.readline())
for i in range(numar_teste):
    print("Testul", i+1)
    N, Max = f.readline().split()
    N = int(N)
    Max = int(Max)
    a = [random.randrange(Max + 1) for j in range(N)]
    print("N =", N, "Max =", Max)
    for sort in sorts:
        start = time.time()
        if sort == BubbleSort and N >= 10**6:
            print("N este prea mare pentru ca Bubblesort sa rezolve in timp util")
            continue

        if sort != QuickSort and sort != RadixSort:
            sort(a)
        elif sort == QuickSort:
            sort(a, 0, len(a)-1)
        elif sort == RadixSort:
            nr = get_num(a)
            if N >= 10**8:
                print("N este prea mare ca RadixSort sa rezolve in timp util")
                continue
            a = RadixSort(a, nr)

        end = time.time()
        print(sortnames[sort], "\n", "Timp executare:", end-start, "\n", "Status sortare:", test_sort(a), "\n", sep="")
        

start=time.time()
a = [random.randrange(10**7+1) for i in range(10**6)]
QuickSort(a,0,len(a)-1)
end=time.time()
print(end-start)








