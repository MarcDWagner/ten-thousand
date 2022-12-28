import collections
import random

points_table = {
        1: {
            1: 100,
            2: 200,
            3: 1000,
            4: 2000,
            5: 4000,
            6: 8000
        },
        2: {
            3: 200,
            4: 400,
            5: 800,
            6: 1600
        },
        3: {
            3: 300,
            4: 600,
            5: 1200,
            6: 2400
        },
        4: {
            3: 400,
            4: 800,
            5: 1200,
            6: 1600
        },
        5: {
            1: 50,
            2: 100,
            3: 500,
            4: 1000,
            5: 1500,
            6: 2000
        },
        6: {
            3: 600,
            4: 1200,
            5: 1800,
            6: 2400
        }
    }


class GameLogic:
    def __init__(self):

        def calculate_score(self, choices):
            score = 0
            self.choices = choices

    # def roll_dice(amount):
    #     dice_min = 1
    #     dice_max = 6
