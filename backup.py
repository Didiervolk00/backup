import os
import subprocess
from datetime import date

base_dir = r"C:\Users\Medewerker\Documents\Backup"

xavier_ip = "10.23.xxx.yyy"

for subnet in range (1, 2):
	
	sub_xavier_ip = xavier_ip.replace("xxx", f"{subnet}")
 
	for machine_id in range (11, 14):
	
		machine_xavier_ip = sub_xavier_ip.replace("yyy", f"{machine_id}")

		sub_dir = os.path.join(base_dir, machine_xavier_ip)
		
		os.makedirs(sub_dir, exist_ok=True)
		
		today = str(date.today())
		
		today_dir = os.path.join(sub_dir, today)
		
		os.makedirs(today_dir, exist_ok=True)
		
		pull_backup = f"scp root@{machine_xavier_ip}:/home/nvidia/QualityGrader/device_settings.ini {today_dir}"
	
		subprocess.run(pull_backup)

		if len(os.listdir(today_dir)) == 0:
			os.rmdir(today_dir)
			if len(os.listdir(sub_dir)) == 0:
				os.rmdir(sub_dir)

lastbackup = f"The last backup run was made on: {today}"
with open(os.path.join(base_dir, 'lastbackup.txt'), 'w') as datefile:
    datefile.writelines(lastbackup)


