from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
from nltk.corpus import stopwords


filename = 'words_michi.txt'
with open (filename, 'r') as file:
    text = file.read().splitlines()
print(len(text))

german_stop_words = stopwords.words('german')
string_text = ' '.join(text)

wc = WordCloud(
        width= 5000,
        height = 3000,
        margin=5, 
        max_words=30,
        background_color='white',
        colormap='viridis',
        collocations=False,
        stopwords=german_stop_words
    ).generate(string_text)

plt.imshow(wc) 
plt.axis('off')
plt.show()