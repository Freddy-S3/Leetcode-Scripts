class MyHashSet {
    int num[];
    public MyHashSet() {
        num = new int[31251];
    }
	
	// set the bit if that element is present
    public void add(int key) {
        num[getIdx(key)]|=getMask(key);
    }
	
	//unset the bit if a key is not present
    public void remove(int key) {
        num[getIdx(key)] &= (~getMask(key));
    }
	
	//check if bit corresponding to the key is set or not
    public boolean contains(int key) {
        return (num[getIdx(key)]&getMask(key))!=0;
    }
	
	// idx of num[] to which this key belongs
	// for key = 37, it will give 1
    private int getIdx(int key)
    {
        return (key/32);
    }
	
	// get mask representing the bit inside num[idx] that corresponds to given key.
	// for key = 37, it will give 00000000000000000000000000100000
    private int getMask(int key)
    {
        key%=32;
        return (1<<key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */

/*
 * Design a HashSet without using any built-in hash table libraries.

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
 */