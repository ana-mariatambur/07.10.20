"""Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la
începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să
realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi
iepuri sunt în crescătorie. """
l=int(input("numarul de iepuri la inceput de saptamana:"))
m=int(input("numarul de iepuri morti:"))
n=int(input("numarul de iepuri nascuti:"))
total=l-m+n
print("la sfarsitul acestei luni in crescatorie sunt",total,"iepuri")
