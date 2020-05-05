from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import padding
import os.path as p

#first
msg = buildPaddedMessage(b"Alice,16")
aesMsg=encryptAes(msg)
key=getKey("1")
rsaMsg = encryptRSA(key, aesMsg)
#finalMsg=appendLength(rsaMsg)
#sendMessage(finalMsg)


def getKey(key) :
	keyPath = p.join("..", "pems", "publpublic-key-mix-"+key+".pem")
	with open(keyPath, "rb") as key_file:
		private_key = serialization.load_pem_private_key(
			key_file.read(),
			password=None,
			backend=default_backend()
		)
	return private_key

#done
def buildPaddedMessage(message) :
	"""Builds the requested unencrypted message"""
	padder = padding.PKCS7(128).padder()
	#expects byte array
	return padder.update(message) + padder.finalize()

def encryptAes(message):
	'''applies AES encryption.'''
	print("encrypting AES")
	key = os.urandom(16)
	iv = os.urandom(16)
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), default_backend())
	encryptor = cipher.encryptor()
	ct = encryptor.update(message) + encryptor.finalize()
	return ct

def encryptRSA(key, message):
	encrypted = key.encrypt (
		message,
		padding.OAEP(

		)
	)

def appendLength(encryptedMessages):
	'''prepends 4 bytes of length to each message in encryptedMessages'''
	pass

def sendMessage(port, encryptedMessages):
	'''send the encrypted messages'''
	pass

#First Step
