package repetição;

public class exercicio08 {

	public static void main(String[] args) {
		double soma =0;
		int soma3=0, soma5=0,somaTotal=0;
		
		for (int i =1; i<= 20; i = i + 1) {
			if(i % 3 == 0) {
				soma3 = soma3 + i;	
			}
			if(i % 5 == 0) {
				soma5 = soma5 + i;
			}
		}
		somaTotal = soma3 + soma5;
		System.out.println(soma3);
		System.out.println(soma5);
		System.out.println(somaTotal);
	}

}
