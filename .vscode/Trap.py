from typing import List


class Trap:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        #scan the front list
        listFront = [0]
        frontIdx = 0
        hLen = len(height)
        for idx in range(1, hLen):
            if height[idx] > height[frontIdx]:
                listFront.append(idx)
                frontIdx = idx
        
        #scan the back list
        listBack = [hLen-1]
        backIdx = hLen-1
        for idx in range(hLen-2, -1, -1):
            if height[idx] > height[backIdx]:
                listBack.append(idx)
                backIdx = idx
        
        #compute front list
        front = listFront[0]
        TotalValue = 0
        for idx in range(1, len(listFront)):
            back = listFront[idx]
            value = height[front]
            for comIdx in range(front, back):
                TotalValue += (value-height[comIdx])
            front = back
        
        back = listBack[0]
        #compute back list
        for idx in range(1,len(listBack)):
            front = listBack[idx]
            value = height[back]
            for comIdx in range(back, front, -1):
                TotalValue += (value - height[comIdx])
            back = front
        
        value = height[frontIdx]
        for idx in range(frontIdx, backIdx):
            TotalValue += (value - height[idx])

        return TotalValue

tr = Trap()
heights = [0,1,0,2,1,0,1,3,2,1,2,1]      
res = tr.trap(heights)

print("res: ",res)
print(1)
