import json
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

names = ['Chris Buob', 'Valentin Anklin', 'Philipp Hadjimina', 'Fluffy Octopus', 'David', 'Mischa Buob']
WHO = names[0]
USE_SW = False


def load_stopwords():
    with open('stopwords.txt', 'r') as f:
        if f.mode == 'r':
            contents = f.read()
            res = contents.split('\n')
            return res


def load_data():
    with open('chat.json', 'r', encoding='utf-8') as f:
        chat_dict = json.load(f)
        cd = chat_dict['messages']
        text = ''
        for i in cd:
            if i['type'] == 'message' and 'file' not in i and i['from'] == WHO:
                t = ''
                for elem in i['text']:
                    if not 'type' in elem:
                        t += elem
                try:
                    text += t
                except TypeError:
                    print(t)
        return text


def gen_wordcloud(text, sw):
    if USE_SW:
        wordcloud = WordCloud(stopwords=sw, background_color="white", width=800, height=400).generate(text)
        wordcloud.to_file("out/{}_with_stopwords.png".format(WHO[0:4]))
    else:
        wordcloud = WordCloud(background_color="white", width=800, height=400).generate(text)
        wordcloud.to_file("out/{}_no_stopwords.png".format(WHO[0:4]))

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def gen_wordcloud_4all():
    global WHO, USE_SW, names
    sw = set(load_stopwords())
    for name in names:
        WHO = name
        data = load_data()
        gen_wordcloud(data, sw)
        USE_SW = True
        gen_wordcloud(data, sw)
        USE_SW = False


if __name__ == "__main__":
    gen_wordcloud_4all()