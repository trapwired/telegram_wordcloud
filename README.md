# telegram_wordcloud
Generate a wordcloud from a Telegram chat, exported as json

# How-to
the script present in main.py looks for a file called chat.json, present in the root directory. It assumes this file to be a direct telegram-group-chat export (no media, json) and parses it to get all messages.
by specifying the global variable WHO, one can choose which group-users messages will be added to the wordcloud.
By changing the boolean value of USE_SW (use stopwords), one can add a custom dictionary of words to ignore in the wordcloud. The already present stopwords.txt file is a small example of swiss-german words.

# Requirements
json
wordcloud (https://github.com/amueller/word_cloud)
