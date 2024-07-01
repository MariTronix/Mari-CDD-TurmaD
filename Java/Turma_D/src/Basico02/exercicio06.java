package Basico02;

public class exercicio06 {

	public static void main(String[] args) {
		int x = 1;
		int y = 1000000000;
		
		for(int i = x; i < y; i++) {
			if (i % 19 == 0) {
				System.out.println("Achei um número divisível por 19 entre x e y" + " " + i);
				break;
			}
		}

	}

}
