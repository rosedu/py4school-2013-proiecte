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

def cuvant(lungime):
    i=random.randint(97, 122)   
    caracter=chr(i)

    adresa="http://dexonline.ro/lista-cuvinte/"+caracter
    r = requests.post(adresa)
    text = r.text
    cuvinte =  re.findall(r"/definitie/([a-z]+)\"", text)
    cuvinte = [c for c in cuvinte if len(c) == lungime]
    a=random.choice(cuvinte)
    return a

def cuvant_prost(b):
    r = requests.get('http://dexonline.ro/definitie/'+b)   
    content = r.text
    val= r.content.find('<span class="def"')==-1 or r.content.find('</abbr>')==-1
    return val
    
def definitie(b):
    #sa verifice daca e corect si sa extraga definitia
    r = requests.get('http://dexonline.ro/definitie/'+b)
    content = r.text
    s = content.index('</abbr>')
    content = content[s:]
    s = content.index('&')
    content=content[:s]
    content=remove_html_markup(content)
    return content

def anagram(a):
    o=0
    l=len(a)
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
    return anagram

##MAIN
raspuns=1
while raspuns==1:
    lungime=input("Numarul de litere ale cuvantului:")
    a=cuvant(lungime)   
    while cuvant_prost(a):
        a=cuvant(lungime)
    b=a
    a=anagram(a)
    print a
    print definitie(b)
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
