package Heranca;

public class Faculdade {
	public static void main(String[] args) {
		aluno a1 = new aluno("Mariana", 27);
		a1.matricula = "123456789";
		professor p1 = new professor("Wellington", 50);
		p1.disciplina = "Matematica";
		p1.salario = 20000;
		funcionario f1 = new funcionario("Daniel", 25);
		f1.cargo = "Assistente";
		f1.salario = 2000;
	}
}
