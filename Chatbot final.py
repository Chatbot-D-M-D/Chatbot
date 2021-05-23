from silence_tensorflow import silence_tensorflow
silence_tensorflow()

#Pasul 1: Importarea de librarii si date necesare
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

#Pasul 2: Preprocesarea de date
words=[]
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open('intents.json').read()
intents = json.loads(data_file)
for intent in intents['intents']:
    for pattern in intent['patterns']:

        #Tokenize
        w = nltk.word_tokenize(pattern)
        words.extend(w)

        documents.append((w, intent['tag']))

        #adaugam clasele
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
#Lemmatize
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
#Sortam clasele
classes = sorted(list(set(classes)))
print (len(documents), "documents")
print (len(classes), "classes", classes)
print (len(words), "unique lemmatized words", words)
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

#Pasul 3: Crearea spatiului de antrenament
#import nltk
#from nltk.stem import WordNetLemmatizer

#lemmatizer = WordNetLemmatizer()
#import json
#import pickle

#import numpy as np
#from keras.models import Sequential
#from keras.layers import Dense, Activation, Dropout
#from keras.optimizers import SGD
#import random

#words = []
#classes = []
#documents = []
#ignore_words = ['?', '!']
#data_file = open('intents.json').read()
#intents = json.loads(data_file)

#for intent in intents['intents']:
#    for pattern in intent['patterns']:
#
#        # Tokenize
#        w = nltk.word_tokenize(pattern)
#        words.extend(w)
#        documents.append((w, intent['tag']))
#
#        # Adaugam clasele
#        if intent['tag'] not in classes:
#            classes.append(intent['tag'])
#
# Lemmaztize
#words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
#words = sorted(list(set(words)))
# Sortam clasele
#classes = sorted(list(set(classes)))
#print(len(documents), "documents")
# clase = intents
#print(len(classes), "classes", classes)
# words = toate cuvintele
#print(len(words), "unique lemmatized words", words)

#pickle.dump(words, open('words.pkl', 'wb'))
#pickle.dump(classes, open('classes.pkl', 'wb'))

# Am creat training data-ul
#training = []
#output_empty = [0] * len(classes)
#for doc in documents:
#    bag = []
#    # Lista covintelor tokenized
#    pattern_words = doc[0]
#    # Lemmatize din nou
#    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
#    for w in words:
#        bag.append(1) if w in pattern_words else bag.append(0)

#    output_row = list(output_empty)
#    output_row[classes.index(doc[1])] = 1

#    training.append([bag, output_row])
#random.shuffle(training)
#training = np.array(training)
#train_x = list(training[:, 0])
#train_y = list(training[:, 1])
#print("Training data created")

# Crearea modelului
#model = Sequential()
#model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
#model.add(Dropout(0.5))
#model.add(Dense(64, activation='relu'))
#model.add(Dropout(0.5))
#model.add(Dense(len(train_y[0]), activation='softmax'))

#Compilam modelul
#sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
#model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#Salvam modelul
#hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
#model.save('chatbot_model.h5', hist)

#print("model created")

#Pasul 4 si 5: Interationarea cu bot-ul si crearea GUI-ului
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):

    sentence_words = nltk.word_tokenize(sentence)

    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):

    sentence_words = clean_up_sentence(sentence)

    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:

                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):

    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(text):
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res
#Crearea GUI-ului cu Tkinter (Interfata)
import tkinter
from tkinter import *

def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("Chatbot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Crearea ecranului de chat
ChatLog = Text(base, bd=0, bg="#48bda3", height="8", width="50", font="Arial")

ChatLog.config(state=DISABLED)

#Punem scrollbar-ul in ecranul de chat
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="dot")
ChatLog['yscrollcommand'] = scrollbar.set

#Crearea butonului de send
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="10", height=5,
                    bd=0, bg="#3c9d9b", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Crearea ecranului de mesaj
EntryBox = Text(base, bd=0, bg="#ffffff",width="29", height="5", font="Arial")

#Plasarea tuturor componentelor pe ecran
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()