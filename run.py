import subprocess
import sys

number_of_sims = 2500

for i in range(0, number_of_sims):
	if (i+1)%250 == 0:
		print(i+1)
	pid = subprocess.call('python main.py {}'.format(i+1), shell=True)