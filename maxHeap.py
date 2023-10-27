class MaxHeap:
    def __init__(self,lst = []):
        self.data = lst
        self._buildHeap()

    def isEmpty(self):
        return len(self.data) == 0
    
    def _parent_(self,idx):
        return(idx-1)//2
    def _lchild_(self,idx):
        return(2*idx+1)
    def _rchild_(self,idx):
        return(2*idx+2)
    
    def swap(self,i,j):
        self.data[i],self.data[j] = self.data[j],self.data[i]
    
    def _buildHeap(self):
        length = len(self.data)
        start = (length-2)//2
        for idx in range(start,-1,-1):
            self._downHeap(idx,length)

    def _downHeap(self,idx,length):
        if self._lchild_(idx) < length:
            left = self._lchild_(idx)
            bigchild = left
            if self._rchild_(idx) < length:
                right = self._rchild_(idx)
                if self.data[right] > self.data[left]:
                    bigchild = right
            if self.data[bigchild] > self.data[idx]:
                self.swap(bigchild,idx)
                self._downHeap(bigchild,length)

    def addElem(self,key):
        self.data.append(key)
        self._upHeap(len(self.data)-1)
        
    def _upHeap(self,j):
        parent = self._parent_(j)
        if j>0 and self.data[j] > self.data[parent]:
            self.swap(j,parent)
            self._upHeap(parent)
    
    def get_maximum(self):
        if self.isEmpty():
            return None
        return max(self.data)
    
    def extract_maximum(self):
        if not self.isEmpty():
            if len(self.data) == 1:
                return self.data.pop()
            maximum = self.data.pop(0) 
            self._downHeap(0,len(self.data))
            return maximum

    
    def count_elements(self):
        return len(self.data)
    
    def testMaxHapProperty(self):
        if not self.isEmpty():
            flag = 1
            for idx in range(len(self.data)-1, 0, -1):
                if self.data[idx] <= self.data[self._parent_(idx)]:
                    continue
                else:
                    flag = 0
        return flag == 1

    def HeapSort(self):
        if not self.isEmpty():
            for idx in range(len(self.data)-1,0,-1):
                self.swap(0,idx)
                self._downHeap(0,idx)        