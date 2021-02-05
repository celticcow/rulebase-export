#!/usr/bin/python3

import json
import requests
import sys


def main():
    print("start of main")

    ## rule json output
    rules = {}

    with open('rule-ex1.json', 'r') as f:
        rules = json.load(f)
    
    print(len(rules['rulebase']))
    print(rules['from'])

    #rules['rulebase'][<index1>][rulebase][<index2>][source-ranges]

    len1 = len(rules['rulebase'])

    for i in range(len1):

        len2 = len(rules['rulebase'][i]['rulebase'])

        for j in range(len2):
            #print("Source Ranges")
            #print(rules['rulebase'][i]['rulebase'][j]['source-ranges'])

            len3 = len(rules['rulebase'][i]['rulebase'][j]['source-ranges']['ipv4'])

            print("Source")
            for k in range(len3):
                print(rules['rulebase'][i]['rulebase'][j]['source-ranges']['ipv4'][k])
            
            len4 = len(rules['rulebase'][i]['rulebase'][j]['destination-ranges']['ipv4'])
            print("Dest")
            for k in range(len4):
                print(rules['rulebase'][i]['rulebase'][j]['destination-ranges']['ipv4'][k])

            len4 = len(rules['rulebase'][i]['rulebase'][j]['service-ranges']['tcp'])
            print("TCP Ports")
            for k in range(len4):
                print(rules['rulebase'][i]['rulebase'][j]['service-ranges']['tcp'][k])

            len4 = len(rules['rulebase'][i]['rulebase'][j]['service-ranges']['udp'])
            print("UDP Ports")
            for k in range(len4):
                print(rules['rulebase'][i]['rulebase'][j]['service-ranges']['udp'][k])



if __name__ == "__main__":
    main()
#end of program