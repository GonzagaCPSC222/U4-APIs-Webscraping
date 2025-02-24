import requests
import json
import html
import random

url = "https://opentdb.com/api.php?amount=5&category=20&difficulty=easy"

# make the HTTP GET request
response = requests.get(url)
print(response.text)
json_obj = json.loads(response.text)
results_list = json_obj["results"]
# TODO: print out the possible answers
# and look into html.unescape() to handle the &quot...
for result_obj in results_list:
    # GS adding after class
    print(html.unescape(result_obj["question"]))
    possible_answers = [result_obj["correct_answer"]] + result_obj["incorrect_answers"]
    random.shuffle(possible_answers)
    for i in range(len(possible_answers)):
        print(f"\t{chr(ord('a') + i)}) {possible_answers[i]}")
    # TODO: challenge: prompt the user for a guess and check their answer
    print()

