import pygame
import csv
from datetime import date

today = date.today()

# Read high scores from csv-file and return a list sorted by highest score:s
def read_hiscores():
    high_scores = []
    with open("hiscores.csv", newline = "", encoding = "utf8") as document:
        for row in csv.reader(document, delimiter = ";"):
            high_scores.append([int(row[0]), row[1], row[2]])
    return sorted(high_scores, reverse = True)

# Add a new score to csv-file:
def write_hiscores(player_name, game_score):
    name = player_name
    if len(name) > 20:
        name = name[0:20]
    if len(name) == 0:
        name = "Player"
    score = game_score
    date = today.strftime("%d %b %Y")
    with open("hiscores.csv", "a", newline = "", encoding = "utf8") as document:
        save_score = csv.writer(document, delimiter = ";")
        save_score.writerow([score, name, date])

# Check if the new score is a high score:       
def check_highscore(score):
    high_scores = []
    with open("hiscores.csv", newline = "", encoding = "utf8") as document:
        for row in csv.reader(document, delimiter = ";"):
            high_scores.append(int(row[0]))
    high_scores.sort(reverse = True)
    if len(high_scores) == 0 or score > high_scores[0]:
        return True
