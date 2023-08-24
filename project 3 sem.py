#pip install googletrans 3.1.0a0
print("Cross Dialect Connect".center(50))
from googletrans import Translator
t = Translator()

s =  input("Enter the message:")
a = input("Enter the language to convert:")
l = a.lower()
# Make a dictionary of all languages and access all language code
#LANG = ["english","hindi","german","gujarati"]
 
try:
    if l=="hindi":
        h = t.translate(s,dest="hi")
        print(h.text)
    elif l=="german":
        g= t.translate(s,dest= "de")
        print(g.text)
    elif l=="english":
        e= t.translate(s,dest="en")
        print(e.text)
    elif l=="gujarati":
        m = t.translate(s,dest="gu")
        print(m.text)
    elif l=="tamil":
        T = t.translate(s,dest="ta")
        print(T.text)
    elif l=="bengali":
        b = t.translate(s,dest="bn")
        print(b.text)
    elif l=="special":
        s = t.translate(s,dest="ee")
        print(s.text)
    else:
        print("invalid input".title())
        
except:
    print("Check your internet connection")
        





"""print(out.pronunciation)
print(out.text)"""
