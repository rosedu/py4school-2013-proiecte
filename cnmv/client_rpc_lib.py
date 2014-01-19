import xmlrpclib
import uuid
import thread
import time
key=str(uuid.uuid4())

client=xmlrpclib.ServerProxy("http://localhost:8000/")
print client.salut(key)

def check_inbox():
    while True:
        ret_text=client.input("verificare inbox",key)
        if  ret_text:
            print ret_text
        time.sleep(15)
    
thread.start_new_thread(check_inbox,())

while True:
    msg=raw_input()
    print client.input(msg,key)
    

    
