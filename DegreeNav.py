from DegRead import TranscriptRead
from DegRBSCheck import Check
from DegPreReq import PreReq

while True:
    prompt = input("\n" + "Hi Welcome to the RBS Directory! Please choose what you would like to do" + "\n" + "1: Check what classes you've taken or your GPA"
    + "\n" + "2: Check what RBS classes still need to be taken" +  "\n" + "3: Check RBS Class Prequesities or Update Transcript" 
    "\n" +  "Please Choose 1, 2 or 3: ")
    match prompt:
        case '1':
            TranscriptRead()
        case '2':
            Check()
        case '3':
            PreReq()
        case _:
            try:
                5 +'5'
            except:
                print("\n" + "Please Choose 1, 2, or 3!")
                continue
    
    continueLoop = input("\n" + "Would you like to continue? (Please type yes or no): ")

    if continueLoop == 'no':
        break
