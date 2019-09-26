
import time
print("                                        Welcome in UniverseSandbox!"'\n')
time.sleep(0)

class Galaktyka():




    def __init__(self,nazwa,masa,temp,pr_orb):
        self.nazwa = nazwa
        self.masa = masa
        self.temp = temp
        self.pr_orb = pr_orb


    def fullname(self):
        print(":Name: Mass(as moon mass) : Temperature C : Rotational Period:")
        return f'{self.nazwa} : {self.masa} : {self.temp} : {self.pr_orb}'



    def zmiana_masy(self):
        a1 = input("Manual(M) mass change or Auto(A)?: ")
        if a1 is 'A':
            print("Set the mass change'\n'")
            m = input("For how many percent do you want to change mass?[1:5%/2:25%/3:50%]: ")
            if m is '1':
                raise_masa = 1.05
            elif m is '2':
                raise_masa = 1.35
            elif m is '3':
                raise_masa = 1.50
            a = input("[Mass]Increase?(I) Decrease?(D): ")
            if a is "I":
                self.masa = int(self.masa * raise_masa)
            elif a is "D":
                self.masa = int(self.masa / raise_masa)
            else:
                exit()
        elif a1 is 'M':
            a2 = int(input("Set mass: "))
            self.masa = a2




    def zmiana_temp(self):
        a1 = input("Manual(M) change or Auto(A)?: ")
        if a1 is 'A':
            print("Set the temperature change'\n'")
            m = input("For how many percent do you want to change temp.?[1:5%/2:25%/3:50%]: ")
            if m is '1':
                raise_temp = 1.05
            elif m is '2':
                raise_temp = 1.25
            elif m is '3':
                raise_temp = 1.50
            a = input("[Temp.]Increase?(I) Decrease?(D): ")
            if a is "I":
                self.temp = int(self.temp * raise_temp)
            elif a is "D":
                self.temp = int(self.temp / raise_temp)
            else:
                exit()
        elif a1 is 'M':
            a2 = int(input("Set temperature: "))
            self.temp = a2

    def control(self):
        if self.masa >= 7500000:
            self.temp = int(self.temp + 2000)






#np - masa planety , x1,x2,x3.. - wartosci
def planet_engine_M(np,x0,x1,x3,x4,x5,x6):
    if np < x0:
        print("The planet decreases""\n")
    if np > x1 and np < x3:
        print("The planet increases" "\n")
    if np >= x3:
        print("Red dwarf" "\n")
    if np > x4:
        print("Sun" "\n")
    if np > x5:
        print("Sun Nova" "\n")
    if np > x6:
        print("Nova" "\n")
        print("What have you done! you destroyed everything!! restart")
        time.sleep(5)
        exit()

def planet_engine_T(np,x1,x2,x3,x4,x5,x6):
    if np < x1:
        print("The planet cools" "\n")
    if np < x2:
        print("The planet Freezes"'\n')
    if np > x3:
        print("The planet is warming up" "\n")
    if np > x4:
        print("The water evaporates" "\n")
    if np > x5:
        print(" Only Gas and Solid" "\n")
    if np > x6:
        print("Iron is melting" "\n")


slonce = Galaktyka('Sun',27200980,5575,23.05)
merkury = Galaktyka('Mercury',4,166,50.12)
wenus = Galaktyka('Venus',66,613,34.9)
ziemia = Galaktyka('Earth',81,15.5,29.3)
mars = Galaktyka('Mars',9,-56.6,12.5)
jowisz = Galaktyka('Jupiter',25828,-166,22.5)
saturn = Galaktyka('Saturn',7733,-193,10)
uran = Galaktyka('Uranus',1181,-216,6.76)
neptun = Galaktyka('Neptune',1394,-226,5.47)



class Material(Galaktyka):
    def __init__(self,nazwa,iron,silicate,water,organics,hydrogen):
        self.nazwa = nazwa
        self.iron = iron
        self.silicate = silicate
        self.water = water
        self.organics = organics
        self.hydrogen = hydrogen
        #super().__init__(nazwa,masa,temp,pr_orb)

    def fullname1(self):
        print(":Name: Iron: Silicate: Water: Organics: Hydrogen")
        return f'{self.nazwa} : {self.iron} : {self.silicate} : {self.water} : {self.organics} : {self.hydrogen}'


def material_engine(x1,x2,x3,x4,x5,m1):
    if x1 > 0:
        if m1 >= 1500:
            print("Iron = Plasma")
        if m1 < 1500:
            print("Iron = Solid")
        if m1 > 2500:
            print("Iron = Gas")
    if x2 > 0:
        if m1 < 1400:
            print("Silicate = Solid")
        if m1 >= 1400:
            print("Silicate = Plasma")
        if m1 > 2200:
            print("Silicate = Gas")
    if x3 > 0:
        if m1 <= 0:
            print("Water = Solid")
        if m1 > 0 and m1 < 100:
            print("Water = Liquid")
        if m1 >=100:
            print("Water = Gas")
    if x4 > 0:
        if m1 < 0 or m1 < 400:
            print("Organics = Solid")
        if m1 > 400:
            print("Organics = Gas")
    if x5 > 0:
        if m1 <= -240:
            print("Hydrogen = Solid")
        if m1 > -230:
            print("hydrogen = Gas")






mat_1 = Material('Sun',0,0,0,0,100)
mat_2 = Material('Mercury',46,54,0,0,0)
mat_3 = Material('Venus',20,80,0,0,0)
mat_4 = Material('Earth',24,75,0.7,0.3,0)
mat_5 = Material('Mars',10,90,0,0,0)
mat_6 = Material('Jupiter',0,2,0,0,98)
mat_7 = Material('Saturn',0.3,2,0.7,0,97)
mat_8 = Material('Uranus',4.67,14,74.7,0,6.67)
mat_9 = Material('Neptune',4.78,14.4,74.5,0,6.32)




def engine():
    q = input("What you want to do? Change mass?,Temp. or Planet Composition?(M/T/H) Exit(W): ")
    if q is 'M':
        r = input("Which planet? Give me the first two letters: "  )
        print('\n')
        if r == 'su':
            print(slonce.fullname())
            slonce.zmiana_masy()
            print(slonce.masa)
            slonce.control()
            planet_engine_M(slonce.masa,27200979,27200981,7500000,27200980,32000000,40000000)
        elif r == 'me':
            print(merkury.fullname())
            merkury.zmiana_masy()
            print(merkury.masa)
            merkury.control()
            planet_engine_M(merkury.masa,3,5,7500000,27200980,32000000,40000000)
        elif r == 've':
            print(wenus.fullname())
            wenus.zmiana_masy()
            print(wenus.masa)
            wenus.control()
            planet_engine_M(wenus.masa,65,67,7500000,27200980,32000000,40000000)
        elif r == 'ea':
            print(ziemia.fullname())
            ziemia.zmiana_masy()
            print(ziemia.masa)
            ziemia.control()
            planet_engine_M(ziemia.masa,80,82,7500000,27200980,32000000,40000000)
        elif r == 'ma':
            print(mars.fullname())
            mars.zmiana_masy()
            print(mars.masa)
            mars.control()
            planet_engine_M(mars.masa,8,10,7500000,27200980,32000000,40000000)
        elif r == 'ju':
            print(jowisz.fullname())
            jowisz.zmiana_masy()
            print(jowisz.masa)
            jowisz.control()
            planet_engine_M(jowisz.masa,25800,25830,7500000,27200980,32000000,40000000)
        elif r == 'sa':
            print(saturn.fullname())
            saturn.zmiana_masy()
            print(saturn.masa)
            saturn.control()
            planet_engine_M(saturn.masa,7732,7734,7500000,27200980,32000000,40000000)
        elif r == 'ur':
            print(uran.fullname())
            uran.zmiana_masy()
            print(uran.masa)
            uran.control()
            planet_engine_M(uran.masa,1180,1182,7500000,27200980,32000000,40000000)
        elif r == 'ne':
            print(neptun.fullname())
            neptun.zmiana_masy()
            print(neptun.masa)
            neptun.control()
            planet_engine_M(neptun.masa,1393,1395,7500000,27200980,32000000,40000000)
    elif q is 'T':
        x = input("Which planet? Give me the first two letters: ")
        print('\n')
        if x == 'su':
            print(slonce.fullname())
            slonce.zmiana_temp()
            print(slonce.temp)
        elif x == 'me':
            print(merkury.fullname())
            merkury.zmiana_temp()
            print(merkury.temp)
            planet_engine_T(merkury.temp,160,0,170,300,400,1500)
        elif x == 've':
            print(wenus.fullname())
            wenus.zmiana_temp()
            print(wenus.temp)
            planet_engine_T(wenus.temp,600,0,650,100,400,1500)
        elif x == 'ea':
            print(ziemia.fullname())
            ziemia.zmiana_temp()
            print(ziemia.temp)
            planet_engine_T(ziemia.temp,13,0,18,100,400,1500)
        elif x == 'ma':
            print(mars.fullname())
            mars.zmiana_temp()
            print(mars.temp)
            planet_engine_T(mars.temp,-60,0,-40,100,400,1500)
        elif x == 'ju':
            print(jowisz.fullname())
            jowisz.zmiana_temp()
            print(jowisz.temp)
            planet_engine_T(jowisz.temp,-170,0,-160,100,400,1500)
        elif x == 'sa':
            print(saturn.fullname())
            saturn.zmiana_temp()
            print(saturn.temp)
            planet_engine_T(saturn.temp,-200,0,-180,100,400,1500)
        elif x == 'ur':
            print(uran.fullname())
            uran.zmiana_temp()
            print(uran.temp)
            planet_engine_T(uran.temp,-220,0,-210,100,400,1500)
        elif x == 'ne':
            print(neptun.fullname())
            neptun.zmiana_temp()
            print(neptun.temp)
            planet_engine_T(neptun.temp,-230,0,-220,100,400,1500)
    elif q is 'H':
        x = input("Which planet? Give me the first two letters: ")
        print('\n')
        if x == 'su':
            print(mat_1.fullname1())
            material_engine(mat_1.iron,mat_1.silicate,mat_1.water,mat_1.organics,mat_1.hydrogen,slonce.temp)
        elif x == 'me':
            print(mat_2.fullname1())
            material_engine(mat_2.iron,mat_2.silicate,mat_2.water,mat_2.organics,mat_2.hydrogen,merkury.temp)
        elif x == 've':
            print(mat_3.fullname1())
            material_engine(mat_3.iron,mat_3.silicate,mat_3.water,mat_3.organics,mat_3.hydrogen,wenus.temp)
        elif x == 'ea':
            print(mat_4.fullname1())
            material_engine(mat_4.iron,mat_4.silicate,mat_4.water,mat_4.organics,mat_4.hydrogen,ziemia.temp)
        elif x == 'ma':
            print(mat_5.fullname1())
            material_engine(mat_5.iron,mat_5.silicate,mat_5.water,mat_5.organics,mat_5.hydrogen,mars.temp)
        elif x == 'ju':
            print(mat_6.fullname1())
            material_engine(mat_6.iron,mat_6.silicate,mat_6.water,mat_6.organics,mat_6.hydrogen,jowisz.temp)
        elif x == 'sa':
            print(mat_7.fullname1())
            material_engine(mat_7.iron,mat_7.silicate,mat_7.water,mat_7.organics,mat_7.hydrogen,saturn.temp)
        elif x == 'ur':
            print(mat_8.fullname1())
            material_engine(mat_8.iron,mat_8.silicate,mat_8.water,mat_8.organics,mat_8.hydrogen,uran.temp)
        elif x == 'ne':
            print(mat_9.fullname1())
            material_engine(mat_9.iron,mat_9.silicate,mat_9.water,mat_9.organics,mat_9.hydrogen,neptun.temp)
    elif q is 'W':
        exit()
    else:
        print("Enter the correct command ")

run_times = 0

for i in range(20):
    engine()
    run_times += 1
    #print(run_times)
