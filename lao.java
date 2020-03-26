import java.util.*;

public class lao {
        
   
   
    public static void main(String[] args) {
        int N=11;
        int [] arr=new int[N];
        for(int i=0;i<arr.length-1;i++){
        	arr[i]=i+1;
        	
        }
        int index=new Random().nextInt(N);
        arr[arr.length-1]=new Random().nextInt(N);
        util.swap(arr,index,arr.length-1)
        	util.print(arr);
        
        
    }
}
