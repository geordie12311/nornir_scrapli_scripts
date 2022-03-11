import getpass
import os
from calendar import c
from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result
from tqdm import tqdm
#Importing scrapli send configs from file and also tqdm to drive a progress bar

nr = InitNornir(config_file="config.yaml")
password = getpass.getpass()
nr.inventory.defaults.password = password
#above section is initialising nornir and using getpass to prompt the user to enter their password

def send_configs(task, progress_bar):
    task.run(task=send_configs_from_file, file="configtest.txt")
    progress_bar.update()
#the function above will run the task send configs from file and send
#the commands listed in the configtest.txt file. It will also create
#a progress bar that will will be associated with tqdm further down in the script

with tqdm(total=len(nr.inventory.hosts)) as progress_bar:
    results = nr.run(task=send_configs, progress_bar=progress_bar)
#the above section of the script is going to tell tqdm to use the length of the hosts
#in the inventory to drive a process bar to show how nornir is progressing in terms of 
#pushing out the configuration in the configtest.txt file
print_result(results)



