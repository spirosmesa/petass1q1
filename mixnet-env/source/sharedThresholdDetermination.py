import cryptography
import socket

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.primitives import padding as pd
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding 
import os.path as p
import socket
from sys import argv

#done
def buildPaddedMessage(message) :
	"""Builds the requested unencrypted message"""
	padder = pd.PKCS7(128).padder()
	#expects byte array
	return padder.update(message) + padder.finalize()

def getKey(key) :
	with open("./public-key-mix-"+key+".pem", "rb") as key_file:
		private_key = serialization.load_pem_public_key(
			key_file.read(),
			backend=default_backend()
		)
	return private_key

def encryptAes(message):
	'''applies AES encryption.'''
	key = os.urandom(16)
	iv = os.urandom(16)
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
	encryptor = cipher.encryptor()
	ct = encryptor.update(message) + encryptor.finalize()
	return [ct, key, iv]

def encryptRSA(key, message):
	return key.encrypt(
		message,
		padding = padding.OAEP(
            mgf = padding.MGF1(hashes.SHA1()),
            algorithm = hashes.SHA1(),
            label = None,
        )
	)

def appendLength(encryptedMessages):
	'''prepends 4 bytes of length to each message in encryptedMessages'''
	
	encryptLength=len(encryptedMessages)
	return encryptLength.to_bytes(4, byteorder='big')+encryptedMessages

def sendMessage(message, port) :
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((socket.gethostbyname("pets.ewi.utwente.nl"), port))
	s.send(message)
	return s.recv(1)

def determine(message, port) :
    """Just a function which groups together the functionality
    of the mixnetClient.py script, into one, to make it easier
    to use."""

    #First Step
    msg = buildPaddedMessage(message)
    aesLst = encryptAes(msg)
    rsaMsg = encryptRSA(getKey("3"), aesLst[2] + aesLst[1])
    msg = rsaMsg + aesLst[0]

    #second round
    msg = buildPaddedMessage(msg)
    aesLst = encryptAes(msg)
    rsaMsg = encryptRSA(getKey("2"), aesLst[2] + aesLst[1])
    msg = rsaMsg + aesLst[0]

    #third round
    msg = buildPaddedMessage(msg)
    aesLst = encryptAes(msg)
    rsaMsg = encryptRSA(getKey("1"), aesLst[2] + aesLst[1])
    msg = rsaMsg + aesLst[0]

    appended = appendLength(msg)

    print(str(sendMessage(appended, port)))

determine( str("test,num: " + str(argv[1])).encode("UTF-8"), int(argv[2]))
	
	


