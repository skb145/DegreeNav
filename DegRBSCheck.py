
def Check():
    with open('Classes.txt', 'r') as file1, open('Transcript.txt', 'r') as file2:
        contents1 = file1.readlines()
        contents2 = file2.readlines()

        classesTaken = []
        
        doubleMajor = input("Are you are double buisness major yes or no: ")
        ConcentrationQ = input("Do you have any buisness concentrations yes or no: ")
        
        if doubleMajor == 'yes':
            majcount = 0
        else:
            majcount = 1
      
    
        for content2 in contents2:
            ClassComp = content2.strip().split(',')
            if len(ClassComp) == 4:
                classesTaken.append(ClassComp[0])
        
        while majcount < 2:
            if doubleMajor == 'yes':
                if majcount == 0:
                    major = input("\n" + "Choose your major:" + "\n" "Type FN for Finance" + "\n" "Type BAIT for Buisness Analytics & Information Technology" 
                    + "\n" "Type ACT for Accounting" + "\n" "Type SCN for Supply Chain" + "\n" "Type MAR for Marketing" 
                    + "\n" "Type LM for Leadership & Management" + "\n" "Please enter your major: ")
                    print("\n")
                elif majcount == 1 and mj1 == 'SCN':
                    major = mj2
                else:
                    major = input("\n" + "Choose your second major:" + "\n" "Type FN for Finance" + "\n" "Type BAIT for Buisness Analytics & Information Technology" 
                    + "\n" "Type ACT for Accounting" + "\n" "Type SCN for Supply Chain" + "\n" "Type MAR for Marketing" 
                    + "\n" "Type LM for Leadership & Management" + "\n" "Please enter second your major: ")
                    print("\n")
            else:
                major = input("\n" + "Choose your major:" + "\n" "Type FN for Finance" + "\n" "Type BAIT for Buisness Analytics & Information Technology" 
                    + "\n" "Type ACT for Accounting" + "\n" "Type SCN for Supply Chain" + "\n" "Type MAR for Marketing" 
                    + "\n" "Type LM for Leadership & Management" + "\n" "Please enter your major: ")
                print("\n")
            
               
            def CoreClassCheck():
                for content1 in contents1[:24]:
                    classes = content1.strip().split(',')
                    if len(classes) == 4:
                        if classes[0] not in classesTaken:
                            if classes[0] == 'Buisness Law':
                                pass
                            elif classes[0] == 'Buisness Ethics':
                                if 'Buisness Law' in classesTaken:
                                    pass
                                else: 
                                    print("Either Buisness Law or Buisness Ethics need to be taken!")
                            elif classes[0] == 'Financial Managment':
                                if major == 'Finance':
                                    pass
                                else:
                                    print(f"{classes[0]} still needs to be taken!")
                            elif classes[0] == 'Financial Managment for Finance':
                                if major != 'FN':
                                    pass
                                else:
                                    print(f"{classes[0]} still needs to be taken!")
                            elif classes[0] == 'Management Info Sys':
                                if major == 'ACT':
                                    pass
                                else:
                                    print(f"{classes[0]} still needs to be taken!")
                            elif classes[0] == 'Accounting Info Sys':
                                if major != 'ACT':
                                    pass
                                else:
                                    print(f"{classes[0]} still needs to be taken!")
                            else: 
                                print(f"{classes[0]} still needs to be taken!")
            
            if majcount == 0:
                mj1 = major
                CoreClassCheck()
            elif (majcount == 1 and doubleMajor == 'yes'):
                pass
            else:
                CoreClassCheck()
            
            match major:
                case 'FN':
                    FinCount = 0 
                    print("\n")
                    for content1 in contents1[26:44]:
                        classes = content1.strip().split(',')
                        if len(classes) == 4:
                            if ((classes[0] not in classesTaken) and (classes[0] == 'Corporate Finance' or classes[0] == 'Investment Analysis' or classes[0] == 'Derivatives')):
                                print(f"{classes[0]} still needs to be taken!")

                    for content2 in contents2:
                        ClassComp = content2.strip().split(',')
                        if len(ClassComp) == 4:
                            if 'FN' in ClassComp[-1]:
                                FinCount = FinCount + 1
                    
                    if FinCount == 7:
                        print("Finance Major Requirement is Completed!")
                    else:
                        print("\n"+ f"{7-FinCount} Finance classes still need to be taken!")
                            
                case 'BAIT':
                    BAITCount = 0 
                    print("\n")
                    for content1 in contents1[47:60]:
                        classes = content1.strip().split(',')
                        if len(classes) == 4:
                            if ((classes[0] not in classesTaken) and (classes[0] == 'Foundations of Business Programming' or classes[0] == 
                            'Buisness Data Management' or classes[0] == 'Business Decision Analytics under Uncertainty' or classes[0] == 'Time Series Modeling')):
                                print(f"{classes[0]} still needs to be taken!")

                    for content2 in contents2:
                        ClassComp = content2.strip().split(',')
                        if len(ClassComp) == 4:
                            if 'BAIT' in ClassComp[-1]:
                                BAITCount = BAITCount + 1
                    
                    if BAITCount == 7:
                        print("BAIT Major Requirement is Completed!")
                    else:
                        print("\n"+ f"{7-BAITCount} BAIT classes still need to be taken!")
                
                case 'ACT':
                    print("\n")
                    ACTcount = 0
                    for content1 in contents1[62:70]:
                        classes = content1.strip().split(',')
                        if classes[0] not in classesTaken:
                            print(f"{classes[0]} still needs to be taken!")
                        else: ACTcount = ACTcount + 1

                        if ACTcount == 8:
                            print("Accounting Major Requirement is Completed!")

                
                case 'SCN':
                    SCCount = 0 
                    print("\n")
                    for content1 in contents1[72:93]:
                        classes = content1.strip().split(',')
                        if len(classes) == 4:
                            if ((classes[0] not in classesTaken) and (classes[0] == 'Global Procurement and Sourcing Strategies' or classes[0] == 
                            'Business Logistics and Transportation' or classes[0] == 'Demand Planning and Fulfillment' or 
                            classes[0] == 'Intro to Project Management' or classes[0] == 'Supply Chain Internship' or classes[0] == 'Supply Chain Co-Op')):
                                if classes[0] == 'Supply Chain Internship':
                                    pass
                                elif classes[0] == 'Supply Chain Co-Op':
                                    print("A Supply Chain Internship or Co-Op needs to be Completed!")
                                else:
                                    print(f"{classes[0]} still needs to be taken!")

                    
                    for content2 in contents2:
                        ClassComp = content2.strip().split(',')
                        if len(ClassComp) == 4:
                            if 'SCN' in ClassComp[-1]:
                                SCCount = SCCount + 1

                    if doubleMajor == 'yes':
                        if mj1 == 'SCN':
                            mj2 = input("\n" + "What is your second major: ")
                            if mj2 == 'FN':
                                if ('Treasury Management' in classesTaken):
                                    SCCount = SCCount + 1
                            elif mj2 == 'ACT':
                                if ('Cost Accounting' in classesTaken):
                                    SCCount = SCCount + 1
                            else:
                                pass
                        if majcount == 1:
                            if mj1 == 'FN':
                                if ('Treasury Management' in classesTaken):
                                    SCCount = SCCount + 1
                            elif mj1 == 'ACT':
                                if ('Cost Accounting' in classesTaken):
                                    SCCount = SCCount + 1
                            else:
                                pass
                    
                    if SCCount == 8:
                        print("Supply Chain Major Requirement is Completed!")
                    else:
                        print("\n"+ f"{8-SCCount} Supply Chain classes still need to be taken!")        
                
                case 'MAR':
                    MarkCount = 0 
                    print("\n")
                    for content1 in contents1[95:115]:
                        classes = content1.strip().split(',')
                        if len(classes) == 4:
                            if ((classes[0] not in classesTaken) and (classes[0] == 'Marketing Research' or classes[0] == 
                            'Consumer Behavior' or classes[0] == 'Marketing Strategy and Decision Making')):
                                print(f"{classes[0]} still needs to be taken!")

                    for content2 in contents2:
                        ClassComp = content2.strip().split(',')
                        if len(ClassComp) == 4:
                            if 'MAR' in ClassComp[-1]:
                                MarkCount = MarkCount + 1
                    
                    if MarkCount == 7:
                        print("Marketing Major Requirement is Completed!")
                    else:
                        print("\n"+ f"{7-MarkCount} Marketing classes still need to be taken!")
                case 'LM':
                    ManCount = 0
                    ManE1Count = 0
                    ManE2Count = 2 
                    print("\n")
                    for content1 in contents1[117:124]:
                        classes = content1.strip().split(',')
                        if len(classes) == 4:
                            if ((classes[0] not in classesTaken) and (classes[0] == 'International Business' or classes[0] == 'Executive Leadership')):
                                print(f"{classes[0]} still needs to be taken!")
                            
                            if classes[0] in classesTaken:
                                ManCount = ManCount + 1
                                ManE1Count = ManE1Count + 1
                                if ManE1Count < 2:
                                    print("1 more Leadership & Management mandatory elective still needs to be fullied!")
                    
                    for content1 in contents1[125:140]: 
                        classes = content1.strip().split(',')
                        if len(classes) == 4:
                            if classes[0] in classesTaken:
                                if ManE2Count > 0:
                                    ManCount = ManCount + 1
                                    ManE2Count = ManE2Count - 1
                                else:
                                    pass
                    
                    if ManCount == 7:
                        print("Management Major Requirement is Completed!")
                    else:
                        print("\n"+ f"{7-ManCount} Management classes still need to be taken!")
            
            majcount = majcount + 1

        if ConcentrationQ == 'yes':
            Concentration = input("\n" + "Choose your Concentration:" + "\n" "Type BSA for Business Analytics" + "\n" "Type FNC for Finance" 
                    + "\n" "Type GB for Global Buisness" + "\n" "Type LS for Leadership Skills" + "\n" "Type MIS for Management Information Systems" 
                    + "\n" "Type PSL for Sales" + "\n" "Type RS Real Estate" + "\n" "Please enter your Concentration: ")
        
        if ConcentrationQ == 'yes':
            match Concentration:
                case 'BSA':
                    if doubleMajor != 'yes':
                        mj1 = major
                    
                    if ((major == 'BAIT') or (mj1 == 'BAIT')):
                        pass
                    else:
                        BSACount = 0 
                        print("\n")
                        for content1 in contents1[47:50]:
                            classes = content1.strip().split(',')
                            if len(classes) == 4:
                                if ((classes[0] not in classesTaken) and (classes[0] == 'Business Decision Analytics under Uncertainty' or classes[0] == 'Time Series Modeling')):
                                    print(f"{classes[0]} still needs to be taken!")

                        for content2 in contents2:
                            ClassComp = content2.strip().split(',')
                            if len(ClassComp) == 4:
                                if 'BSA' in ClassComp[-1]:
                                    BSACount = BSACount + 1
                    
                    if BSACount == 3:
                        print("Buisness Analytics Concentration Requirement is Completed!")
                    else:
                        print("\n"+ f"{3-BSACount} Buisness Analytics Concentration classes still need to be taken!")
                                    
                case 'FNC':
                    if doubleMajor != 'yes':
                        mj1 = major
                    
                    if ((major == 'Finance') or (mj1 == 'Finance')):
                        pass
                    else: 
                        print("\n")
                        for content1 in contents1[26:30]:
                            classes = content1.strip().split(',')
                            if len(classes) == 4:
                                if ((classes[0] not in classesTaken) and (classes[0] == 'Corporate Finance' or classes[0] == 'Investment Analysis' or classes[0] == 'Derivatives')):
                                    print(f"{classes[0]} still needs to be taken!")
                                if (('Corporate Finance' in classesTaken) and ('Investment Analysis' in classesTaken) and ('Derivatives' in classesTaken)):
                                    print("Finance Concentration Requirement is Completed!")
                
                case 'GB':
                    if doubleMajor != 'yes':
                        mj1 = major
                    
                    if ((major == 'Management') or (mj1 == 'Management')):
                        pass
                    else:
                        GBCount = 0 
                        print("\n")
                        for content1 in contents1[117:130]:
                            classes = content1.strip().split(',')
                            if len(classes) == 4:
                                if ((classes[0] not in classesTaken) and (classes[0] == 'Global Management & Strategy' or classes[0] == 'International Business')):
                                    print(f"{classes[0]} still needs to be taken!")

                        for content2 in contents2:
                            ClassComp = content2.strip().split(',')
                            if len(ClassComp) == 4:
                                if 'GB' in ClassComp[-1]:
                                    GBCount = GBCount + 1
                    
                        if GBCount == 3:
                            print("Global Buisness Concentration Requirement is Completed!")
                        else:
                            print("\n"+ f"{3-GBCount} Global Buisness Concentration classes still need to be taken!")
                
                case 'LS':
                    LSCount = 0 
                    print("\n")
                    for content1 in contents1[118:121]:
                        classes = content1.strip().split(',')
                        if len(classes) == 4:
                            if ((classes[0] not in classesTaken) and (classes[0] == 'Executive Leadership')):
                                print(f"{classes[0]} still needs to be taken!")
                            
                            if ((classes[0] not in classesTaken) and (classes[0] == 'Effective Leadership Communications')):
                                pass
                            elif ((classes[0] not in classesTaken) and (classes[0] == 'Negotiations')):
                                print("Either Effective Leadership Communications or Negotiations still needs to be taken!")
                            else:
                                pass

                    for content2 in contents2:
                        ClassComp = content2.strip().split(',')
                        if len(ClassComp) == 4:
                            if 'LS' in ClassComp[-1]:
                                LSCount = LSCount + 1
                
                    if LSCount == 3:
                        print("Leadership Skills Concentration Requirement is Completed!")
                    else:
                        print("\n"+ f"{3-LSCount} Leadership Skills Concentration classes still need to be taken!")
                case 'MIS':
                    if doubleMajor != 'yes':
                        mj1 = major
                    
                    if ((major == 'BAIT') or (mj1 == 'BAIT')):
                        pass
                    else:
                        MISCount = 0 
                        print("\n")
                        for content1 in contents1[47:55]:
                            classes = content1.strip().split(',')
                            if len(classes) == 4:
                                if ((classes[0] not in classesTaken) and (classes[0] == 'Foundations of Business Programming' or classes[0] == 'Buisness Data Management')):
                                    print(f"{classes[0]} still needs to be taken!")

                        for content2 in contents2:
                            ClassComp = content2.strip().split(',')
                            if len(ClassComp) == 4:
                                if 'MIS' in ClassComp[-1]:
                                    MISCount = MISCount + 1
                    
                    if MISCount == 3:
                        print("MIS Concentration Requirement is Completed!")
                    else:
                        print("\n"+ f"{3-MISCount} MIS classes still need to be taken!")
                                    
                case 'PSL':
                    if doubleMajor != 'yes':
                        mj1 = major
                    
                    if ((major == 'Marketing') or (mj1 == 'Marketing')):
                        pass
                    else:
                        PSLCount = 0 
                        print("\n")
                        for content1 in contents1[95:115]:
                            classes = content1.strip().split(',')
                            if len(classes) == 4:
                                if ((classes[0] not in classesTaken) and (classes[0] == 'Professional Selling' or classes[0] == 'Sales Management')):
                                    print(f"{classes[0]} still needs to be taken!")

                        for content2 in contents2:
                            ClassComp = content2.strip().split(',')
                            if len(ClassComp) == 4:
                                if 'PSL' in ClassComp[-1]:
                                    PSLCount = PSLCount + 1
                    
                    if PSLCount == 3:
                        print("Pro Concentration Requirement is Completed!")
                    else:
                        print("\n"+ f"{3-PSLCount} Sales classes still need to be taken!")
                case 'RS':
                    if doubleMajor != 'yes':
                        mj1 = major
                    print("\n")
                    RScount = 0
                    for content1 in contents1[142:147]:
                            classes = content1.strip().split(',')
                            if len(classes) == 4:
                                if (classes[0] not in classesTaken) and (major == 'FN' or mj1 == 'FN'):
                                    if classes[0] == 'Essentials of Real Estate Finance':
                                        pass
                                    else:
                                        print(f"{classes[0]} still needs to be taken!")
                                elif (classes[0] not in classesTaken) and (major != 'FN' or mj1 != 'FN'):
                                    if classes[0] == 'Real Estate Finance and Mortgage Backed Securities':
                                        pass
                                    else:
                                        print(f"{classes[0]} still needs to be taken!")
                                else:
                                    RScount = RScount + 1
                    
                    if RScount == 4:
                        print("Real Estate Concentration Requirement is Completed!")

        print("\n")        
        AHcount = 0
        SCLcount = 0
        HSTcount = 0
        CCcount = 0
        WCcount = 0
        NScount = 0
        for content2 in contents2:
            ClassComp = content2.strip().split(',')
            if len(ClassComp) == 4:
                if ('D' in ClassComp[1]) or ('F' in ClassComp[1]) or ('NC' in ClassComp[1]):
                    if (('AH' in ClassComp[-1]) or ('SCL' in ClassComp[-1]) or ('HST' in ClassComp[-1]) or ('CC' in ClassComp[-1]) 
                    or ('WC' in ClassComp[-1]) or ('NS' in ClassComp[-1])):
                        print(f"You did not recieve credit for {ClassComp[0]}!")
                    else:
                        print(f"You did not recieve credit for {ClassComp[0]}! You still need to take it!")
            
            if 'AH' in ClassComp[-1]:
                AHcount = AHcount + 1
            
            if 'SCL' in ClassComp[-1]:
                SCLcount = SCLcount + 1
            
            if 'HST' in ClassComp[-1]:
                HSTcount = HSTcount + 1
            
            if 'CC' in ClassComp[-1]:
                CCcount = CCcount + 1

            if 'WC' in ClassComp[-1]:
                WCcount = WCcount + 1
            
            if 'NS' in ClassComp[-1]:
                NScount = NScount + 1
        
        
        if 'Expository Writing' not in classesTaken:
            print("You still need to take Expository Writing!")
        
        if AHcount < 2:
            print(f"You need to take {AHcount} Art & Humanities Classes!")

        if SCLcount < 1:
            print(f"You need to take a Social Analysis Class!")

        if HSTcount < 1:
            print(f"You need to take a Historical Analysis Class!")
        
        if CCcount < 2:
            print(f"You need to take {CCcount} Art & Humanities Classes!")
        
        if WCcount < 2:
            print(f"You need to take {WCcount} Writing Core Classes!")
        
        if NScount < 2:
            print(f"You need to take {NScount} Natural Science Classes!")

        


        
                
