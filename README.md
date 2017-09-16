# NimmtAI

This is a plotform for playing Nimmt with your AI.  
You can make your own AI by inherit Player class in player.py and correct game.py.  
You can check the strength of your AI by excuting "python game.py".  

By default, four greedy player play game.  
You can see games by "python game.py".  
Cards are showed like "(5, 2)".  
This means that the number of card is 5 and the point of card is 2.

This is an example of a game.  
```
..............................
..............................

----------- turn  9 ----------
(5, 2) (6, 1)
(19, 1) (20, 3) (26, 1) (27, 1) (30, 3)
(58, 1) (59, 1) (62, 1) (67, 1) (70, 3)
(60, 3) (90, 3)
(85, 2) (86, 1) (88, 5) (91, 1) (99, 5)
player  0 shows  (96, 1)
player  1 shows  (100, 3)
player  2 shows  (15, 2)
player  3 shows  (102, 1)
point of player  0 is  4
point of player  1 is  24
point of player  2 is  18
point of player  3 is  0
----------- turn  10 ----------
(5, 2) (6, 1) (15, 2)
(19, 1) (20, 3) (26, 1) (27, 1) (30, 3)
(58, 1) (59, 1) (62, 1) (67, 1) (70, 3)
(60, 3) (90, 3) (96, 1)
(100, 3) (102, 1)
player  0 shows  (52, 1)
player  1 shows  (104, 1)
player  2 shows  (17, 1)
player  3 shows  (103, 1)
point of player  0 is  13
point of player  1 is  24
point of player  2 is  18
point of player  3 is  0
----------- result ----------
sum of point of player  0 is  1227
sum of point of player  1 is  966
sum of point of player  2 is  1143
sum of point of player  3 is  1253
```
