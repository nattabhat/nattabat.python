with open("story.txt", "r") as f: # using with will close the file automatically
    story = f.read()

words = set()
# to make all strings added to words unique, we must set()
start_of_word = -1

target_start = "<"
target_end = ">"

#Next step is finding all <> inside the story.txt
for i, char in enumerate(story): #enumertate gives access to the positions and their elements
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

#Next step, ask user to input replacement words by set up dictionary {}
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)