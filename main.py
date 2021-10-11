def get_temp(T,From,To):
    # Afiseaza temperatura dintr-o scara data intr-o alta scara data
    # Input: temperartura, scara data, scara ceurta
    # Output: temperatura in scara ceruta

    if From == "C" and To == "K":
        tc = T + 273.15
    else:
        if From == "K" and To == "C":
            tc = T - 273.15
        elif From == "C" and To == "F":
            tc = (T * 1.8) + 32
        elif From == "F" and To == "C":
            tc = (T - 32) * (5 / 9)
        elif From == "K" and To == "F":
            tc = (T - 273.15) * (9 / 5) + 32
        elif From == "F" and To == "K":
            tc = (T - 32) * (5 / 9) + 273.15
    return round(tc, 2)


def test_get_temp():
    assert (get_temp(300,"K","C") == 26.85)
    assert (get_temp(25,"C","K") == 298.15)
    assert (get_temp(100,"F","C") == 37.78)
    assert (get_temp(50,"C","F") == 122.0)
    assert (get_temp(25,"K","F") == -414.67)
    assert (get_temp(30,"F","K") == 272.04)

def get_cmmmc(list):
# Afiseaza cel mai mic multiplu comun pentru n numere
#Input: lista de numere ( list)
#Output: cmmmc (int)
    cmmmc=list[0]
    for i in range (1,len(list)):
        cmmmc1=cmmmc
        clist=list[i]
        while cmmmc1!=clist:
            if cmmmc1 >clist:
                cmmmc1=cmmmc1-clist
            else:
                clist=clist-cmmmc1
        cmmmc=cmmmc*(list[i]//clist)
    return cmmmc

def test_get_cmmmc():
    list = [1, 3, 5, 6, 2]
    assert (get_cmmmc(list) == 30)  # true
    list1 = [2, 3, 4]
    assert (get_cmmmc(list1) == 12)  # true

def is_palindrome(n):
    #Descriere: Determina daca un numar este palindrom
    #Input: Un numar natural x
    #Output: True/False
    if n<10:
        return n
    else:
        n1=0
        a=n
        while n>0:
            uc=n%10
            n1=n1*10+uc
            n=n//10
    if n1==a:
        return True
    else:
        return False

def test_is_palindrome():
    assert(is_palindrome(121)==True)
    assert(is_palindrome(9)==9)
    assert(is_palindrome(243)==False)

def run():
    test_get_cmmmc()
    test_get_temp()
    test_is_palindrome()
    ans = True
    while ans:
        print("1.Sa se afiseze cmmmc:")
        print("2.Sa se afiseze temperatura dintr-o scara data intr-o alta scara data")
        print("3.Sa se determine daca un numar este palindrom")
        print("4.Iesire")
        optiune = input("Dati optiunea:")
        if optiune == "1":
            n = int(input("Dati numarul de valori:"))
            list = []
            for i in range(0, n):
                nr = int(input("Nr" + str(i + 1) + ":"))
                list.append(nr)
            print(get_cmmmc(list))
        elif optiune == "2":
            T = float(input("T: "))
            From=input("From: ")
            To=input("To: ")
            print(get_temp(T,From,To))
        elif optiune == "3":
            nr = int(input("Dati numarul:"))
            print(is_palindrome(nr))
        elif optiune=="4":
            ans=False
        else:
            print("Optiune gresita!Reincercati!")


run()