# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
# By Vanchev Lev. Data Analysis in Python HA 2
#%%
# Task 1
def isprime(a):
    c=int(round(a**0.5))
    if a<=1:
        return False
    else:
        for i in range(2, c+1):
            if a%i == 0:
                return False
        return True
#%%
def factorize(a):
    divs=[]
    n=a
    while n!=1:
        if n==2:
            divs.append(2)
            return divs
        c=int(round(n**0.5))
        for i in range(2, c+1):
            if n%i == 0 and isprime(i):
                divs.append(i)
                n=n//i
                break
            if i==c:
                divs.append(n)
                return divs
#%%
factorize(123456789)
#%%
factorize(1234567890123456789012345678901234567890)

#%% 
# Task 2
def queens():
    import random
    a=random.randint(1,8)
    b=random.randint(1,8)
    c=random.randint(1,8)
    d=random.randint(1,8)
    e=random.randint(1,8)
    f=random.randint(1,8)
    g=random.randint(1,8)
    h=random.randint(1,8)
    while b==a or b-1==a or b+1==a:
        b=random.randint(1,8)
    while c==a or c==b or c-1==b or c+1==b:
        c=random.randint(1,8)
    while d==a or d==b or d==c or d-1==c or d+1==c:
        d=random.randint(1,8)
    while e==a or e==b or e==c or e==d or e-1==c or e+1==c:
        e=random.randint(1,8)
    while f==a or f==b or f==c or f==d or f==e or f-1==e or f+1==e:
        f=random.randint(1,8)
    while g==a or g==b or g==c or g==d or g==e or g==f or g-1==f or g+1==f:
        g=random.randint(1,8)
    while h==a or h==b or h==c or h==d or h==e or h==f or h==g or h-1==g or h+1==g:
        h=random.randint(1,8)
    k='.......'
    s1=k[:a-1]+"Q"+k[a-1:]
    s2=k[:b-1]+"Q"+k[b-1:]
    s3=k[:c-1]+"Q"+k[c-1:]
    s4=k[:d-1]+"Q"+k[d-1:]
    s5=k[:e-1]+"Q"+k[e-1:]
    s6=k[:f-1]+"Q"+k[f-1:]
    s7=k[:g-1]+"Q"+k[g-1:]
    s8=k[:h-1]+"Q"+k[h-1:]
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)
    print(s7)
    print(s8)
#%%
queens()
#%%
# Task 3
def frequencies(a):
    file = open(a, 'r', encoding='utf-8')
    s=file.read()
    s=s.lower()
    list=['а','б','в','г','д','е','ё','ж','з','и','й','к','л',\
    'м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы',\
    'ь','э','ю','я']
    counts=[]
    freq=[]
    for elem in list:
        counts.append(s.count(elem))
    for elem in counts:
        freq.append(elem/sum(counts)*100)
    for i in range(0, len(freq)):
        print(list[i],":", "%.2f" % freq[i],"%")
    file.close
#%%
frequencies('tolstoi.txt')
#%%
frequencies('tolstoi.enc')
#%%
# Task 4
def freq(a):
    file = open(a, 'r', encoding='utf-8')
    s=file.read()
    s=s.lower()
    list=['а','б','в','г','д','е','ё','ж','з','и','й','к','л',\
    'м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы',\
    'ь','э','ю','я']
    counts=[]
    freq=[]
    for elem in list:
        counts.append(s.count(elem))
    for elem in counts:
        freq.append(elem/sum(counts)*100)
    file.close
    return freq
#%%
freq('tolstoi.txt')
#%%
def decipher(a,b):
    list=['а','б','в','г','д','е','ё','ж','з','и','й','к','л',\
    'м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы',\
    'ь','э','ю','я']
    freqsource=freq(a)
    freqenc=freq(b)
    pmaxsource=100
    psource=0
    lsource=""
    
    pmaxenc=100
    penc=0
    lenc=""
    
    dct={}
    while len(dct)<len(list):
        for i in range(0, len(freqsource)):
            if freqsource[i]>psource and freqsource[i]<pmaxsource:
                psource=freqsource[i]
                lsource=list[i]
        for j in range(0, len(freqenc)):
            if freqenc[j]>penc and freqenc[j]<pmaxenc:
                penc=freqenc[j]
                lenc=list[j]
    
        dct[lenc]=lsource
    
        pmaxsource=psource
        pmaxenc=penc
    
        psource=0
        penc=0
    
    file = open(b,'r',encoding='utf-8')
    for line in file:
        for char in line:
            if char in dct.keys():
                print(dct[char], end = '')
            else:
                print(char,end = '')
#%%
decipher('tolstoi.txt','tolstoi.enc')
#%%
# Task 5
class Data():
    def __init__(self, data):
        self.data=data
    def count(self):
        return len(self.data)
    def sum(self):
        return sum(self.data)
    def moment(self, k):
        return sum(elem**k for elem in self.data)/self.count()
    def mean(self):
        return self.moment(1)
    def var(self):
        return sum((elem-self.mean())**2 for elem in (self.data))/self.count()
    def std(self):
        return self.var()**0.5
    def percentile(self, p):
        elem=int(p*self.count())+(self.count()%4 > 0)
        return self.data[elem-1]
    def median(self):
        return self.percentile(0.5)
    def __str__(self):
        print("Count:", self.count())
        print("Mean:", self.mean())
        print("Variance:", self.var())
        print("Standard deviation:", self.std())
        print("2nd moment:", self.moment(2))
        print("3rd moment:", self.moment(3))
        print("4th moment:", self.moment(4))
        print("Median:", self.median())
        print("25% quantile:", self.percentile(0.25))
        print("75% quantile:", self.percentile(0.75))
        return ""
#%%
x = Data([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(x)
#%%
# Task 6
import urllib.request
from bs4 import BeautifulSoup
import data
def cpitoinf(cpi):
    inf=[]
    for i in range(1, len(cpi)):
         inf.append((cpi[i]-cpi[i-1]) / cpi[i-1]*100)
    return inf
#%%
def CPI(url):
    with urllib.request.urlopen(url) as resp:
        page=resp.read()
    soup=BeautifulSoup(page, 'html.parser')
    table=soup.find_all("td", {'align': 'right'})
    CPI_row=[]
    for elem in table:
        if ',' in elem.text: 
            CPI_row.append(float(elem.text.replace(",", ".")))
    infl = data.Data(cpitoinf(CPI_row))
    return infl
#%%
x=CPI("http://sophist.hse.ru/exes/tables/CPI_Y_CHI.htm")
print(x)