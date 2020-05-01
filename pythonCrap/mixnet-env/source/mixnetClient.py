from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.backends.openssl.rsa import _RSAPublicKey as rsapk

#done
def buildMessage() :
	"""Builds the requested unencrypted message"""
	return ("Alice,16", "Frank,16", "Charlie,16")

def encryptAes(key, message: str):
	'''applies AES encryption.'''
	print("encrypting AES")
	fernet=Fernet(key)
	return fernet.encrypt(message.encode())
	
def encryptRSA(key, message):
	'''applies RSA encryption'''
	pass

def encryptMessage(message, keys):
	"""encrypts the message based on the given algo"""
	for string in message:
		pass

def appendLength(encryptedMessages):
	'''prepends 4 bytes of length to each message in encryptedMessages'''
	pass

def sendMessage(port, encryptedMessages):
	'''send the encrypted messages'''
	pass

print("debug")
key1=b'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAp04ZWyGbJtmm4/tDvo2YAcpBhJGLdevLYrjr1egh7L0riog5AshZJHfbP7qiIWl7CTtdtfgWw1lGVdEWyZFnqiOUvKVIg/i+EeKQqsoJSbJW0dhM/jny3N1D18q35tJ+JT+16rzmBoJLDJ0yDZjJueapbOD4vZrRqri+b20qNZPq//FlKarvEg3wAAc4HIxk5afz3Pc8tbjCPvcV3i+z8a9ao/vBHLMl/vi75LFcPPX1U74e43iBBvFnFqmSUYBjSLLp5xeQtKoz5UZ/wX8yqHLRi/eVXUXXPNWIeBd4n395tT0C5vmlKZztE+hE1YIO7B2PUkkpGhi//VPzlhPqgQIDAQAB'
key1=base64.urlsafe_b64encode(key1)
print("type is")

#message = encryptAes(type(base64.urlsafe_b64encode(key1)), "hi there")
print("message is")
#print(message)
