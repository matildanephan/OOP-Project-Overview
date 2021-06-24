# We are creating a program to manage tasks.
# Only the admin with the username and password "admin" can log into the system.
# In the program the admin can view all the tasks and registered users.
# All the members' task can be seen as well as on a individual basis
# New users will be created by the admin
# Then there is also menu options for viewing statisticks and general reports.
# Other details are in external txt files for more information.
# We also have a list of user/members, the status of tasks, and statistics 

import datetime
import os.path

print('\t\t-== TASK MANAGER ==-\n')
print("LOGIN")

# Here we need to ask for username and password
def login():
    valid_user_and_pass = False

    while valid_user_and_pass == False:    
# The use.txt file needs to be opened.e
        userfile = open('user.txt', 'r+', encoding='utf-8')
# We are going to use a global username variable for use later
        global username
        username = input("Please enter your username: ").lower()
        password = input(f"Hello {username}, please enter your password: ")
        for user in userfile:
            userlist = user.strip().replace("\n", "").split(', ')
            if username == userlist[0] and password == userlist[1]:
                valid_user_and_pass = True
                print("You have logged in!\n")
                userfile.close()
                menu()
        if not valid_user_and_pass:
            print("Invalid username and password, please try again.\n")

# Here is our menu
def menu():
    print("Please select one of the following options:\n")
    print("r   - \tRegister User")
    print("a   - \tAdd Task")
    print("va  - \tview all tasks")
    print("vm  - \tview my tasks")
    
    if username == 'admin':
        print("gr - \tgenerate reports")
        print("ds   - \tdisplay statistics")

    print("s   - \tsign-out\n")
    print("e   - \texit\n")
    
    user_option = input("Selection: ").lower()
    user_menu_option(user_option)

# We have user options, the user will choose any of the options according to want they need
def user_menu_option(option):
    if option == 'r' and username == 'admin':
        reg_user()
    elif option == 'r' and username != 'admin':
        print(f"{username} is not authorised to register new users.")
        menu()
    elif option == 'a':
        add_task()
    elif option == 'va':
        view_all()
    elif option == 'vm':
        view_mine()
    elif option == 'ds' and username == 'admin':
        display_admin_stats()
    elif option == 'gr' and username == 'admin':
        generate_reports_admin()
    elif option == 'e':
        print('Good-Bye')
        exit()
    elif option == 's':
        print("Signed out.")
        login()
    elif (option != 'r') and (option != 'a') and (option != 'va') and (option != 'vm') and (option != 'ds') and (option != 'gr') and (option != 'e') and (option != 's'):
        print("-== Invalid selection, please try again ==- ")
        menu()

# When the user opt to exit and go back to the main menu
def exit_menu():
    menu_back = input("Back to the menu, N to exit? Y/N: ").lower()
    
    while menu_back != 'n' and menu_back != 'y':
        menu_back = input("Invalid selection, back to the menu, N to exit? Y/N: ")
    
    if menu_back == 'n':
        print("Good-bye.")
        exit()
    elif menu_back == 'y':
        menu()

# When there is need to verify whether the user already exist in the file to avoid duplication
def user_check(user):
    user_dictionary = user_dict()
        
    for count in user_dictionary:
        user_exist = user_dictionary[count]
        if user == user_exist['username']:
            print(f"{user} already exists, please try again.")
            reg_user()
            
# New user registration, whe we need to add a new user to the file.
def reg_user():   
    userfile = open('user.txt', 'a+', encoding='utf-8')
    new_username = input("Please enter a new username to register: ")
    user_check(new_username)
    
# Ask the user for passwords for the new user and check if they are the same
# If not, try again, if yes, write new user and password to the file
    new_password = input("Please enter a new password: ")
    confirm_password = input("Please confirm the new password: ")
    if new_password == confirm_password:
        userfile.write(f"\n{new_username}, {new_password}")
        print(f"{new_username} has been registered!")
        userfile.close()
    else:
        print("\nPasswords do not match. Please try again.\n")
        reg_user()
    
    exit_menu()
    
# Add a task
def add_task():
    with open('tasks.txt', 'a+', encoding='utf-8') as taskfile:
        current_date = datetime.date.today()
        task_name = input("Please enter the title of the task: ")
        task_desc = input("Enter a description of the task: ")
        assigned_user = input("Please enter username of the person that the task is assigned to: ")
        task_due_date = input("Enter the due date of the task (eg: 4 february 2020): ")
        task_complete = "No"
        x = current_date.strftime("%d %b %Y") # Formatting the date to be day, monthh, year
# Write the above to the file
        taskfile.write(f"{assigned_user}, {task_name}, {task_desc}, {x}, {task_due_date}, {task_complete}")

    exit_menu()

# Create a dictionary of the tasks for use in later functions
def task_dict():
    with open('tasks.txt', 'r', encoding='utf-8') as taskfile:
            task_dictionary = {}
            
            for i,line in enumerate(taskfile):
                values = line.strip().split(', ')
                task_dictionary[i + 1] = {
                                            'username' : values[0],
                                            'task_desc' : values[1],
                                            'task_note' : values[2],
                                            'date_created': values[3],
                                            'date_due' : values[4],
                                            'task_complete' : values[5]
                                            }
    return task_dictionary

# We need to create a dictionary of the users for use in later functions
def user_dict():
    with open('user.txt', 'r', encoding='utf-8') as userfile:
            user_dictionary = {}
            
            for i,line in enumerate(userfile):
                values = line.strip().split(', ')
                user_dictionary[i + 1] = {
                                            'username' : values[0],
                                            'password' : values[1]
                                            }
    
    return user_dictionary

# Display all the tasks to the screen
# Call task_dict and loop through and print to screen        
def view_all():
    task_dictionary = task_dict()
        
    for count in task_dictionary:
        task = task_dictionary[count]
        
        print(f"{count}) Task: \t\t{task['task_desc']}")
        print(f"   Assigned to: \t{task['username']}")
        print(f"   Task description: \t{task['task_note']}")
        print(f"   Date assigned: \t{task['date_created']}")
        print(f"   Due date: \t\t{task['date_due']}")
        print(f"   Task Complete?: \t{task['task_complete']}")
        print('')
            
    exit_menu()

# Display only user specific tasks to the screen    
def view_mine():
    task_dictionary = task_dict()
    found = False
    user_tasks = []
    
    for count in task_dictionary:
        task = task_dictionary[count]
        if username == task['username']:
            print(f"{count}) Task: \t\t{task['task_desc']}")
            print(f"   Assigned to: \t{task['username']}")
            print(f"   Task description: \t{task['task_note']}")
            print(f"   Date assigned: \t{task['date_created']}")
            print(f"   Due date: \t\t{task['date_due']}")
            print(f"   Task Complete?: \t{task['task_complete']}")
            print('')
            user_tasks.append(count)
            found = True
    
    if not found:
        print(f"No tasks found for user {username}")
        exit_menu()
    
# Error checking, making sure the user can only edit his/her task
    user_option = int(input("Choose a task number to edit or type -1 to return to the menu: "))
    while user_option!= -1 and user_option not in user_tasks:
         user_option = int(input(f"Invalid option, choose a task number that belongs to user \"{username}\" or type -1 to return to the menu: "))
    
    if user_option != -1 and user_option in user_tasks:
        edit_user_task(user_option,task_dictionary)
    elif user_option == -1:
        menu()

# Edit the task based on user choice in view_mine()           
def edit_user_task(x,dictionary): 
    print("-==  Options  ==-\n")
    print("1) Mark the task as complete")
    print("2) Edit the task")
    print("3) Back to main menu\n")
    user_option = input(f"Edit task ({x}) or mark as complete?: ")

    # Checking that the task isn't marked complete already
    # If it is, display the error, if not, mark as complete
    if user_option == '1':
        if dictionary[x]['task_complete'] == 'Yes':
                print("Task already complete, cannot set to complete again.")
        else:
            dictionary[x]['task_complete'] = 'Yes'
            print(f"Task \"{dictionary[x]['task_desc']}\" marked as complete.")
        
    elif user_option == '2':
            # Same error check as above
            if dictionary[x]['task_complete'] == 'Yes':
                print("Task already complete, cannot edit.")
                exit_menu()
                
            print("-==  Options  ==-\n")
            print(f"1) Change the user the task \"{dictionary[x]['task_desc']}\" is assigned to")
            print(f"2) Change the due date for \"{dictionary[x]['task_desc']}\"")
            print("3) Back to main menu\n")
            user_option_change = input(f"Your choice?: ")
            
            if user_option_change == '1':
                new_username = input(f"Please enter the new user to which the task \"{dictionary[x]['task_desc']}\" will be assigned: ")    
                dictionary[x]['username'] = new_username
            elif user_option_change== '2':
                new_due_date = input(f"Please enter the new due date for task \"{dictionary[x]['task_desc']}\": ")
                dictionary[x]['date_due'] = new_due_date
            elif user_option == '3':
                menu()
                
    elif user_option == '3':
        menu()
    
    with open('tasks.txt', 'w', encoding='utf-8') as task_file:
        for count in dictionary:
            task_file.write(f"{dictionary[count]['username']}, {dictionary[count]['task_desc']}, {dictionary[count]['task_note']}, {dictionary[count]['date_created']}, {dictionary[count]['date_due']}, {dictionary[count]['task_complete']}\n")
    
    exit_menu()

# We need to display only admin specific statistics to the screen
def display_admin_stats():
    if not os.path.exists('task_overview.txt') and not os.path.exists('user_overview.txt'):
        generate_task_overview()
        generate_user_overview()
    
    print("\t\t -== statistics ==-\n")
    user_dictionary = user_dict()
    task_dictionary = task_dict()
    
    print(f"Total number of tasks: {len(task_dictionary)}")
    print(f"Total number of users: {len(user_dictionary)}")
            
    with open('task_overview.txt', 'r', encoding='utf-8') as task:
        print('\n\t\t -== TASK OVERVIEW ==-\n')
        for line in task:
            print(line.strip())
        
    with open('user_overview.txt', 'r', encoding='utf-8') as task:
        print('\n\t\t -== USER OVERVIEW ==-\n')
        for line in task:
            print(line.strip())
            
    exit_menu()

# Here we are generating the task overview text file
def generate_task_overview():
    task_dictionary = task_dict()
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    
# Open the file, creates it if it doesn't exist
# Reads each task from the task_dict function
# And applies the logic to write to the file
    with open('task_overview.txt', 'w', encoding='utf-8') as task_overview:
        for count in task_dictionary:
            task = task_dictionary[count]
            if 'Yes' == task['task_complete']:
                completed_tasks += 1
            elif 'No' == task['task_complete']:
                uncompleted_tasks += 1
            
            # Comparing the dates to check if the task is overdue
            datetime_object = datetime.datetime.strptime(task['date_due'], '%d %b %Y')
            if datetime_object < datetime.datetime.today() and 'No' == task['task_complete']:
                overdue_tasks += 1
                
        percentage_incomplete = (uncompleted_tasks * 100) / (len(task_dictionary))
        percentage_overdue = (overdue_tasks * 100) / (len(task_dictionary))

        task_overview.write(f"Total number of tasks generated using Task Manager: {len(task_dictionary)}\n")
        task_overview.write(f"Number of completed tasks: {completed_tasks}\n")
        task_overview.write(f"Number of uncompleted tasks: {uncompleted_tasks}\n")
        task_overview.write(f"Number of uncompleted tasks that are overdue: {overdue_tasks:.0f}\n")
        task_overview.write(f"Percentage of uncompleted tasks: {percentage_incomplete:.0f}%\n")
        task_overview.write(f"Percentage of uncompleted overdue tasks: {percentage_overdue:.0f}%\n")
    
        print("Task_overview.txt written.")

#Here we are generating the user overview text file
def generate_user_overview():
    user_dictionary = user_dict()
    task_dictionary = task_dict()
    
    # Open the file, creates it if it doesn't exist
    # Reads each task from the task_dict function
    # And users from the user_dict function
    # And applies the logic to write to the file
    with open('user_overview.txt', 'w', encoding='utf-8') as user_overview:
        user_overview.write(f"Total number of users registered with Task Manager: {len(user_dictionary)}\n")
        user_overview.write(f"Total number of tasks generated using Task Manager: {len(task_dictionary)}")
        
        # Loops through users one by one and compares their name
        # To the name in the task and applies the logic
        for count in user_dictionary:
            tmp_user = user_dictionary[count]['username']

            task_counter = 0
            user_completed_tasks = 0
            user_uncompleted_tasks = 0
            overdue_tasks = 0
            for x in task_dictionary:
                task = task_dictionary[x]
                if tmp_user in task_dictionary[x]['username']:
                    task_counter +=1
                    if task['task_complete'] == 'Yes':
                        user_completed_tasks += 1
                    elif task['task_complete'] == 'No':
                        user_uncompleted_tasks += 1

                    # Compare due date to current date. If due date is older than current date
                    # And the task completed is No, increment overdue_tasks by 1
                    datetime_object = datetime.datetime.strptime(task['date_due'], '%d %b %Y')
                    if datetime_object < datetime.datetime.today() and 'No' == task['task_complete']:
                        overdue_tasks += 1
            
            # Calculate the required task percentages        
            if user_completed_tasks > 0:
                percent_tasks_completed = (float(user_completed_tasks) * 100) / float(task_counter)   
            elif user_completed_tasks == 0:
                percent_tasks_completed = 0
            
            if user_uncompleted_tasks > 0:
                percent_tasks_uncompleted = (float(user_uncompleted_tasks) * 100) / float(task_counter)   
            elif user_uncompleted_tasks == 0:
                percent_tasks_uncompleted = 0

            if overdue_tasks > 0:
                percentage_overdue = (overdue_tasks * 100) / (user_uncompleted_tasks)
            elif overdue_tasks == 0:
                percentage_overdue = 0
            
            # here we are printing everything to the file
            user_overview.write("\n")           
            user_overview.write(f"\nTotal tasks assigned to user \"{tmp_user}\": {task_counter}\n")
            user_overview.write(f"Percentage of total number of tasks assigned to user \"{tmp_user}\": {(float(task_counter) * 100) / float(len(task_dictionary)):.2f}%\n")
            user_overview.write(f"Percentage of tasks assigned to user \"{tmp_user}\" completed: {percent_tasks_completed:.2f}%\n")
            user_overview.write(f"Percentage of tasks assigned to user \"{tmp_user}\" not completed: {percent_tasks_uncompleted:.2f}%\n")
            user_overview.write(f"Percentage of tasks assigned to user \"{tmp_user}\" not completed and are overdue: {percentage_overdue:.2f}%")
            
        print("User_overview.txt written.")
    
#Here we are generating Reports for the admin user   
def generate_reports_admin():
    generate_task_overview()
    generate_user_overview()
    exit_menu()
    
login()

