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
	print("encrypting AES")
	key = os.urandom(16)
	iv = os.urandom(16)
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
	encryptor = cipher.encryptor()
	ct = encryptor.update(message) + encryptor.finalize()
	return [ct, key, iv]

def encryptRSA(key, message):
	return key.encrypt (
		message,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
		)
	)

def appendLength(encryptedMessages):
	'''prepends 4 bytes of length to each message in encryptedMessages'''
	
	encryptLength=len(encryptedMessages)
	return encryptLength.to_bytes(4, byteorder='big')+encryptedMessages

def sendMessage(msg):
	'''send the encrypted messages'''
	pass

#First Step
msg = buildPaddedMessage(b"Alice,16")
aesLst=encryptAes(msg)
rsaMsg = encryptRSA(getKey("1"), aesLst[2] + aesLst[1])
sendMessage(appendLength(rsaMsg+aesLst[2]+aesLst[1]))

#sendMessage(appendLength(rsaMsg+aesLst[0]))
#sendMessage(appendLength(rsaMsg+aesLst[0]))
