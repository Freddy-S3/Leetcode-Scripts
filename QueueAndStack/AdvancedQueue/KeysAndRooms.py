class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if len(rooms) < 2:
            return True
        
        #BFS
        keyQueue = [0]
        visited = set()
        for key in keyQueue: #check each key in queue
            visited.add(key)
            for newKey in rooms[key]:
                if newKey not in visited:
                    keyQueue.append(newKey)
        
        return len(visited) == len(rooms)


        """
        if len(rooms) < 2:
            return True
        
        #memory saver
        keyQueue = [0]
        visited = set()
        
        j = 0
        while j < len(keyQueue):
            visited.add(keyQueue[j])
            for newKey in rooms[keyQueue[j]]:
                if newKey not in visited:
                    keyQueue.append(newKey)
            del keyQueue[j]         
            
        
        return len(visited) == len(rooms)
        """
        
        """
        #sequential search
        roomQueue = []
        keys = {0}
        i = 0
        for i in range(len(rooms)):
            if i in keys:
                for key in rooms[i]:
                    keys.add(key)
            else:
                roomQueue.append(i)#add to queue
        
        if roomQueue != []:
            j = 0
            while j < len(roomQueue):
                if roomQueue[j] in keys:
                    for key in rooms[roomQueue[j]]:
                        keys.add(key)
                    del roomQueue[j]
                    j = 0
                else:
                    j += 1
        
        return roomQueue == []
        """



"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
 

Constraints:

n == rooms.length
2 <= n <= 1000
0 <= rooms[i].length <= 1000
1 <= sum(rooms[i].length) <= 3000
0 <= rooms[i][j] < n
All the values of rooms[i] are unique.
"""