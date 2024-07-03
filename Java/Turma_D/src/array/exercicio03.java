package array;

import java.util.Arrays;

public class exercicio03 {

	public static void main(String[] args) {
		int[] array = {81,32,17,8,20,91,43};
		int[] arrayInvertido = new int[array.length];
		
		
		for(int x= array.length-1; x >= 0; x--) {
			System.out.print(array[x] + " ");
			 
		}
		System.out.println();
		
		for(int y= 0; y < array.length; y++) {
				arrayInvertido[y] = array[6-y];
			}
		
		for(int i= 0; i < arrayInvertido.length; i++) {
			System.out.print(arrayInvertido[i] + " ");
		
		}
		
		System.out.println();
				
		Arrays.sort(array);
		
		for (int z : array) {
            System.out.print(z + " ");
		}

	}
}


