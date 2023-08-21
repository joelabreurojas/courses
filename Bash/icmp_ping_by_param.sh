#!/bin/bash
#

host=$1

test=$( ping -c 1 $host | grep icmp* | wc -l )

if [ $test -eq 0 ]
then
    echo "The Host don't respond the ICMP's ping."
else
    echo "The Host is activated."
fi
