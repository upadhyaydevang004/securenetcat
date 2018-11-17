import os, random, socket, sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

message = sys.stdin.read()

#generate random IV
IV = ''
for i in range(16):
	IV += chr(random.randint(0, 0xFF))

#generate random salt
salt = ''
for i in range(16):
	salt += chr(random.randint(0, 0xFF))	

#hash the password
def getKey(password):
	
	hasher = SHA256.new(password)
	return hasher.digest()

def pad(s):
	return s + ((16-len(s) % 16 ) * '{')
	
#encrypt function
def encrypt(plaintext, key):

	cipher = AES.new(getKey(key), AES.MODE_CBC, IV)
	return  IV + cipher.encrypt(pad(plaintext))

#decrypt function
def decrypt(ciphertext, key):        
	
	IV = ciphertext[:16]
	cipher = AES.new(getKey(key), AES.MODE_CBC, IV)
	plaintext = cipher.decrypt(ciphertext[AES.block_size:])
	l = plaintext.count('{')
	return plaintext[:len(plaintext)-l]

#client side connection
def client():
    
    arg_key = '--key'
    host1 = '127.0.0.1'
    port1 = '9999'
    my_arguments = sys.argv
    if(my_arguments[1] == arg_key):
	if(my_arguments[3] == host1):
		if(my_arguments[4] == port1):
	
		
	    	
	    		s = socket.socket()
	    		s.connect((my_arguments[3], int(my_arguments[4])))

  
       			data_c = s.send(encrypt(message, my_arguments[2]))
        			
        			
    			
		else:
	 		print("Invaild arguments")

	else:
		print("Invalid hostname")
    else:
		print("Invalid key argument")

#server side connection
def server():
    arg_key = '--key'
    host1 = '127.0.0.1'
    port1 = '9999'
    my_arguments = sys.argv
    if(my_arguments[1] == arg_key):
	if(my_arguments[3] == host1):
		if(my_arguments[4] == port1):
			
			
    			s = socket.socket()
    			s.bind((my_arguments[3], int(my_arguments[4])))

    			s.listen(1)
    			c, addr = s.accept()
    			print("Connection established")
    
			data = c.recv(1024)
				
        		if data:
				plaintext = decrypt(data, my_arguments[2])
				print("Data from user:" +plaintext)
				

        				
        			
    			c.close()
   		else:
   			print("Invalid port")
	else:
		print("Invalid hostname")
    else:
		print("Invalid key argument")


listen = '-l'
my_arguments = sys.argv
#check if the user is running the client side or server side
try:
	if(my_arguments[5] == listen):
		server()
except IndexError:
	client()





	
