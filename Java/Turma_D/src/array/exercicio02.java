package array;

import java.util.Scanner;

public class exercicio02 {

	public static void main(String[] args) {
		double[] nota = new double[5];
		double soma = 0;
		double media = 0;
		
		Scanner input = new Scanner(System.in);
		
		for(int i=0; i<nota.length; i++) {
			System.out.print("Nota do aluno: ");
			nota[i] = input.nextDouble();	 
		}
		
		for(int x=0; x<nota.length; x++) {
			soma += nota[x];
				
		}
		media = soma / nota.length;
		
		System.out.println(soma);
	}
}
