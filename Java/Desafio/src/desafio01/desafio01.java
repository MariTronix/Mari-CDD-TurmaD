package desafio01;

import java.util.Scanner;

public class desafio01 {

	public static void main(String[] args) {
		 System.out.println("Responda com 1-Sim 2-Não");
		 Scanner input = new Scanner(System.in);
		 System.out.println("Telefonou para a vítima? ");
		 int resp = input.nextInt();
		 System.out.println("Esteve no local do crime? ");
		 int resp2 = input.nextInt();
		 System.out.println("Mora perto da vítima? ");
		 int resp3 = input.nextInt();
		 System.out.println("Devia para a vítima? ");
		 int resp4 = input.nextInt();
		 System.out.println("Já trabalhou com a vítima?");
		 int resp5 = input.nextInt();
		 
		 int contagem = 0;
		 
		 /* Saber se a resposta é "sim" e adicionar na contagem*/
		 if(resp == 1) {
			 contagem++;
			 System.out.println(contagem);
		 }
		 if(resp2 == 1) {
			 contagem++;
		 }
		 if(resp3 == 1) {
			 contagem++;
		 }
		 if(resp4 == 1) {
			 contagem++;
		 }
		 if(resp5 == 1) {
			 contagem++;
		 }
		 
		 /*Fazer a classificação do suspeito*/
		 if (contagem == 5) {
			 System.out.println("Assassino");
		 }
		 else if (contagem == 2) {
			 System.out.println("Suspeita");
		 }
		 else if (contagem == 3 || contagem == 4) {
			 System.out.println("Cúmplice");
		 }
		 else{
			 System.out.println("Inocente");
		 }
	}

}
