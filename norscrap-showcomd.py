#python script using nornir_scrapli plugin "send_command"
#script will send the command "show ip interface brief"
#to all the hosts in the nornir host file and output
#results to the screen

from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def show_command_test(task):
    task.run(task=send_command, command="show ip interface brief")

results = nr.run(task=show_command_test)
print_result(results)
