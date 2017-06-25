import nuki_messages
import nuki

nukiMacAddress = "54:D2:72:B8:3C:91"
Pin = "%04x" % 1234

nuki = nuki.Nuki(nukiMacAddress)
nuki.readLockState()
nuki.lockAction("UNLOCK")
logs = nuki.getLogEntries(10,Pin)
print "received %d log entries" % len(logs)

available = nuki.isNewNukiStateAvailable()
print "New state available: %d" % available
