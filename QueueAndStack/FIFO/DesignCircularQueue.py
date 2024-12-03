class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = []
        self.front = 0
        self.back = 0
        self.k = k
        for i in range(k):
            self.queue.append([])
        #print(self.queue)
                
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.queue[self.front] != []:
            #print(self.queue)
            return False
        else:
            if self.queue[self.back] == []:
                self.queue[self.back].append(value)
                self.front = (self.back + 1)%self.k
            else:
                self.queue[self.front].append(value)
                self.front = (self.front+1)%self.k
            #print(self.queue)
            return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.queue[self.back] != []:
            self.queue[self.back] = []
            if self.queue[(self.back+1)%self.k] != []:
                self.back = (self.back+1)%(self.k)
            #print(self.queue)
            return True
        else:
            #print(self.queue)
            return False
                
        

    def Front(self):
        """
        :rtype: int
        """
        if self.queue[(self.back-1)%self.k] == []:
            if self.queue[self.back] == []:
                return -1
            else:
                return self.queue[self.back][0] #rear +1
        if self.queue[self.front] != []:
            #print(self.back, self.front)
            return self.queue[self.front][0]
        else:
            #print(self.back, self.front)
            return self.Rear()



    def Rear(self):
        """
        :rtype: int
        """
        if self.queue[(self.front-1)%self.k] != []:
            #print(self.back, self.front)
            return self.queue[(self.front-1)%self.k][0]
        else:
            #print(self.back, self.front)
            return -1

        

    def isEmpty(self):
        """
        :rtype: bool
        """
        for item in self.queue:
            if item != []:
                return False
        return True
        

    def isFull(self):
        """
        :rtype: bool
        """
        for item in self.queue:
            if item == []: 
                return False
        return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""