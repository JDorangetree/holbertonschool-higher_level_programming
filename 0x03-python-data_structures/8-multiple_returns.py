#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        x = len(sentence)
        y = sentence[0]
    else:
        y = ""
        x = 0
    packed = (x, y)
    return(packed)
