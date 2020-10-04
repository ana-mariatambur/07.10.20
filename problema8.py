"""Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
aceste cifre luate o singură dată."""
a=int(input("introduceti 1 numar:"))
b=int(input("introduceti 2 numar:"))
c=int(input("introduceti 3 numar:"))
print(str(a)+str(b)+str(c),str(a)+str(c)+str(b),str(b)+str(a)+str(c),str(b)+str(c)+str(a),str(c)+str(a)+str(b))
