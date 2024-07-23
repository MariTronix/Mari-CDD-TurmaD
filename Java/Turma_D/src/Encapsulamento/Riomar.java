package Encapsulamento;

public class Riomar extends Pet {

	public static void main(String[] args) {
		Pet p1 = new Pet();
		p1.setNome("Pipoca");
		p1.setSigno("Peixe");
		p1.setRaca("Branca");
		p1.setNomeDoDono("Mariana");
		p1.setPadrinho("Daniel");
		p1.setVacinado(true);
		
		String nome = p1.getNome();
		String signo = p1.getSigno();
		String raca = p1.getRaca();
		String nomeDoDono = p1.getNomeDoDono();
		String padrinho = p1.getPadrinho();
		boolean vacinado = p1.isVacinado();
		
		
		System.out.println(nome);
		System.out.println(signo);
		System.out.println(raca); 
		System.out.println(nomeDoDono); 
		System.out.println(padrinho); 
		System.out.println(vacinado); 
	}
}