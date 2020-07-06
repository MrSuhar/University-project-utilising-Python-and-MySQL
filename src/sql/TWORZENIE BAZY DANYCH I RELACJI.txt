CREATE database Projekt

#---------------TWORZENIE TABEL-------------------------
USE Projekt;
CREATE TABLE Sala 
(
    adres VARCHAR(40),
    budynek VARCHAR(3),
    nr_sali INT,
    sala_id INT
);

USE Projekt;
CREATE TABLE Spotkanie
(
    data_rozpoczecia DATE,
    data_zakonczenia DATE,
    temat_spotkania VARCHAR(50),
    sala_id INT,
    stowarzyszenie_id INT
);

USE Projekt;
CREATE TABLE Stowarzyszenie
(    
    nazwa VARCHAR(50),
    ilosc_czlonków INT,
    stowarzyszenie_id INT,
    czlonek_id INT,
    przewodniczacy_id int,
    sala_id int
);

USE Projekt;
CREATE TABLE Członek
(    
    imię VARCHAR(30),
    nazwisko VARCHAR(30),
    telefon INT,
    mail VARCHAR(50),
    indeks INT,
    wydział VARCHAR(50),
    czlonek_id INT,
    stowarzyszenie_id INT,    
    przewodniczacy_id INT   
);

#-------------------DODAWANIE KLUCZY GŁÓWNYCH------------------
USE Projekt;
alter table Sala
add PRIMARY KEY(sala_id);

USE Projekt;
alter table Stowarzyszenie
add PRIMARY KEY(stowarzyszenie_id);

USE Projekt;
alter table Członek
add PRIMARY KEY(czlonek_id);

#------------------DODAWANIE KLUCZY OBCYCH---------------------
USE Projekt;
alter table Spotkanie
add FOREIGN KEY(sala_id) REFERENCES Sala(sala_id),
add FOREIGN KEY(stowarzyszenie_id) REFERENCES Stowarzyszenie(stowarzyszenie_id);

USE Projekt;
alter table Stowarzyszenie
add FOREIGN KEY(czlonek_id) REFERENCES Członek(czlonek_id),
add FOREIGN KEY(sala_id) REFERENCES Sala(sala_id);

USE Projekt;
alter table Członek
add FOREIGN KEY(stowarzyszenie_id) REFERENCES Stowarzyszenie(Stowarzyszenie_id);


