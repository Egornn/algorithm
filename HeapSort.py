def heapify(ar, n, i):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and ar[largest]<ar[l]: largest =l
    if r<n and ar[largest]<ar[r]: largest =r
    if largest!=i: 
        ar[i],ar[largest]=ar[largest],ar[i]
        heapify(ar, n, largest)

def heapSort(arr):
    n = len(arr)
 
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
    
if __name__ == '__main__':

    arr = [12, 11, 13, 5, 6, 7, 34, 12, 123, 4323, ]
    heapSort(arr)
    n = len(arr)
 
    print("Sorted array is")
    for i in range(n):
        print("%d" % arr[i], end=" ")


