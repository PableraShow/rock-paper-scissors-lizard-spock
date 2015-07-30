# Rock paper scissors lizard Spock game

The game
-------
It is first used to settle a dispute about what to watch on TV between Sheldon and Raj in "The Lizard-Spock Expansion".
It is mentioned again in "The Euclid Alternative" and "The Rothman Disintegration", where Sheldon explains the rules to Penny and Barry Kripke.

The game was originally created by Sam Kass with Karen Bryla. According to an interview with Kass, the series producers did not originally ask for permission to use the game, but Kass was officially referenced by Sheldon as the creator of the game during the "The Rothman Disintegration", after which he states, "Hail Sam Kass!" to which Leonard, Howard, Raj, and Sheldon all then chant "Hail!" while raising their hands.

Rules
-------
![png](images/rock-paper-scissors-lizard-spock.png)
<img src="https://github.com/PableraShow/rock-paper-scissors-lizard-spock/images/rock-paper-scissors-lizard-spock.png" width="400px" height="400px" alt="rock-paper-scissors-lizard-spock">

The game is an expansion on the game Rock, Paper, Scissors. Each player picks a variable and reveals it at the same time. The winner is the one who defeats the others. In a tie, the process is repeated until a winner is found. Almost always, the boys will all pick Spock at the same time and tie over and over again.

Mini-project development process requirements
-------
Build a helper function name_to_number(name) that converts the string name into a number between 0 and 4 as described above. This function should use a sequence of if/elif/else clauses. You can use conditions of the form name == 'paper', etc. to distinguish the cases. To make debugging your code easier, we suggest including a final else clause that catches cases when name does not match any of the five correct input strings and prints an appropriate error message. You can test your implementation of name_to_number() using this name_to_number testing template. (Also available in the Code Clinic tips thread).
Next, you should build a second helper function number_to_name(number) that converts a number in the range 0 to 4 into its corresponding name as a string. Again, we suggest including a final else clause that catches cases when number is not in the correct range.
Implement the first part of the main function rpsls(player_choice). Print out a blank line (to separate consecutive games) followed by a line with an appropriate message describing the player's choice. Then compute the number player_number between 0 and 4 corresponding to the player's choice by calling the helper function name_to_number() using player_choice.
Implement the second part of rpsls() that generates the computer's guess and prints out an appropriate message for that guess. In particular, compute a random number comp_number between 0 and 4 that corresponds to the computer's guess using the function random.randrange(). Then compute the name comp_choice corresponding to the computer's number using the function number_to_name() and print an appropriate message with the computer's choice to the console.
Implement the last part of rpsls() that determines and prints out the winner. Specifically, compute the difference between comp_number and player_number taken modulo five. Then write an if/elif/else statement whose conditions test the various possible values of this difference and then prints an appropriate message concerning the winner. If you have trouble deriving the conditions for the clauses of this if/elif/else statement, we suggest reviewing the "RPSLS" video which describes a simple test for determine the winner of RPSLS.
This will be the only mini-project in the class that is not an interactive game. Since we have not yet learned enough to allow you to play the game interactively, you will simply call your rpsls function repeatedly in the program with different player choices. You will see that we have provided five such calls at the bottom of the template. Running your program repeatedly should generate different computer guesses and different winners each time. While you are testing, feel free to modify those calls, but make sure they are restored when you hand in your mini-project, as your peer assessors will expect them to be there.

The output of running your program should have the following form:
    Player chooses rock
    Computer chooses scissors
    Player wins!

    Player chooses Spock
    Computer chooses lizard
    Computer wins!

    Player chooses paper
    Computer chooses lizard
    Computer wins!

    Player chooses lizard
    Computer chooses scissors
    Computer wins!

    Player chooses scissors
    Computer chooses Spock
    Computer wins!
