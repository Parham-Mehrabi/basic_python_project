import time
class final:
    def menu(self):
        return """
1- moadele_dovom
2- histogram
3- mashin_hesab
4- ashkal_hendese       
5- tekrarehoroof_Fedition     
6- mobadele_orc_chr       
7- ghalb_yab        
8- bozorg_koochikkon       
9- mosbat_yab
10- copykon      
"""
        #***********************************************************1***********************************************************#
    def moadele_dovom(self):
        print(' \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ^^^ in barname dovomin modale class ro barmigardoone ^^^', end='')
        time.sleep(3)
        switch=1
        while switch:
            a=0
            d=0
            jamiat=1
            while jamiat==1:
                try:
                    tedad=(int(input('chandnafarid? ')))
                    jamiat=2
                except ValueError:
                    print('tedad nafarat ra be adad vared konid ! ! !')
            while tedad: 
                try:
                    tedad-= 1
                    v= float(input('moadelet chande? '))
                    if v>a:
                        d=a
                        a=v
                    elif v<a:
                        if d<v:
                            d=v
                    if v>d :
                        v=d  
                except ValueError:
                    print('moadel ha ra be adad vared konid ! ! !')
                    tedad+=1
            print (d)
            sr=input('baraye restart r va baraye bazgasht be menu asli enter ra beznid  :')
            if sr=='r' or sr=='R':
                pass
            else:
                switch=0
                t=5
                while t:
                    print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
                    t-=1
                    time.sleep(1)
        #***********************************************************1***********************************************************#
        #***********************************************************2***********************************************************#
    
    def histogram(self):
        print(' \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ^^^ in barname histogram listi static ro barmigardoone ^^^', end='\r')
        time.sleep(3)
        switch=1
        while switch:
            asgar='anghezi'
            fehrest = [1,3,asgar,5,7,8,'a',9,10.4,22.6]
            for s in fehrest :
                try:
                    z=int(s)
                    while z:
                        z-=1
                        print('* ',end=' ')
                    else:
                        print(s,'(',int(s),")")
                except ValueError:
                    print('list bayad fght havi adad bashad',f'*"{s}" ghabele ghabool nist ! ! !*')
            sr=input('baraye restart r va baraye bazgasht be menu asli enter ra beznid  :')
            if sr=='r' or sr=='R':
                pass
            else:
                switch=0
                t=5
                while t:
                    print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
                    t-=1
                    time.sleep(1)
        #***********************************************************2***********************************************************#
        #***********************************************************3***********************************************************#
    def mashin_hesab(self):
        print(' \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ^^^ iek mashin hesab sadeh (+ / - *) ba modiriate khata ^^^')
        time.sleep(3)
        switch=1
        while switch:
            t=t2=1
            while t==1:
                try:
                    a1=float(input('adadi vared konid (#1) : '))
                    t=2
                except ValueError:
                    print('add khali vared konid na chiz dg')
            alaem=['/','*','+','-']
            s=input('amal riazi ee ra vared konid : ')
            while s not in alaem:
                s=input('amal riazi ee ra vared konid (/,*,-,+) : ')
            while t2==1:
                try:
                    a2=float(input('adadi vared konid (#2) : '))
                    t2=2
                except ValueError:
                    print('add khali vared konid na chiz dg')
            if s=="/":
                j=a1/a2
                print(f'{a1} / {a2} = {j}')
            if s=="+":
                j=a1+a2
                print(f'{a1} + {a2} = {j}')
            if s=="*":
                j=a1*a2
                print(f'{a1} * {a2} = {j}')
            if s=="-": 
                j=a1-a2
                print(f'{a1} - {a2} = {j}')
            sr=input('baraye restart r va baraye bazgasht be menu asli enter ra beznid  :')
            if sr=='r' or sr=='R':
                pass
            else:
                switch=0
                t=5
                while t:
                    print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
                    t-=1
                    time.sleep(1)
        #***********************************************************3***********************************************************#
        #***********************************************************4***********************************************************#
    def hendese(self):
        print(' \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ^^^ mohasebe mohit va masahate moraba mostatil va dayere ^^^')
        time.sleep(3)
        pi=3.14
        c=1
        r=1
        while r:
            while c==1:
                v=input('choose a geometric shape : ')
                m1='circle'
                m2='square'
                m3='rectangle'
                s=v.lower()
                if s==m1:
                    t=1
                    while t==1:
                        try:
                            r=float(input('enter the radios : '))
                            t+=1
                        except ValueError:
                            print('shoa ra be adad vared konid ! ! !')
                    v=(pi)*r*r
                    s=(pi)*r*2
                    print('the square Perimeter is %.3f and the area is %.3f'% (s,v))
                    c+=1
                elif s==m2:
                    t=1
                    while t==1:
                        try:
                            x=float(input('enter the side length : '))
                            t+=1
                        except ValueError:
                            print('toole zel ro be adad vared konid ! ! !')
                    ss=4*x
                    vs=x*x
                    print('the square Perimeter is {} and the area is {}'.format(ss,vs))
                    c+=1
                elif s==m3:
                    t=1
                    while t==1:
                        try:
                            l=(float(input('enter the length : ')))
                            t+=1
                        except ValueError:
                            print('tool ra be adad vared konid ! ! !')
                    t=1
                    while t==1:
                        try:
                            w=(float(input('enter the width : ')))
                            t+=1
                        except ValueError:
                            print('arz ra be adad vared konid ! ! !')
                    sm=2*(w+l)
                    vm=(w*l)
                    print('the rectangle Perimeter is {} and the area is {}'.format(sm,vm))
                    c+=1
                else:
                    print(f'*** {v} *** is not defined', '\n', 'here is your options : "circle" "square" "Rectangle"')
            v2=input('type "restart"  to continue or press enter to end: ')
            s2=v2.lower()
            if s2=='restart'or s2=='R':
                c=1
            else:
                r=0
        t=5
        while t:
            print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
            t-=1
            time.sleep(1)
        #***********************************************************4***********************************************************#
        #***********************************************************5***********************************************************#
    def takrarshomar(self):
        print(' \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ^^^ shomareshgare horoofe sedadar va letter "F" dar jomle(F ba try except) ^^^')
        time.sleep(3)
        switch=1
        while switch:
            z=input('iki jomle vared konid : ')
            ac=ec=uc=ic=oc=0
            c3=0
            c=c2=1
            class ErrorF(Exception):
                pass
            for a in z:
                c3+=1
                try:
                    if a=="a"or a=='A':
                        ac+=1
                    elif a=="e"or a=='E':
                        ec+=1
                    elif a=="u"or a=='U':
                        uc+=1
                    elif a=="i"or a=='I':
                        ic+=1
                    elif a=="o"or a=='O':
                        oc+=1
                    elif a=='F':
                        raise ValueError
                    elif a=='f':
                        raise ErrorF
                except ValueError:
                    print(f'{c} "F" peyda kardim dar charecter {c3} :O ')
                    c+=1
                except ErrorF:
                    print(f'{c2} "f" peyda kardim dar charecter {c3}  ^_^ ')
                    c2+=1
            print(f'a = {ac}',f'e = {ec}',f'u = {uc}',f'i = {ic}',f'o = {oc}',sep='\n')
            sr=input('baraye restart r va baraye bazgasht be menu asli enter ra beznid  :')
            if sr=='r' or sr=='R':
                pass
            else:
                switch=0
                t=5
                while t:
                    print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
                    t-=1
                    time.sleep(1)
        #***********************************************************5***********************************************************#
        #***********************************************************6***********************************************************#
    def mobadele_ascii(self):
        switch=1
        while switch:       #baraye restart rahat tar barname
            def sep(r):
                for b in r:
                    c=1
                    a=ord(b)
                    if a >=48 and a<=57:        #check kardan noe vooroodi
                        pass
                    else:
                        c+=1
                if c!=1:
                    #voroodi adad nist
                    def my_ord():     
                        for p in r:
                            print('/'+str(ord(p)),end='') #str kardam ke ba '/' jam beshe
                    my_ord()
                    print()
                if c==1:
                    #voroodi adade
                    def my_chr():
                        t=len(r)
                        t2=t-3
                        i=0
                        if t%2==0:                #akharesh tak nemiofte
                            while t:
                                p=r[i]+r[i+1]
                                t-=2
                                i+=2
                                print(chr(int(p)),end='')
                            print()
                        else:                     #tahesh mikhad iki tak biofte
                            while t2:
                                if t>3:           #agar reshte fard kamtar az 3 charecter bashe
                                    p=r[i]+r[i+1]
                                    t2-=2
                                    i+=2
                                    print(chr(int(p)),end='')
                            p2=r[-3]+r[-2]+r[-1]               #3 taye akhare reshte fard
                            print(chr(int(p2)))
                    my_chr()
            v=input('vooroodi bede ! ! ! ')
            sep(v)
            restart=input('*********************baraye restart r befrest vagarna enter bezan********************* : ')
            if restart =='r' or restart=='R':
                pass
            else:              # baraye etmame barname
                switch=0
        t=5
        while t:
            print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
            t-=1
            time.sleep(1)
        #***********************************************************6***********************************************************#
        #***********************************************************7***********************************************************#
    def ghalb_yab(self):
        switch=1
        while switch:
            a=123
            t=("mmd",'arra','doorood','achbar','alila','asgaragsa','118898811',a,'goorbeh/hebroog')
            def checkkon(*aykres):
                for a in aykres:
                    gozar=1
                    i=-1
                    try:
                        for a2 in a:
                            i+=1
                    except TypeError:
                        print('ERROR : faghat string dakhel list bezarid ! ! !')
                        gozar+=1
                    mi=0
                    v=i/2
                    p=1
                    if gozar==1:
                        while a[i]==a[mi] and p==1:
                            i-=1
                            mi+=1
                            if mi>=v:
                                print(a)
                                p+=1
                        else:
                            p+=1
            checkkon(*t)
            sr=input('baraye restart r va baraye bazgasht be menu asli enter ra beznid  :')
            if sr=='r' or sr=='R':
                pass
            else:
                switch=0
                t=5
                while t:
                    print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
                    t-=1
                    time.sleep(1)

        #***********************************************************7***********************************************************#
        #***********************************************************8***********************************************************#
    def chapekon(self):
        switch=1
        while switch:
            def koochikkon(o): #tabe koochik konande
                o+=32
                z=chr(o)
                return z
            def goondakon(o): #tabe bozorg konande
                o-=32
                z=chr(o)
                return z
            class NaHarfError(Exception):
                pass
            t=1
            kh=''   #khooroooji
            while t==1:
                t=1
                s=0
                try:
                    v=input('reshte ee az horoof vared konid: ')
                    for a0 in v:
                        t=1
                        s+=1
                        o=ord(a0)
                        if o>=65 and o<=90 or a0==' ':
                            t+=1
                        elif o>=97 and o<=122:
                            t+=1
                        elif o<65 or o>122 or o in range(91,97):  
                            raise NaHarfError
                except NaHarfError:
            
                    print(f'*******        vojoode charecter na alphabet dar charecter {s}om ! ! !        *******')
                    print('inbar reshte ee tamaman az horoof vared konid')
                    t=1
            for a in v:
                o=ord(a)
                if a==' ':
                    kh=kh+' '
                if o>=65 and o<=90:                                 #agar bozorg bood bere too koochik konande
                    kh=kh+koochikkon(o)
                elif o>=97 and o<=122:
                    kh=kh+goondakon(o)                             #agar bozorg bood bere too bozorg konande


            print(kh)
            sr=input('baraye restart r va baraye bazgasht be menu asli enter ra beznid  :')
            if sr=='r' or sr=='R':
                pass
            else:
                switch=0
                t=5
                while t:
                    print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
                    t-=1
                    time.sleep(1)
        #***********************************************************8***********************************************************#
        #***********************************************************9***********************************************************#
    def mosbat_lumbda(self):
        switch=1
        while switch:
            l=[12,-42,533,55,123,-234,-556,-23444,235,'salam',7,-12,2223,21,1,-1]
            j=1
            print('***********************************************************************************************************')
            for a in l:
                if type(a) is not int:
                    print(f'ozve {j} list adad nabood ke delete shod !!! ')
                    print('list bayad faghat havi adad bashe ! ! ! ')
                    print()
                    l.pop(j-1)
                    j+=1
                else:
                    j+=1
            positives=list(filter(lambda x : x>0,l))
            print(f'mosbat ha : {positives} ')
            sr=input('baraye restart r va baraye bazgasht be menu asli enter ra beznid  :')
            if sr=='r' or sr=='R':
                pass
            else:
                switch=0
                t=5
                while t:
                    print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
                    t-=1
                    time.sleep(1)
        #***********************************************************9***********************************************************#
        #***********************************************************10**********************************************************#
    def copy_kon(self):
        switch=1
        while switch:
            c=c2=1
            while c==1:
                try:
                    z=input('masire va name file maabda: \n')
                    with open(f'{z}','rt+',encoding='utf-8') as f:
                        p=f.read()
                        c=2
                except PermissionError:
                    print('masir kafi nist khode file ham moarefi konid ! ! !')
                except FileNotFoundError:
                    print('in file dar in adress peyda nashod dobare adress bedin ! ! !')
                except UnicodeDecodeError:
                    try:
                        with open(f'{z}','rb+') as f:
                            p=f.read()
                            c=2
                    except FileNotFoundError:
                        print('in file dar in adress peyda nashod dobare adress bedin ! ! !')
                    except OSError:
                        print('dari bad eshtebah mizani')
            while c2==1:
                try:
                    z2=input('masire file maghsad: \n')
                    z3=input('name file maghsad (ba format): ')
                    try :
                        with open(f'{z2}/{z3}','wt+',encoding='utf-8')as f2:
                            f2.write(p)
                            c2=2
                    except FileNotFoundError:
                        print('**************************')
                        print('masire file maghsad vojood nadare ! ! !')
                except UnicodeDecodeError:
                    try:
                        with open(f'{z2}/{z3}','wb+')as f3:
                            f3.write(p)
                            c2=2
                    except FileNotFoundError:
                        print('**************************')
                        print('masire file maghsad vojood nadare ! ! !')        
                except TypeError:
                    try:
                        with open(f'{z2}/{z3}','wb+')as f3:
                            f3.write(p)
                            c2=2
                    except FileNotFoundError:
                        print('**************************')
                        print('masire file maghsad vojood nadare ! ! !') 
                except OSError:
                        print('dari bad eshtebah mizani')
            sr=input('baraye restart r va baraye bazgasht be menu asli enter ra beznid  :')
            if sr=='r' or sr=='R':
                pass
            else:
                switch=0
                t=5
                while t:
                    print(f'  bargasht be menu asli dar {t} sanie dg',end='\r')
                    t-=1
                    time.sleep(1)            
                    #***********************************************************10**********************************************************#
f = final()
while True:
    print(f.menu())
    p = input("choose a number of program: ")
    if p == "end":
        exit()

    if p == "1":
        f.moadele_dovom()
    elif p == "2":
        f.histogram()
    elif p == "3":
        f.mashin_hesab()
    elif p == "4":
        f.hendese()
    elif p=='5':
        f.takrarshomar()
    elif p=='6':
        f.mobadele_ascii()
    elif p=='7':
        f.ghalb_yab()
    elif p=='8':
        f.chapekon()
    elif p=='9':
        f.mosbat_lumbda()
    elif p=='10':
        f.copy_kon()
    else:
        print("داداش اشتباه زدی دوباره تلاش کن")