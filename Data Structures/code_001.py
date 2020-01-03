

def BinarySearch(int Array[],int start, int end, int key):
    while start<end:
        mid=(start+end)/2
        if Array[mid]>key:
            start=mid+1
        elif Array[mid]>key:
            end=mid-1
        else:
            return mid
    return -1

    
