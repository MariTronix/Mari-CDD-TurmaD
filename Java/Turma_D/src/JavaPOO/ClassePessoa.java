package JavaPOO;

public class ClassePessoa {
	String nome, acao = "";
	
	public void comer(){
		if(acao.isEmpty()) {
			System.out.printf("%s está comendo", nome);
			acao = "comendo";
		}
		else {
			if(acao.equals("dormindo")) {
				System.out.printf("%s está dormindo, não pode comer", nome);
			}
			else if(acao.equals("andando")) {
				System.out.printf("%s está andando, não pode comer", nome);
			}
		}
	}
	
	public void pararcomer(){
		if(acao.equals("comendo")) {
			System.out.printf("%s parou de comer", nome);
			acao = "";
		}
		else {
			if(acao.isEmpty()) {
				System.out.printf("%s não está comendo, não pode parar de comer", nome);
			}
			else if(acao.equals("dormindo")) {
				System.out.printf("%s está dormindo, não pode parar de comer", nome);
			}
			else if(acao.equals("andando")) {
				System.out.printf("%s está andando, não pode parar de comer", nome);
			}
		}
	}
	
	
	public void dormir() {
		if(acao.isEmpty()) {
			System.out.printf("%s está dormindo", nome);
			acao = "dormindo";
		}
		else {
			if(acao.equals("comendo")) {
				System.out.printf("%s está comendo, não pode dormir", nome);
			}
			else if(acao.equals("andando")) {
				System.out.printf("%s está andando, não pode dormir", nome);
			}
		}
		
	}
	
	public void parardormir(){
		if(acao.equals("dormindo")) {
			System.out.printf("%s parou de dormir", nome);
			acao = "";
		}
		else {
			if(acao.isEmpty()) {
				System.out.printf("%s não está dormindo, não pode parar de dormir", nome);
			}
			else if(acao.equals("dormindo")) {
				System.out.printf("%s está dormindo, não pode parar de dormir", nome);
			}
			else if(acao.equals("andando")) {
				System.out.printf("%s está andando, não pode parar de dormir", nome);
			}
		}
	}
	
	
	public void andar() {
		if(acao.isEmpty()) {
			System.out.printf("%s está andando", nome);
			acao = "andando";
		}
		else {
			if(acao.equals("dormindo")) {
				System.out.printf("%s está dormindo, não pode andar", nome);
			}
			else if(acao.equals("comendo")) {
				System.out.printf("%s está comendo, não pode andar", nome);
			}
		}
	}
	
	public void pararandar(){
		if(acao.equals("andando")) {
			System.out.printf("%s parou de andar", nome);
			acao = "";
		}
		else {
			if(acao.isEmpty()) {
				System.out.printf("%s não está andando, não pode parar de andar", nome);
			}
			else if(acao.equals("dormindo")) {
				System.out.printf("%s está dormindo, não pode parar de andar", nome);
			}
			else if(acao.equals("comendo")) {
				System.out.printf("%s está comendo, não pode parar de andar", nome);
			}
		}
	}
}