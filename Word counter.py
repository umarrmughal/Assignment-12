import pyttsx3

sentence = input("Enter a Sentence:")

#   For get the words entered howmany times in dictionary 
words = sentence.split()
word_freq = {}

for i in words:
    if i in word_freq:
        word_freq[i] += 1
    else:
        word_freq[i] = 1


#   for read the sentence 
def customize_engine():
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.setProperty('volume',0.4)
    
    return engine

engine = customize_engine()
engine.say(sentence)
engine.runAndWait()


print(word_freq)