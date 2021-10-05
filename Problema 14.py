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
    list=[1,3,5,6,2]
    assert (get_cmmmc(list)==30) #true
    list1=[2,3,4]
    assert (get_cmmmc(list1)==12) #true


def run():
    test_get_cmmmc()
    n = int(input("Dati numarul de valori:"))
    list = []
    for i in range(0, n):
        nr = int(input("Nr"+str(i+1)+":"))
        list.append(nr)
    print(get_cmmmc(list))
run()
