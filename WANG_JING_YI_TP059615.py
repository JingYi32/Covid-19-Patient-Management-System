#WANG JING YI
#TP059615

#Menu
def opt_f():
    opt = input ("\n\t\t   ******* WELCOME TO APU HOSPIHAL *******\n\t\t***** HERE IS THE MENU OF APU HOSPITAL *****\n\nHere are Your Options:\n1.   Add new patient detail.\n2.   Undergoes Test.\n3.   Search Specific Patient detail.\n4.   Print the Total Number.\n5.   Change the Status of Patients.\n6.   Exit Menu\n\nSelect your choice:")
    while (opt != '6'):
        if (opt == "1"):
            #Registration
            opt1()
        elif (opt == "2"):
            opt2()
        elif (opt=="3"):
            #Search Details
            opt3()
        elif (opt=="4"):
            #Print Total
            opt4()
        elif (opt=="5"):
            #Change Status
            opt5()
        else:
            print ("Wrong insert, kindly select again.\n")
        opt = input ("\n\t\t   ******* WELCOME TO APU HOSPIHAL *******\n\t\t***** HERE IS THE MENU OF APU HOSPITAL *****\n\nHere are Your Options:\n1.   Add new patient detail.\n2.   Undergoes Test.\n3.   Search Specific Patient detail.\n4.   Print the Total Number.\n5.   Change the Status of Patients.\n6.   Exit Menu\n\nSelect your choice:")


############################################################################
#OPT1: Registration
def opt1():
    #MAIN PART
    print ("\n\t\t  ******* WELCOME TO APU HOSPIHAL *******\n\t  ******* HERE IS THE REGISTRATION OF APU HOSPITAL *******")
    #Details of Patient
    print ("\nPlease fill up the following details of the patient:")
    name = str (input ("Enter the name of patient\t\t:"))
    age = func_age()
    gen = func_gen()
    pn = func_pn()
    zone = fucn_zone()          #ZONE
    code, flag = f_group()      #ID
    if (flag == 1):
        x = 1
        f = open("Details of Patient.txt", "r")
        for line in f:
            x = x + 1
        ID = str(x-3)+'-'+code
        print("\nHere is Your Patient's ID:", ID,"\n\n")
        f = open("Details of Patient.txt", "a")
        f.write ("\n "+str(x-3)+"\t\t"+name+"\t\t"+ID+"\t\t"+gen+"\t\t"+str(age)+"\t\t"+zone+"\t\t"+code+"\t\t"+str(pn))
        f.close()

    elif (flag == 0):
        print ("\n\n*** You are not a patient of COVID-19 ***")

    else:
        print ("\n\n*** Sorry, our hospital will not conduct test on individuals who belong to more than one group, kindly move to state general hospital. ***")
        
#Gender
def func_gen():
    while True:
        try:
            gender = input ("Enter the gender of patient(M /F)\t:")
            if (gender == "M" or gender == "m"):
                GEN = "Male"
            elif (gender == "F" or gender == "f"):
                GEN = "Female"
            else:
                print ("Insert wrongly, kindly insert again.\n")
                continue
        except ValueError:
            print ("Insert wrongly, kindly insert again.\n")
            continue
        return GEN

#Age
def func_age():
    while True:
        try:
            AGE = int (input ("Enter the age of patient\t\t:"))
        except ValueError:
            print ("Insert wrongly, kindly insert again.\n")
            continue
        return AGE

#Phone Number
def func_pn():
    while True:
        try:
            PN = int(input ("Enter the phone number of patient\t:"))
        except ValueError:
            print ("Insert wrongly, kindly insert again.\n")
            continue
        else:
            break
    return PN


#Zone
def fucn_zone():
    while True:
        try:
            print ("\nZONE A\t: East\nZONE B\t: West\nZONE C\t: North\nZONE D\t: South")
            ZONE = str (input("Which ZONE do patient came from(A /B /C /D):"))
            if (ZONE == "A" or ZONE == "a"):
                ZONE = "EAST"
            elif (ZONE == "B" or ZONE == "b"):
                ZONE = "WEST"
            elif (ZONE == "C" or ZONE == "c"):
                ZONE = "NORTH"
            elif (ZONE == "D" or ZONE == "d"):
                ZONE = "SOUTH"
            else:
                print ("Insert wrongly, kindly insert again.\n")
                continue
        except ValueError:
            print ("Insert wrongly, kindly insert again.\n")
            continue
        return ZONE

#Group
def f_group():
    FLAG = 0
    CODE = 'none'
    print ("\n\nAnswer 'Y' as YES, others as NO.\n")

    ans1 = input ("Had you travelled to countries with high COVID-19 cases but do not show any COVID-19 symptoms? :")
    ans2 = input ("Had you close contact with active COVID-19 patients but do not show any COVID-19 symptoms? :")
    ans3 = input ("Had you attended event associated with known COVID-19 outbreak but do not show any COVID-19 symptoms? :")
    ans4 = input ("Have you shown COVID-19 symptoms? :")
    ans5 = input ("Are you Hospital staff who have not shown any COVID-19 symptoms? :")

    if(ans1 == "y" or ans1 == "Y"):
        group = "Asymptomatic individuals with history of travelling overseas"
        CODE = 'ATO'
        FLAG = FLAG + 1

    if (ans2 == "y" or ans2 == "Y"):
        group = "Asymptomatic individuals with history of contact with known case of COVID-19"
        CODE = 'ACC'
        FLAG = FLAG + 1

    if (ans3 == "y" or ans3 == "Y"):
        group = "Asymptomatic individuals who had attended event associated with known COVID-19 outbreak"
        CODE = 'AEO'
        FLAG = FLAG + 1

    if (ans4 == "y" or ans4 == "Y"):
        group = "Symptomatic individuals"
        CODE = 'SID'
        FLAG = FLAG + 1

    if (ans5 == "y" or ans5 == "Y"):
        group = "Asymptomatic hospital staff"
        CODE = 'AHS'
        FLAG = FLAG + 1
    return (CODE,FLAG)


############################################################################
#OPT2: Testing
def opt2():
    while True:
        try:
            print ("\n\t\t   ******* WELCOME TO APU HOSPIHAL *******\n\t  ******* HERE IS THE TESTING CENTRE OF APU HOSPITAL *******")
            file = open ("Details of Patient.txt","r")
            check = input ("\nPlease Enter Patient ID (Please Do Not Type Name to Prevent Duplication):")
            for line in file:
                if not check in line:
                    continue
                else:
                    print ("\nBil.\t\tName\t\t\tID\t\tGender\t\tAge\t\tZone\t\tGroup\t\tPhone Number")
                    print (line)
                    data = line.split("\t\t")
                    name = data[1]
                    code = data[6]
                    ID = data[2]
                    zone = data[5]
                    def dgroupc():
                        QHNF = "Quarantine in Hospital"
                        HQNF = "Home Quarantine"
                        QDFR = "Quarantine in Designated Centres"
                        HQFR = "Home Quarantine"
                        CWFR = "Continue Working"
                        RU = "Allow to reunion with family"
                        CW = "Continue Working"
                        if (code == "ATO" or code == "ACC" or code == "AEO"):
                            W = QHNF
                            Y = QDFR
                            Z = RU

                        elif (code == "SID"):
                            W = QHNF
                            Y = HQFR
                            Z = RU

                        elif (code == "AHS"):
                            W = HQNF
                            Y = CWFR
                            Z = CW

                        return W, Y, Z
                    A, B, C = dgroupc()
                    
                    #CONFORM INPUT
                    conform = input("\nPress Any Key to Conform this Detail is Belong to Patient Insert and Press '1' to Exit:")
                    s = 1
                    sf = open("Status.txt", "r")
                    for line in sf:
                        s = s + 1
                    sf.close
                    #START TESTING
                    if (conform != '1'):
                        while True:
                            try:
                                opt2 = int(input("\nHere are your option:\n1.   Test 1\n2.   Test 2\n3.   Test 3\n\nPlease Enter The Number of Test:"))
                                #TEST1
                                if (opt2 == 1):
                                    f = open ("Test.txt","r")
                                    read = f.read()
                                    for line in read:
                                        if not check in read:
                                            print ("\nYour Option Selected is the Test 1. \nPlease Enter the Result of Test 1 after you tested.")
                                            opt2_1 = int(input("\n\nResult of Test 1:\n1.   Positive\n2.   Negative\nSelect Option:"))
                                            if (opt2_1 == 1):
                                                ROOM = roommmm()
                                                f = open ("Test.txt","a")
                                                line = "\n"+name+"\t\t"+ID+"\t\t\t"+code+"\t\tT1: Positive\t\tXFollow-up test\t\tXFollow-up test\t\t"+A+"\t\t"+ROOM
                                                f.write (line)
                                                f.close()
                                                print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION\t\t\t\tROOM QUARANTINE")
                                                print (line)
                                                print ("\n*** Patient Need to", A,"***")
                                                CID = "COVID19-"+str(s-3)
                                                ssf = open ("Status.txt","a")
                                                ssf.write("\n"+str(s-3)+"\t\t"+name+"\t\t"+CID+"\t\t"+ID+"\t\t"+zone+"\t\t"+"ACTIVE")
                                                ssf.close()
                                                break
                                            elif (opt2_1 == 2):
                                                f = open ("Test.txt","a")
                                                line = "\n"+name+"\t\t"+ID+"\t\t\t"+code+"\t\tT1: Negative\t\tT2: X Tested\t\tT3: X Tested\t\t"+B
                                                f.write (line)
                                                f.close()
                                                print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION")
                                                print (line)
                                                print ("\n*** Patient required to undergo a second test which will be conducted 2-4 days after the first test.***")
                                                break
                                            else:
                                                print ("Wrong Insert, kindly insert again.")

                                        else:
                                            print ("\n*** Patient had done Test 1, patient not allow to do again. ***")
                                            break
                                        
                                #TEST2
                                elif (opt2 == 2):
                                    #CHECK AVAILABLE OF PATIENT IN FILE
                                    f_data = ""
                                    f = open ("Test.txt","r")
                                    for line in f:
                                        if check in line:
                                            if "XFollow-up test" in line:
                                                print("\n*** Patient had tested POSITIVE in previous test, he/she do not has follow-up test. ***")
                                                print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION")
                                                print(line)
                                                f_data = f_data + line
                                            elif "T2: Positive" in line or "T2: Negative" in line:
                                                print ("\n*** Patient had done Test 2, patient not allow to do again. ***")
                                                print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION")
                                                print (line)
                                                f_data = f_data + line
                                            else:
                                                while True:
                                                    try:
                                                        print ("\nYour Option Selected is the Test 2. \nPlease Enter the Result of Test 2 after you tested.")
                                                        opt2_2 = int(input("\n\nResult of Test 2:\n1.   Positive\n2.   Negative\nSelect Option:"))
                                                        if (opt2_2 == 1):
                                                            ROOM = roommmm()
                                                            values = line.split("\t\t")
                                                            replace_result = line.replace(values[4],"T2: Positive")
                                                            replace_test3 = replace_result.replace(values[5],"XFollow-up test")
                                                            replace_action = replace_test3.replace(values[6],A+"\t\t"+ROOM)
                                                            f_data = f_data + replace_action + "\n"
                                                            print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION\t\t\t\tROOM QUARANTINE")
                                                            print (replace_action)
                                                            print ("Patient Need to", A)
                                                            CID = "COVID19-"+str(s-3)
                                                            ssf = open ("Status.txt","a")
                                                            ssf.write("\n"+str(s-3)+"\t\t"+name+"\t\t"+CID+"\t\t"+ID+"\t\t"+zone+"\t\t"+"ACTIVE")
                                                            ssf.close()
                                                        elif (opt2_2 == 2):
                                                            values = line.split("\t\t")
                                                            replace_result = line.replace(values[4],"T2: Negative")
                                                            replace_action = replace_result.replace(values[6],B)
                                                            f_data = f_data + replace_action + "\n"
                                                            print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION")
                                                            print (replace_action)
                                                            print ("\n***Patient required to undergo the last test which will be conducted 12-13 days after the second test.***")
                                                        else:
                                                            print ("Wrong Insert, kindly insert again.")
                                                            f_data = f_data + line
                                                            continue
                                                    except ValueError:
                                                        print ("Wrong Insert, kindly insert again.")
                                                        f_data = f_data + line
                                                        continue
                                                    else:
                                                        break
                                        else:
                                            f_data = f_data + line
                                    f = open("Test.txt","w")
                                    f.write(f_data)
                                    f.close()

                                #TEST3
                                elif (opt2 == 3):
                                    f = open ("Test.txt","r")
                                    f_data = ""
                                    for line in f:
                                        if check in line:
                                            if "XFollow-up test" in line:
                                                print("\n*** Patient had tested POSITIVE in previous test, he/she do not has follow-up test. ***")
                                                print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION")
                                                print (line)
                                                f_data = f_data + line
                                            elif not "T2: Negative" in line:
                                                print ("\n*** Patient has not done Test 2, patient are not allow to do this test. ***")
                                                print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION")
                                                print (line)
                                                f_data = f_data + line
                                            elif "T3: Positive" in line or "T3: Negative" in line:
                                                print ("\n*** Patient had done Test 3, patient are not allow to do it. ***")
                                                print (line)
                                                f_data = f_data + line
                                            else:
                                                while True:
                                                    try:
                                                        print ("\nYour Option Selected is the Test 3. \nPlease Enter the Result of Test 3 after you tested.")
                                                        opt2_3 = int(input("\n\nResult of Test 3:\n1.   Positive\n2.   Negative\nSelect Option:"))
                                                        if (opt2_3 == 1):
                                                            ROOM = roommmm()
                                                            values = line.split("\t\t")
                                                            replace_result = line.replace(values[5],"T3: Positive")
                                                            replace_action = replace_result.replace(values[6],A+"\t\t"+ROOM)
                                                            f_data = f_data + replace_action + "\n"
                                                            print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION")
                                                            print (replace_action)
                                                            print ("\n*** Patient Need to", A,"***")
                                                            CID = "COVID19-"+str(s-3)
                                                            ssf = open ("Status.txt","a")
                                                            ssf.write("\n"+str(s-3)+"\t\t"+name+"\t\t"+CID+"\t\t"+ID+"\t\t"+zone+"\t\t"+"ACTIVE")
                                                            ssf.close()
                                                        elif (opt2_3 == 2):
                                                            values = line.split("\t\t")
                                                            replace_result = line.replace(values[5],"T3: Negative")
                                                            replace_action = replace_result.replace(values[6],C)
                                                            f_data = f_data + replace_action + "\n"
                                                            print("\nName\t\t\tPatientID\t\tGroup\t\tResult of T1\t\tResult of T2\t\tResult of T3\t\tACTION")
                                                            print (replace_action)
                                                            print ("\n***Patient can", C, "***")
                                                        else:
                                                            print ("Wrong Insert, kindly insert again.")
                                                            f_data = f_data + line
                                                            continue
                                                    except ValueError:
                                                        print ("Wrong Insert, kindly insert again.")
                                                        f_data = f_data + line
                                                        continue
                                                    else:
                                                        break
                                        else:
                                            f_data = f_data + line
                                    f = open("Test.txt","w")
                                    f.write(f_data)
                                    f.close()
                                    
                            except ValueError:
                                #ERROR OF (CONFORM INPUT)
                                print ("Wrong Insert, kindly insert again.")
                                continue
                            else:
                                break
                    else:
                        print ("Exit.")
                        break
            file.close()
        except ValueError:
            print ("Wrong input, kindly insert again.\n")
            continue
        else:
            break

def roommmm():
    while True:
        try:
            roomm = input ("ROOM QUARANTINE(ICU/NW)\t:")
            if roomm == "ICU" or roomm == "icu":
                room = "Intensive Care Unit (ICU)"
            elif roomm == "nw" or roomm == "NW":
                room = "Normal Ward (NW)"
            else:
                print ("Wrong input, kindly insert again.\n")
                continue
        except ValueError:
            print ("Wrong input, kindly insert again.\n")
            continue
        else:
            break
    return room

############################################################################
#OPT3: Search Details
def opt3():
    print ("\n\t\t ******* WELCOME TO APU HOSPIHAL *******\n\t******* HERE IS THE SEARCHING TOOL OF APU HOSPITAL *******")
    ans_opt2 = input("\nYour Options are:\n1.   Patient's record.\n2.   Status of patient.\n3.   Record of Deceased Patients.\n4.   Exit Option\n\nSelect your option:")
    while (ans_opt2!= '4'):
        if (ans_opt2 == '1'):
            file=open("Details of Patient.txt","r")
            data = input ("Please Enter Patient ID or Name to Search Record in File:")
            for line in file:
                line=line.rstrip()
                if not data in line:
                    continue
                else:
                    print ("\nBil.\t\tName\t\t\tID\t\tGender\t\tAge\t\tZone\t\tGroup\t\tPhone Number")
                    print(line)

        elif (ans_opt2 == '2'):
            file=open("Status.txt","r")
            data = input ("Please Enter Case ID to Search Patient's Status:")
            for line in file:
                line=line.rstrip()
                if not data in line:
                    continue
                else:
                    print("\nBil.\t\tName\t\t\tCases ID\t\tID\t\tZone\t\tStatus")
                    print(line)

        elif (ans_opt2 == '3'):
            file=open("Status.txt","r")
            for line in file:
                line=line.rstrip()
                if not 'DECEASED' in line:
                    continue
                else:
                    data=line.split("\t\t")
                    name = data[1]
                    f = open("Details of Patient.txt","r")
                    for line in f:
                        if name in line:
                            print (line)
                    f.close()
        else:
            print("Insert wrongly. Kindly insert again.")
        ans_opt2 = input("\nYour Options are:\n1.   Patient's record.\n2.   Status of patient.\n3.   Record of Deceased Patients.\n4.   Exit Option\n\nSelect your option:")


############################################################################
#Opt4: Print the total
def opt4():
    print ("\n\t\t       ******* WELCOME TO APU HOSPIHAL *******\n\t******* HERE TO PRINT TOTAL NUMBER OF PATIENT IN APU HOSPITAL *******")
    opts= input("\nYour Option to display the total number of:\n1.   Tests carried out.\n2.   Patients tested.\n3.   Recoverd cases.\n4.   Patients test positive for COVID-19 group wise.\n5.   Active cases zone wise.\n6.   Exit Option.\n\nSelect your option:")
    while (opts != '6'):
        if (opts == '1'):
            #Tests carried out (i.e. total of T1, T2 and T3).
            OPT4_1()
        elif (opts == '2'):
            #Patients tested. 
            OPT4_2()
        elif (opts == '3'):
            #Recovered cases.
            OPT4_3()
        elif (opts == '4'):
            #Patients test positive for COVID-19 group wise.
            OPT4_4()
        elif (opts == '5'):
            #Active cases zone wise. 
            OPT4_5()
        else:
            print ("Wrong insert, kindly select again.\n")
        opts= input("\nYour Option to display the total number of:\n1.   Tests carried out.\n2.   Patients tested.\n3.   Recoverd cases.\n4.   Patients test positive for COVID-19 group wise.\n5.   Active cases zone wise.\n6.   Exit Option.\n\nSelect your option:")

#OPT4-1: Tests carried out (i.e. total of T1, T2 and T3)
def OPT4_1():
    file=open("Test.txt","r")
    lines=file.read()
    x = lines.count("T1: Positive")+lines.count("T1: Negative")
    y = lines.count("T2: Positive")+lines.count("T2: Negative")
    z = lines.count("T3: Positive")+lines.count("T3: Negative")
    file.close()
    print ("the Total Tests Carried out:\na.   Test 1:   ",x,"\nb.   Test 2:   ",y,"\nc.   Test 3:   ",z)

#OPT4-2: Patients tested.
def OPT4_2():
    N_PT = open("Status.txt","r")
    y = 0
    for line in N_PT:
        y = y + 1
    print ("the Total Number of Patients Tested: ",y)

#OPT4-3: Recovered cases.
def OPT4_3():
    file=open("Status.txt","r")
    lines=file.read()
    x = lines.count("RECOVERED")
    file.close()
    print ("The Total Recovered Cases\t:",x)

#OPT4-4:Patients test positive for COVID-19 group wise.
def OPT4_4():
    file=open("Test.txt","r")
    ATON = 0
    AEON = 0
    SIDN = 0
    AHSN = 0
    ACCN = 0
    for line in file:
        if "ATO" in line and "Positive" in line:
            ATON = ATON + 1
        elif "AEO" in line and "Positive" in line:
            AEON = AEON + 1
        elif "SID" in line and "Positive" in line:
            SIDN = SIDN + 1
        elif "AHS" in line and "Positive" in line:
            AHSN = AHSN + 1
        elif "ACC" in line and "Positive" in line:
            ACCN = ACCN + 1
    file.close()
    print ('Total Number of Patients Test Positive for COVID-19 Group Wise:')
    print ('a.   Asymptomatic  Travelled Overseas(ATO)\t:',ATON)
    print ('b.   Asymptomatic  Close Contact(ACC)\t\t:',ACCN)
    print ('c.   Asymptomatic  Event Outbreak(AEO)\t\t:',AEON)
    print ('d.   Symptomatic  Individuals(SID)\t\t:',SIDN)
    print ('e.   Asymptomatic  Hospital Staff(AHS)\t\t:',AHSN)

#OPT4-5: Active cases zone wise.
def OPT4_5():
    file=open("Status.txt","r")
    EASTN = 0
    WESTN = 0
    SOUTHN = 0
    NORTHN = 0
    for line in file:
        if "EAST" in line and "ACTIVE" in line:
            EASTN = EASTN + 1
        elif "WEST" in line and "ACTIVE" in line:
            WESTN = WESTN + 1
        elif "SOUTH" in line and "ACTIVE" in line:
            SOUTHN = SOUTHN + 1
        elif "NORTH" in line and "ACTIVE" in line:
            NORTHN = NORTHN + 1
    file.close()
    print ('Total Number of Active Cases Zone Wise:')
    print ('a.   Zone EAST\t:',EASTN)
    print ('b.   Zone WEST\t:',WESTN)
    print ('c.   Zone SOUTH\t:',SOUTHN)
    print ('d.   Zone NORTH\t:',NORTHN)


############################################################################
#OPT5: Change Status of Patient 
def opt5():
    print ("\n\t\t     ******* WELCOME TO APU HOSPIHAL *******\n\t******* HERE TO CHANGE STATUS OF PATIENT IN APU HOSPITAL *******")
    opt5 = input("Press any key to continue, 'x' to exit.")
    while (opt5 != 'x'):
        f_data = ""
        anws = input ("\nEnter patient-ID or cases-ID:")
        file=open ("Status.txt","r")
        for line in file:
            line = line.rstrip()
            if not anws in line:
                f_data += line
            else:
                print (line)
                c_status = input ("\nYour Option to change status:\n1.\tACTIVE\n2.\tRECOVERED\n3.\tDECEASED\n4.\tExit Option.\n\nSelect your option:")
                if (c_status == '1'):
                    values = line.split("\t\t")
                    replace_line = line.replace(values[5],"ACTIVE")
                    f_data = f_data + replace_line + '\n'
                    print (replace_line)
                elif (c_status == '2'):
                    values = line.split("\t\t")
                    replace_line = line.replace(values[5],"RECOVERED")
                    f_data = f_data + replace_line + '\n'
                    print (replace_line)
                elif (c_status == '3'):
                    values = line.split("\t\t")
                    replace_line = line.replace(values[5],"DECEASED")
                    f_data = f_data + replace_line + '\n'
                    print (replace_line)
                else:
                    f_data += line
        f = open  ("Status.txt","w")
        f.write(f_data)
        f.close()
        opt5 = input("Press any key to continue, 'x' to exit.")


def end():
    print ("\n\n******* Goodbye. Wish you have a good day. *******")

opt_f()
end()
