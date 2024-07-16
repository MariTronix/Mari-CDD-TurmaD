package Turma_D;

public class OperadorExemplo7 {

	public static void main(String[] args) {
		int a = 10;
		int b = 10;
		double media = (a + b) / 2;
		
		System.out.println(media >= 7 ? "Par" : "Impar");
		System.out.println(media >= 7 ? "Aprovado": media >= 4 ? "Recuperação" : "Reprovado");

	}

}
