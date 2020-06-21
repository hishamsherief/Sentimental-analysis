punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#creating list of positive words

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#creating list of negative words

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def strip_punctuation(s):
	"""fuction for removing punctuations"""
    for i in punctuation_chars:
        s = s.replace(i,'')
    return s

def get_pos(s):
	"""funtion for getting positive score"""
    p = 0
    s = strip_punctuation(s)
    s = s.split(' ')
    for i in s:
        i = i.lower()
        if i in positive_words:
            p += 1
    return p

def get_neg(s):
	"""funtion for getting negative score"""
    n = 0
    s = strip_punctuation(s)
    s = s.split(' ')
    for i in s:
        i = i.lower()
        if i in negative_words:
            n += 1
    return n


with open("sample_twitter_data.csv") as inn:
    twt = []
    lines = inn.readlines()
    for raw in lines[1:]:
        lst = raw.split(',')
        a = lst[1]                   #getting number of retweets
        b = lst[2].replace('\n','')  #getting number of replies 
        c = get_pos(lst[0])          #get positive score
        d = get_neg(lst[0])          #get negative score
        e = c-d                      #get effective score
        twt.append((a,b,c,d,e))

with open("resulting_data.csv", "w") as out:
    out.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score') #writing titles
    out.write('\n')
    for cont in twt:
        row_string = '{},{},{},{},{}'.format(cont[0], cont[1], cont[2], cont[3], cont[4])
        out.write(row_string)    #writing data
        out.write('\n')
out.close()