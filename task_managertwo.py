# Creating a progam for small business that can help manage tasks assigned to each member of the team.
# Two txt files will be created named user.txt and tasks.txt
# open user.txt file.
user = open('user.txt', 'r')
login = False

# The user needs to enter their username and password
while not login:
    username = input("Please enter your username : ")
    password = input("Please enter your password : ")

# We need to verify whether the username and password is correct
    for lines in user:
        temp = lines.strip()
        temp = temp.split(", ")
# The postion of the username is in user.txt
        valid_username = temp[0]
# The postion of the password is in user.txt        
        valid_password = temp[1]  
        if username == valid_username and password == valid_password:  # checks if the correct passord is in and gives accuse to user
            login = True
            print("Task Manager Desk \n")
            user.seek(0)
            break
        
# A message will be displyed that the password is incorrect
    if username != valid_username or password != valid_password:  
        login = False
        print("Please enter the correct username and password")
    user.seek(0)

user.close()

# The option variable has been declared to creat an option menu
option = False

# once user has successfully logged on show the option menu so that user can see their options
while login == True:
    option = input("""Please select one of the following options :
    r - Register user
    a - Add task
    va - View all tasks
    vm - View my tasks
    s - statistics
    e - Exit
    """)
    
# If user option is to register user, the user should be prompted for a new username and password.
# The user should also be asked to confirm the password.
# If the value entere to confirm the password matches the password, the username and password must be wtitten to user.txt in the appropeiate format.
    if option.lower() == "r":  
        option = True
# only admin is allowed to use this option
#request admin to login
        admin_login = False
        while not admin_login:
            admin = input("Please enter admin username : ")
            password = input("Please enter admin password : ")

            if admin == "admin" and password == "adm1n":  
                admin_login = True
                print("Welcome Admin")
            else:
                print("Please enter a valid username and password")

# when the admin logs on he can  add new users to the register
# open user.txt file to add new users
        user = open('user.txt', 'r+')
        
 # The admin will be requested to enter the username and password.
 # The admin will be requested to enter the password again for confirmation
        for lines in user:
            new_username = input("Please Enter new username : ")  
            new_password = input("Please enter new password : ")  
            confirm_password = input("Please enter password again : ")
            
#if password match the user is added to user list
            if confirm_password == new_password:  
                with open('user.txt', 'r+'):
                    user.write("\n" + new_username + ", " + new_password)
            else:
                print("Password do not match ")
            break
        user.close()
        
# If the user chooses 'a' to add a task, the user should be prompted to enter the usernamne of the person the task is assignned to, the title of the task'
# A description of the task and the due date of the task.
    elif option.lower() == "a":  # user choices to add task
        option = True
 # Open tasks.txt if user chooses add a task
        task = open('tasks.txt', 'r+')
        for line in task:
            temp = line.strip()
            temp = temp.split(", ")
            
 # Request user to enter task details
            username = input("Please enter the user task is assigined to : ")
            description = input("Please enter the description of task : ")
            date = input("Please enter the date that this task is being entered : ")
            due_date = input("Please enter the due date for task to be complete : ")
            complete = input("Please enter Yes or No if task was completed or not : ")

# Sorting the task details in tasks.txt
            task.write("\n" + username + ", " + description + ", " + date + ", " + due_date + ", " + complete)
            break

# If the user chooses 'va' to view all task, display the information for each task.
    elif option.lower() == "va":  
        option = True
# opening the tasks.txt
# We have to allign indices to each word in the task.
        tasks = open('tasks.txt', 'r+')
        for lines in tasks:
            temp = lines.strip()
            temp = temp.split(", ")  
            print("Username : ", temp[0])
            print("Description : ", temp[1])
            print("Date : ", temp[2])
            print("Due Date : ", temp[3])
            print("Complete : ", temp[4])
            print("\n")
        tasks.close()

# If the user chooses 'vm' to vie the taska that are assigned to them, only display all the task tha have been asigned to the user
# That is currently logged in.
    elif option.lower() == "vm":  
        option = True
        tasks = open('tasks.txt', 'r+')
        for lines in tasks:
            user, description, date, due_date, complete = lines.split(", ")  
            if username == user:  # if usersname is in the the details show the  user tasks
                print("Username : ", user)
                print("Description : ", description)
                print("Date : ", date)
                print("Due Date : ", due_date)
                print("Complete : ", complete)
                print("\n")
        tasks.seek(0)
        tasks.close()
# Only the user with the username 'admin' is allowed to register a user      
# The admin user is provided with a menu optiom that allows them to display statistics
# When the menu otpion is selected, the total number of tasks and tje total number of users should be displayed.
    elif option.lower() == "s":  
# admin only will be allowed to use this option
        if username == "admin":  
            option = True
            user = open('user.txt', 'r')
            total_users = 0
            for lines in user:  
                total_user = lines.split()
                total_users += 1
                print("Total Number of Users: " + str(total_users))
            user.seek(0)

            tasks = "tasks.txt"
            total_tasks = 0
            with open(tasks, 'r') as task:
                for i in task:  # show the number of task in task.txt file
                    total = i.split()
                    total_tasks = total_tasks + 1
                    print("Total.Task: " + str(total_tasks))
                task.seek(0)
                break

# This will be displayed to the users, that this option is for admin only
        else:
            print("Only admin is allowed\n")  

    elif option.lower() == "e":  # exit option  stops running once this option is selected
        option = True
        print("Thank you!!")
        break  # allows menu to show again for every option beside the exit option

    else:
        option = False
        print("Please enter a valid option")  # user only allowed to enter options shown on the menu
