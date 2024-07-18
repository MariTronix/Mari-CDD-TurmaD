package construtores;

public class Carro {
	public String cor;
	public double preco;
	public String modelo;
	public boolean acao = false;
	
	public Carro() {
		
	}
	
	public Carro(String cor) {
		this.cor = cor;
	}
	
	public Carro(String cor, double preco ) {
		this.cor = cor;
		this.preco = preco;
	}
	
	public Carro(String cor, double preco, String modelo ) {
		this.cor = cor;
		this.preco = preco;
		this.modelo = modelo;
	}

	public void ligar() {
		if(acao == false) {
			acao = true;
			System.out.println("Carro está ligado");
		}
		else if(acao = true) {
			System.out.println("Carro já está ligado");
		}
	}
	
	public void desligar() {
		if(acao == true) {
			acao = false;
			System.out.println("Carro desligou");
		}
		else if(acao == false) {
			System.out.println("Carro já está desligado");
		}
	}
	
	public void status() {
		if(acao == false) {
			System.out.println("Carro está desligado");
		}
		else if(acao == true) {
			System.out.println("Carro está ligado");
		}
	}
}
