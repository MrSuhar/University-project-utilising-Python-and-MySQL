import sys;

import funkcje;

# from nazwa_pliku import * #importowanie wszystkoch funkcji z pliku
#--------------------------WYKORZYSTYWANE FUNKCJE-----------------------------------------#
#ZARZADZANIE CZLONKAMI
def zarz_czlonkami():
	print("\nMENU CZLONKOW");								#gut
	print("1.Dodaj czlonka do bazy");						#gut
	print("2.Usun czlonka z bazy");							#gut
	print("3.Edytuj dane istniejacego czlonka");			#gut
	print("4.Wypisz wszystkich czlonkow z bazy");1			#gut
	print("5.Powrot do glownego menu");						#gut
	decyzja = int(raw_input("Wybierz co chcesz zrobic\n"));

	if decyzja == 1:
		funkcje.dodawanie_czlonka_do_bazy();
		zarz_czlonkami();
	elif decyzja == 2:
		funkcje.usun_rekord_z_bazy("Czlonek");
		zarz_czlonkami();
	elif decyzja == 3:
		funkcje.edycja_czlonka();
		zarz_czlonkami();
	elif decyzja == 4:
		funkcje.wypisywanie_z_bazy("Czlonek");
		zarz_czlonkami();
	elif decyzja == 5:
		glowne_menu();
	else:
		print("Podaj poprawna opcje\n");
		zarz_czlonkami();


# ZARZADZANIE STOWARZYSZENIEM
def zarz_stowarzyszenie():
	print("\nMENU STOWARZYSZEN");
	print("1.Dodaj nowe stowarzyszenie do bazy");
	print("2.Usun istniejace stowarzyszenie");
	print("3.Edytuj istniejace stowarzyszenie");
	print("4.Wypisz wszystkie istniejace stowarzyszenia");
	print("5.Dodaj czlonka do stowarzyszenia");
	print("6.Usun czlonka z stowarzyszenia");
	print("7.Wypisz wsystkich czlonkow wybranego stowarzyszenia");
	print("8.Wypisz wszystkie spotkania wybranego stowarzyszenia");
	print("9.Wypisz ilosc spotkan wybranego stowarzyszenia");
	print("10.Wypisz ilosc czlonkow wybranego stowarzyszenia");
	print("11.Powrot do glownego menu\n")
	decyzja = int(raw_input("Wybierz co chcesz zrobic\n"));

	
	

	if decyzja == 1:
		nazwa = raw_input("Wprowadz nazwe nowego stowarzyszenia");
		przewodniczacy_id = raw_input("Wprowadz id przewodniczacego nowego stowarzyszenia");
		funkcje.dodawanie_stowarzyszenia_do_bazy(nazwa, przewodniczacy_id);
		zarz_stowarzyszenie()
	elif decyzja == 2:  # usuwanie istniejacego stowarzyszenia
		funkcje.usun_rekord_z_bazy("Stowarzyszenie");
		zarz_stowarzyszenie()
	elif decyzja == 3:
		funkcje.edycja_stowarzyszenia();
		zarz_stowarzyszenie()
	elif decyzja == 4:
		funkcje.wypisywanie_z_bazy("Stowarzyszenie");
		zarz_stowarzyszenie()
	elif decyzja == 5:  # dodawanie czlonka do stowarzyszenia
		funkcje.dodawanie_usuwanie_czlonkow_stowarzyszenie("dodaj");
		zarz_stowarzyszenie();
	elif decyzja == 6:  # usuwanie czlonka ze stowarzyszenia
		funkcje.dodawanie_usuwanie_czlonkow_stowarzyszenie("usun");
		zarz_stowarzyszenie();
	elif decyzja == 7:
		funkcje.wypisz_czlonkow_stowarzyszenia();
		zarz_stowarzyszenie();
	elif decyzja == 8:
		funkcje.wypisz_wszystkie_spotkania();
		zarz_stowarzyszenie();
	elif decyzja == 9:
		funkcje.ilosc_czlonkow_spotkan_stowarzyszenia("Spotkanie");
		zarz_stowarzyszenie();
	elif decyzja ==10:
		funkcje.ilosc_czlonkow_spotkan_stowarzyszenia("Czlonek");
		zarz_stowarzyszenie();
	elif decyzja == 11:
		glowne_menu();
	else:
		print("Podaj poprawna opcje\n");
		zarz_stowarzyszenie();


# ZARZADZANIE SPOTKANIEM
def zarz_spotkanie():
	print("\nMENU SPOTKAN");
	print("1.Stworz spotkanie");
	print("2.Edytuj istniejace spotkanie");
	print("3.Usun spotkanie");
	print("4.Wypisz wszystkie spotkania");
	print("5.Pokaz spotkania ktore sie odbyly");
	print("6.Pokaz spotkania ktore sie odbeda");
	print("7.Powrot do glownego menu");
	decyzja = int(raw_input("Wybierz co chcesz zrobic\n"));

	if decyzja == 1:  # tworzenie nowych spotkan
		funkcje.dodawanie_spotkania_do_bazy();
		zarz_spotkanie();
	elif decyzja == 2:
		funkcje.edycja_spotkania();
		zarz_spotkanie();
	elif decyzja == 3:  # usuwanie spotkan
		funkcje.usun_rekord_z_bazy("Spotkanie");
		zarz_spotkanie();
	elif decyzja == 4:
		funkcje.wypisywanie_z_bazy("Spotkanie");
		zarz_spotkanie();
	elif decyzja == 5:
		funkcje.starespotkania();
		zarz_spotkanie();
	elif decyzja == 6:
		funkcje.nowespotkania();
		zarz_spotkanie();
	elif decyzja == 7:
		glowne_menu();
	else:
		print("Podaj poprawna opcje\n");
		zarz_spotkanie();

def zarz_salami():
	print("\nMENU SAL");
	print("1.Dodaj sale");
	print("2.Usun sale");
	print("3.Wypisz wszystkie sale");
	print("4.Powrot do glownego menu");
	decyzja = int(raw_input("Wybierz co chcesz zrobic\n"));
	if decyzja == 1:
		funkcje.dodaj_sale();
		zarz_salami();
	elif decyzja == 2:
		funkcje.usun_rekord_z_bazy("Sala");
		zarz_salami();
	elif decyzja == 3:
		funkcje.wypisywanie_z_bazy("Sala");
		zarz_salami();
	elif decyzja == 4:
		glowne_menu();
	else:
		print("Podaj poprawna opcje\n");
		zarz_salami();

# WYSWIETLENIE GLOWNEGO MENU
def glowne_menu():
	print("\nMENU GLOWNE");
	print("1.Zarzadzanie czlonkami");
	print("2.Zarzadzanie stowarzyszeniami");
	print("3.Zarzadzanie spotkaniami");
	print("4.Zarzadzanie salami");
	print("5.Statystyki klubu");
	print("6.Zamknij program");
	decyzja = int(raw_input("Wybierz co chcesz zrobic\n"));

	if decyzja == 1:
		zarz_czlonkami();
	elif decyzja == 2:
		zarz_stowarzyszenie();
	elif decyzja == 3:
		zarz_spotkanie();
	elif decyzja == 4:
		zarz_salami();
	elif decyzja == 5:
		funkcje.statystyki();
	elif decyzja == 6:
		sys.exit();
	else:
		print("Podaj poprawna opcje\n");
		glowne_menu();


# --------------------GLOWNA CZESC PROGRAMU-----------------------------------
glowne_menu();