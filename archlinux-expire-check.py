#!/usr/bin/env python3
from datetime import datetime
import sys
with open('/var/log/pacman.log') as pacman_log:
		for line in pacman_log:
			if 'pacman -Syu'  in line or 'pacman --color auto -Sy' in line :
				last_update_date=line[1:11]
			
d_now=datetime.now()
d_last_check=datetime.strptime(last_update_date,"%Y-%m-%d")
d_expire=(d_now-d_last_check).days
if len(sys.argv) == 1:
	print("You haven't update system for {} days".format(d_expire))
elif d_expire > int(sys.argv[1]):
	print("You haven't update system for {} days".format(d_expire))

