package Basico03;

public class exercicio14 {

	public static void main(String[] args) {
		String texto01 = "Será que são iguais?";
		String texto02 = "Será que são iguais?";
		
		boolean b1 = texto01.equals(texto02);
		
		if(b1 == true) {
			System.out.println("São iguais");
		}
		else {
			System.out.println("Não são iguais");
		}
	}
}
