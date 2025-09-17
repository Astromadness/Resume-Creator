print("Hi, I will make you a custom resume for you job quickly! Beware of conjunctions.")
def extraInfo():
    global extraInfo
    global choice
    global askextraInfo
    isTrue = input("Do you want to add any extra info (Y/N): ")
    if isTrue.lower() == "y":
        choice = True
        askextraInfo = input("Enter extra info: ")
        askextraInfo = "\n\tAnother thing i want to add is, " + askextraInfo
        execute()
    elif isTrue.lower() == "n":
        choice = False
        print("Okay")
        execute()
    else:
        print("Invalid answer!")
        extraInfo()

def execute():
    txt = f"\tMy name is {name},\n\tI am {age} years old,\n\tI studied in {previousSchool}.\n\tI used to work in {previousOrganization} with {yearsOfExperience} years of experience.\n\tI am applying for the job of {job} because {reasonForJob}. "
    if choice == True:
        txtWithExtraInfo = askextraInfo

    contact = f"\n\tEmail: {email}\n\tMobile number: {number}"
    if choice == True:
        finalTxt = txt + txtWithExtraInfo + contact
    elif choice == False:
        finalTxt = txt + contact
    print(finalTxt)

def infograbber():
    global name
    global age
    global previousSchool
    global previousOrganization
    global yearsOfExperience
    global job
    global reasonForJob
    global email
    global number
    name = input("Name: ")
    age = input("Age: ")
    previousSchool = input("Previous school: ")
    previousOrganization = input("Previous Organization: ")
    yearsOfExperience = input("Years of Experience: ")
    job = input("Job: ")
    reasonForJob = input("Why you like this job?: ")
    email = input("E-mail: ")
    number = input("Mobile number: ")
    extraInfo()


infograbber()