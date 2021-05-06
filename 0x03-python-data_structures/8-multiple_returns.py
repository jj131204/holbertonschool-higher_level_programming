#!/usr/bin/python3
def multiple_returns(sentence):

    largue = len(sentence)
    if largue == 0:
        return (0, None)
    else:
        return (largue, sentence[0])
