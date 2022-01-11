import random
import time
import os
from enum import Enum


class SlotMachine:
    INITIAL_STAKE = 50
    INITIAL_JACKPOT = 1000

    class Reel(Enum):
        CHERRY = 1
        LEMON = 2
        ORANGE = 3
        PLUM = 4
        BELL = 5
        BAR = 6
        SEVEN = 7

    _values = list(Reel)
    payout = {
        Reel.CHERRY: 7,
        Reel.ORANGE: 10,
        Reel.PLUM: 14,
        Reel.BELL: 20,
        Reel.BAR: 250,
        Reel.SEVEN: 'jackpot'
    }

    def __init__(self, stake=INITIAL_STAKE, jackpot=INITIAL_JACKPOT):
        self.current_stake = stake
        self.current_jackpot = jackpot

   