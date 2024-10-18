import FileManagement

def CreateSections():
    num_of_sections = 0
    task_per_section = []
    while( num_of_sections < 1 or num_of_sections > 10):
        try:
            num_of_sections = int(input("Enter the number of sections you would like to create"))
        except:
            print("Incorrect value, please enter a number between 1-10 (inclusive)")

    for section in range(0, num_of_sections):
        while( num_of_sections < 1 or num_of_sections > 40):
            try:
                task_per_section[section] = int(input(f"Enter the number of tasks in section {section+1}"))
            except:
                print("Incorrect value, please enter a number between 1-40 (inclusive)")
    
    for task_num in task_per_section:
        print("not implemented")
        #Create folder (section number)
        #Enter folder
        #Create [n] tasks where [n] is task_per_section[task_num]
        #Navigate back to root folder