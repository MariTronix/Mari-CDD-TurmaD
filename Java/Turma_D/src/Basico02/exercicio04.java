package Basico02;

public class exercicio04 {

	public static void main(String[] args) {
		int par = 1;
		while(par < 101) {
			if(par % 2 == 0) {
				System.out.print(par + " " );
			}
		par++;
		}
		System.out.println();
		
		int impar = 1;
		while(impar < 101) {
			if(impar % 2 == 1) {
				System.out.print(impar + " ");
			}
		impar++;
		}

	}

}
