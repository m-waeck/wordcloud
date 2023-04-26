from create_wc import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import itertools 
import os 
import re

filename = '_chat_michi.txt'
savefile = 'words_michi.txt'
rm_words = ['omitted', 'image', 'audio', 'video', 'sticker', 'gif', 'http']

# read in line by line
with open (filename, "r") as file:
    messages = []
    for line in file:
        messages.append(str(line[23:]).lower())

# delete first few irrelevant notifications
del messages[0:1]
# remove everything before colon and symbols
messages_only = []
for message in messages: 
    for char in message:
        if char == ':':
            message = re.sub(r'[^\w\s]', '', message)
            message = message.split()
            messages_only.append(message)
            break 
        else:
            message = message[1:]
            # messages_only.append(message)

# conconate lists
words = list(itertools.chain.from_iterable(messages_only))
print(words[:10])

# remove stuff
while any(w in rm_words for w in words):
    for i, w in enumerate(words):
        if len(words[i]) == 1:
            words.pop(i)
        elif any(char.isdigit() for char in words[i]):
            words.pop(i)
        for rm_word in rm_words:
            if rm_word in words[i]:
                w = words.pop(i)
print(words[:10])

# save txt
with open (savefile, 'w') as f:
    for word in words:
        f.write (word + os.linesep)

