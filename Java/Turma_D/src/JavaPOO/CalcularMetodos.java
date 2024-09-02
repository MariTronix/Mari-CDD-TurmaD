package JavaPOO;

public class CalcularMetodos {
	
	int somar(int a, int b) {
		return a+b;
	}
	
	int somar(int a, int b,int c ) {
		return a+b+c;
	}
	int sub(int a, int b) {
		return a-b;
	}
	
	int sub(int a, int b,int c ) {
		return a-b-c;
	}
	
	int mult(int a, int b) {
		return a*b;
	}
	
	int mult(int a, int b,int c ) {
		return a*b*c;
	}
	double div(int a, int b) {
		// se b for diferente de 0 calcular
		  if (b != 0) {
		        if (b < a) {
		            return a / b;
		            
		        } else {
		            return 0;
		        }
		        
		    } else {
		        // se b == 0, verificar se a também é zero para decidir a mensagem
		        if (a == 0) {      	
		        // Retornar NaN (Not a Number)
		            return Double.NaN; 
		        } else {
		        	// Ou outra forma de indicar erro de divisão por zero
		            return Double.POSITIVE_INFINITY; 
		        }
		    }
	}
	
	double div(int a, int b,int c ) {
		return a/b/c;
	}
}
