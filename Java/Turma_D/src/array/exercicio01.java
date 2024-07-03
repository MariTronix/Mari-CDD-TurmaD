package array;

import java.util.Scanner;

public class exercicio01 {

	public static void main(String[] args) {
		int[] A = new int [10];
		int[] B = new int [10];
		int[] C = new int [10];
		int[] D = new int [10];
		Scanner input = new Scanner(System.in);
		
		for(int a=0; a<A.length; a++) {
			System.out.print("Digite valor para valor array A: ");
			A[a] = input.nextInt();		 
		}
		for(int b=0; b<A.length; b++) {
			System.out.print("Digite valor para valor array B: ");
			B[b] = input.nextInt();		 
		}
		for(int c=0; c<A.length; c++) {
			System.out.print("Digite valor para valor array C: ");
			C[c] = input.nextInt();		 
		}
		for(int d=0; d<A.length; d++) {
			System.out.print("Digite valor para valor array D: ");
			D[d] = input.nextInt();		 
		}
		
		
		for(int i=0; i<A.length; i++) {
			System.out.println(A[i] + " ");
		}
		for(int i=0; i<B.length; i++) {
			System.out.println(B[i] + " ");
		}
		for(int i=0; i<C.length; i++) {
			System.out.println(C[i] + " ");
		}
		for(int i=0; i<D.length; i++) {
			System.out.println(D[i] + " ");
		}
	}

}
