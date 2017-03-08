# User Guide for 2048 AI
By Jianpu Ma jm4437

###Introduction 
This is the python program for Columbia University Artificial Intelligent class, simnlating the 2048 game process between the Computer
and User, we implement a strategy to automatically play the game with computer and see the final result.

###Runing guide
To run the program, simply type $ python GameManager.py, and the whole process will be displayed in the terminal screen.

###Game Performance
The best performance for this Algorithm has reached 4096 as the screenshot shows.


According to the result running the program 20 times,it has a possibility of to reach 2048
1024
512
1024
1024
1024
512
2048
1024
1024
2048
2048
1024
1024
2048
1024
1024
2048
512
1024
2048


###Algorithm overview
The 2048 game use the mini-max pruning algorithm and heuristic funcition by empty tile number and snake-route weight with bonus penalty score in evaluating the possible move

###Evaluation 
The minimax pruning with heuristic has significant different between the vanilla minimax according to our comparison,while the vanilla minimax can't even reach the 2048, yet with heuristic it has a chance of reaching 2048







