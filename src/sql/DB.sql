#drop database dbprojekt;
/*
SET SQL_MODE='ALLOW_INVALID_DATES';
create database dbprojekt;
use dbprojekt;
#---------------TWORZENIE TABEL-------------------------
CREATE TABLE Sala 
(
	sala_id INT auto_increment,
    adres VARCHAR(40) not null,
    budynek VARCHAR(3) not null,
	nr_sali INT not null,
    primary key(sala_id)
);
CREATE TABLE Spotkanie
(
	spotkanie_id int auto_increment,
    sala_id INT not null,
	stowarzyszenie_id INT not null,
    data_rozpoczecia timestamp not null,
    data_zakonczenia timestamp not null,
    temat_spotkania VARCHAR(50),
    primary key(spotkanie_id)
);
CREATE TABLE Stowarzyszenie
(    
	stowarzyszenie_id INT auto_increment,
    nazwa VARCHAR(50) unique not null,
    przewodniczacy_id int,
    primary key(stowarzyszenie_id)
);

CREATE TABLE Czlonek
(    
	indeks INT(6) auto_increment,
    imie VARCHAR(30) not null,
    nazwisko VARCHAR(30) not null,
    wydzial VARCHAR(50) not null,
    stowarzyszenie_id INT,   
    telefon int not null unique,
    mail varchar(50) not null unique,
    primary key(indeks)
);



#------------------DODAWANIE KLUCZY OBCYCH---------------------

alter table Spotkanie
add FOREIGN KEY(sala_id) REFERENCES Sala(sala_id),
add FOREIGN KEY(stowarzyszenie_id) REFERENCES Stowarzyszenie(stowarzyszenie_id);

alter table Stowarzyszenie
add FOREIGN KEY(przewodniczacy_id) REFERENCES Czlonek(indeks);


alter table Czlonek
add FOREIGN KEY(stowarzyszenie_id) REFERENCES Stowarzyszenie(stowarzyszenie_id);

#---------------------------------------------------------------

insert into Sala(adres,budynek,nr_sali) values("Rostafinskiego 666","A-2",105);
insert into Sala(adres,budynek,nr_sali) values("Rostafinskiego 666","A-2",122);
insert into Sala(adres,budynek,nr_sali) values("Mickiewicza 44","A-4",13);
insert into Sala(adres,budynek,nr_sali) values("Słowackiego 21","A-3",4);
insert into Sala(adres,budynek,nr_sali) values("Jana Pawła II 37","A-1",90);
select * from Sala;

#NAJPIERW WPROWADZIC CZLOWIEKA DO BAZY, POTEM TWORZENIE STOWARZYSZENIA, POTEM NADANIE STOWARZYSZENIE_id
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail) values("Dawid","Pasieka","WMS",105105997,"DawidPasieka@gmail.com");
insert into Stowarzyszenie(nazwa,przewodniczacy_id) values ("Miłośnicy Fizyki",1);
update Czlonek set stowarzyszenie_id=1 where indeks=1;
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Jakub","Trapczak","WFiIS",112999998,"JakubTrapczak@gmail.com",1);
select * from Stowarzyszenie;

insert into Czlonek(imie,nazwisko,wydzial,telefon,mail) values("Geralt","Riv","WFiIS",11231298,"Gerwald@gmail.com");
insert into Stowarzyszenie(nazwa,przewodniczacy_id) values ("Miłośnicy RPG",3);
update Czlonek set stowarzyszenie_id=2 where indeks=3;
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Zenon","Bury","WIMiIP",123456789,"Bezimienny@gmail.com",2);
select * from Stowarzyszenie;
select * from Czlonek;

#LEPSZA WERSJA - DODANIE STWARZYSZENIA BEZ ID,DODANIE CZLONKOW,NADANIE STOWARZYSZENIU PRZEWODNICZACEGO
insert into Stowarzyszenie(nazwa) values ("Novigrad");
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Sigismund","Djikstra","WIMiIP",000456789,"Sigi@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Triss","Merigold","WIMiC",11231000,"Triss@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Jaskier","Jaskier","WIMiC",11231001,"Jaskier@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Ulu","Mulu","WIMiC",11231002,"Ulumulu@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Randy","Lahey","WIMiC",11231004,"Randylahey@gmail.com",3);
insert into Czlonek(imie,nazwisko,wydzial,telefon,mail,stowarzyszenie_id) values("Cory","Trevor","WIMiIP",11231003,"CoryTrevor@gmail.com",3);
update Stowarzyszenie set przewodniczacy_id=5 where stowarzyszenie_id=3;
select * from Czlonek;


insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-07 10:00:00','2020-07-07 14:00:00',"Pierwsze spotkanie",1,1);
insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-14 10:00:00','2020-07-14 14:00:00',"Drugie spotkanie",2,1);
insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-21 10:00:00','2020-07-21 14:00:00',"Robienie fajnych rzeczy",1,1);

insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-07 7:00:00','2020-07-07 14:00:00',"Pierwsze spotkanie",3,2);
insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-10 8:30:00','2020-07-10 10:00:00',"Pierwsze spotkanie",1,2);
insert into Spotkanie(data_rozpoczecia,data_zakonczenia,temat_spotkania,sala_id,stowarzyszenie_id) values('2020-07-12 8:40:00','2020-07-12 12:00:00',"Pierwsze spotkanie",1,2);
*/

use dbprojekt;

#spotkania ktore sie odbyly
select Spotkanie.stowarzyszenie_id,Spotkanie.sala_id,Sala.adres,Sala.budynek,Sala.nr_sali,Spotkanie.spotkanie_id,Spotkanie.data_rozpoczecia,Spotkanie.data_zakonczenia,Spotkanie.temat_spotkania 
from Spotkanie inner join Sala on Spotkanie.sala_id=Sala.sala_id where data_zakonczenia<=current_timestamp() order by data_rozpoczecia asc;

#spotkania ktore sie odbeda
select Spotkanie.stowarzyszenie_id,Spotkanie.sala_id,Sala.adres,Sala.budynek,Sala.nr_sali,Spotkanie.spotkanie_id,Spotkanie.data_rozpoczecia,Spotkanie.data_zakonczenia,Spotkanie.temat_spotkania 
from Spotkanie inner join Sala on Spotkanie.sala_id=Sala.sala_id where data_rozpoczecia>=current_timestamp() order by data_rozpoczecia asc;

#statystyka
select 
	Stowarzyszenie.stowarzyszenie_id as "ID stowarzyszenia" ,
    Stowarzyszenie.nazwa as "Nazwa stowarzyszenia",
    count(Stowarzyszenie.stowarzyszenie_id) as "Ilosc czlonkow w stowarzyszeniu"
from Czlonek  join Stowarzyszenie on Czlonek.stowarzyszenie_id=Stowarzyszenie.stowarzyszenie_id group by Stowarzyszenie.nazwa;

select (Spotkanie.data_rozpoczecia) as "Pierwsze spotkanie" from Spotkanie;

select max(Spotkanie.data_zakonczenia) as "Ostatnie odbyte spotkanie" from Spotkanie where(Spotkanie.data_zakonczenia<=current_timestamp());

select count(distinct Czlonek.indeks) as 'Ilosc czlonkow klubu' from Czlonek;
select count(distinct Stowarzyszenie.stowarzyszenie_id) as 'Ilosc stowarzyszen' from Stowarzyszenie;
select count(distinct Sala.adres) as 'Ilosc dostepnych sal'  from Sala;
