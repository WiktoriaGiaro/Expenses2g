from datetime import datetime


class Wydatek:
    def __init__(self, nazwa, kwota, data, typ="t"):
        self.kwota=kwota
        self.data = datetime.strptime(data, '%Y-%m-%d')
        self.typ=typ
        self.nazwa=nazwa
    def __str__(self):
        return " ".join([self.nazwa, str(self.kwota), self.data.__str__(), self.typ])
    def __repr__(self):
        return " ".join([self.nazwa, str(self.kwota), self.data.__str__(), self.typ,"\n"])
class Lista_wydatkow:
    def __init__(self):
        self.lista=list()
    def dodaj(self, wydatek):
        self.lista.append(wydatek)
    def __str__(self):
        tmp="*"*50+"\nLista wydatków\n"
        for w in self.lista:
            tmp=tmp+w.__str__()+"\n"
        return tmp
    def wyswietl_od_daty(self, data):
        data_graniczna=datetime.strptime(data, '%Y-%m-%d')
        for w in self.lista:
            if w.data>data_graniczna:
                print(w)
    def wyswietl_od_typu(self, typ):
        for w in self.lista:
            if w.typ==typ:
                print(w)
    def wyswietl_od_daty_i_typu(self,typ,data):
        data_graniczna = datetime.strptime(data, '%Y-%m-%d')
        for w in self.lista:
            if w.typ==typ and w.data>data_graniczna:
                print(w)
    def wyswietl_od_kwoty(self,kwota_min=0.0,kwota_max=1e6):
        for w in self.lista:
            if w.kwota>=kwota_min and w.kwota<=kwota_max:
                print(w)
    def sortuj_od_kwoty(self,reverse_=False):
        self.lista.sort(key=lambda x: x.kwota, reverse=reverse_)
        print(self.lista)
class Menu_And_Saving(Lista_wydatkow):
    def zapisz_wydatek(self):
        file1=open("wydatki.txt", "a+")
        file1.write(str(lw))
    def Przegladaj_wydatek(self):
        file1=open("wydatki.txt", "r+")
        print(file1.read())
    def display_menu(self):
        print("1 - Dodaj wydatek")
        print("2 - Przeglądaj wydatki")
        print("3 - Wyświetl od...")
        print("4 - Sortuj od kwoty")
        print("5 - Zakończ program")
        while True:
            choice=int(input())
            if choice==1:
                lw.dodaj(Wydatek(input("Co kupiłeś?: "), int(input("Ile wydałeś?: ")), "2020-06-29", typ=input("Towar czy usluga?: ")))
                self.zapisz_wydatek()
                print(lw)
                input("Wciśnij enter aby kontynuować")
                self.display_menu()
            elif choice==2:
                self.Przegladaj_wydatek()
                input("Wciśnij enter aby kontynuować")
                self.display_menu()
            elif choice==3:
                print("d - od daty")
                print("t - od typu")
                print("dt - od daty i typu")
                print("k - od kwoty")
                choice=input()
                if choice=="d":
                    lw.wyswietl_od_daty(data="2019-09-01")
                    input("Wciśnij enter aby kontynuować")
                    self.display_menu()
                elif choice=="t":
                    lw.wyswietl_od_typu(typ="t")
                    input("Wciśnij enter aby kontynuować")
                    self.display_menu()
                elif choice=="dt":
                    lw.wyswietl_od_daty_i_typu(typ="t", data="2019-09-01")
                    input("Wciśnij enter aby kontynuować")
                    self.display_menu()
                elif choice=="k":
                    lw.wyswietl_od_kwoty(kwota_min=50, kwota_max=100)
                    input("Wciśnij enter aby kontynuować")
                    self.display_menu()
            elif choice==4:
                lw.sortuj_od_kwoty()
                input("Wciśnij enter aby kontynuować")
                self.display_menu()
            elif choice==5:
                print("Do zobaczenia :)")
            break

lw=Lista_wydatkow()
menu=Menu_And_Saving()
menu.display_menu()

