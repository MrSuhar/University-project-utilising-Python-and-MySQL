import pymysql;
import mysql.connector;
import datetime;

def wypisywanie_z_bazy(nazwa_tabeli):
	mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="dbprojekt"
		)
	mycursor = mydb.cursor()
	if nazwa_tabeli == "Czlonek":
		print("Indeks   Imie   Nazwisko   Wydzial   Telefon   Mail     Nazwa Stowarzyszenie");
		mycursor.execute("SELECT Czlonek.indeks,Czlonek.imie,Czlonek.nazwisko,Czlonek.wydzial,Czlonek.telefon,Czlonek.mail,Stowarzyszenie.nazwa FROM Czlonek inner join Stowarzyszenie on Czlonek.stowarzyszenie_id=Stowarzyszenie.stowarzyszenie_id");
	elif nazwa_tabeli == "Stowarzyszenie":
		mycursor.execute("SELECT * FROM Stowarzyszenie");
	elif nazwa_tabeli == "Spotkanie":
		mycursor.execute("SELECT * FROM Spotkanie");
	elif nazwa_tabeli == "Sala":
		mycursor.execute("select * from Sala");
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

def edycja_czlonka():
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);
	numer = raw_input("Podaj id czlonka, ktorego chcesz zmienic dane:");
	#jedno zapytanie - aktualizacja wszystkiego
	#sql2 = "UPDATE Czlonek SET Czlonek.imie=%s, Czlonek.nazwisko=%s,Czlonek.wydzial=%s,Czlonek.telefon=%s,Czlonek.mail=%s,Czlonek.stowarzyszenie_id=%s where Czlonek.indeks=%s";
	try:
		with connection.cursor() as cursor:
			wybor = raw_input("Czy chcesz zmienic imie? t=tak,inny klawisz=nie");
			if (wybor =="t"):
				imie = raw_input("Wprowadz imie:");
				sql2 = "UPDATE Czlonek SET Czlonek.imie=%s where Czlonek.indeks=%s";
				cursor.execute(sql2, (imie,numer));
				result = cursor.fetchall();
			wybor = raw_input("Czy chcesz zmienic nazwisko? t=tak,inny klawisz=nie");
			if (wybor =="t"):
				nazwisko = raw_input("Wprowadz nazwisko:");
				sql2 = "UPDATE Czlonek SET Czlonek.nazwisko=%s where Czlonek.indeks=%s";
				cursor.execute(sql2, (nazwisko,numer));
				result = cursor.fetchall();
			wybor = raw_input("Czy chcesz zmienic wydzial? t=tak,inny klawisz=nie");
			if (wybor =="t"):
				wydzial = raw_input("Wprowadz wydzial:");
				sql2 = "UPDATE Czlonek SET Czlonek.wydzial=%s where Czlonek.indeks=%s";
				cursor.execute(sql2, (wydzial,numer));
				result = cursor.fetchall();
			wybor = raw_input("Czy chcesz zmienic numer telefonu? t=tak,inny klawisz=nie");
			if (wybor =="t"):
				telefon = raw_input("Wprowadz numer telefonu:");
				sql2 = "UPDATE Czlonek SET telefon=%s where Czlonek.indeks=%s";
				cursor.execute(sql2, (telefon,numer));
				result = cursor.fetchall();
			wybor = raw_input("Czy chcesz zmienic adres email? t=tak,inny klawisz=nie");
			if (wybor =="t"):
				mail = raw_input("Wprowadz adres email:");
				sql2 = "UPDATE Czlonek SET Czlonek.mail=%s where Czlonek.indeks=%s";
				cursor.execute(sql2, (mail,numer));
				result = cursor.fetchall();
			wybor = raw_input("Czy chcesz zmienic stowarzyszenie? t=tak,inny klawisz=nie");
			if (wybor =="t"):
				stowarzyszenie = raw_input("Wprowadz id stowarzyszenia:");
				sql2 = "UPDATE Czlonek SET Czlonek.stowarzyszenie_id=%s where Czlonek.indeks=%s";
				cursor.execute(sql2, (stowarzyszenie,numer));
				result = cursor.fetchall();


			print("Poprzednie dane:");
			print(result);
			print("\nZaktualizowane dane:");
			#sql2 = "UPDATE Czlonek SET Czlonek.imie=%s, Czlonek.nazwisko=%s,Czlonek.wydzial=%s,Czlonek.telefon=%s,Czlonek.mail=%s,Czlonek.stowarzyszenie_id=%s where Czlonek.indeks=%s";
			sql = "SELECT * from Czlonek where Czlonek.indeks=%s";
			cursor.execute(sql, numer);
			result = cursor.fetchall();
			for x in result:
				print(x)
		connection.commit()
	finally:
		connection.close();

# --------------DODAWANIE DO BAZY--------------------
def dodawanie_czlonka_do_bazy():
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);

	imie = raw_input("Wprowadz imie:");
	nazwisko = raw_input("Wprowadz nazwisko:");
	wydzial = raw_input("Wprowadz wydzial:");
	telefon = raw_input("Wprowadz telefon:");
	email = raw_input("Wprowadz email:");
	stowarzyszenie = raw_input("Wprowadz id stowarzyszenia:");
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO `Czlonek` (`imie`,`nazwisko`,`wydzial`,`telefon`,`mail`,`stowarzyszenie_id`) VALUES (%s,%s,%s,%s,%s,%s)";
			cursor.execute(sql, (imie,nazwisko,wydzial,telefon,email,stowarzyszenie));
		connection.commit()
	finally:
		connection.close();


def dodawanie_stowarzyszenia_do_bazy(a, b, c):
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);
	try:
		with connection.cursor() as cursor:
			sql = "INSERT INTO `Stowarzyszenie` (`nazwa`,`haslo`,`przewodniczacy_id`) VALUES (%s,%s,%s)";
			cursor.execute(sql, (a, b, c));
		connection.commit()
	finally:
		connection.close();

def dodawanie_spotkania_do_bazy():
	a = raw_input("Podaj numer sali:");
	b = raw_input("Podaj id stowarzyszenia:");
	c = raw_input("Podaj date rozpoczecia w formacie YYYY-MM-DD HH-MM-SS:");
	d = raw_input("Podaj date zakonczenia w formacie YYYY-MM-DD HH-MM-SS:");
	e = raw_input("Podaj temat spotkania:");
	try:
		connection = mysql.connector.connect(host='localhost',
											 user='root',
											 password='',
											 db='dbprojekt',
											 charset='utf8mb4');
		# cursorclass=pymysql.cursors.SSDictCursor);
		cursor = connection.cursor();
		sql = "INSERT INTO `Spotkanie` (`sala_id`,`stowarzyszenie_id`,`data_rozpoczecia`,`data_zakonczenia`,`temat_spotkania`) VALUES (%s,%s,%s,%s,%s)";
		cursor.execute(sql, (a, b, c, d, e));
		connection.commit();

	except mysql.connector.Error as error:
		print("Nie udalo sie dodac rekordu do bazy\n".format(error));
	finally:
		if (connection.is_connected()):
			cursor.close();
			connection.close();


# -----------------USUWANIE DANYCH Z BAZY----------------------------------


def usun_rekord_z_bazy(nazwa_tabeli):
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);
	try:
		with connection.cursor() as cursor:
			if nazwa_tabeli == "Czlonek":
				rekord_id = raw_input("Wprowadz indeks Czlonka ktorego chcesz usunac");
				sql_2 = "DELETE from `Czlonek` where `indeks`=%s";

			elif nazwa_tabeli == "Stowarzyszenie":
				rekord_id = raw_input("Wprowadz id Stowarzyszenia ktore chcesz usunac");
				sql_2 = "DELETE from `Stowarzyszenie` where `stowarzyszenie_id`=%s";

			elif nazwa_tabeli == "Spotkanie":
				rekord_id = raw_input("Wprowadz id Spotkania ktore chcesz usunac");
				sql_2 = "DELETE from `Spotkanie` where `spotkanie_id`=%s";

			elif nazwa_tabeli == "Sala":
				rekord_id = raw_input("Wprowadz id Sali ktore chcesz usunac");
				sql_2 = "DELETE from `Sala` where `sala_id`=%s";

			# Dodac usuwanie np. Przewodniczacych gdy sa usuwani z bazy
			sql = "SET FOREIGN_KEY_CHECKS=0";
			cursor.execute(sql);
			cursor.execute(sql_2, (rekord_id));
			sql = "SET FOREIGN_KEY_CHECKS=1";
			cursor.execute(sql);
		connection.commit();

	finally:
		connection.close();
		print("Rozlaczono z baza\n");

def edycja_stowarzyszenia():
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);

	try:
		with connection.cursor() as cursor:
			numer = raw_input("Podaj id stowarzyszenia, ktorego chcesz zmienic dane:");

			#nazwa = raw_input("Wprowadz nazwe:");
			#przew = raw_input("Wprowadz id przewodniczacego:");
			#sql2 = "UPDATE Stowarzyszenie SET Stowarzyszenie.nazwa=%s,Stowarzyszenie.przewodniczacy_id=%s where Stowarzyszenie.stowarzyszenie_id=%s";
			#cursor.execute(sql2, (nazwa,przew,numer));
			#cursor.execute(sql, numer);
			#result = cursor.fetchall();

			wybor=raw_input("Czy chcesz edytowac nazwe stowarzyszenia? t=tak,inny klawisz=nie")
			if (wybor == "t"):
				nazwa = raw_input("Wprowadz nazwe:");
				sql2 = "UPDATE Stowarzyszenie SET Stowarzyszenie.nazwa=%s where Stowarzyszenie.stowarzyszenie_id=%s";
				cursor.execute(sql2, (nazwa, numer));
				result = cursor.fetchall();
			wybor=raw_input("Czy chcesz edytowac przewodniczacego stowarzyszenia? t=tak,inny klawisz=nie")
			if (wybor == "t"):
				przew = raw_input("Wprowadz indeks studenta ktory ma zostac nowym przewodniczacym:");
				sql2 = "UPDATE Stowarzyszenie SET Stowarzyszenie.przewodniczacy_id=%s where Stowarzyszenie.stowarzyszenie_id=%s";
				cursor.execute(sql2, (przew, numer));
				result = cursor.fetchall();
			sql = "SELECT * from Stowarzyszenie where stowarzyszenie_id=%s";
			cursor.execute(sql, numer);
			result = cursor.fetchall();
			for x in result:
				print(x)
		connection.commit()
	finally:
		connection.close();

def wypisz_czlonkow_stowarzyszenia():
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);

	try:
		with connection.cursor() as cursor:
			numer = raw_input("Podaj id stowarzyszenia, ktorego czlonkow chcesz wypsiac:");
			sql = ("SELECT * from Czlonek where stowarzyszenie_id=%s");
			cursor.execute(sql, numer);
			result = cursor.fetchall();
			for x in result:
				print(x)
		connection.commit()
	finally:
		connection.close();

def wypisz_wszystkie_spotkania():
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);

	try:
		with connection.cursor() as cursor:
			numer = raw_input("Podaj id stowarzyszenia, ktore spotkania chcesz wyswietlic:");
			sql = ("SELECT * from Spotkanie where stowarzyszenie_id=%s");
			cursor.execute(sql, numer);
			result = cursor.fetchall();
			for x in result:
				print(x)
		connection.commit()
	finally:
		connection.close();

def edycja_spotkania():
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);
	try:
		with connection.cursor() as cursor:
			numer=raw_input("Jakiego stowarzyszenia spotkanie chcesz zaktualizowac? Podaj jego ID");
			sql = ("SELECT * from Spotkanie where stowarzyszenie_id=%s");
			cursor.execute(sql, numer);
			result = cursor.fetchall();
			for x in result:
				print(x)
			spid=raw_input("Jakie spotkanie chcesz zaktualizowac? Podaj jego ID");
			wybor = raw_input("Czy chcesz zmienic sale w ktorym ma sie odbyc spotkanie? t=tak,inny klawisz=nie");
			if (wybor == "t"):
				#sql = ("SELECT * from Sala");
				#cursor.execute(sql);
				sala = raw_input("Wprowadz id sali:");
				sql2 = "UPDATE Spotkanie SET Spotkanie.sala_id=%s where Spotkanie.spotkanie_id=%s";
				cursor.execute(sql2, (sala, spid));
				result = cursor.fetchall();
			wybor = raw_input("Czy chcesz zmienic date spotkania? t=tak,inny klawisz=nie");
			if (wybor == "t"):
				data1 = raw_input("Wprowadz date rozpoczecia w formacie RRRR-MM-DD GG:MM");
				sql2 = "UPDATE Spotkanie SET Spotkanie.data_rozpoczecia=%s where Spotkanie.spotkanie_id=%s";
				cursor.execute(sql2, (data1, spid));
				result = cursor.fetchall();
				data2 = raw_input("Wprowadz date zakonczenia w formacie RRRR-MM-DD GG:MM:");
				sql2 = "UPDATE Spotkanie SET Spotkanie.data_zakonczenia=%s where Spotkanie.spotkanie_id=%s";
				cursor.execute(sql2, (data2, spid));
				result = cursor.fetchall();
			wybor = raw_input("Czy chcesz zmienic temat spotkania? t=tak,inny klawisz=nie");
			if (wybor == "t"):
				temat = raw_input("Wprowadz temat spotkania:");
				sql2 = "UPDATE Spotkanie SET Spotkanie.temat_spotkania=%s where Spotkanie.spotkanie_id=%s";
				cursor.execute(sql2, (temat, spid));
				result = cursor.fetchall();
			print("Zaktualizowane dane:");
			sql = ("SELECT * from Spotkanie where spotkanie_id=%s");
			cursor.execute(sql, spid);
		connection.commit()
	finally:
		connection.close();

def dodaj_sale():
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);
	try:
		with connection.cursor() as cursor:
			adres = raw_input("Wprowadz adres sali:");
			budynek = raw_input("Wprowadz identyfikator budynku(np B-4)");
			nr_sali = raw_input("Wprowadz numer sali znajdujacej sie w budynku");
			sql = "INSERT INTO `Sala` (`adres`,`budynek`,`nr_sali`) VALUES (%s,%s,%s)";
			cursor.execute(sql, (adres,budynek,nr_sali));
		connection.commit()
	finally:
		connection.close();


def dodawanie_usuwanie_czlonkow_stowarzyszenie(akcja):
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);

	try:
		with connection.cursor() as cursor:
			if akcja == "dodaj":
				numer = raw_input("Podaj id czlonka, ktorego chcesz dodac do stowarzyszenia:");
				stowarzyszenie = raw_input("Wprowadz id stowarzyszenia:");
				sql = "UPDATE Czlonek SET Czlonek.stowarzyszenie_id=%s where Czlonek.indeks=%s";
				cursor.execute(sql, (stowarzyszenie, numer));

			if akcja == "usun":
				numer = raw_input("Podaj id czlonka, ktorego chcesz usunac ze stowarzyszenia:");
				sql_2 = "UPDATE Czlonek SET Czlonek.stowarzyszenie_id=0 where Czlonek.indeks=%s";
				sql = "SET FOREIGN_KEY_CHECKS=0";
				cursor.execute(sql);
				cursor.execute(sql_2, (numer));
				sql = "SET FOREIGN_KEY_CHECKS=1";
				cursor.execute(sql);

		connection.commit()
	finally:
		connection.close();

#------------------------ZLICZANIE ILOSCI REKORDOW--------------------

def ilosc_czlonkow_spotkan_stowarzyszenia(rodzaj):
	connection = pymysql.connect(host='localhost',
								 user='root',
								 password='',
								 db='dbprojekt',
								 charset='utf8mb4',
								 cursorclass=pymysql.cursors.SSDictCursor);		
	

	try:
		with connection.cursor() as cursor:
		
			cursor = connection.cursor();
			stow_id = raw_input("Podaj id rzadanego stowarzyszenia:\n");

			if rodzaj == "Spotkanie":
				#sql = "SELECT *  ,COUNT(*) FROM `Spotkanie` where `stowarzyszenie_id`=%s";
				sql = "SELECT COUNT(*) AS 'ilosc_spotkan' FROM `Spotkanie` WHERE `stowarzyszenie_id`=%s";				
				cursor.execute(sql,(stow_id));

			elif rodzaj =="Czlonek":
				sql = "SELECT COUNT(*) AS 'ilosc_czlonkow' FROM `Czlonek` WHERE `stowarzyszenie_id`=%s";
				cursor.execute(sql,(stow_id));			
		
			result = cursor.fetchall()
			
			sql = "SELECT `nazwa` FROM `Stowarzyszenie` WHERE `stowarzyszenie_id`=%s"
			cursor.execute(sql,(stow_id));

			result_2=cursor.fetchall();

			print(result_2);			
			print(result);
			
	
	finally:
		connection.close();

def statystyki():
	connection = pymysql.connect(host='localhost',
									 user='root',
									 password='',
									 db='dbprojekt',
									 charset='utf8mb4',
									 cursorclass=pymysql.cursors.SSDictCursor);
	try:
		with connection.cursor() as cursor:
			sql=("select min(Spotkanie.data_rozpoczecia) as 'Pierwsze spotkanie' from Spotkanie;");
			cursor.execute(sql);
			result=cursor.fetchall();
			for x in result:
				print(x);
			sql = ("select max(Spotkanie.data_zakonczenia) as 'Ostatnie odbyte spotkanie' from Spotkanie where(Spotkanie.data_zakonczenia<=current_timestamp())");
			cursor.execute(sql);
			result = cursor.fetchall();
			for x in result:
				print(x);
			sql = ("select count(distinct Czlonek.indeks) as 'Ilosc czlonkow klubu' from Czlonek;");
			cursor.execute(sql);
			result = cursor.fetchall();
			for x in result:
				print(x);
			sql = ("select count(distinct Stowarzyszenie.stowarzyszenie_id) as 'Ilosc stowarzyszen' from Stowarzyszenie;");
			cursor.execute(sql);
			result = cursor.fetchall();
			for x in result:
				print(x);
			sql = ("select count(distinct Sala.adres) as 'Ilosc dostepnych sal'  from Sala;");
			cursor.execute(sql);
			result = cursor.fetchall();
			for x in result:
				print(x);
	finally:
		connection.close();
		print("Rozlaczono z baza\n");

def starespotkania():
	mydb = mysql.connector.connect(
				host="localhost",
				user="root",
				password="",
				database="dbprojekt"
			)
	mycursor = mydb.cursor()
	mycursor.execute("select Spotkanie.stowarzyszenie_id,Spotkanie.sala_id,Sala.adres,Sala.budynek,Sala.nr_sali,Spotkanie.spotkanie_id,Spotkanie.data_rozpoczecia,Spotkanie.data_zakonczenia,Spotkanie.temat_spotkania from Spotkanie inner join Sala on Spotkanie.sala_id=Sala.sala_id where data_zakonczenia<=current_timestamp() order by data_rozpoczecia asc");
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

def nowespotkania():
	mydb = mysql.connector.connect(
				host="localhost",
				user="root",
				password="",
				database="dbprojekt"
			)
	mycursor = mydb.cursor()
	mycursor.execute("select Spotkanie.stowarzyszenie_id,Spotkanie.sala_id,Sala.adres,Sala.budynek,Sala.nr_sali,Spotkanie.spotkanie_id,Spotkanie.data_rozpoczecia,Spotkanie.data_zakonczenia,Spotkanie.temat_spotkania from Spotkanie inner join Sala on Spotkanie.sala_id=Sala.sala_id where data_rozpoczecia>=current_timestamp() order by data_rozpoczecia asc");		myresult = mycursor.fetchall()
	for x in myresult:
		print(x)