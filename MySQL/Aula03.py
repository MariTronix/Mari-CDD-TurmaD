Enter password: ******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 108
Server version: 8.0.37 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+---------------------+
| Database            |
+---------------------+
| curso               |
| desafio             |
| desafio_c           |
| desafiofinal_turmaa |
| information_schema  |
| mysql               |
| performance_schema  |
| sys                 |
| turma_a             |
| turma_b             |
| turma_c             |
| turma_d             |
+---------------------+
12 rows in set (0.05 sec)

mysql> create database desafio_turma_d;
Query OK, 1 row affected (0.05 sec)

mysql> use desafio_turma_d;
Database changed
mysql> mysql> create table alunos(
    ->     ->     matricula int not null auto_increment primary key,
    ->     ->     nome varchar(20) not null,
    ->     ->     telefone char(8) not null
    ->     ->     );^Z^C
mysql> mysql> create table alunos(
    ->          matricula int not null auto_increment primary key,
    ->          nome varchar(20) not null,
    ->          telefone char(8) not null
    ->          );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'mysql> create table alunos(
         matricula int not null auto_increment prima' at line 1
mysql> mysql> create table alunos(
    ->          matricula int not null auto_increment,
    ->          nome varchar(20) not null,
    ->          telefone char(8) not null,
    ->          primary key(matricula)
    ->          );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'mysql> create table alunos(
         matricula int not null auto_increment,
    ' at line 1
mysql> create table alunos(
    ->          matricula int not null auto_increment,
    ->          nome varchar(20) not null,
    ->          telefone char(8) not null,
    ->          primary key(matricula)
    ->          );
Query OK, 0 rows affected (0.13 sec)

mysql> altrer table alunos modify nome varchar(200) not null;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'altrer table alunos modify nome varchar(200) not null' at line 1
mysql> create table disciplinas (
    -> id_disc int not null auto_increment primary key,
    -> nome varchar(100) not null
    -> );
Query OK, 0 rows affected (0.08 sec)

mysql> create table matriculados (
    -> id_mat int not null auto_increment primary key,
    -> matricula int not null,
    -> id_disc int not null,
    -> foreign key(matricula) references alunos(matricula),
    -> foreign key(id_disc) references disciplinas(matricula)
    -> );
ERROR 3734 (HY000): Failed to add the foreign key constraint. Missing column 'matricula' for constraint 'matriculados_ibfk_2' in the referenced table 'disciplinas'
mysql> create table matriculados (
    -> id_mat int not null auto_increment primary key,
    -> matricula int not null,
    -> id_disc int not null,
    -> foreign key(matricula) references alunos(matricula),
    -> foreign key(id_disc) references disciplinas(id_disc)
    -> );
Query OK, 0 rows affected (0.08 sec)

mysql> alter table alunos modify nome varchar(200) not null;
Query OK, 0 rows affected (0.12 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> insert into alunos(nome,telefone)
    -> value ('Mariana','12324242424'),
    -> ('Ludmila','12381818181'),
    -> ('Vitoria','12310101010'),
    -> ('João Pedro','12366666666'),
    -> ('Kananda','12378945612'),
    -> ('Felipe','11145678912'),
    -> ('Esmeralda','11145696325')
    -> ('Izair', '12345678901);
    '> ('Taisa', '12345678912')
    '> ('Aylanna', '12345678909')^Z^C
mysql> insert into alunos(nome,telefone)
    -> value ('Mariana','12324242424'),
    -> ('Ludmila','12381818181'),
    -> ('Vitoria','12310101010'),
    -> ('João Pedro','12366666666'),
    -> ('Kananda','12378945612'),
    -> ('Felipe','11145678912'),
    -> ('Esmeralda','11145696325')
    -> ('Izair', '12345678901);
    '> ('Taisa', '12345678912')
    '> ('Aylanna', '12345678909')
    '> ;
    '> ;
    '> ^C
mysql> insert into alunos(nome,telefone)
    -> values ('Mariana','12324242424'),
    -> ('Ludmila','12381818181'),
    -> ('Vitoria','12310101010'),
    -> ('João Pedro','12366666666'),
    -> ('Kananda','12378945612'),
    -> ('Felipe','11145678912'),
    -> ('Esmeralda','11145696325')
    -> ('Izair', '12345678901);
    '> ('Taisa', '12345678912')
    '> ('Aylanna', '12345678909');
    '> ^C
mysql> ^C
mysql> insert into alunos(nome,telefone)
    -> values ('Mariana','12324242424'),
    -> ('Ludmila','12381818181'),
    -> ('Vitoria','12310101010'),
    -> ('João Pedro','12366666666'),
    -> ('Kananda','12378945612'),
    -> ('Felipe','11145678912'),
    -> ('Esmeralda','11145696325'),
    -> ('Izair', '12345678901),
    '> ('Taisa', '12345678912'),
    '> ('Aylanna', '12345678909');
    '> ^C
mysql> insert into alunos(nome,telefone)
    -> values ('Mariana','12324242424'),
    -> ('Ludmila','12381818181'),
    -> ('Vitoria','12310101010'),
    -> ('João Pedro','12366666666'),
    -> ('Kananda','12378945612'),
    -> ('Felipe','11145678912'),
    -> ('Esmeralda','11145696325'),
    -> ('Izair', '12345678901'),
    -> ('Taisa', '12345678912'),
    -> ('Aylanna', '12345678909');
ERROR 1406 (22001): Data too long for column 'telefone' at row 1
mysql>  altrer table alunos modify telefone char(11) not null;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'altrer table alunos modify telefone char(11) not null' at line 1
mysql>  alter table alunos modify telefone char(11) not null;
Query OK, 0 rows affected (0.06 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> insert into alunos(nome,telefone)
    -> values ('Mariana','12324242424'),
    -> ('Ludmila','12381818181'),
    -> ('Vitoria','12310101010'),
    -> ('João Pedro','12366666666'),
    -> ('Kananda','12378945612'),
    -> ('Felipe','11145678912'),
    -> ('Esmeralda','11145696325'),
    -> ('Izair', '12345678901'),
    -> ('Taisa', '12345678912'),
    -> ('Aylanna', '12345678909');
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> insert into disciplinas(nome)
    -> values ('Portugues'),
    -> ('Matematica'),
    -> ('Historia'),
    -> ('Geografia'),
    -> ('Ingles');
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> insert into matriculados(matricula, id_disc)
    -> values (1, 1),
    -> (1,2),
    -> (2,1),
    -> (3,2),
    -> (4,3),
    -> (5,4),
    -> (6,5),
    -> (7,1)
    -> (8,2)
    -> (9,3)
    -> (10,4)
    -> (2,5);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(8,2)
(9,3)
(10,4)
(2,5)' at line 10
mysql> insert into matriculados(matricula, id_disc)
    -> values (1,1);
Query OK, 1 row affected (0.03 sec)

mysql> show table alunos;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'alunos' at line 1
mysql> show table alunos;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'alunos' at line 1
mysql> insert into matriculados(matricula, id_disc)
    -> values (1,2),
    -> (2,1),
    -> (3,2),
    -> (4,3),
    -> (5,4),
    -> (6,5),
    -> (7,1),
    -> (8,2),
    -> (9,3),
    -> (10,4),
    -> (2,3);
Query OK, 11 rows affected (0.02 sec)
Records: 11  Duplicates: 0  Warnings: 0

mysql> select id_mat, nome from aluno, disciplina, matriculados;
ERROR 1146 (42S02): Table 'desafio_turma_d.aluno' doesn't exist
mysql> select id_mat, nome from alunos, disciplinas, matriculados;
ERROR 1052 (23000): Column 'nome' in field list is ambiguous
mysql> select nome, id_mat from alunos, disciplinas, matriculados;
ERROR 1052 (23000): Column 'nome' in field list is ambiguous
mysql> alter table alunos drop telefone;
Query OK, 0 rows affected (0.12 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> create table telefones (
    -> id_tel int not null auto_increment primary key,
    -> telefone char(11) not null,
    -> matricula int not null,
    -> foreing key(matricula) references alunos(matricula)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'key(matricula) references alunos(matricula)
)' at line 5
mysql> create table telefones (
    -> id_tel int not null auto_increment primary key,
    -> telefone char(11) not null,
    -> matricula int not null,
    -> foreign key(matricula) references alunos(matricula)
    -> );
Query OK, 0 rows affected (0.10 sec)

mysql> create table endereco (
    -> id_end int not null auto_increment primary key,
    -> logradouro varchar(250) not null,
    -> cep char(8)  not null,
    -> bairro varchar(250) not null,
    -> matricula int not null,
    -> foreign key(matricula) references alunos(matricula)
    -> );
Query OK, 0 rows affected (0.18 sec)

mysql> alter table endereco add (
    ->     complemento varchar(100) not null after logradouro);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'after logradouro)' at line 2
mysql> alter table endereco add (
    -> complemento varchar(100) not null after logradouro
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'after logradouro
)' at line 2
mysql> alter table endereco add (
    -> complemento varchar(100) not null after logradouro
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'after logradouro
)' at line 2
mysql> alter table endereco add column(
    -> complemento varchar(100) not null after logradouro
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'after logradouro
)' at line 2
mysql> alter table endereco add column
    -> complemento varchar(100) not null after logradouro;
Query OK, 0 rows affected (0.07 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from endereco;
Empty set (0.02 sec)

mysql> desc endereco;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| id_end      | int          | NO   | PRI | NULL    | auto_increment |
| logradouro  | varchar(250) | NO   |     | NULL    |                |
| complemento | varchar(100) | NO   |     | NULL    |                |
| cep         | char(8)      | NO   |     | NULL    |                |
| bairro      | varchar(250) | NO   |     | NULL    |                |
| matricula   | int          | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
6 rows in set (0.06 sec)

mysql> insert into telefone(telefone, matricula)
    -> values ('81983306681', 1),
    -> ('81983306682', 2),
    -> ('81983306683', 3),
    -> ('81983306684', 4),
    -> ('81983306685', 5),
    -> ('81983306686', 6),
    -> ('81983306687', 7),
    -> ('81983306688', 8),
    -> ('81983306689', 9),
    -> ('81983306690', 10);
ERROR 1146 (42S02): Table 'desafio_turma_d.telefone' doesn't exist
mysql> insert into telefones(telefone, matricula)
    -> values ('81983306681', 1),
    -> ('81983306682', 2),
    -> ('81983306683', 3),
    -> ('81983306684', 4),
    -> ('81983306685', 5),
    -> ('81983306686', 6),
    -> ('81983306687', 7),
    -> ('81983306688', 8),
    -> ('81983306689', 9),
    -> ('81983306690', 10);
Query OK, 10 rows affected (0.06 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> insert into endereco(logradouro, complemento, cep, bairro, matricula)
    -> values ('Rua Jornalista Nelson Rodrigues', 'N15, Lagoa Encantada','51300140', 'Ibura', 1),
    -> ('Rua Jornalista Nelson Rodrigues', 'N16, Lagoa Encantada','51300140', 'Ibura', 2),
    -> ('Rua Jornalista Nelson Rodrigues', 'N17, Lagoa Encantada','51300140', 'Ibura', 3),
    -> ('Rua Jornalista Nelson Rodrigues', 'N18, Lagoa Encantada','51300140', 'Ibura', 4),
    -> ('Rua Jornalista Nelson Rodrigues', 'N19, Lagoa Encantada','51300140', 'Ibura', 5),
    -> ('Rua Jornalista Nelson Rodrigues', 'N20, Lagoa Encantada','51300140', 'Ibura', 6),
    -> ('Rua Jornalista Nelson Rodrigues', 'N21, Lagoa Encantada','51300140', 'Ibura', 7),
    -> ('Rua Jornalista Nelson Rodrigues', 'N22, Lagoa Encantada','51300140', 'Ibura' 8),
    -> ('Rua Jornalista Nelson Rodrigues', 'N23, Lagoa Encantada','51300140', 'Ibura' 9),
    -> ('Rua Jornalista Nelson Rodrigues', 'N24, Lagoa Encantada','51300140', 'Ibura' 10);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '8),
('Rua Jornalista Nelson Rodrigues', 'N23, Lagoa Encantada','51300140', 'Ibur' at line 9
mysql> insert into endereco(logradouro, complemento, cep, bairro, matricula)
    -> values ('Rua Jornalista Nelson Rodrigues', 'N15, Lagoa Encantada','51300140', 'Ibura', 1),
    -> ('Rua Jornalista Nelson Rodrigues', 'N16, Lagoa Encantada','51300140', 'Ibura', 2),
    -> ('Rua Jornalista Nelson Rodrigues', 'N17, Lagoa Encantada','51300140', 'Ibura', 3),
    -> ('Rua Jornalista Nelson Rodrigues', 'N18, Lagoa Encantada','51300140', 'Ibura', 4),
    -> ('Rua Jornalista Nelson Rodrigues', 'N19, Lagoa Encantada','51300140', 'Ibura', 5),
    -> ('Rua Jornalista Nelson Rodrigues', 'N20, Lagoa Encantada','51300140', 'Ibura', 6),
    -> ('Rua Jornalista Nelson Rodrigues', 'N21, Lagoa Encantada','51300140', 'Ibura', 7),
    -> ('Rua Jornalista Nelson Rodrigues', 'N22, Lagoa Encantada','51300140', 'Ibura', 8),
    -> ('Rua Jornalista Nelson Rodrigues', 'N23, Lagoa Encantada','51300140', 'Ibura', 9),
    -> ('Rua Jornalista Nelson Rodrigues', 'N24, Lagoa Encantada','51300140', 'Ibura', 10);
Query OK, 10 rows affected (0.02 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> select alunos.matricula,alunos.nome telefones.telefone from alunos inner join telefones on alunos.matricula = telefone.matricu
la;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '.telefone from alunos inner join telefones on alunos.matricula = telefone.matric' at line 1
mysql> select alunos.matricula,alunos.nome,telefones.telefone from alunos inner join telefones on alunos.matricula = telefone.matricula;
ERROR 1054 (42S22): Unknown column 'telefone.matricula' in 'on clause'
mysql> select alunos.matricula,alunos.nome,telefones.telefone from alunos inner join telefones on alunos.matricula = telefone.matricu
la;
ERROR 1054 (42S22): Unknown column 'telefone.matricula' in 'on clause'
mysql> select alunos.matricula,alunos.nome,telefones.telefone from alunos inner join telefones on alunos.matricula = telefones.matric
ula;
+-----------+------------+-------------+
| matricula | nome       | telefone    |
+-----------+------------+-------------+
|         1 | Mariana    | 81983306681 |
|         2 | Ludmila    | 81983306682 |
|         3 | Vitoria    | 81983306683 |
|         4 | João Pedro | 81983306684 |
|         5 | Kananda    | 81983306685 |
|         6 | Felipe     | 81983306686 |
|         7 | Esmeralda  | 81983306687 |
|         8 | Izair      | 81983306688 |
|         9 | Taisa      | 81983306689 |
|        10 | Aylanna    | 81983306690 |
+-----------+------------+-------------+
10 rows in set (0.02 sec)

mysql> select alunos.matricula,alunos.nome,endereco.logradouro,endereco.cep from alunos inner join endereco on alunos.matricula = endereco.matricula;
+-----------+------------+---------------------------------+----------+
| matricula | nome       | logradouro                      | cep      |
+-----------+------------+---------------------------------+----------+
|         1 | Mariana    | Rua Jornalista Nelson Rodrigues | 51300140 |
|         2 | Ludmila    | Rua Jornalista Nelson Rodrigues | 51300140 |
|         3 | Vitoria    | Rua Jornalista Nelson Rodrigues | 51300140 |
|         4 | João Pedro | Rua Jornalista Nelson Rodrigues | 51300140 |
|         5 | Kananda    | Rua Jornalista Nelson Rodrigues | 51300140 |
|         6 | Felipe     | Rua Jornalista Nelson Rodrigues | 51300140 |
|         7 | Esmeralda  | Rua Jornalista Nelson Rodrigues | 51300140 |
|         8 | Izair      | Rua Jornalista Nelson Rodrigues | 51300140 |
|         9 | Taisa      | Rua Jornalista Nelson Rodrigues | 51300140 |
|        10 | Aylanna    | Rua Jornalista Nelson Rodrigues | 51300140 |
+-----------+------------+---------------------------------+----------+
10 rows in set (0.00 sec)

mysql> select alunos.matricula, alunos.nome, diciplinas.id_disc, diciplinas.nome
    -> from matriculados
    -> inner join alunos on matriculados.matricula = alunos.matricula;
ERROR 1054 (42S22): Unknown column 'diciplinas.id_disc' in 'field list'
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql>
mysql> inner join alunos on matriculados.matricula = alunos.matricula;^C
mysql> select alunos.matricula, alunos.nome,
    -> disciplinas.id_disc, disciplinas.nome
    -> from matriculados
    -> inner join alunos on matriculados.matricula = alunos.matricula
    -> inner join disciplinas on matriculados.id_disc = disciplinas.id_disc;
+-----------+------------+---------+------------+
| matricula | nome       | id_disc | nome       |
+-----------+------------+---------+------------+
|         1 | Mariana    |       1 | Portugues  |
|         2 | Ludmila    |       1 | Portugues  |
|         7 | Esmeralda  |       1 | Portugues  |
|         1 | Mariana    |       2 | Matematica |
|         3 | Vitoria    |       2 | Matematica |
|         8 | Izair      |       2 | Matematica |
|         4 | João Pedro |       3 | Historia   |
|         9 | Taisa      |       3 | Historia   |
|         2 | Ludmila    |       3 | Historia   |
|         5 | Kananda    |       4 | Geografia  |
|        10 | Aylanna    |       4 | Geografia  |
|         6 | Felipe     |       5 | Ingles     |
+-----------+------------+---------+------------+
12 rows in set (0.02 sec)

mysql>