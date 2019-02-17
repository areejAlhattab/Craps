# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 01:08:40 2017

@author: lenovo
"""



from random import randrange

def rolling():
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    dice = dice1 + dice2
    return dice

def craps():
    diceNum = rolling()
    if diceNum == 7 or diceNum == 11:
        return True
    
    if diceNum == 2 or diceNum == 3 or diceNum == 12:
        return False
    
    while diceNum == 4 or diceNum == 5 or diceNum == 6 or diceNum == 8 or diceNum == 9 or diceNum == 10:
        diceNum2 = rolling()
        if diceNum2 == diceNum:
            return True
        if diceNum2 == 7:
            return False
        
    
    