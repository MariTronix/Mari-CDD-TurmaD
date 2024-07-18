package construtores;

public class estacionamento {

	public static void main(String[] args) {
		Carro c1 = new Carro("Azul", 10.10, "Fiat");
		System.out.println(c1.modelo);
		c1.status();
		c1.desligar();
		c1.ligar();
		c1.status();
		c1.desligar();
		
	}
}
