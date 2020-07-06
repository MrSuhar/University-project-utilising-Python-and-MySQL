# Temat projektu
Tematem Projektu jest klub studencki - taki jak np. koła naukowe czy też stowarzyszenie fanów gier planszowych.  

| Nazwisko i imię | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
| :-------------: | :-----: | :------: | :-----: | :---: | :------------: |
| Bartosz Kozłowski        | WIMiIP  | IS       |   4     | 2     | 2019/2020      |
| Jakub Kopeć         | WIMiIP  | IS       |   4     | 3     | 2019/2020      |

## Projekt bazy danych
![Projekt](https://github.com/phajder-databases/db2020-project-klub-studencki/blob/master/src/sql/ProjektDB.svg?raw=true)

Baza danych składa się z czterech encji: Członek,Sala,Stowarzyszenie oraz Spotkanie.
Każde stowarzyszenie może posiadać wielu członków, oraz wiele spotkań. Każdy członek posiada swój indywidualny indeks nadawany automatycznie oraz dane kontaktowe.
Dodatkowo każde stowarzyszenie posiada przewodniczącego. Spotkania mają ustaloną datę rozpoczęcia i zakończenia,temat oraz salę w której się odbywają.

*Przykładowe zapytania DDL:*

```SQL
CREATE TABLE Stowarzyszenie
(    
	stowarzyszenie_id INT auto_increment,
    nazwa VARCHAR(50) unique not null,
    przewodniczacy_id int,
    primary key(stowarzyszenie_id)
);

alter table Stowarzyszenie
add FOREIGN KEY(przewodniczacy_id) REFERENCES Czlonek(indeks);

CREATE TABLE Sala 
(
	sala_id INT auto_increment,
    adres VARCHAR(40) not null,
    budynek VARCHAR(3) not null,
	nr_sali INT not null,
    primary key(sala_id)
);
```

## Implementacja zapytań SQL
**1.Wypisanie wszystkich: członków,spotkań,stowarzyszeń,sal**

_**Członkowie**_

```SQL
SELECT Czlonek.indeks,Czlonek.imie,Czlonek.nazwisko,Czlonek.wydzial,Czlonek.telefon,Czlonek.mail,Stowarzyszenie.nazwa FROM Czlonek left join Stowarzyszenie on Czlonek.stowarzyszenie_id=Stowarzyszenie.stowarzyszenie_id
```
_**Spotkania**_
```SQL
SELECT * FROM Spotkanie
```
_**Stowarzyszenia**_
```SQL
SELECT * FROM Stowarzyszenie
```
_**Sale**_
```SQL
select * from Sala
```

**2.Dodanie nowych: członków,spotkań,stowarzyszeń,sal.**

_**Członkowie**_
```SQL
INSERT INTO `Czlonek` (`imie`,`nazwisko`,`wydzial`,`telefon`,`mail`,`stowarzyszenie_id`) VALUES (%s,%s,%s,%s,%s,%s)
```
_**Stowarzyszenie**_
```SQL
INSERT INTO `Stowarzyszenie` (`nazwa`,`haslo`,`przewodniczacy_id`) VALUES (%s,%s,%s)
```
_**Spotkanie**_
```sql
INSERT INTO `Spotkanie` (`sala_id`,`stowarzyszenie_id`,`data_rozpoczecia`,`data_zakonczenia`,`temat_spotkania`) VALUES (%s,%s,%s,%s,%s)
```
_**Sale**_
``` sql
INSERT INTO `Sala` (`adres`,`budynek`,`nr_sali`) VALUES (%s,%s,%s)
```
**3.Usunięcie: członków,stowarzyszeń,spotkań,sal.**

_**Członkowie**_
``` sql
DELETE from `Czlonek` where `indeks`=%s
```
_**Stowarzyszenie**_
``` sql
DELETE from `Stowarzyszenie` where `stowarzyszenie_id`=%s
```
_**Spotkanie**_
``` sql
DELETE from `Spotkanie` where `spotkanie_id`=%s
```
_**Sale**_
``` sql
DELETE from `Sala` where `sala_id`=%s
```
**4.Edycja: członków,stowarzyszeń,spotkań.**

W przypadku edycji użytkownik wybiera ,które z pól mają zostać edytowane. Tym samym przy edycji konkretnego rekordu nie wszytskie z poniższych zapytań będą wykorzystywane.

_**Członkowie**_
``` sql
UPDATE Czlonek SET Czlonek.imie=%s where Czlonek.indeks=%s
UPDATE Czlonek SET Czlonek.nazwisko=%s where Czlonek.indeks=%s
UPDATE Czlonek SET Czlonek.wydzial=%s where Czlonek.indeks=%s
UPDATE Czlonek SET telefon=%s where Czlonek.indeks=%s
UPDATE Czlonek SET Czlonek.mail=%s where Czlonek.indeks=%s
UPDATE Czlonek SET Czlonek.stowarzyszenie_id=%s where Czlonek.indeks=%s
```
_**Stowarzyszenia**_
``` sql
UPDATE Stowarzyszenie SET Stowarzyszenie.nazwa=%s where Stowarzyszenie.stowarzyszenie_id=%s
UPDATE Stowarzyszenie SET Stowarzyszenie.przewodniczacy_id=%s where Stowarzyszenie.stowarzyszenie_id=%s
```
_**Spotkania**_
``` sql
UPDATE Spotkanie SET Spotkanie.sala_id=%s where Spotkanie.spotkanie_id=%s
UPDATE Spotkanie SET Spotkanie.data_rozpoczecia=%s where Spotkanie.spotkanie_id=%s
UPDATE Spotkanie SET Spotkanie.data_zakonczenia=%s where Spotkanie.spotkanie_id=%s
UPDATE Spotkanie SET Spotkanie.temat_spotkania=%s where Spotkanie.spotkanie_id=%s
```
**5.Dodanie/usunięcie członka ze stowarzyszenia.**

_**Dodanie**_
``` sql
UPDATE Czlonek SET Czlonek.stowarzyszenie_id=%s where Czlonek.indeks=%s
```
_**Usunięcie**_
``` sql
UPDATE Czlonek SET Czlonek.stowarzyszenie_id=0 where Czlonek.indeks=%s
```

**6.Wypisanie wszystkich członków lub spotkań wybranego stowarzyszenia.**

_**Spotkania**_
``` sql
SELECT * from Spotkanie where stowarzyszenie_id=%s
```
_**Członkowie**_
``` sql
SELECT * from Czlonek where stowarzyszenie_id=%s
```

**7.Wypisanie wybranych spotkań**

_**Spotkania które odbyły się w przeszłości**_
```sql
select Spotkanie.stowarzyszenie_id,Spotkanie.sala_id,Sala.adres,Sala.budynek,Sala.nr_sali,Spotkanie.spotkanie_id,Spotkanie.data_rozpoczecia,Spotkanie.data_zakonczenia,Spotkanie.temat_spotkania from Spotkanie inner join Sala on Spotkanie.sala_id=Sala.sala_id where data_zakonczenia<=current_timestamp() order by data_rozpoczecia asc
```
_**Spotkania ,które dopiero się odbędą**_

```sql
select Spotkanie.stowarzyszenie_id,Spotkanie.sala_id,Sala.adres,Sala.budynek,Sala.nr_sali,Spotkanie.spotkanie_id,Spotkanie.data_rozpoczecia,Spotkanie.data_zakonczenia,Spotkanie.temat_spotkania from Spotkanie inner join Sala on Spotkanie.sala_id=Sala.sala_id where data_rozpoczecia>=current_timestamp() order by data_rozpoczecia asc
```

**8.Wypisanie ogólnych statystyk**
W tym wypadku są to: data pierwszego i ostatniego (w kontekście danych w bazie) odbytego spotkania, łączna ilość członków wszystkich klubów, ilość stowarzyszeń oraz dostępnych sal.

```SQL
select min(Spotkanie.data_rozpoczecia) as 'Pierwsze spotkanie' from Spotkanie

select max(Spotkanie.data_zakonczenia) as 'Ostatnie odbyte spotkanie' from Spotkanie where(Spotkanie.data_zakonczenia<=current_timestamp())

select count(distinct Czlonek.indeks) as 'Ilosc czlonkow klubu' from Czlonek;

select count(distinct Stowarzyszenie.stowarzyszenie_id) as 'Ilosc stowarzyszen' from Stowarzyszenie;

select count(distinct Sala.adres) as 'Ilosc dostepnych sal'  from Sala;

```

## Aplikacja
Powstała aplikacja posiada proste tekstowe (w konsoli) menu. Z założenia dostęp do niej posiada jedynie administrator bazy danych przechowującej informacje o poszczególnych członkach, stowarzyszeniach i spotkaniach klubów. Program został napisany w języku Python z wykorzystaniem dwóch bibliotek obsługujących bazy danych: pymysql oraz mysql connector (oczywiście w wersji dla języka Python, istnieją również wersje dla innych języków np. C++).

Aplikacja umożliwia zarządzanie czterema kluczowymi elementami bazy:
-Członkami,
-Stowarzyszeniami,
-Spotkaniami,
-Salami.

Każda z tych funkcjonalności posiada dedykowane menu do którego można dostać się (i przemieszczać) po uruchomieniu programu.

_**Przykładowy use-case**_

Użykownik chcę dodać nowego członka do bazy.

1. Po uruchomieniu programu wyświetla się głowne menu, użytkownik wybiera opcje "Zarządzanie Członkami" poprzez wciśnięcie klawisza '1' ,a następnie klawisza 'enter'.
2. W "MENU CZŁONKÓW" użytkownik wybiera opcję "Dodaj członka do bazy", w sposób identyczny jak w poprzednim kroku.
3. Program prosi użytkownika o wypełnienie poszczególnych pól (tj. imie,nazwisko,wydzial,stowarzyszenie_id,telefon,mail).
4. Po wypełnieniu pól nowy członek zostaje dodany do bazy, na ekranie wyświetla się informacja o rozłączeniu się programu z bazą danych. 
5. Na ekranie wyświetla się ostatnio używane menu (MENU CZŁONKÓW), użytkownik może kontynuować pracę w programie.

## Dodatkowe uwagi
Testy wszystkich funkcjonalności w obrębie aplikacji zostały wykonane dla lokalnej bazy danych ze względu na problemy ze znalezieniem hostingu o zadowalającej prędkości przesyłu danych.

Metodyka pracy tj. wprowadzenie funkcjonalności, jej test, poprawienie błedu jest najbardziej zbliżona do metodyki Continuous Deployment. W odrożnieniu od CD testy były przeprowadzane jedynie manualnie.

Plik aplikacja.py zawiera funkcje wyświetlające poszczególne menu. 
Plik funkcje.py zawiera metody wykorzystujące zapytania sql.
