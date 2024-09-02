package Acabou;

public class TriAtleta implements Corredor, Nadador, Ciclista {
	private boolean descansa = true;
	private boolean pedalando = false;
	private boolean nadando= false;
	private boolean correndo = false;
	
	
	public void Descansar(boolean descansa) {
		this.descansa = descansa;
	}

	public void Pedalando() {
		if(descansa == true && pedalando == false && nadando == false && correndo == false) {
			descansa = false;
			pedalando = true;
			System.out.println("Pedalando");
		}
		else if(pedalando == true ) {
			System.out.println("Atleta já está pedalando");
		}
		else if(nadando == true || correndo == true) {
			System.out.println("Atleta está em exercicio no momento, não pode pedalar");
		}
		else {
			System.out.println("O atleta não está descansado");
		}
		
	}
	
	public void pararPedalando() {
		if(pedalando == true) {
			descansa = true;
			pedalando = false;
			System.out.println("Parou de pedalando");
		}
		else if(pedalando == false ) {
			System.out.println("Atleta não está pedalando");
		}
		else if(nadando == true || correndo == true) {
			System.out.println("Atleta está em exercicio no momento, não pode pedalar");
		}
		else {
			System.out.println("O atleta não está descansado");
		}
		
	}

	public void Nadar() {
		if(descansa == true && pedalando == false && nadando == false && correndo == false) {
			descansa = false;
			nadando = true;
			System.out.println("Nadando");
		}
		else if(nadando == true ) {
			System.out.println("Atleta já está nadando");
		}
		else if(pedalando == true || correndo == true) {
			System.out.println("Atleta está em exercicio no momento");
		}
		else {
			System.out.println("O atleta não está descansado");
		}
		
	}
	
	public void pararNadar() {
		if(nadando == true) {
			descansa = true;
			nadando = false;
			System.out.println("Parou de pedalando");
		}
		else if(pedalando == false ) {
			System.out.println("Atleta não está nadando");
		}
		else if(pedalando == true || correndo == true) {
			System.out.println("Atleta está em exercicio no momento");
		}
		else {
			System.out.println("O atleta não está descansado");
		}
		
	}

	public void Correr() {
		if(descansa == true && pedalando == false && nadando == false && correndo == false) {
			descansa = false;
			correndo = true;
			System.out.println("Correndo");
		}
		else if(correndo == true ) {
			System.out.println("Atleta já está correndo");
		}
		else if(pedalando == true || nadando == true) {
			System.out.println("Atleta está em exercicio no momento, não pode correr");
		}
		else {
			System.out.println("O atleta não está descansado");
		}
	}
	
	public void pararCorrer() {
		if(correndo == true) {
			descansa = true;
			correndo = false;
			System.out.println("Parou de pedalando");
		}
		else if(correndo == false ) {
			System.out.println("Atleta não está correndo");
		}
		else if(pedalando == true || correndo == true) {
			System.out.println("Atleta está em exercicio no momento");
		}
		else {
			System.out.println("O atleta não está descansado");
		}
		
	}
}
