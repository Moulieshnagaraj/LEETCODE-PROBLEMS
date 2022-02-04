class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res=[[] for i in range(n)]

        left, right=0, n
        top,bottom=0,n
        ele = 1
        while (left < right) and (top < bottom):
            for i in range(left, right):
                res[top].insert(i, ele)
                ele+=1
            top+=1

            for i in range(top, bottom):
                res[i].insert(top-1,ele)
                ele+=1
            right-=1

            for i in range(right-1, left-1,-1):
                res[bottom-1].insert(left,ele)
                ele+=1
            bottom-=1

            for i in range(bottom-1, top-1, -1):
                res[i].insert(left,ele)
                ele+=1
            left+=1
        return res
