from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def parseKeys(filePath=None):
	"""parses the crypto keys either through the provide filePath var, or 
		through the predetermined file path, which is ../pems/. 
		Returns a dictionary of 3 elements, containing the keys for mixes 
		1 to 3"""
	print("Parsing crypto keys")
	print("filePath is: " + str(filePath))

	keysDict = dict()
	for i in range(1, 4):
		path="../pems/public-key-mix-"+str(i)+".pem"
		print("getting key: " + path)
		with open(path, "rb") as key_file:
			public_key = serialization.load_pem_public_key(
				key_file.read(),
				backend=default_backend()
			)
			if public_key is not None:
				keysDict[i] = public_key
				print("public key is " + str(public_key))
			"""key = o.read()
			if key is not None : 
				key = key.replace("-", "").replace("BEGIN", "").replace("END", "").replace("PUBLIC KEY", "").replace("\n", "").strip()
				keysDict[i] = key
			else:
				print("key of " + str(i) + "is None.")
				continue"""
	return keysDict			

def buildMessage() :
	"""Builds the requested unencrypted message"""
	return "Alice,16"

def encryptMessage(message, keys):
	"""encrypts the message based on the given algo"""
	encrypted = keys[3].encrypt(message,
	padding.OAEP(
		)
	)

	for i in range(3, 0, -1):
		message=keys[i].encrypt(message)


def appendLength(encryptedMessage):
	pass

def sendMessage(port, encryptedMessage):
	pass

encryptMessage(None, None)
#sendMessage(1234, appendLength(encryptMessage(parseKeys, buildMessage)))