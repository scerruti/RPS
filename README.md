# Rock, Paper, Scissors Assignment:

**Learning objective:** Scholars will demonstrate the ability to apply Python selection statements to implement a real-world game inside their webserver projects.

**Standards** :

*9-12.AP.12* Design algorithms to solve computational problems using a combination of original and existing algorithms.

*9-12S.AP.25* Use version control systems, integrated development environments (IDEs), and collaborative tools and practices (e.g., code documentation) while developing software within a group.

**Instructions** : Write the `play_rps` function to complete the RPS game for your Python webserver. Document how your code works and submit the final version on GitHub classroom. View your pull request to see the feedback on your submission.

# Step 1. Define the Problem

Explain the game of rock, paper, and scissors. Provide examples of how you win and how you lose. Include your understanding of the purpose of the `play_rps` function.

|                       |
|-----------------------|

# Step 2: Plan the Solution

1. Complete this table to list all of the possible outcomes of the game.

| Player 1 | Player 2 | Result |
| --- | --- | --- |
| Rock | Rock | Tie |
| Rock | Paper | Player 2 Wins |
| Rock | Scissors | Player 1 Wins |
| Paper | Rock |
 |
| Paper | Paper |
 |
| Paper | Scissors |
 |
| Scissors | Rock |
 |
| Scissors | Paper |
 |
| Scissors | Scissors |
 |

2. Write pseudocode of your solution.

|                    |
|--------------------|

# Step 3: Implement your Plan

1. Add the project files to your existing webserver project.
2. Run your project and navigate to [http://localhost:8080/rps\_game.html](http://localhost:8080/rps_game.html), you should be able to play a game of rock, paper, scissors but you will always win.
3. Write your Python solution in the appropriate place in rps.py, be sure to document your code.

# Step 4: Reflect

1. Test and debug your solution.
2. You can modify this URL [http://localhost:8080/rps?yourMove=paper&myMove=paper](http://localhost:8080/rps?yourMove=paper&myMove=paper) to directly compare outcomes to your table above.
3. Get a code review from a classmate or TA. Implement a suggestion for improvement. Name of the reviewer:

|                            |
|----------------------------|

4. Check your work against the rubric before submitting.

# Rubric

| Category | Extensive Evidence<br> (4 points)                                                                                                                            | Significant Evidence<br> (3 points) | Limited Evidence<br> (2 points) | No Evidence<br> (1 point)                                                                                      |
| --- |--------------------------------------------------------------------------------------------------------------------------------------------------------------| --- | --- |------------------------------------------------------------------------------------------------------------|
| Activity Guide | The activity guide is filled out and demonstrates work was completed for each step.                                                                          | The activity guide was mostly filled out. | One section of the activity guide was completed. | The activity guide was not completed.                                                                      |
| Correct Algorithm | The algorithm is correct for all cases.                                                                                                                      | The algorithm is correct for most cases. | The algorithm is correct for some cases. | The algorithm rarely generates the correct response, the code does not run or no submission was turned in. |
| Code Neatness and Documentation | Code contained documentation explain the algorithm, variable and function names followed convention and whitespace was used to make the code easier to read. | Code contained documentation explain the algorithm and either variable and function names followed convention or whitespace was used to make the code easier to read. | Code contained documentation explain the algorithm or variable and function names followed convention or whitespace was used to make the code easier to read. | The code did not demonstrate care regarding format, naming or documentation.                               |
| Selection Statements | Both elif and nested ifs were used.                                                                                                                          | Either elif or nested ifs were used. | If statements were used. | No if statement was used, even if the algorithm works.                                                     |

# Extension Investigation

While you are encouraged to complete the extension activities, please remember to turn in a solution to be scored against the rubric and not one that demonstrates extension.

**Rock, Paper, Scissors is Math**

It is possible to represent the moves as numeric values and use math to implement a solution to rock paper scissors. For example, if rock is 1 and paper is 2 then paper – rock is positive and rock – paper is negative.

1. Return to step 2 and plan a solution that relies entirely on a mathematical expression to solve the issue.
2. What is one reason a computer scientist might give to argue that a solution with an if statement would be better than a mathematical solution in this case?

**Rock, Paper, Scissors, Lizard, Spock**

The television show The Big Bang Theory popularized a version of the game with five moves. Research the game and attempt to implement a solution.

1. Predict, does the number of outcomes increase linearly or exponentially from 3 moves to 5 moves?
2. Construct a table to demonstrate the answer.