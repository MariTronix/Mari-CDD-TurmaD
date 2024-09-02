package Polimorfismo;

public class triangulo extends formas {
	
	public void CalcArea(double b, double a) {
		 System.out.println((b*a)/2);
	}
	
	public void CalcPerimetro(double a, double b, double c) {
		System.out.println(a+b+c);
	}
	public void CalcPerimetro(double a) {
		System.out.println(a*3);
	}
}
