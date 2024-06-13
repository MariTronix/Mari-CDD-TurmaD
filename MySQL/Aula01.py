"""mysql> show databases;

mysql> show databases;

mysql> use turma_d;

mysql> create table alunos(
    ->     codigo int not null auto_increment,
    ->     nome varchar(20) not null,
    ->     telefone char(8) not null,
    ->     primary key(codigo)
    ->     );

mysql> show tables
mysql> desc alunos;

mysql> select * from alunos;

mysql> insert into alunos(nome,telefone)
    -> values ('Izair Junior','12345678');

mysql> insert into alunos(nome,telefone)
    ->     value ('Mariana','24242424'),
    ->     ('Ludmila','81818181'),
    ->     ('Vitoria','10101010'),
    ->     ('João Pedro','66666666'),
    -> ('Kananda','78945612'),
    -> ('Felipe','45678912'),
    -> ('Esmeralda','45696325');

mysql> select * from alunos;


mysql>  create table funcionarios(
    ->     id_funcionarios int not null auto_increment,
    ->     nome varchar(20) not null,
    ->     cpf char(11) not null,
    ->     departamento int not null,
    ->     cpf_supervisor char(11) not null,
    ->     salario float not null,
    ->     primary key(id_funcionarios)
    ->     );

mysql> insert into funcionarios(nome,cpf,departamento,cpf_supervisor,salario)
    ->     value ('Mario jose','12345678941','3','98765432198','3500'),
    ->     ('Maria Clara','32169854741','2','87654321908','3423'),
    ->     ('João Pedro','36985214725','3','76543210987','7004'),
    ->     ('Vinicius Morais','47856985471','5','45678902134','34234'),
    ->     ('Wellington Oliveira','32145698741','1','21345365476','16045'),
    ->     ('Clarisse Santos','11111111111','5','12345434567','7856'),
    ->     ('Vilma Malria','22222222222','4','87656787654','4354'),
    ->     ('José Pereira','66666666666','3','23454321234','76545'),
    ->     ('Claudemir Silva','99999999999','2','32432543678','9876');


mysql> select * from funcionarios;

mysql> select nome,salario from funcionarios;

mysql> select nome,salario from funcionarios where id_funcionarios = 3;

mysql> select nome, salario from funcionarios where salario<4000;

mysql> select nome,salario from funcionarios where salario>6000;

mysql> select nome,salario from funcionarios where departamento=5;

mysql> update funcionarios set nome = 'Jose mario' where id_funcionarios = 1;

mysql> select * from funcionarios;

mysql> update funcionarios set salario = 3423 where id_funcionarios = 4;

mysql> select * from funcionarios;"""