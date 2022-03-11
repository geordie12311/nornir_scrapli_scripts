#python script to use netconf plugin to return router-id from hosts
import xmltodict
from nornir import InitNornir
from nornir_scrapli.tasks import netconf_get_config
from nornir_utils.plugins.functions import print_result
#note imporitng xmltodict and also netconf_get_config
nr = InitNornir(config_file="config1.yaml")

def pull_netconfig_stuff(task):
    result = task.run(task=netconf_get_config, source="running", filters="/native/router", filter_type="xpath")
    task.host["facts"] = xmltodict.parse(result.result)
    ospf_rid = task.host["facts"]["rpc-reply"]["data"]["native"]["router"]["ospf"]["router-id"]
    print(f"{task.host} has an OSPF router-id of {ospf_rid}")
#above function is using netconf_get_config to get the running configuration off the hosts
#then filtering it for /native/router using xpath. Then it is using dict to lookup the router-id
#in the structured data path and printing out each host router-id details
results = nr.run(task=pull_netconfig_stuff)

