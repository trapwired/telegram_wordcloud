import json
from wordcloud import WordCloud
import configparser

import matplotlib.pyplot as plt


CHAT = 'sample_chat.json'


def load_stopwords():
    """
    :return: a list of all stopwords stored in sample_stopwords_swiss_german.txt
    """
    with open('sample_stopwords_swiss_german.txt', 'r') as file:
        if file.mode == 'r':
            contents = file.read()
            stopwords_list = contents.split('\n')
            return stopwords_list


def load_data(name: str):
    """
    :param name: messages from name will be added to complete_message_text
    :return: returns a string containing all messages from name in chat.json
    """
    with open(CHAT, 'r', encoding='utf-8') as chat_file:
        chat_dictionary = json.load(chat_file)
        message_dictionary = chat_dictionary['messages']
        complete_message_text = ''
        for message in message_dictionary:
            if message['from'] == name:
                if message['type'] == 'message' and 'file' not in message:
                    message_text = ''
                    for word in message['text']:
                        if 'type' not in word:
                            message_text += word
                    try:
                        complete_message_text += message_text
                    except TypeError:
                        print(message_text)
        return complete_message_text


def gen_wordcloud(text: str, stopwords: list, name: str):
    """
    :param text: the text to generate the wordcloud from
    :param stopwords: these words will be excluded in the wordcloud
    :param name: for labelling the file, include the name of the person
    :return: does not return anything, wordcloud is saved in root as png
    """

    wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(text)
    wordcloud.to_file("sample_output/{}_without_stopwords.png".format(name))

    wordcloud = WordCloud(background_color="white", width=800, height=400).generate(text)
    wordcloud.to_file("sample_output/{}_complete.png".format(name))

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def generate_wordcloud_all_persons(people: list):
    """
    :param people: a list of all people in the chat we want to generate a wordcloud from
    :return: does not return anything
    """
    stopwords = set(load_stopwords())

    for name in people:
        data = load_data(name)
        gen_wordcloud(data, stopwords, name)


def clean_config(raw_str: str):
    """
    :param raw_str: String to parse from config
    :return: a list of all names separated by a comma
    """
    raw_list = raw_str.replace("\n", "").split(",")
    return list(map(lambda x: x.strip(), raw_list))


if __name__ == "__main__":
    config = configparser.RawConfigParser()
    config.read('config.ini', encoding="utf8")
    generate_wordcloud_all_persons(clean_config(config["INFO"]["persons"]))