import java.util.Scanner;

public class timeDifference {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
         final int NUMBER = 5;        
		 int int2 = 0; int int1 = 0;long startTime = System.currentTimeMillis();
		 String wrongAnswer = " "; Scanner question = new Scanner(System.in);   // String1 were renamed to "wrongAnswe" and String2 were renamed to "question" to make it more descriptive.
			
			while (int1 < NUMBER) {      // The program will stop if there is 5 wrong answers by the user.

				int number1 = (int)(Math.random() * 10);
				int number2 = (int)(Math.random() * 10);
				
				if (number1 < number2) {     // in effect this block of code says if number1 < number2, swap number1 with number2
				int swap = number1;          // the original variable name "temp" were changed to "swap" to make the code more applicable to the process of swapping taking place.
				number1 = number2;
				number2 = swap;
				}
				System.out.print("What is " + number1 + " - " + number2 + "? ");    // ask the user what is number1 - number2
				int answer = question.nextInt();
				
				if (number1 - number2 == answer) {      
					System.out.println("You are correct");
				    int2++;
			    }
				else {
			     System.out.println("Your answer is wrong. \n" + number1 + " - " + number2 + " should be " + (number1 - number2));
			        int1++;
			        					
				wrongAnswer += "\n" + number1 + "-" + number2 + "=" + answer + ((number1 - number2 == answer) ? " correct" : " wrong");

			    }
		        long endTime = System.currentTimeMillis();   //The output will show the seconds taken for a iteration set in motion by the user.
		        
		        long testTime = endTime -  startTime;
		        System.out.println("Correct count is " + int2 + "\nTest time is " + testTime / 1000 + " seconds\n" + wrongAnswer);
			}
		}
    }




