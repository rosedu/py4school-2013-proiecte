import random
import requests
import time
import re
import json
def remove_html_markup(s):
    tag = False
    quote = False
    out = ""
    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out

raspuns=1
while raspuns==1:
    lungime=input("Numarul de litere ale cuvantului:")

    i=random.randint(97, 122)   
    caracter=chr(i)

    adresa="http://dexonline.ro/lista-cuvinte/"+caracter
    r = requests.post(adresa)
    text = r.text
    cuvinte =  re.findall(r"/definitie/([a-z]+)\"", text)
    cuvinte = [c for c in cuvinte if len(c) == lungime]

    indice=random.randint(0, len(cuvinte))
    a=cuvinte[indice]

    l=len(a)
    b=a
    o=0
    while o==0:
        o=1
        anagram=''
        while l>0:
            l=l-1
            r=random.randint(0,l)
            anagram=anagram+a[r]
            a=a[:(r)]+a[(r+1):]
        if anagram==b:
            o=0
            a=anagram
    print anagram
    ##r = requests.get('http://dexonline.ro/definitie/'+b)
    ##
    ##content = r.text
    ##s = content.index('</abbr>')
    ##content = content[s:]
    ##s = content.index('&')
    ##content = content[:s]
    ##i=0
    ##content=remove_html_markup(content)
    ##while not unicode.isalpha(content[i]) or not unicode.isalpha(content[i+1]):
    ##    i+=1
    ##content=content[i:]
    ##print content
    print ' '
    start=time.time()
    t=0
    n=0
    while t==0 and n<5:
        v=raw_input()
        if v==b:
            print "Bravo"
            t=1
        else:
            print "Mai incearca"
        n+=1
    if t==1:
        print "Ati rezolvat anagrama in %.2f secunde" %(time.time()-start)
    else:
        print "Ai pierdut 5 incercari. Cuvantul era %s" %(b)
    v=raw_input("Doriti sa reincerdati? ")
    if not v=="da" and not v=="Da" and not v=="DA":
        raspuns=0
    print ''
