class Solution:
    def GetMinCalculateCount(self, sourceX, sourceY, targetX, targetY) :
        if sourceX > targetX or sourceY > targetY:
            return -1
        
        ret = 0
        
        while targetX >= (sourceX * 2) and targetY >= (sourceY * 2):
            if targetX % 2 == 0 and targetY % 2 == 0:
                targetX, targetY  = targetX // 2,  targetY // 2
            else:
                targetX, targetY  = targetX - 1,  targetY - 1
            ret += 1

        if sourceX == targetX and sourceY == targetY:
            return ret
        if targetX - sourceX == targetY - sourceY:
            return ret + (targetX - sourceX)
        else:
            return -1
            


if __name__ == "__main__":
    s = Solution()
    sourceX, sourceY, targetX, targetY = 10, 100, 9, 
    print(s.GetMinCalculateCount(sourceX, sourceY, targetX, targetY))
