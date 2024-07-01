package repetição;

import java.util.Scanner;

public class exercicio07 {

	public static void main(String[] args) {
		int alunos = 0;
		double notas = 0,soma=0, media=0;
		Scanner input = new Scanner(System.in);
		System.out.println("Quantos alunos tem na sala de aula? ");
		alunos = input.nextInt();
		int qtd = alunos;
		
		for (int i = 0; i <= alunos; i++) {
			System.out.println("Nota do alunos ");
			notas = input.nextDouble();
			soma += notas;			
			alunos --;
		}
		
		media = soma / qtd;
		System.out.println(media);
		input.close();
	}

}
