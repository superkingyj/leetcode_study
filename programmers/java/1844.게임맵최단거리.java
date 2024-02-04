import java.util.Queue; 
import java.util.LinkedList;

class Pair{
    int x, y, cnt;
    public Pair(int x, int y, int cnt){
        this.x = x;
        this.y = y;
        this.cnt = cnt; 
    }
}

class Solution {
    public static int MAX_NUM = 100;
    public static int[][] grid = new int[MAX_NUM][MAX_NUM];
    public static int[][] visited = new int[MAX_NUM][MAX_NUM];
    public static Queue<Pair> q = new LinkedList<>();
    public static int N, M;
    public static int[] dx = new int[]{0, 1, 0, -1};
    public static int[] dy = new int[]{-1, 0, 1, 0};
    
    public static boolean inRange(int x, int y){
        return 0 <= x && x < N && 0 <= y && y < M;
    }
    
    public static boolean canGo(int x, int y){
        if (!inRange(x, y)) { return false; }
        if (visited[x][y] > 0) { return false; }
        if (grid[x][y] == 0) { return false; }
        return true;
    }
    
    public static void BFS(){
        q.add(new Pair(0, 0, 1));
        visited[0][0] = 1;
        
        while(!q.isEmpty()){
            Pair curr = q.poll();
            int x = curr.x, y = curr.y, cnt = curr.cnt;
            System.out.println(x);
            System.out.println(y);
            System.out.println(cnt);
            
            for(int i = 0; i < 4; i++){
                int newX = x+dx[i];
                int newY = y+dy[i];
                
                if (canGo(newX, newY)) {
                    visited[newX][newY] = cnt+1;
                    q.add(new Pair(newX, newY, cnt+1));
                }
            }
        }
    }
    
    public int solution(int[][] maps) {
        int answer = 0;
        N = maps.length;
        M = maps[0].length;
        BFS();
        answer = visited[N-1][M-1];
        return answer;
    }
}

public static void main(String[] args) {
    Solution solution = new Solution();
    int[][] grid = {{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}};
    solution.solution(grid);

}