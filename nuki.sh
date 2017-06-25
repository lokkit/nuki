#!/bin/bash

# switch commands
command=""
case "$1" in
	LOCK)
	command=UNLOCK
	;;
	UNLOCK)
	command=LOCK
	;;
	*)
	echo "Usage: $0 LOCK|UNLOCK"
	exit 1
esac

runuser -u pi -- /bin/bash -c "(cd /home/pi/lokkit/nuki/nukiPyBridge; python nuki_controller.py \"$command\")"
