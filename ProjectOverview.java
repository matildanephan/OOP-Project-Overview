import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.DateFormat;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Date;
import java.util.Scanner;

public class ProjectOverview {

   //This is the main method of the program

   public static void main( String[] args) {

       //Creating a array list
       
        ArrayList<Project> ProjectArray = new ArrayList<Project>();

       //Reading file and writing to array list
       
       try (BufferedReader ProjectReader = new BufferedReader(new FileReader("CompletedTasks.txt"))) {
           while (ProjectReader.ready()) {
 
               //Creating a temporary array to convert items in file from string to different
               //data types
               
                String[] temp = ProjectReader.readLine().split("#");
                Person Architect = new Person(temp[10], temp[11], Integer.parseInt(temp[12]), temp[13], temp[14]);
                Person Customer = new Person(temp[15], temp[16], Integer.parseInt(temp[17]), temp[18], temp[19]);
                Person Contractor = new Person(temp[20], temp[21], Integer.parseInt(temp[22]), temp[23], temp[24]);

               //Format string to date
               
                DateFormat df = DateFormat.getDateInstance();
                Date completionDate = null;
                try {
                   completionDate = df.parse(temp[9]);
                } catch ( ParseException e) {
                   System.out.println("No date item found in file");
                }
                Project tempProj = new Project(Integer.parseInt(temp[0]), temp[1], temp[2], temp[3],
                       Integer.parseInt(temp[4]), Double.parseDouble(temp[5]), Double.parseDouble(temp[6]), temp[7],
                       temp[8], completionDate, Architect, Customer, Contractor);
                ProjectArray.add(tempProj);

           }
       }catch ( IOException e) {

           //Handles a potential exception
        
           System.out.println("File not found");
       }

       //Output message to User
       
       System.out.println("==========Project Management System==========");

      // while (true) {

           //User Menu
           
            System.out.println("Please make a selection from the menu:" + "\n1. Create a new project:"
                   + "\n2. Change the due date of the project:" + "\n3. Change the total number of the fee paid:"
                   + "\n4. Update contractors contact details" + "\n5. View completed projects"
                   + "\n6. View uncompleted tasks" + "\n7. Revise Project:" + "\n8. Exit Program");

           //Call scanner class to capture input
           
            Scanner input = new Scanner(System.in);
            String userChoice = input.nextLine();

            if (userChoice.equals("1")) {

               //Enter new project number used try and catch block to make sure user enter a
               //correct format
               
                int typedProjectNumber = 0;
                while (true) {
                    try {
                       System.out.println("Enter Project Number:");
                       typedProjectNumber = input.nextInt();
                       input.nextLine();
                       break;

                    } catch ( Exception e) {
                       System.out.println("Please enter correct format");
                       input.next();
                    }
                }

               //Enter new project name
               
                System.out.println("Enter Project Name: ");
                String typedProjectName = input.nextLine();

               
                //Enter building type
               
                System.out.println("Enter building type: ");
                String typedBuildingType = input.nextLine();

               
                //Enter physical address
               
                System.out.println("Enter project physical address: ");
                String typedProjectAddress = input.nextLine();

               //Enter Erf number added a try and catch block to make sure user enters a
               //correct format
               
                int typedErfNumber = 0;
                while (true) {
                    try {
                       System.out.println("Enter Erf Number: ");
                       typedErfNumber = input.nextInt();
                       input.nextLine();
                       break;
                    } catch ( Exception e) {
                       System.out.println("Please enter correct format");
                       input.next();
                    }
                }

               //Enter total fee
               
                Double typedTotalFee = 0.0;
                while (true) {
                    try {
                       System.out.println("Enter project total fee (numbers only): ");
                       typedTotalFee = input.nextDouble();
                       input.nextLine();
                       break;
                    }  catch ( Exception e) {
                       System.out.println("Please enter correct format");
                       input.next();
                    }
                }

                //Enter amount paid by customer added try and catch to make sure user enters
                //correct format
               
                Double typedTotalPaid = 0.0;
                while (true) {
                    try {
                        System.out.println("Enter amount paid by customer (number only): ");
                        typedTotalPaid = input.nextDouble();
                        input.nextLine();
                        break;
                    } catch ( Exception e) {
                        System.out.println("Please enter correct format");
                        input.next();
                    }
               }

               //Enter project deadline
               
                System.out.println("Enter due date for example 12 July 2019: ");
                String typedProjectDeadline = input.nextLine();

                //Set project completed to no
               
                String projectCompleted = ("No");
                Date defaultDate = null;

                //Get architect inputs
               
                System.out.println("Enter Architect name:");
                String architectName = input.nextLine();

                System.out.println("Enter Architect surname:");
                String architectSurname = input.nextLine();

                //Added try catch block to make sure user inputs correct format
               
                int architectPhoneNumber = 0;
                while (true) {
                    try {
                       System.out.println("Enter Architect phone number");
                       architectPhoneNumber = input.nextInt();
                       input.nextLine();
                       break;

                    }   catch ( Exception e) {
                        System.out.println("Please enter correct format");
                        input.next();
                    }
               }

                System.out.println("Enter Architect email address:");
                String architectEmail = input.nextLine();

                System.out.println("Enter Architect address:");
                String architectAddress = input.nextLine();

                //Get Customer inputs
               
                System.out.println("Enter Customer name:");
                String customerName = input.nextLine();

                System.out.println("Enter Customer surname:");
                String customerSurname = input.nextLine();

                //Added try catch block to make sure user inputs correct format
               
                int customerPhoneNumber = 0;
                while (true) {
                    try {
                       System.out.println("Enter Customer number:");
                       customerPhoneNumber = input.nextInt();
                       input.nextLine();
                       break;
                    } catch ( Exception e) {
                       System.out.println("Please enter correct format");
                       input.next();
                    }
                }

                System.out.println("Enter Customer email address");
                String customerEmail = input.nextLine();

                System.out.println("Enter Customer address");
                String customerAddress = input.nextLine();

                //Get Contractor inputs
               
                System.out.println("Enter Contractor name");
                String contractorName = input.nextLine();

                System.out.println("Enter Contractor surname:");
                String contractorSurname = input.nextLine();

                //Added try catch block to make sure user inputs correct format
               
                int contractorNumber = 0;
                while (true) {
                try {
                       System.out.println("Enter Contractor number:");
                       contractorNumber = input.nextInt();
                       input.nextLine();
                       break;
                    }  catch ( Exception e) {
                       System.out.println("Please enter correct format");
                       input.next();
                    }
                }

                System.out.println("Enter Contrator email address:");
                String contractorEmail = input.nextLine();

                System.out.println("Enter Contractor address:");
                String contractorAddress = input.nextLine();

                //Create Architect
               
                Person Architect = new Person(architectName, architectSurname, architectPhoneNumber, architectEmail,
                       architectAddress);

                //Create Customer
               
                Person Customer = new Person(customerName, customerSurname, customerPhoneNumber, customerEmail,
                       customerAddress);

                //Create Contractor
               
                Person Contractor = new Person(contractorName, contractorSurname, contractorNumber, contractorEmail,
                       contractorAddress);
             
                //Create Project
               
                Project newProject = new Project(typedProjectNumber, typedProjectName, typedBuildingType,
                       typedProjectAddress, typedErfNumber, typedTotalFee, typedTotalPaid, typedProjectDeadline,
                       projectCompleted, defaultDate, Architect, Customer, Contractor);

                ProjectArray.add(newProject);
              
                //Printing message to customer and displaying the project
               
                System.out.println("\nNew project has been created!");
                System.out.println(newProject.toString());
             
                //If user does not enter project name
               
                if (typedProjectName.equals("")) {
                   newProject.setProjectName(typedBuildingType + " " + customerSurname);

                }
            }

            else if (userChoice.equals("2")) {

               
                //Ask customer which project they want to change deadline
               
                int deadlineIndex = 0;
                while (true) {
                    try {
                       System.out.println("Please enter project you want to edit by index:");
                       deadlineIndex = input.nextInt();
                       input.nextLine();
                       deadlineIndex = deadlineIndex - 1;
                       break;
                    } catch ( Exception e) {
                       System.out.println("Enter correct format:");
                       input.next();
                    }
                }            
               
                //Change due date of the project
               
                System.out.println("Enter new project deadline date for example 15 July 2020:");
                String newDeadline = input.nextLine();
          
                //Setting new deadline in array
               
                ProjectArray.get(deadlineIndex).setDeadline(newDeadline);
               
                //Output updated project to user
               
                System.out.println(ProjectArray.get(deadlineIndex).toString());
            }

            else if (userChoice.equals("3")) {
          
                //Asking user which project they want to change the fee paid for
               
                int feePaidIndex = 0;
                while(true) {
                   try {
                System.out.println("Please enter project you want to edit by index:");
                feePaidIndex = input.nextInt();
                input.nextLine();
                feePaidIndex = feePaidIndex - 1;
                break;
                    }
                    catch( Exception e) {
                        System.out.println("Enter correct format:");
                        input.next();
                    }
                }         
               
                //Change fee paid used try and catch block to determine correct input
               
                Double newFeePaid = 0.0;
                while (true) {
                    try {
                        System.out.println("Enter new fee paid by the customer:");
                        newFeePaid = input.nextDouble();
                        input.nextLine();

                       /**
                       * Set amount paid in array list
                       */
                       ProjectArray.get(feePaidIndex).setAmountPaid(newFeePaid);
                       break;
                    }

                    catch ( Exception e) {
                        System.out.println("Please enter correct format");
                        input.next();
                    }
                }
               
                //Displaying updated project to user
                
                System.out.println(ProjectArray.get(feePaidIndex).toString());
            }

            else if (userChoice.equals("4")) {
                            
                //Asking user which project contractor they want to edit according to index
                
                int contractorIndex = 0;
                while(true) {
                try {
                System.out.println("Please enter project you want to edit by index:");
                contractorIndex = input.nextInt();
                input.nextLine();
                contractorIndex = contractorIndex - 1;
                break;
                }
                catch( Exception e) {
                    System.out.println("Enter correct format:");
                    input.next();
                    }
                }
                            
                    //Update contractors details
                
                //Change telephone number used try and catch block to determine correct input
                
                int newPhoneNumber = 0;
                while (true) {
                    try {
                        System.out.println("Enter new contractors phone number:");
                        newPhoneNumber = input.nextInt();
                        input.nextLine();
                        ProjectArray.get(contractorIndex).Contractor.setTelephoneNumber(newPhoneNumber);
                        break;
                    } catch ( Exception e) {
                        System.out.println("Please enter correct format");
                        input.next();
                    }
                }

                //Change email address
                
                System.out.println("Enter new contractors email address:");
                    String newEmailAddress = input.nextLine();
                ProjectArray.get(contractorIndex).Contractor.setEmailAddress(newEmailAddress);

                    //Display updated contractor to user
                
                System.out.println(ProjectArray.get(contractorIndex).Contractor.toString());
            } else if (userChoice.equals("5")) {

                //Looping through array to print completed projects
                
                for (int i = 0; i < ProjectArray.size(); i++) {
                    if (ProjectArray.get(i).projectCompleted.equals("Yes")) {
                        System.out.println(ProjectArray.get(i).toString());
                    }
                }
            } else if (userChoice.contentEquals("6")) {

                
                //Looping through array to print uncompleted projects
                
                for (int i = 0; i < ProjectArray.size(); i++) {
                    if (ProjectArray.get(i).projectCompleted.equals("No")) {
                        System.out.println(ProjectArray.get(i).toString());
                    }
                }
            } else if (userChoice.equals("7")) {

                //Asking user which project they want to edit according to index
                
                int isedIndex = 0;
                while(true) {
                    try {
                System.out.println("Please enter project you want to edit by index:");
                isedIndex = input.nextInt();
                input.nextLine();
                isedIndex = isedIndex - 1;
                break;
                    }
                    catch( Exception e) {
                        System.out.println("Please enter correct format");
                        input.next();
                    }
                }
                
                //Created date variable
                
                    Date currentDate = new Date();

                //Defined difference and calculating difference
                
                Double Difference = 0.0;
                Difference = ProjectArray.get(isedIndex).totalFee - ProjectArray.get(isedIndex).amountPaid;

                if (Difference == 0) {
    
                    //Displaying message to user and setting project as completed
                    
                    System.out.println("No invoice is needed marking project as completed");
                    ProjectArray.get(isedIndex).setProjectCompleted("Yes");
                    ProjectArray.get(isedIndex).setDateCompleted(currentDate);
                } else {
                    System.out.println("Invoice generated");
                    System.out.println(ProjectArray.get(isedIndex).Customer.toString());
                    System.out.println("Your amount owed is R" + Difference);
                }

            } else if (userChoice.equals("8")) {

                //Exiting loop
                
                //break;

            } else {
                System.out.println("Incorrect selection made try again");
            }

            input.close();
    
            }

        }
 