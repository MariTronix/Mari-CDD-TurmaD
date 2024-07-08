package Basico03;

import java.util.Scanner;
import java.util.StringTokenizer;

public class exercicio15 {

	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);
		System.out.print("Digite um texto: ");
		String texto = entrada.nextLine();
		String resultado = texto.toUpperCase();
		System.out.println(resultado);
		
		entrada.close();

	}
}
