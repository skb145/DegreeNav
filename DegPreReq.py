def PreReq():
    global decision
    with open('Classes.txt', 'r') as file1, open('Transcript.txt', 'r') as file2:
        contents1 = file1.readlines()
        contents2 = file2.readlines()

        AllClasses = {}
        ClassCodeSearch = {}
        classesTaken = []
        NameOfClass = "Class"
        ClassPreReqCheck = 1
        

        for content2 in contents2:
            ClassComp = content2.strip().split(',')
            if len(ClassComp) == 4:
                classesTaken.append(ClassComp[0])
    
    
    def PreReqCheck():
        nonlocal contents1
        nonlocal contents2
        nonlocal AllClasses
        nonlocal ClassCodeSearch
        nonlocal NameOfClass
        nonlocal ClassPreReqCheck
        ClassLst = []
        for content1 in contents1:
            classes = content1.strip().split(',')
            if len(classes) == 4:
                AllClasses[classes[0]] = classes
                ClassCodeSearch[classes[1]] = classes[0]
                ClassLst.append(classes[0])
        
        SeeClassList = input("Would you like to see a list of RBS classes (type yes or no): ")
        
        if SeeClassList == 'yes':
            print("\n")
            for Lst in ClassLst:
                print(Lst)
            print("\n")
        
        NameOfClass = input("Please enter class: ")
        print("\n")
        
        if NameOfClass not in ClassLst:
            pass
        else:
        
            if '|' in AllClasses[NameOfClass][-1]:
                ClassSplit = AllClasses[NameOfClass][-1]
                ClassSplit = ClassSplit.split('|')
                ClassLen = len(ClassSplit)
                ClassPreReqCheck = len(ClassSplit)
                print("The Prerequisite(s) Are:")
                for ORs in ClassSplit:
                    Or = ClassCodeSearch[ORs]
                    if ClassLen > 1:
                        print("\n" + Or, end= " OR ")
                        ClassLen = ClassLen - 1
                        if Or not in classesTaken:
                            ClassPreReqCheck = ClassPreReqCheck - 1   
                    else:
                        print(Or)
                        if Or not in classesTaken:
                            ClassPreReqCheck = ClassPreReqCheck - 1
                    
                    
            elif '==' in AllClasses[NameOfClass][-1]:
                ClassSplit = AllClasses[NameOfClass][-1]
                ClassSplit = ClassSplit.split('==')
                ClassLen = len(ClassSplit)
                ClassPreReqCheck = len(ClassSplit)
                print("The Prerequisite(s) Are:")
                for ANDs in ClassSplit:
                    And = ClassCodeSearch[ANDs]
                    if ClassLen > 1:
                        print("\n" + And, end= " AND ")
                        ClassLen = ClassLen - 1
                        if And not in classesTaken:
                            ClassPreReqCheck = 0
                    else:
                        print(And)
                        if And not in classesTaken:
                            ClassPreReqCheck = 0
            
            elif '++' in AllClasses[NameOfClass][-1]:
                ClassSplit = AllClasses[NameOfClass][-1]
                ClassSplit = ClassSplit.split('++')
                for Nclass in ClassSplit:
                    if '/' in Nclass:
                        ClassSplitInd = ClassSplit.index(Nclass)
                        ClassSplit[ClassSplitInd] = ClassSplit[ClassSplitInd].split("/")
                ClassLen = len(ClassSplit)
                ClassPreReqCheck = len(ClassSplit)
                print("The Prerequisite(s) Are:")
                for AndOr in ClassSplit:
                    AndOrLen = len(AndOr)
                    if (((AndOrLen == 2) or (AndOrLen == 3) or (AndOrLen == 4)) and (ClassLen > 1)):
                        def AndOrfunc():
                            nonlocal ClassPreReqCheck
                            nonlocal ClassLen
                            nonlocal AndOrLen
                            if ClassPreReqCheck == 0:
                                pass
                            else:
                                ClassPreReqCheck = AndOrLen
                            for OrsOfAnd in AndOr:
                                if AndOrLen > 1:
                                    print(ClassCodeSearch[OrsOfAnd], end=' OR ')
                                    AndOrLen = AndOrLen - 1
                                    if OrsOfAnd not in classesTaken:
                                        ClassPreReqCheck = ClassPreReqCheck - 1
                                else:
                                    print(ClassCodeSearch[OrsOfAnd])
                                    ClassLen = ClassLen - 1
                                    if OrsOfAnd not in classesTaken:
                                        ClassPreReqCheck = ClassPreReqCheck - 1
                        AndOrfunc()
                        print("AND")
                    elif ((AndOrLen == 2) or (AndOrLen == 3) or (AndOrLen == 4)):
                        AndOrfunc()
                    else:
                        print(ClassCodeSearch[AndOr])
                        if ClassPreReqCheck == 0:
                            pass
                        else:
                            if AndOr not in classesTaken:
                                ClassPreReqCheck = 0

            elif '//' in AllClasses[NameOfClass][-1]:
                ClassSplit = AllClasses[NameOfClass][-1]
                ClassSplit = ClassSplit.split('//')
                for Nclass in ClassSplit:
                    if '+' in Nclass:
                        ClassSplitInd = ClassSplit.index(Nclass)
                        ClassSplit[ClassSplitInd] = ClassSplit[ClassSplitInd].split("+")
                ClassLen = len(ClassSplit)
                ClassPreReqCheck = len(ClassSplit)
                print("The Prerequisite(s) Are:")
                for OrAnd in ClassSplit:
                    OrAndLen = len(OrAnd)
                    if (((OrAndLen == 2) or (OrAndLen == 3) or (OrAndLen == 4)) and (ClassLen > 1)):
                        def OrAndfunc():
                            nonlocal ClassPreReqCheck
                            nonlocal ClassLen
                            nonlocal OrAndLen
                            ClassPreReqCheck = OrAndLen
                            for AndsOfOr in OrAnd:
                                if OrAndLen > 1:
                                    print(ClassCodeSearch[AndsOfOr], end=' AND ')
                                    OrAndLen = OrAndLen - 1
                                    if AndsOfOr not in classesTaken:
                                        ClassPreReqCheck = 0
                                else:
                                    print(ClassCodeSearch[AndsOfOr])
                                    ClassLen = ClassLen - 1
                                    if AndsOfOr not in classesTaken:
                                        ClassPreReqCheck = 0
                        OrAndfunc()
                        print("OR")
                    elif ((OrAndLen == 2) or (OrAndLen == 3) or (OrAndLen == 4)):
                        OrAndfunc()
                    else:
                        ClassPreReqCheck = OrAndLen
                        print(ClassCodeSearch[OrAnd])
                        if OrAnd not in classesTaken:
                            ClassPreReqCheck = ClassPreReqCheck - 1
            
            elif AllClasses[NameOfClass][-1] != 'N/A':
                print("The Prerequisite(s) Are:")
                print(ClassCodeSearch[AllClasses[NameOfClass][-1]])
            elif AllClasses[NameOfClass][-1] == 'N/A':
                print("The class does not have any prerequisites")
            else:
                pass
        
    def WriteTranscript():
        nonlocal contents1
        nonlocal contents2
        nonlocal AllClasses
        nonlocal ClassCodeSearch
        nonlocal NameOfClass
        nonlocal ClassPreReqCheck
        file = open("Transcript.txt", "a")
        
        seminput = input("\n" + "Which semester do you want to write information for?" + "\n" + "Format like: Spring 2022 or Summer 2023" +
        "\n" + "If you have AP Credits completed format like: AP Credits"+ "\n" +"Please choose a Semester: ")

        file.write("\n" + seminput)

        CCDec = input("Would you like too see how to enter Core Credits into Transcript? (Please type yes or no): ")
        if CCDec == 'yes':
                print("\n")
                print("HST is for Historical Analysis" + "\n" + "SCL is for Social Analysis" + "\n" + "CC is for Contemporary Challenges"
                + "\n" + "WC is for Writing Core" + "\n" + "NS is for Natural Science" + "\n" + "AH is for Art & Humanities" + "\n" + 
                "PB is for Pre-Buisness" + "\n" + "BC is for Buisness Core" + "\n" + "FN is for Finance Major" + "\n" + 
                "BAIT is for BAIT Major" + "\n" + "ACT is for Accounting Major" + "\n" + "SCN is for Supply Chain Major" + "\n" 
                + "MAR is for Marketing Major" + "\n" + "LM is for Leadership & Management Major" + "\n" + "BSA is for Buisness Analytics Concentration" 
                + "\n" + "FNC is for Finance Concentration" + "\n" + "GB is for Global Buisness" + "\n" + "LS is for Leadership Skills Concentration" 
                + "\n" + "MIS is for MIS Concentration" + "\n" + "PSL is for Professional Selling Concentration" + "\n" + "RS is for Real Estate Concentration")
                print("\n")
        
        while True:
            add_class = input("Would you like to add a class. Please enter yes or no: ")
            add_class.lower()
            match add_class:
                case 'yes':
                    PreReqCheck()
                    if ClassPreReqCheck == 0:
                        print("\n" + "You cannot take this class as you did not take the necessary prerequisites!")
                        break
                    ClassGrade = input("Please enter the grade: ")
                    ClasCred = input("Please how many credits: ")
                    CoreCred = input("Please enter core reqs: ")
                    classTransac = f"{NameOfClass}, {ClassGrade}, {ClasCred}, {CoreCred}"

                    
                    file.writelines("\n"+ classTransac)
                    print("Transaction Went Trough Successfully")  
                case 'no':
                    break
                case _:
                    pass

        file.close()

    
    decision = input("Please choose if you want to Check Class Prerequisites or Write in Transcript?" + "\n" + 
    "Type P for Class Prerequisites or W for Writing in Transcipt" + "\n" + "Please Choose: ")
    if decision == 'P':
        while True:
            PreReqCheck()
            Further = input("Would you like to pick another class? Please type yes or no: ")
            if Further == 'yes':
                pass
            else:
                break
    
    elif decision == 'W':
        WriteTranscript()
    else:
        print("Please Choose P or W")




