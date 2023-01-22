import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ12865 {
    private static int N, K;
    private static int[] W;
    private static int[] V;

    private static void knapsack(){
        int[] dp = new int[K+1];

        for(int n=1; n<=N; n++){
            int w = W[n-1];
            int v = V[n-1];
            for(int k=K; k>=w; k--){
                dp[k] = Math.max(dp[k], dp[k-w]+v);
            }
        }
        System.out.println(dp[K]);
    
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        W = new int[N]; 
        V = new int[N];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine(), " ");
            W[i] = Integer.parseInt(st.nextToken());
            V[i] = Integer.parseInt(st.nextToken());
        }

        knapsack();
    }

}