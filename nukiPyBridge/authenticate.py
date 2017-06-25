import nuki_messages
import nuki
from nacl.public import PrivateKey

nukiMacAddress = "54:D2:72:B8:3C:91" #Nuki_08B83C91
# generate the private key which must be kept secret
keypair = PrivateKey.generate()
myPublicKeyHex = keypair.public_key.__bytes__().encode("hex")
myPrivateKeyHex = keypair.__bytes__().encode("hex")
myID = 50
# id-type = 00 (app), 01 (bridge) or 02 (fob)
# take 01 (bridge) if you want to make sure that the 'new state available'-flag is cleared on the Nuki if you read it out the state using this library
myIDType = '01'
myName = "PiBridge"

nuki = nuki.Nuki(nukiMacAddress)
nuki.authenticateUser(myPublicKeyHex, myPrivateKeyHex, myID, myIDType, myName)
