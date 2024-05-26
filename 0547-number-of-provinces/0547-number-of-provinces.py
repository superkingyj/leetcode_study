class Solution:
    def _dfs(self, i):
        self.visited[i] = True

        for j in range(0,self.n):
            if self.arr[i][j] == 1 and not self.visited[j]:
                self._dfs(j)
                
    def findCircleNum(self, array: List[List[int]]) -> int:
        self.arr = array
        self.n = len(array)
        self.visited = [0] * self.n
        result = 0

        for i in range(0 , self.n):
            if not self.visited[i]:
                self._dfs(i)
                result +=1
        
        return result
        