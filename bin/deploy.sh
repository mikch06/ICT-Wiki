#!/bin/bash
# deploy generated html files to web

if [ -z "$1" ]
then
  echo "Plase enter \$1 for username and \$2 for domain"
  else
    scp -r web/* images $1@$2:www/kissel.ch/ict/
fi
exit
