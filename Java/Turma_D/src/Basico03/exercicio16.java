package Basico03;

public class exercicio16 {

	public static void main(String[] args) {
		String caracteres[] = {"a", "vida", "é", "bela"};
		String texto = "";
		for(String a: caracteres) {
			texto += a + " ";
		}
		
		System.out.print(texto.toUpperCase());
		
		for(int i = 0; i < caracteres.length; i++) {
			String texto01 = caracteres[i].toUpperCase();
			System.out.print(texto01 + " ");
		} 

	}

}
