# Wordle Game and Solver
original game: https://www.powerlanguage.co.uk/wordle/

## Play a game
```python
Python 3.8.10 (default, Nov 26 2021, 20:14:08) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from game import Game
>>> g = Game()
>>> g.guess("serai")
serai
'  .  '
>>> g.guess("brunt")
brunt
' X   '
>>> g.guess("pagod")
flood
'X  . '
>>> g.guess("mooli")
grovy
'  X  '
>>> g.guess("proxy")
proxy
'XXXXX'
```

## Original to compare
![game screenshot](/img/example_game.png)

## Solve a game
```python
Python 3.8.10 (default, Nov 26 2021, 20:14:08) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from solver import Solver
>>> s = Solver()
>>> s.get_next_guess()
'serai'
>>> s.game_result("serai", "  .  ")
214 solutions remain
>>> s.get_next_guess()
100%|###################################################################################################|
'brunt'
>>> s.game_result("brunt", " X   ")
26 solutions remain
>>> s.get_next_guess()
100%|###################################################################################################|
'pagod'
>>> s.game_result("pagod", "X  . ")
4 solutions remain
>>> s.get_next_guess()
100%|###################################################################################################|
'mooli'
>>> s.game_result("mooli", "  X  ")
1 solutions remain
>>> s.get_next_guess()
found the word!
total compute time: 22.981862545013428 seconds
'proxy'
```
