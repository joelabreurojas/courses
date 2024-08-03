#!/bin/bash

Ip=$1

function scan {
    echo "The Ip to follow is: $Ip"
    ping -c 5 $Ip
}

scan
