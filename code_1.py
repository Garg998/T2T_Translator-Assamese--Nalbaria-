
import string
import re

print("Vowels: \n-------\nঅ ax | আ aa | ই i | ঈ i | উ u | ঊ u | ঋ ri | এ e | ঐ oi | ও o | ঔ ou\n\nConsonants: \n-----------\nক k | খ kh | গ g | ঘ gh | ঙ ng \nচ s | ছ s | জ j | ঝ jh | ঞ y \n-------------\nট T | ঠ th | ড d | ঢ dh | ণ n \nত t | থ th | দ d | ধ dh | ন n \n-------------\nপ p | ফ ph | বb | ভ bh | ম m \nয j | ৰ r | ল l | ৱ w | শ x | ষ x \n-------------\nস x | হ h | ক্ষ khy | ড় r | ঢ় r | য় y | ৎ t")

std_sen = input("\nEnter the std assamese sentence(using the transliterations above): ")

#Punctuation stripping
std_sen = std_sen.translate(str.maketrans('', '', string.punctuation))
#change the whole string into lowercase letters
std_sen = std_sen.lower()
#tokenise
sen = std_sen.split(" ");
sen

#-------Stemming--------

#gather the data
root_words = [line.rstrip() for line in open('assamese_rootwords.txt')]
suffixes = [line.rstrip() for line in open('suffix.txt')]

# Function to detect which suffix is attached
def suffix_detection(word): 
    lis = ['xxxx']
    maxm = 0
    for j in range(len(suffixes)):   
        if word.endswith(suffixes[j]) and len(suffixes[j]) > maxm:
            maxm = len(suffixes[j])
            lis[0] = suffixes[j]   #add the prefix to the dictionary
    
    return lis

#check whether the word given is alreasy a root word
word = {} #dictionary to  keep track of what suffixes are possible for the coeesponding word
for i in range(len(sen)):
    if sen[i] in root_words:
        word[sen[i]] = 'None'
    else:
        suffix = suffix_detection(sen[i])
        if suffix[0] != 'xxxx':
            pos = sen[i].rfind(suffix[0])
            root = sen[i][:pos]
            word[root] = suffix[0]
        else:
            root = sen[i]
            word[root] = suffix[0]

print("WORD AND ITS SUFFIX-->(Standard) ",word)

#using regular expression we will implement some rules
def rule10(i):
    pattern = re.compile('(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)*(ax|aa|ri|i|u|e|oi|ou|o)+(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(ax)')
    x = re.findall(pattern, i)
    if not x:
        return i
    print('rule 10')
    index = i.rfind('ax')
    txt = i[:(index+1)] + 'a' + i[(index+2):]
    return txt 

def rule11(i):
    eleven = re.compile('(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(ax|o)+(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|ph|n|p|bh|b|m|r|l|w|x|h|y)+(ax|aa|ri|i|u|e|oi|ou|o)+')
    x = re.findall(eleven,i)
    if not x:
        return i
    print('rule 11')
    if x[0][1] == 'ax':
        index = i.find('ax')
        txt = i[:(index)] + 'aa' + i[(index+2):]
    elif x[0][1] == 'o':
        index = i.find('o')
        txt = i[:(index)] + 'ax' + i[(index+1):]
    return txt

def rule8(i):
    eight = re.compile('(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)*(ax|e)+(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(aa)')
    x = re.findall(eight, i)
    if not x:
        return i
    
    print('rule 8')
    if x[0][1] == 'ax':
        index = i.find('ax')
        txt = i[:(index)] + 'aa' + i[(index+2):]
    elif x[0][1] == 'e':
        index = i.find('e')
        txt = i[:(index)] + 'aa' + i[(index+1):]
    
    return txt

def rule15(i):
    
    index = i.find('x')
    if index == -1 or index == 0:
        return i
    print('rule 15')
    if index == len(i) - 1:
        txt = i[:(index)] + 'h'
    else:
        txt = i[:(index)] + 'kh' + i[(index + 1):]
    
    return txt

def rule19(i):
    
    if word[i].endswith(('jaxn','jaxnaa','jaxni','gaxraaki')):
        if word[i] == 'jaxnaa':
             word[i].replace('jaxnaa','tu')
        elif word[i] == 'jaxni':
            word[i].replace('jaxni','jaxni')
        if word[i] == 'jaxn' or word[i] == 'gaxraaki':
            word[i].replace('jaxn','tu').replace('gaxraaki','tu')
        i = i + word[i]
        print('rule 19')
    return i

def rule25(i):
    if word[i].endswith('re'):
        word[i] = word[i].replace('re','di')
        i = i + word[i]
        print('rule 25')
    return i

def rule23(i):
    if word[i].endswith(('le','ile')):
        i = i + word[i].replace('le','laak').replace('ile','ilaak')
        print('rule 23')
    return i

def rule1(txt): #check
    one = re.compile('(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(ax|aa|ri|i|u|e|oi|ou|o)+(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(ax|aa|ri|i|u|e|oi|ou|o)+(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(ax|aa|ri|i|u|e|oi|ou|o)+')
    x = re.findall(one, txt)
    if not x:
        return txt
    print('rule 1')
    v = ""
    for i in range(len(x[0])):
        if i == 3:
            continue
        v = v + x[0][i]
    return v

def rule12(i):
    if i.startswith('ek'):
        i = i.replace('ek','aak')
        print('rule 12')
    return i

def rule17(txt):
    seventeen = re.compile('.+(ax|aa)(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(ax|aa|ri|i|u|e|oi|ou|o)+')
    x = re.findall(seventeen, txt)
    if not x:
        return txt
    print('rule 17')
    v = ""
    for i in range(len(x[0])):
        v = v + x[0][i]
    if x[0][0] == 'ax':
        txt = txt[:(txt.find(v))] + 'e' + txt[(txt.find(v) + 2):]
    elif x[0][0] == 'aa':
        txt = txt[:(txt.find(v))] + 'e' + txt[(txt.find(v) + 2):]
    return txt

def rule18(i):
    if word[i].endswith(('bor','bilaal','hat','heten')):
        i = i + word[i].replace('bor','gilaa').replace('bilaal','gilaal').replace('hat','hun').replace('heten','hoi')
        print('rule 18')
    return i

def rule5(txt): 
    five = re.compile('.+(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(ax|aa|ri|i|u|e|oi|ou|o)+(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(ax|aa|ri|i|u|e|oi|ou|o)+')
    x = re.findall(five, txt)
    if not x:
        return txt
    print(x)
    print('rule 5')
    f = ""
    v = x[0][1]
    for i in range(len(x[0])):
        f = f + x[0][i]
        if i == 1:
            continue;
        v = v + x[0][i]
    txt = txt[:(txt.find(f))] + v
    return txt

def rule13(i):
    thirteen = re.compile('.*(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(khy|kh|k|gh|g|ng|s|jh|j|y|th|t|dh|d|n|ph|p|bh|b|m|r|l|w|x|h|y)+(ax)$')
    x = re.findall(thirteen,i)
    if not x:
        return False
    else:
        print('rule 13')
        return True

# -------- mapping ---------#
# will implement sets and dictionary so that when membership operator 'in' 
# is used the average search time is O(1)

mapped = {} #keeping the mapped words in this dictionary
#implementing rule 9 and 10
do_not_change = {'saabi', 'prithibi', 'soukaa', 'gaxru', 'kaali','dilu','paani','bhaat','khaxn','aaji','baxhut','raani','tumi'}
change_completely = {'kaxkaa':'aataa','aaitaa':'aabu','pitai':'pitei','dhuniyaa':'thougaa','tirotaa':'tiri',
                     'maxtaa':'maxraxd','baacchaa':'soli','baxraxxun':'boirhaan',
                     'jaxlaxkiyaa':'bhaxjluk','laxraa':'aapaa','pelaai':'phele','haxnkraanti':'domahi',
                     'nigaxni':'ningni','bhaxraal':'bhaakhri','xaxru':'saanaa',
                     'daangaxr':'dhumaa','hihaxtaxr':'taahaar','eraal':'daxraxkh','suwaali':'aapi',
                     'nangaxl':'langaxl','leseraa':'neseraa','lon':'nun','nowaarilo':'nollu',
                     'kaxrile ':'kaxille','nowaaro':'nuoru','paarilo':'paaillu','xorir':'xoril',
                     'hoise':'hoissi','goise':'geissi','aase':'aaisi','khon':'khen', 'gol':'gel'}

#checking if root words belong to either of above two lists of words
for i in word:
    if i in do_not_change:
        mapped[i] = i
    elif i in change_completely:
        mapped[i] = change_completely[i]
    elif word[i] == 'axloi': # rule 6
        mapped[i] = i + 'aaklegi'
    elif word[i] == 'oi' or word[i] == 'ou':#rule 9
        if word[i] == 'oi':
            mapped[i] = i + 'e'
        else:
            mapped[i] = i + 'o'
    elif (i != (r := rule1(i))):
        mapped[i] = r
    elif (i != (r := rule10(i))):
        mapped[i] = r
    elif (i != (r := rule11(i))):
        mapped[i] = r
    elif (i != (r := rule8(i))):
        mapped[i] = r
    #elif (i != (r := rule15(i))):
      #  mapped[i] = r
    elif (i != (r := rule19(i))):
        mapped[i] = r
    elif (i != (r := rule25(i))):
        mapped[i] = r
    elif (i != (r := rule23(i))):
        mapped[i] = r
    elif (i != (r := rule12(i))):
        mapped[i] = r
    elif (i != (r := rule17(i))):
        mapped[i] = r
    elif (i != (r := rule18(i))):
        mapped[i] = r
    elif (i != (r := rule5(i))):
        mapped[i] = r
    elif rule13(i):
        mapped[i] = i[:(len(i) - 2)] + 'o'
    elif word[i] == 'xxxx':
        mapped[i] = i 
    else:
        if word[i] == 'None':
            mapped[i] = i
        else:
            mapped[i] = i + word[i]

print("\nMAPPED WORDS--> ", mapped)
print("\nNALBARIA SENTENCE: ")
for i in mapped:
    print(mapped[i],' ',end='')



       

