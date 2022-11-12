from io import StringIO
import math


def heap_print(tree, total_width=24, fill=" "):
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write("\n")
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print("-" * total_width)
    return



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

def max_insert(array, newNum):
    
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            max_heapify(array,len(array),  i)
            
def min_insert(array, newNum):
    
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            min_heapify(array,len(array),  i)



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
        max_heapify(A,n, smallest)



def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,len(A),k)

def heap_max(array):
    build_max_heap(arr)
    return array[0]

def heap_min(arr):
    build_min_heap(arr)
    return arr[0]

def heap_extract_max(array):
    heapSort(array,max_heapify)
    n = len(array)-1
    a = 0
    minimus = array[n]
    array[n] = array[a]
    a = a + 1
    array.pop()
    
    return minimus

def heap_extract_min(array):
    heapSort(array,min_heapify)
    n = len(array)-1
    a = 0
    minimus = array[n]
    array[n] = array[a]
    a = a + 1
    array.pop()
    
    return minimus

def heapSort(arr,max_heapify):
    n = len(arr)
 
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
 
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr,n,i)
 
 # One by one extract elements
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        max_heapify(arr, i,0)
def increase_key(A, i, key):
    
    if (key < A[i-1]):
        print('lol')
        #except "wrong!"
    arr[i-1] = key
    while(i > 0 and arr[(i//2)-1]<arr[i-1]):
        A[i-1], A[(i//2)-1] = A[(i//2)-1], A[i-1]
        i = (i)//2
        heapSort(A,min_heapify)


def decrease_key(A, i, key):
    
    if (key > A[i-1]):
        print('lol')
        #except "wrong!"
    arr[i-1] = key
    while(i > 0 and arr[(i//2)-1]>arr[i-1]):
        A[i-1], A[(i//2)-1] = A[(i//2)-1], A[i-1]
        i = (i)//2
        heapSort(A,min_heapify)
        
        
   


arr = []



while(True):
        x=int(input('Choose option\n1) max Insert\n2) min_insert \n3) decrease_key\n4) increase key\n\n5) extract min\n\n6)extract max'))
        if x==0:
                max_insert(arr, 50)
                min_insert(arr, 30)
                max_insert(arr, 20)
                min_insert(arr, 40)
                max_insert(arr, 70)
                min_insert(arr, 60)
                max_insert(arr, 80)
                heap_print(arr,len(arr)*4," ")

        elif x==1:
                
                try:
                        a=int(input('Put for insert '))
                        max_insert(arr,a)
                        print('\n\n\n')
                        heap_print(arr,len(arr)*4," ")
                except ValueError:
                        print("only int!")
                
                
        elif x==2:
                try:
                        a=int(input('Put for insert '))
                        min_insert(arr,a)
                        print('\n\n\n')
                        heap_print(arr,len(arr)*4," ")
                except ValueError:
                        print("only int!")
        elif x==3:
                try:
                        a=int(input('Put for insert '))
                        b = int(input('which index'))
                        decrease_key(arr,b,a)
                        print('\n\n\n')
                        heap_print(arr,len(arr)*4," ")
                except ValueError:
                        print("only int!")
        elif x==4:
            
            a=int(input('Put for insert '))
            b = int(input('which index'))
            increase_key(arr,b,a)
            print('\n\n\n')
            heap_print(arr,len(arr)*4," ")
                
        elif x==5:
            heap_extract_max(arr)
            print('\n\n\n')
            heap_print(arr,len(arr)*4," ")

        elif x==6:
             heap_extract_min(arr)
             print('\n\n\n')
             heap_print(arr,len(arr)*4," ")
                

            
            



