from minHeap import *
min_heap = MaxHeap([8,2,100,18,22,1030])
def testMaxheap():
    min_heap.addElem(8000)
    print(min_heap.data)
testMaxheap() 

print("Minimum element:", min_heap.get_minimum()) 
print("Is the data in max-data order?", min_heap.testMinHapProperty())  
print("Extracted maximum element:", min_heap.extract_minimum()) 
print("Is the data in max-data order?", min_heap.testMinHapProperty())  
print("Number of elements in the data:", min_heap.count_elements())
min_heap.HeapSort()
print('Sorted Heap:',min_heap.data)