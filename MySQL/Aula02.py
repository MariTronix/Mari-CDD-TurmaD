'''mysql> use turma_d
Database changed

mysql> show table;

mysql> show tables;

mysql> select * from alunos;

mysql> select * from funcionario;

mysql> alter table funcionario add (
telefone char(11)
    -> );

mysql> select * from funcionario;

mysql> update funcionario set telefone = '12345678901' where id_funcionario = 1;

mysql> select * from funcionario;

mysql> update funcionario set telefone = '12345678902' where id_funcionario = 2;

mysql> update funcionario set telefone = '12345678903' where id_funcionario = 3;

mysql> update funcionario set telefone = '12345678904' where id_funcionario = 4;

mysql> update funcionario set telefone = '12345678905' where id_funcionario = 5;

mysql> update funcionario set telefone = '12345678906' where id_funcionario = 6;

mysql> update funcionario set telefone = '12345678907' where id_funcionario = 7;

mysql> update funcionario set telefone = '12345678908' where id_funcionario = 8;
Query OK, 1 row affected (0.01 sec)

mysql> update funcionario set telefone = '12345678909' where id_funcionario = 9;

mysql> select * from funcionario;

mysql> alter table funcionario add (
    -> logradouro varchar(50)
    -> );

mysql> alter table funcionario add (
    -> complemento varchar(50) not null,
    -> cep char(11) not null,
    -> bairro varchar(50) not null,
    -> cidade varchar(50) not null);

mysql> select * from funcionario;


mysql> update funcionario set logradouro = 'rua jornalista nelson rodrigues', complemento = '15', cep = '51300140', bairro = 'Ibura', cidade = 'recife' wher
e id_funcionario = 1;

mysql> pdate funcionario set logradouro = 'rua jornalista nelson rodrigues',
    -> complemento = '15',
    -> cep = '51300140',
    -> bairro = 'Ibura',
    -> cidade = 'recife'
    -> cidade = 'recife'^Z^C
mysql> pdate funcionario set logradouro = 'rua jornalista nelson rodrigues',
    -> complemento = '15',
    -> cep = '51300140',
    -> bairro = 'Ibura',
    -> cidade = 'recife'
    -> where id_funcionario = 1;^C
mysql> update funcionario set logradouro = 'travessa jornalista nelson rodrigues',
    -> complemento = '15',
    -> cep = '51300140',
    -> bairro = 'Ibura',
    -> cidade = 'recife'
    -> where id_funcionario = 2;
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update funcionario set logradouro = 'avenida jornalista nelson rodrigues',
    -> complemento = '15',
    -> cep = '51300140',
    -> bairro = 'Ibura',
    -> cidade = 'recife'
    -> where id_funcionario = 3;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from funcionario;
+----------------+-------------+-------------+--------------+----------------+---------+-------------+--------------------------------------+-------------+----------+--------+--------+
| id_funcionario | nome        | cpf         | departamento | cpf_supervisor | salario | telefone    | logradouro                           | complemento | cep      | bairro | cidade |
+----------------+-------------+-------------+--------------+----------------+---------+-------------+--------------------------------------+-------------+----------+--------+--------+
|              1 | jose mario  | 10203040231 |            3 | 98765432198    |    3500 | 12345678901 | rua jornalista nelson rodrigues      | 15          | 51300140 | Ibura  | recife |
|              2 | Maria clara | 32123123424 |            2 | 87654321908    |    3423 | 12345678902 | travessa jornalista nelson rodrigues | 15          | 51300140 | Ibura  | recife |
|              3 | João        | 23124532345 |            3 | 76543210987    |    7004 | 12345678903 | avenida jornalista nelson rodrigues  | 15          | 51300140 | Ibura  | recife |
|              4 | Vinicius    | 23124512347 |            5 | 76543212345    |    3423 | 12345678904 | NULL                                 |             |          |        |        |
|              5 | Wellington  | 12344512345 |            1 | 12543212345    |   16045 | 12345678905 | NULL                                 |             |          |        |        |
|              6 | Clarisse    | 12344654321 |            5 | 31254365432    |    7856 | 12345678906 | NULL                                 |             |          |        |        |
|              7 | Vilma       | 51234460987 |            4 | 31254365567    |    4354 | 12345678907 | NULL                                 |             |          |        |        |
|              8 | José        | 37034460987 |            3 | 31251235567    |   76545 | 12345678908 | NULL                                 |             |          |        |        |
|              9 | Claudemir   | 51075360987 |            2 | 31254365567    |    9876 | 12345678909 | NULL                                 |             |          |        |        |
+----------------+-------------+-------------+--------------+----------------+---------+-------------+--------------------------------------+-------------+----------+--------+--------+
9 rows in set (0.02 sec)

mysql> alter table funcionario drop telefone;
Query OK, 0 rows affected (0.21 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> select * from funcionario;
+----------------+-------------+-------------+--------------+----------------+---------+--------------------------------------+-------------+----------+--------+--------+
| id_funcionario | nome        | cpf         | departamento | cpf_supervisor | salario | logradouro                           | complemento | cep      | bairro | cidade |
+----------------+-------------+-------------+--------------+----------------+---------+--------------------------------------+-------------+----------+--------+--------+
|              1 | jose mario  | 10203040231 |            3 | 98765432198    |    3500 | rua jornalista nelson rodrigues      | 15          | 51300140 | Ibura  | recife |
|              2 | Maria clara | 32123123424 |            2 | 87654321908    |    3423 | travessa jornalista nelson rodrigues | 15          | 51300140 | Ibura  | recife |
|              3 | João        | 23124532345 |            3 | 76543210987    |    7004 | avenida jornalista nelson rodrigues  | 15          | 51300140 | Ibura  | recife |
|              4 | Vinicius    | 23124512347 |            5 | 76543212345    |    3423 | NULL                                 |             |          |        |        |
|              5 | Wellington  | 12344512345 |            1 | 12543212345    |   16045 | NULL                                 |             |          |        |        |
|              6 | Clarisse    | 12344654321 |            5 | 31254365432    |    7856 | NULL                                 |             |          |        |        |
|              7 | Vilma       | 51234460987 |            4 | 31254365567    |    4354 | NULL                                 |             |          |        |        |
|              8 | José        | 37034460987 |            3 | 31251235567    |   76545 | NULL                                 |             |          |        |        |
|              9 | Claudemir   | 51075360987 |            2 | 31254365567    |    9876 | NULL                                 |             |          |        |        |
+----------------+-------------+-------------+--------------+----------------+---------+--------------------------------------+-------------+----------+--------+--------+
9 rows in set (0.01 sec)

mysql> create table telefones (
    ->     id_tel int not null auto_increment primary key,
    ->     telefone char(11) not null,
    ->     id_funcionarios int not null,
    ->     foreing key(id_funcionario) references funcionario(id_funcionario)
    ->     );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'key(id_funcionario) references funcionario(id_funcionario)
    )' at line 5
mysql> create table telefones (
    ->     id_tel int not null auto_increment primary key,
    ->     telefone char(11) not null,
    ->     id_funcionario int not null,
    ->     foreing key(id_funcionario) references funcionario(id_funcionario)
    ->     );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'key(id_funcionario) references funcionario(id_funcionario)
    )' at line 5
mysql> create table telefones (
    ->     id_tel int not null auto_increment primary key,
    ->     telefone char(11) not null,
    ->     id_funcionario int not null,
    ->     foreing key(id_funcionario) references funcionario(id_funcionario)
    ->     );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'key(id_funcionario) references funcionario(id_funcionario)
    )' at line 5
mysql> create table telefones (
    ->     id_tel int not null auto_increment primary key,
    ->     telefone char(11) not null,
    ->     id_funcionario int not null,
    ->     foreign key(id_funcionario) references funcionario(id_funcionario)
    ->     );
Query OK, 0 rows affected (0.15 sec)

mysql> show tables;
+-------------------+
| Tables_in_turma_d |
+-------------------+
| alunos            |
| funcionario       |
| telefones         |
+-------------------+
3 rows in set (0.04 sec)

mysql> insert into telefones(telefone,id_funcionario)
    -> value ('012345678901', 1);
ERROR 1406 (22001): Data too long for column 'telefone' at row 1
mysql> insert into telefones(telefone, id_funcionario)
    -> value ('012345678901', 1);
ERROR 1406 (22001): Data too long for column 'telefone' at row 1
mysql> desc funcionario;
+----------------+-------------+------+-----+---------+----------------+
| Field          | Type        | Null | Key | Default | Extra          |
+----------------+-------------+------+-----+---------+----------------+
| id_funcionario | int         | NO   | PRI | NULL    | auto_increment |
| nome           | varchar(20) | NO   |     | NULL    |                |
| cpf            | char(11)    | NO   |     | NULL    |                |
| departamento   | int         | NO   |     | NULL    |                |
| cpf_supervisor | char(11)    | NO   |     | NULL    |                |
| salario      | float       | NO   |     | NULL    |                |
| logradouro     | varchar(50) | YES  |     | NULL    |                |
| complemento    | varchar(50) | NO   |     | NULL    |                |
| cep            | char(11)    | NO   |     | NULL    |                |
| bairro         | varchar(50) | NO   |     | NULL    |                |
| cidade         | varchar(50) | NO   |     | NULL    |                |
+----------------+-------------+------+-----+---------+----------------+
11 rows in set (0.07 sec)

mysql> show tables;
+-------------------+
| Tables_in_turma_d |
+-------------------+
| alunos            |
| funcionario       |
| telefones         |
+-------------------+
3 rows in set (0.04 sec)

mysql> insert into telefones(telefone,id_funcionario)
    -> value ('012345678901', 1);
ERROR 1406 (22001): Data too long for column 'telefone' at row 1
mysql> select * from telefones;
Empty set (0.04 sec)

mysql> insert into telefones(telefone, id_funcionario)
    -> value ('81983306684', 1);
Query OK, 1 row affected (0.05 sec)

mysql> insert into telefones(telefone, id_funcionario)
    -> value ('81983306685', 2),
    -> ('8193306686', 2);
Query OK, 2 rows affected (0.05 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from telefones;
+--------+-------------+----------------+
| id_tel | telefone    | id_funcionario |
+--------+-------------+----------------+
|      1 | 81983306684 |              1 |
|      2 | 81983306685 |              2 |
|      3 | 8193306686  |              2 |
+--------+-------------+----------------+
3 rows in set (0.00 sec)

mysql> insert into telefones(telefone, id_funcionario)
    -> value ('81983306685', 2),
    -> ^C
mysql> insert into telefones(telefone, id_funcionario)
    -> value ('81983306686', 3),
    -> ('81983306687', 3),
    -> ('81983306688', 4);
Query OK, 3 rows affected (0.04 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> ('81983306689', 40);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''81983306689', 40)' at line 1
mysql> update telefone set telefone = '81933066869' where id_funcionarios = 3;
ERROR 1146 (42S02): Table 'turma_d.telefone' doesn't exist
mysql> update telefones set telefone = '81933066869' where id_funcionarios = 3;
ERROR 1054 (42S22): Unknown column 'id_funcionarios' in 'where clause'
mysql> update telefones set telefone = '81933066869' where id_funcionario = 3;
Query OK, 2 rows affected (0.02 sec)
Rows matched: 2  Changed: 2  Warnings: 0

mysql> select * from telefones;
+--------+-------------+----------------+
| id_tel | telefone    | id_funcionario |
+--------+-------------+----------------+
|      1 | 81983306684 |              1 |
|      2 | 81983306685 |              2 |
|      3 | 8193306686  |              2 |
|      4 | 81933066869 |              3 |
|      5 | 81933066869 |              3 |
|      6 | 81983306688 |              4 |
+--------+-------------+----------------+
6 rows in set (0.00 sec)

mysql> update telefone set telefone = '81933066869' where id_tel = 3;
ERROR 1146 (42S02): Table 'turma_d.telefone' doesn't exist
mysql> update telefones set telefone = '81933066869' where id_tel = 3;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from telefones;
+--------+-------------+----------------+
| id_tel | telefone    | id_funcionario |
+--------+-------------+----------------+
|      1 | 81983306684 |              1 |
|      2 | 81983306685 |              2 |
|      3 | 81933066869 |              2 |
|      4 | 81933066869 |              3 |
|      5 | 81933066869 |              3 |
|      6 | 81983306688 |              4 |
+--------+-------------+----------------+
6 rows in set (0.00 sec)

mysql> update telefones set telefone ='81983306686' where id_tel = 3),
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '),' at line 1
mysql> update telefones set telefone ='81983306686' where id_tel = 3;
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update telefones set telefone ='81983306687' where id_tel = 4;
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update telefones set telefone ='81983306688' where id_tel = 4;
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from telefones;
+--------+-------------+----------------+
| id_tel | telefone    | id_funcionario |
+--------+-------------+----------------+
|      1 | 81983306684 |              1 |
|      2 | 81983306685 |              2 |
|      3 | 81983306686 |              2 |
|      4 | 81983306688 |              3 |
|      5 | 81933066869 |              3 |
|      6 | 81983306688 |              4 |
+--------+-------------+----------------+
6 rows in set (0.00 sec)

mysql> update telefones set telefone = '81933066889' where id_tel = 5;
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from telefones;
+--------+-------------+----------------+
| id_tel | telefone    | id_funcionario |
+--------+-------------+----------------+
|      1 | 81983306684 |              1 |
|      2 | 81983306685 |              2 |
|      3 | 81983306686 |              2 |
|      4 | 81983306688 |              3 |
|      5 | 81933066889 |              3 |
|      6 | 81983306688 |              4 |
+--------+-------------+----------------+
6 rows in set (0.00 sec)

mysql> update telefones set telefone ='81983306690' where id_tel = 6;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from telefones;
+--------+-------------+----------------+
| id_tel | telefone    | id_funcionario |
+--------+-------------+----------------+
|      1 | 81983306684 |              1 |
|      2 | 81983306685 |              2 |
|      3 | 81983306686 |              2 |
|      4 | 81983306688 |              3 |
|      5 | 81933066889 |              3 |
|      6 | 81983306690 |              4 |
+--------+-------------+----------------+
6 rows in set (0.00 sec)

mysql> update telefones id_funcionario = 3 where id_tel = 6;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '= 3 where id_tel = 6' at line 1
mysql> update telefones id_funcionario = '6' where id_tel = 6;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '= '6' where id_tel = 6' at line 1
mysql> update telefones id_funcionario = 3 where id_tel = 6;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '= 3 where id_tel = 6' at line 1
mysql> update telefones set id_funcionario = 3 where id_tel = 6;
Query OK, 1 row affected (0.04 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from telefones;
+--------+-------------+----------------+
| id_tel | telefone    | id_funcionario |
+--------+-------------+----------------+
|      1 | 81983306684 |              1 |
|      2 | 81983306685 |              2 |
|      3 | 81983306686 |              2 |
|      4 | 81983306688 |              3 |
|      5 | 81933066889 |              3 |
|      6 | 81983306690 |              3 |
+--------+-------------+----------------+
6 rows in set (0.00 sec)

mysql> create table func2 select * from funcionario;
Query OK, 9 rows affected (0.11 sec)
Records: 9  Duplicates: 0  Warnings: 0

mysql> show tables;
+-------------------+
| Tables_in_turma_d |
+-------------------+
| alunos            |
| func2             |
| funcionario       |
| telefones         |
+-------------------+
4 rows in set (0.04 sec)

mysql> alter table func2 add(
    -> id_funcionarios primary key);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'primary key)' at line 2
mysql> alter table func2 update(
    -> id_funcionarios ^Crimary key);
mysql> alter table func2 modify id_funcionarios int not null auto_increment primary key;
ERROR 1054 (42S22): Unknown column 'id_funcionarios' in 'func2'
mysql> alter table func2 modify id_funcionarios int not null auto_increment primary key;
ERROR 1054 (42S22): Unknown column 'id_funcionarios' in 'func2'
mysql> alter table func2 modify id_funcionario int not null auto_increment primary key;
Query OK, 9 rows affected (0.16 sec)
Records: 9  Duplicates: 0  Warnings: 0

mysql> select * from func2;
+----------------+-------------+-------------+--------------+----------------+---------+--------------------------------------+-------------+----------+--------+--------+
| id_funcionario | nome        | cpf         | departamento | cpf_supervisor | salario | logradouro                           | complemento | cep      | bairro | cidade |
+----------------+-------------+-------------+--------------+----------------+---------+--------------------------------------+-------------+----------+--------+--------+
|              1 | jose mario  | 10203040231 |            3 | 98765432198    |    3500 | rua jornalista nelson rodrigues      | 15          | 51300140 | Ibura  | recife |
|              2 | Maria clara | 32123123424 |            2 | 87654321908    |    3423 | travessa jornalista nelson rodrigues | 15          | 51300140 | Ibura  | recife |
|              3 | João        | 23124532345 |            3 | 76543210987    |    7004 | avenida jornalista nelson rodrigues  | 15          | 51300140 | Ibura  | recife |
|              4 | Vinicius    | 23124512347 |            5 | 76543212345    |    3423 | NULL                                 |             |          |        |        |
|              5 | Wellington  | 12344512345 |            1 | 12543212345    |   16045 | NULL                                 |             |          |        |        |
|              6 | Clarisse    | 12344654321 |            5 | 31254365432    |    7856 | NULL                                 |             |          |        |        |
|              7 | Vilma       | 51234460987 |            4 | 31254365567    |    4354 | NULL                                 |             |          |        |        |
|              8 | José        | 37034460987 |            3 | 31251235567    |   76545 | NULL                                 |             |          |        |        |
|              9 | Claudemir   | 51075360987 |            2 | 31254365567    |    9876 | NULL                                 |             |          |        |        |
+----------------+-------------+-------------+--------------+----------------+---------+--------------------------------------+-------------+----------+--------+--------+
9 rows in set (0.01 sec)

mysql> alter table telefones modify numeros where telefone;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'where telefone' at line 1
mysql> update telefones numero where telefone;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'where telefone' at line 1
mysql> ALTER TABLE telefone CHANGE COLUMN numero;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> ALTER TABLE telefones rename telefone to numero;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'to numero' at line 1
mysql> ALTER TABLE telefones rename column telefone to numero;
Query OK, 0 rows affected (0.24 sec)
Records: 0  Duplicates: 0  Warnings: 0"""
