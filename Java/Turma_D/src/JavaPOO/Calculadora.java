package JavaPOO;

public class Calculadora {

	public static void main(String[] args) {
		CalcularMetodos num = new CalcularMetodos();
		System.out.println(num.somar(10, 10));
		System.out.println(num.somar(1, 20, 30));
		System.out.println(num.sub(10, 10));
		System.out.println(num.sub(1, 20, 30));
		System.out.println(num.mult(10, 10));
		System.out.println(num.mult(1, 20, 30));
		System.out.println(num.div(20, 0));
		System.out.println(num.div(2, 2, 100));
	}

}
