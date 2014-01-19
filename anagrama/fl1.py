from flask import *
import random
import requests
import re
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asgfdasfdas'


@app.route('/')
#@app.route('/hello/<name>')
def hello(name=None):
    logging.info("Sunt pe prima pagina")
    if 'cuvant' in session:
        del session['cuvant']
        del session['litere']
    return render_template('anagrama.html', name=name)

@app.route('/joc')
def joc():
    if 'cuvant' not in session:
        cuvant, litere = get_litere(int(request.args.get('dificultate', 4)))
        session['cuvant'], session['litere'] = cuvant, litere
        session['nume'] = request.args.get('nume', '')
        
    cuvant, litere = session['cuvant'], session['litere']
    nume = session['nume']
    gresit = request.args.get('gresit', False)
    
    return render_template('joc.html', litere=litere, cuvant=cuvant,
                           nume=nume, gresit=gresit)


@app.route('/solutie')
def solutie():
    v=request.args['solutie']
    cuvant, litere = session['cuvant'], session['litere']
    nume = session['nume']
    if v==session['cuvant']:
      return render_template('solutiebuna.html', litere=litere, cuvant=cuvant, nume=nume)
    else:
      return redirect('/joc?gresit=1')


def get_litere(lungime):
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
    return b, anagram

app.run(debug=True, port=5003)
