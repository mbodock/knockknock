#!/bin/bash

# Get all ips and macadress and puts in <1> file.csv
arp -a | cut -d'o' -f 1|tr -d '?()'| sed 's/ at /, /' > $1
