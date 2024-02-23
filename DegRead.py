def TranscriptRead():
    
    with open('Transcript.txt', 'r') as file:
        contents = file.readlines()
        CountGb = 0
        semclasses = []
        ClassLst = []

    for content in contents:
            ClassComp = content.strip().split(',')
            semclasses.append(ClassComp)
    
    
    def ClassRead():
        seminput = input("\n" + "Which semester do you want to retrieve information from?" + "\n" + "Format like: Spring 2022 or Summer 2023" +
        "\n" + "If you have AP Credits completed format like: AP Credits"+ "\n" +"Please choose a Semester: ")
        SemList = []
        
        for semclass in semclasses:
            nonlocal CountGb
            SemList.append(semclass[0])
            if seminput in semclass[0]:
                break
            else:
                CountGb = CountGb + 1
        
        if f"{seminput}:" not in SemList:
            print("\n" + "That Semester is Not in the Transcript!")
    
    cumulative = input("\n" + "Do you want transcipt information pertaining a particular semester or cumulatively?" + "\n" 
    + "Default is Cumulative!" + "\n" + "Type S or Particular Semester or Type C for Cumulative: ")
    
    def ChooseSem():
        print("\n")
        for NameOfClass in ClassLst:
            if len(NameOfClass) > 1:
                for Name in NameOfClass:
                    if Name != NameOfClass[-1]:
                        print(Name, end=",")
                    else:
                        print(Name)
                        break
            elif ((cumulative != 'S') or (":" in NameOfClass[0])):
                print(NameOfClass[0])
            else:
                break
           
    def ClassInfo():
        nonlocal ClassLst
        if cumulative == 'S':
            ClassRead()
            ClassLst = semclasses[CountGb:]
            ChooseSem()
        else:
            ClassLst = semclasses
            ChooseSem()

    def GPA():
        def calcGPA():
            TotalGrades = 0
            TotalCredits = 0
            TotalCreditsTaken = 0
            for NameOfClass in ClassLst:
                if len(NameOfClass) > 1:
                    classGrade = NameOfClass[1]
                    
                    if 'P' in classGrade:
                        classCredits = 0
                        creditsTaken = float(NameOfClass[2])
                    elif 'NC' in classGrade:
                        classCredits = 0
                        creditsTaken = 0
                    elif 'F' in classGrade:
                        classCredits = float(NameOfClass[2])
                        creditsTaken = 0
                    else:
                        classCredits = float(NameOfClass[2])
                        creditsTaken = float(NameOfClass[2])

                    
                    if 'A' in classGrade:
                        classGrade = 4.0 * classCredits
                    elif 'B+' in classGrade:
                        classGrade = 3.5 * classCredits
                    elif 'B' in classGrade:
                        classGrade = 3.0 * classCredits
                    elif 'C+' in classGrade:
                        classGrade = 2.5 * classCredits
                    elif 'C' in classGrade:
                        classGrade = 2.0 * classCredits
                    elif 'D' in classGrade:
                        classGrade = 1.0 * classCredits
                    else: 
                        classGrade = 0.0 * classCredits       
                    
                    TotalGrades = TotalGrades + classGrade
                    TotalCredits = TotalCredits + classCredits
                    TotalCreditsTaken = TotalCreditsTaken + creditsTaken
            
                    

            GradePointAvg = TotalGrades / TotalCredits
            GradePointAvg = round(GradePointAvg, 3)
            GradePointAvg = print(f"Your GPA is a {GradePointAvg} and you have completed {TotalCreditsTaken} credits")
        
        if cumulative == 'S':
            nonlocal ClassLst
            ClassRead()
            ClassLst = semclasses[CountGb:]
            calcGPA()
        else:
            ClassLst = semclasses
            calcGPA()
    
    while True:
        decision = input("Would you like to GPA or List of Classes Taken?" + "\n" + "Type GPA or List: ")
        if decision == 'List':
            ClassInfo()
            break
        elif decision == 'GPA':
            GPA()
            break
        else:
            print("Please type either GPA or List")
