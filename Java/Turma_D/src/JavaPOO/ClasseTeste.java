package JavaPOO;

public class ClasseTeste {

	public static void main(String[] args) {
		ClassePessoa aluno01 = new ClassePessoa();
		aluno01.nome = "Wellington";
		aluno01.comer();
		System.out.println();
		aluno01.pararcomer();
		System.out.println();
		aluno01.andar();
		System.out.println();
		aluno01.pararandar();
		System.out.println();
		aluno01.dormir();
	}
}