drop table personnes

create table personnes (prenom varchar(30) not null, nom varchar(30) not null, age integer not null, primary key (nom,prenom))

insert into personnes(prenom, nom, age) values('Paul', 'Langevin', 48)
insert into personnes(prenom, nom, age) values('Sylvie', 'Lefur', 70)

select prenom, nom, age from personnes

xx

insert into personnes(prenom, nom, age) values('Pierre','Nicazou',35)
insert into personnes(prenom, nom, age) values('Geraldine','Colou',26)
insert into personnes(prenom, nom, age) values('Paulette','Girond',56)

select prenom, nom, age from personnes
select nom, prenom from personnes
select nom, prenom from personnes order by nom asc, prenom desc

select nom, prenom from personnes where age between 20 and 40 order by age desc, nom asc, prenom asc

insert into personnes(prenom, nom, age) values ('Josette','Bruneau',46)

update personnes set age=47 where nom='Bruneau'

select nom, prenom, age from personnes where nom='Bruneau'

delete from personnes where nom='Bruneau'

select nom,prenom,age from personnes where nom='Bruneau'

