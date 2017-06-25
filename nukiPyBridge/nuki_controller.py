import sys
import nuki

if len(sys.argv) < 2:
	print "Usage: %s unlock/lock" % sys.argv[0] 
	sys.exit(1)

command = sys.argv[1]
print "Received command: %s" % command

nukiMacAddress = "54:D2:72:B8:3C:91"
nuki = nuki.Nuki(nukiMacAddress)
nuki.lockAction(command.upper())
