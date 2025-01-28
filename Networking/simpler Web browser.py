import urllib.request,urllib.parse,urllib.error

hand = urllib.request.urlopen("http://data.pr4e.org/clown.txt")
#for i in hand:
#    print(i.decode().strip())
dic = dict()
for line in hand:
    print(line)
    words = line.decode().split()
    for word in words:
        dic[word] = dic.get(word,0) + 1
print(dic)
