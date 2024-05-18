class MyHashSet:

    def __init__(self):
        self.arr = [None] * 8
        self.capacity = 8
        self.size = 0
        self.thres = 2 / 3
        
    def hash(self, key): return key % self.capacity
        
    def rehash(self, key): return (5 * key + 1) % self.capacity
    
    def insertPos(self, key):
        pos = self.hash(key)
        #using -1 to represent the "removed" item
        while self.arr[pos] is not None:
            if self.arr[pos] == key: return -1
            #here is the small bug, the following item may contain the key
            if self.arr[pos] == -1: break
            pos = self.rehash(pos)
        return pos
    
    def safeAdd(self, key):
        pos = self.insertPos(key)
        #already in, 
        if pos == -1: return 
        self.arr[pos] = key
        self.size += 1
    
    def safeAddArr(self, arr):
        for val in arr: 
            if val is not None: self.safeAdd(val)

    def add(self, key):
        def preAdd(self):
            if self.size / self.capacity <= self.thres: return 
            self.capacity <<= 1
            oldArr, self.arr = copy.deepcopy(self.arr), [None] * self.capacity
            self.safeAddArr(oldArr)
        
        preAdd(self)
        #fix the small bug by precheck before add
        if self.contains(key): return
        self.safeAdd(key)
         
    def remove(self, key):
        pos = self.hash(key)
        while self.arr[pos] is not None:
            if self.arr[pos] == key: 
                #you cannot assign None, because you will lose track of continuous items
                self.arr[pos] = -1
                self.size -= 1
                return
            pos = self.rehash(pos)
        return

    def contains(self, key):
        pos = self.hash(key)
        while self.arr[pos] is not None:
            if self.arr[pos] == key: return True
            pos = self.rehash(pos)
        return False

"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 

Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.
"""