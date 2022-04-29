"""Note:
    1: pseudo mark
    2: pay attention on fix() and unfix(), it does not operate as '!' operation.    
"""

class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitset = [0] * size
        self.bitsum = sum(self.bitset)
        self.flip_flag = False


    def fix(self, idx: int) -> None:
        if self.bitset[idx] == 1 and self.flip_flag:
            self.bitsum += 1
            self.bitset[idx] = 0
        if self.bitset[idx] == 0 and not self.flip_flag:
            self.bitsum += 1
            self.bitset[idx] = 1
        


    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == 0 and self.flip_flag:
            self.bitsum -= 1
            self.bitset[idx] = 1
        if self.bitset[idx] == 1 and not self.flip_flag:
            self.bitsum -= 1
            self.bitset[idx] = 0

    def flip(self) -> None:
        self.flip_flag = not self.flip_flag
        self.bitsum = self.size - self.bitsum

    def all(self) -> bool:
        if self.bitsum == self.size:
            return True
        else:
            return False

    def one(self) -> bool:
        if self.bitsum != 0:
            return True
        else:
            return False

    def count(self) -> int:
        return self.bitsum


    def toString(self) -> str:
        if self.flip_flag:
            string = [str(i ^ 1) for i in self.bitset]
        else:
            string = [str(i) for i in self.bitset]
        return ''.join(string)