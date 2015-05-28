__author__ = 'dheepan'
# Source: https://pythonism.wordpress.com/2010/04/18/a-simple-chatbot-in-python/
# I have included the lexicon which I trained from
# Harry potter and the chamber of secrets. You could find the training code in the
# link above.
import pickle,random
a=open('lexicon-hp','rb')
successorlist=pickle.load(a)
a.close()
def nextword(a):
    if a in successorlist:
        return random.choice(successorlist[a])
    else:
        return 'the'
speech=''
while speech!='quit':
    speech=input('>')
    s=random.choice(speech.split())
    response=''
    while True:
        neword=nextword(s)
        response+=' '+neword
        s=neword
        if neword[-1] in ',?!.':
            break
    print(response)