from maxHeap import *
max_heap = MaxHeap([8,2,100,18,22,1030])
def testMaxheap():
    max_heap.addElem(8000) 
    # max_heap.addElem(2900)
    print(max_heap.data)
testMaxheap() 

print("Maximum element:", max_heap.get_maximum()) 
print("Is the data in max-data order?", max_heap.testMaxHapProperty())  
print("Extracted maximum element:", max_heap.extract_maximum()) 
print("Is the data in max-data order?", max_heap.testMaxHapProperty())  
print("Number of elements in the data:", max_heap.count_elements())
max_heap.HeapSort()
print('Sorted Heap:',max_heap.data)