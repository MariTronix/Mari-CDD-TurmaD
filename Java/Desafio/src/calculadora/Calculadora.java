package calculadora;

public class Calculadora {

	public static void main(String[] args) {
		CalcularMetodos num = new CalcularMetodos();
		System.out.println(num.somar2num(10, 10));
		System.out.println(num.somar3num(1, 20, 30));
		System.out.println(num.sub2num(10, 10));
		System.out.println(num.sub3num(1, 20, 30));
		System.out.println(num.mult2num(10, 10));
		System.out.println(num.mult3num(1, 20, 30));
		System.out.println(num.div2num(10, 10));
		System.out.println(num.div3num(1, 20, 30));
	}

}
