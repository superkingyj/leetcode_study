import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] arr;
    static int N;
    static int M;
    static int[][] dp;
    static int max_val;

    private static void dynamic_programming(){
        dp = new int[N+1][M+1];

        for(int i=1; i<N+1; i++){
            for(int j=1; j<M+1; j++){
                if(arr[i][j]==0){
                    dp[i][j] = Math.min(Math.min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])+1;
                    max_val = Math.max(max_val, dp[i][j]);
                }
            }
        }

        System.out.println(max_val);
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N+1][M+1];

        for(int i=1; i<N+1; i++){
            st = new StringTokenizer(br.readLine(), " ");
            for(int j=1; j<N+1; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dynamic_programming();
    }
}
