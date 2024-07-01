package repetição;

public class exercicio06 {

	public static void main(String[] args) {
		double x = 0;
		for (int i = 1; i < 50; i++) {
			if(i %2 == 0) {
				x = i/2;
				System.out.println(x);
			}
			else {
				x = 3*i+1;
				System.out.println(x);
			}
		}

	}

}
