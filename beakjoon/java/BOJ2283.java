import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ2283 {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] prefix = new int[1000002];
        
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine(), " ");
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            prefix[s+1] += 1;
            prefix[e+1] -= 1;
        }

        for(int i=1; i<1000001; i++){
            prefix[i] += prefix[i-1];
        }

        int left = 0; int right = 0;
        int value = 0;
        boolean flag = false;
        while(left < 1000001 && right < 1000001){
            if(value == K){ flag = true; break;}
            else if(value < K){value += prefix[++right];}
            else {value -= prefix[++left];}
        }

        if(flag){ System.out.println(left+" "+right);}
        else{ System.out.println("0 0");}  
    }
    
}
