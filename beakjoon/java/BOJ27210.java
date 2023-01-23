import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ27210 {

    private static int N;
    private static int[] arr;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        arr = new int[N+1];
        arr[0] = 0;
        int[] prefix1 = new int[N+1];
        int[] prefix2 = new int[N+1];
        int result = Integer.MIN_VALUE;

        st = new StringTokenizer(br.readLine(), " ");
        for(int i=1; i<N+1; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for(int i=1; i<N+1; i++){
            if(arr[i] == 1){
                prefix1[i] = prefix1[i-1]+1;
            }
            else{
                prefix1[i] = (prefix1[i-1] > 0) ? prefix1[i-1]-1 : 0;
            }
        }

        for(int i=1; i<N+1; i++){
            if (arr[i] == 2){
                prefix2[i] = prefix2[i-1]+1;
            }
            else{
                prefix2[i] = (prefix2[i-1] > 0) ? prefix2[i-1]-1 : 0;
            }
        }

        for (int i = 1; i < N+1; i++) {
            result = Math.max(result, Math.max(prefix1[i], prefix2[i]));
        }
        
        System.out.println(result);
    }
}
