print("*****Welcome*****")
print("     Employe Name             ||  Rate Per hour  ||  Over time Rate  ||")
print("[1] Bautista, Sheryl Ann S.   ||        75       ||        97        ||")
print("[2] Reyes, Sedney             ||        75       ||        97        ||")
print("[3] Santos, Alfredo Jr. F.    ||        75       ||        97        ||")
option1=input("""Do you want to continue?(Y/N)
 >>""").upper()
if option1=="Y":
    while True:
     option2=int(input("Enter Employe: "))
     if option2 ==1:
        month=input("Enter Month: ").upper()
        hour=int(input("Hour of work: "))
        over=int(input("Hour of Overtime: "))
        print("Dedaction")
        Ca=int(input("C/A: "))
        late=int(input("Mins of Late: "))
        rate=75
        rover=97
        rlate=2
        SSS=300
        Phealth=300
        amount1=rate*hour
        amount2=over*rover
        amount3=amount1+amount2
        amount4=amount3-SSS
        amount5=amount4-Phealth
        amount6=amount5-Ca
        amount7=rlate*late
        day=hour/8
        total=amount6-amount7
        print("*********************************")
        print("          ",month,"              ")
        print("  Bautista, Sheryl Ann S.")
        print("    Day: ",day)
        print("    Hours: ",hour)
        print("    Overtime: ",over)
        print("    Dedaction")
        print("    SSS: ",SSS)
        print("    PHealth: ",Phealth)
        print("    C/A: ",Ca)
        print("    Mins of Late: ",late)
        print("    Gross Pay: ",amount3)
        print("*********************************")
        print("     Total: ",total)
        option3=input("""Do you want to continue?(Y/N)
>>""").upper()
        if option3=="Y":
            pass
        else:
            print("Than you for using the app")
            pass
            break
     elif option2 ==2:
        month=input("Enter Month: ").upper()
        hour=int(input("Hour of work: "))
        over=int(input("Hour of Overtime: "))
        print("Dedaction")
        Ca=int(input("C/A: "))
        late=int(input("Mins of Late: "))
        rate=75
        rover=97
        rlate=2
        SSS=300
        Phealth=300
        amount1=rate*hour
        amount2=over*rover
        amount3=amount1+amount2
        amount4=amount3-SSS
        amount5=amount4-Phealth
        amount6=amount5-Ca
        amount7=rlate*late
        day=hour/8
        total=amount6-amount7
        print("*********************************")
        print("          ",month,"              ")
        print("  Reyes, Sedney    ")
        print("    Day: ",day)
        print("    Hours: ",hour)
        print("    Overtime: ",over)
        print("    Dedaction")
        print("    SSS: ",SSS)
        print("    PHealth: ",Phealth)
        print("    C/A: ",Ca)
        print("    Mins of Late: ",late)
        print("    Gross Pay: ",amount3)
        print("*********************************")
        print("     Total: ",total)
        option3=input("""Do you want to continue?(Y/N)
>>""").upper()
        if option3=="Y":
            pass
        else:
            print("Than you for using the app")
            pass
            break
     elif option2 ==3:
        month=input("Enter Month: ").upper()
        hour=int(input("Hour of work: "))
        over=int(input("Hour of Overtime: "))
        print("Dedaction")
        Ca=int(input("C/A: "))
        late=int(input("Mins of Late: "))
        rate=75
        rover=97
        rlate=2
        SSS=300
        Phealth=300
        amount1=rate*hour
        amount2=over*rover
        amount3=amount1+amount2
        amount4=amount3-SSS
        amount5=amount4-Phealth
        amount6=amount5-Ca
        amount7=rlate*late
        day=hour/8
        total=amount6-amount7
        print("*********************************")
        print("          ",month,"              ")
        print("  Santos, Alfredo Jr. F.")
        print("    Day: ",day)
        print("    Hours: ",hour)
        print("    Overtime: ",over)
        print("    Dedaction")
        print("    SSS: ",SSS)
        print("    PHealth: ",Phealth)
        print("    C/A: ",Ca)
        print("    Mins of Late: ",late)
        print("    Gross Pay: ",amount3)
        print("*********************************")
        print("     Total: ",total)
        option3=input("""Do you want to continue?(Y/N)
>>""").upper()
        if option3=="Y":
            pass
        else:
            print("Than you for using the app")
            pass
            break
     
if option1 != "Y":
    print("Than you for using the app")