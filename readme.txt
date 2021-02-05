

get rule_base:

show packages -> drill down to layers
-> ex GPC-Prod-Transist -> Network
-> -> uid = xxxxx

api call show access-rulebase
{
uid : xxxx
limit : int
offset : int
show-as-ranges : true
}

get rulebase w/o object dict 

mgmt_cli -r true -d 199.81.216.205 show access-rulebase uid "ad92843e-687a-4c37-a9f0-e3273628c455" limit 20 offset 20 show-as-ranges "true" 
   use-object-dictionary "false" --format json


got to limit get to 20 
