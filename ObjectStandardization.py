manual_dict = {'rt':"retweet","smh":"shaking my head","lol": "laughing out loud","luv":"love"}

def lookup_words(input_text):

    words = input_text.split(" ")

    new_words = []

    for word in words:

        if word.lower() in manual_dict.keys():
            word = manual_dict[word.lower()]
            
        new_words.append(word)     
    print(new_words)

    new_text = " ".join(new_words)


    return new_text



if __name__ == '__main__':

    print(lookup_words("RT this is a retweeted tweet by elon who made me lol and smh with luv"))
