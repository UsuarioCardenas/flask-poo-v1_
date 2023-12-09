drop database db_poo;

create database db_poo;

use db_poo;

CREATE TABLE usuario (
  id int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  telefono varchar(50) NOT NULL,
  email varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into usuario(nombre,telefono,email)
values ('Jaime','999888777','jaime@abc.com');


CREATE TABLE empleado (
  cod_emp int(5) NOT NULL primary key auto_increment,
  nombre varchar(50) NOT NULL,
  telefono varchar(50) NOT NULL,
  email varchar(50) NOT NULL,
  fecha_emp date NOT NULL,
  puesto varchar(50) NOT NULL,
  salario int NOT NULL
  ) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into empleado(nombre,telefono,email,fecha_emp, puesto, salario)
values ('Abel','916620659','thesheepmt@gmail.com','02/10/19','Analista','1200');

insert into empleado(nombre,telefono,email,fecha_emp, puesto, salario)
values ('Juan','999298654','perez@gmail.com','02/09/10','Administrador','1500');

insert into empleado(nombre,telefono,email,fecha_emp, puesto, salario)
values ('Mauricio','989288654','perezperez@gmail.com','03/08/10','Administrador','1200');

insert into empleado(nombre,telefono,email,fecha_emp, puesto, salario)
values ('Diego','989255654','cardenas@gmail.com','01/04/10','Analista','1000');
