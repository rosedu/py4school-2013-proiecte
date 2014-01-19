import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
utilizatori=[]
chei={}
inbox={}
def salut(id):
    return "Salut! Bine ai venit! Foloseste comanda help pentu instructiuni."
def input(msg,id):
    print msg
    if(msg=="help"):
        return "Comenzile sunt: register nume;chatlist;chat with nume mesaj;verificare inbox"
    elif(msg.startswith("register")):
        text=msg.split(' ')
        username=text[1]
        if not(username in utilizatori):
            utilizatori.append(username)
            chei[id]=username
            return "Numele a fost inregistrat."
        else:
            return "Numele este deja luat."
    elif(msg=="chatlist"):
        return utilizatori
    elif(msg.startswith("chat with")):
         text=msg.split(' ')
         chatuser=text[2]
         mesaj=" ".join(text[3:])
         if chatuser not in utilizatori or chatuser==chei[id]:
             return "Utilizatorul nu este valid."
         else:
             if chatuser not in inbox:
                 inbox[chatuser] = []
             mesaj_de_trimis = ":".join([chei[id],mesaj])
             inbox[chatuser].append(mesaj_de_trimis)
             return "Mesajul <%s> a fost trimis." % mesaj_de_trimis
    elif(msg=="verificare inbox"):
         if id not in chei.keys() or chei[id] not in inbox:
             return ""
         tmp = inbox[chei[id]]
         inbox[chei[id]] = []
         return tmp
    else:
        return ""
         
    
server=SimpleXMLRPCServer(("localhost",8000))
server.register_function(salut, "salut")
server.register_function(input,"input")
server.serve_forever()
