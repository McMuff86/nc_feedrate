import math

#NC Vorschub Rechenprogramm, zum berechnen von Vorschüben und Drehzahlen auf einer NC Maschine

#Math Functions
def calc_vf():
    '''calculate vf -> vf = n * z * fz'''
    try:
        print("\nBerechnen der Vorschubgeschwindigkeit(vf) in mm/min:\n")
        fz = float(input("Vorschub pro Zahn(vf) angeben: "))
        n = int(input("Drehzahl(n) angeben: "))
        z = int(input("Zähnezahl(z) angeben: "))
        vf = n * z * fz
        print("\nDie Vorschubgeschwindigkeit betraegt " + str(vf) + " mm/min\n")
    except ValueError:
        print("Kein gültiger Wert...")

def calc_fz():
    '''calculate fz -> fz = vf / (n*z)'''
    try:
        print("\nBerechnen des Zahnvorschubes (fz) pro Umdrehung:\n")
        vf = float(input("Vorschubgeschwindigkeit angeben? "))
        n = int(input("Drehzahl angeben "))
        z = int(input("Zähnezahl angeben "))
        fz = vf / (n*z)
        print("\nDer Vorschub pro Zahn betraegt " +str(fz) + " mm/Zahn\n")
    except ValueError:
        print("Kein gültiger Wert...")

def calc_n():
    try:
        print("\nBerechnen der Spindeldrehzahl(n) in min-1:\n")
        vc = float(input("Schnittgeschwindigkeit (vc) in m/min angeben: "))
        d_eff = float(input("effektiver Durchmesser des Fräsers in mm angeben: "))
        n = (vc*1000)/(math.pi*d_eff)
        print("\nDie Spindeldrehzahl bertaegt " + str(n) + " min-1\n")
    except ValueError:
        print("Kein gültiger Wert...")


def calc_vc():
    try:
        print("\nBerechnen der Schnittgeschwindigkeit(vc) in m/min:\n")
        n = int(input("Drehzahl (n) in min-1 angeben: "))
        d_eff = float(input("effektiver Durchmesser des Fräsers in mm angeben: "))
        vc = (math.pi*d_eff*n)/1000
        print("\nDie Schnittgeschwindigkeit bertaegt " + str(vc) + " m/min\n")
    except ValueError:
        print("Kein gültiger Wert...")

set_flag = True


while set_flag:
    print("\n" + 25*"=" + " McMuff's NC Vorschubrechner " + 25*"=" + "\n")
    calc_value = int(input("Was soll berechnet werden?\n\n 1. Vorschubgeschwindigkeit(vf)\n 2. Zahnvorschub(fz)\n 3. Spindeldrehzahl(n)\n 4. Schnittgeschwindigkeit(vc)\n 5. Programm beenden\n\n"))
    
    if calc_value == 5:
        print("Programm wird beendet....")
        set_flag = False

    elif calc_value == 1:
        calc_vf()

    elif calc_value == 2:
        calc_fz()

    elif calc_value == 3:
        calc_n()
    
    else:
        calc_vc()

    # calc_vf(18000, 2, 0.1)
    # calc_n(150, 12)

