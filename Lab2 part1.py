def max_heapify(A,n,k):
    l = left(k)
    r = right(k)
    if l < n and A[l] > A[k]:
        largest = l
    else:
        largest = k
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != k:
        A[k], A[largest] = A[largest], A[k]
        max_heapify(A,n, largest)

def left(k):
    return 2 * k + 1

def right(i):
    return 2 * i + 2

def build_max_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        max_heapify(A,len(A),k)

def insert(array, newNum):
    
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            max_heapify(array,len(array),  i)

def min_heapify(A,n,k):
    l = left(k)
    r = right(k)
    if l < n and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < n and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A,n, smallest)



def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,len(A),k)

def heapSort(arr,heapify):
    n = len(arr)
 
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr,n,i)
 
 # One by one extract elements
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i,0)

A = []


heapSort(A,min_heapify)




while(True):
        x=int(input('Choose option\n1) Insert\n2) max heap \n3) min heap\n4) successor node\n\n'))
        if x==0:
                insert(A, 50)
                insert(A, 30)
                insert(A, 20)
                insert(A, 40)
                insert(A, 70)
                insert(A, 60)
                insert(A, 80)
                print(A)

        elif x==1:
                
                try:
                        a=int(input('Put for insert '))
                        insert(A,a)
                        print('\n\n\n')
                        print(A)
                except ValueError:
                        print("only int!")
                
                
        elif x==2:
                build_max_heap(A)
                print(A)
        elif x==3:
                build_min_heap(A)
                print(A)
        elif x==4:
            a = int(input('1 - min 2 - max : '))
            if a==1:
                
                heapSort(A,min_heapify)
                print(A)
            if a==2:
                heapSort(A,max_heapify)
                print(A)
        

