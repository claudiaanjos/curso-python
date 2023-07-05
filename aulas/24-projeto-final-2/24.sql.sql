create table horarios(
horario_id serial PRIMARY KEY,
linha varchar(60) NOT NULL,
origem varchar(30) NOT NULL,
destino varchar(30) NOT NULL,
diasemana varchar(30) NOT NULL,
hora TIME NOT NULL );


insert into horarios (linha,origem,destino,diasemana,hora) values ('Sm/Nh','Santa Maria','Novo Hamburgo','Segunda-feira','10:30');
insert into horarios (linha,origem,destino,diasemana,hora) values ('Sm/Poa','Santa Maria','Novo Hamburgo','Segunda-feira','15:40');
insert into horarios (linha,origem,destino,diasemana,hora) values ('Sm/Flp','Santa Maria','Novo Hamburgo','Segunda-feira','20:30');
insert into horarios (linha,origem,destino,diasemana,hora) values ('Sm/SP','Santa Maria','Novo Hamburgo','Segunda-feira','13:30');
insert into horarios (linha,origem,destino,diasemana,hora) values ('Sm/RJ','Santa Maria','Novo Hamburgo','Segunda-feira','11:30');
insert into horarios (linha,origem,destino,diasemana,hora) values ('Sm/Nh','Santa Maria','Novo Hamburgo','Segunda-feira','12:30');
insert into horarios (linha,origem,destino,diasemana,hora) values ('Sm/Nh','Santa Maria','Novo Hamburgo','Segunda-feira','13:30');
insert into horarios (linha,origem,destino,diasemana,hora) values ('Sm/Nh','Santa Maria','Novo Hamburgo','Segunda-feira','14:30');


select * from horarios