def get_temp(t):
#Afiseaza temperatura dintr-o scara data intr-o alta scara data
#Input: temperartura, scara data, scara ceurta
#Output: temperatura in scara ceruta 
    grade=int(t[:-2])
    scaraD=t[-2]
    scaraC=t[-1]
    if scaraD=="C" and scaraC=="K":
        tc=grade+273.15
    else:
        if scaraD=="K" and scaraC=="C":
            tc=grade-273.15
        elif scaraD=="C" and scaraC=="F":
            tc= (grade*1.8)+32
        elif scaraD=="F" and scaraC=="C":
            tc=(grade-32)*(5/9)
        elif scaraD=="K" and scaraC=="F":
            tc=(grade-273.15)*(9/5)+32
        elif scaraD=="F" and scaraC=="K":
            tc=(grade-32)*(5/9) +273.15
    return round(tc,2)
def test_get_temp():
    assert(get_temp('300KC')==26.85)
    assert(get_temp('25CK')==298.15)
    assert(get_temp('100FC')==37.78)
    assert(get_temp('50CF')==122.0)
    assert(get_temp('25KF')==-414.67)
    assert(get_temp('30FK')==272.04)
def run():
    test_get_temp()
    t=input("t= ")
    print(get_temp(t))
run()
      
    

  
