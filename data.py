dictionary = 'dictionary.txt'

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

letter_score = {letter:score for score,letters in scrabble_scores for letter in letters.split()}
letter_score.update({letter.lower():score for score,letters in scrabble_scores for letter in letters.split()})