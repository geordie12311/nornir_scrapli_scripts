#python script to output next hop information for each host but with handling exception 
# built in to bypass Keyerrors rather than just failing
import os
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config1.yaml")
nr.inventory.defaults.username = os.environ["USERNAME"]
nr.inventory.defaults.password = os.environ["PASSWORD"]
#initalizing nornir and using username and password exported in CLI in above section
def get_routing_info(task):
    show_result = task.run(task=send_command, command="show ip route")
    task.host["facts"] = show_result.scrapli_response.genie_parse_output()
    routes =task.host["facts"]["vrf"]["default"]["address_family"]["ipv4"]["routes"]
#Above function is going to parse the information from show ip route and using
#strucutured data fields look for the routes for each interface
    for key in routes:
        try: 
            next_hop_list = routes[key]['next_hop']['next_hop_list']
            rprint(f"{task.host} NEXT HOP INFO: {next_hop_list}")
#next we create an object called key and try to look for the next hop and next hop list
        except KeyError:
            pass
#if there is a keyerror it will pass by it and continue to output the information
results = nr.run(task=get_routing_info)
#finally we print out the get_routing_info
