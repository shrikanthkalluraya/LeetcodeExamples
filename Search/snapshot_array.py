'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id'
'''
class SnapshotArray:

    def __init__(self, length: int):
        self.histories = [[[-1, 0]] for _ in range(length)]
        self.snap_id=0
        

    def set(self, index: int, val: int) -> None:
        self.histories[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        left, right, pos = 0, len(self.histories[index])-1, -1
        while left <= right:
            mid = (left+right) // 2
            if self.histories[index][mid][0] <= snap_id:
                left = mid + 1
                pos = mid
            else:
                right = mid - 1
        return self.histories[index][pos][1]
