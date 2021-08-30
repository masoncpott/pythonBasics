def sentence_maker(phrase):
    interrogatives = ("How", "What", "Why", "Where")
    phrase = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(phrase)
    else:
        return "{}.".format(phrase)

print(sentence_maker("how are you")) #returns "How are you?"

results = []
while True:
    user_input = input("Say something: ")
    if user_input == 'end':
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))