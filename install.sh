#!/bin/bash -x

# if giving no argument, then install the *.py  to ~/.local/bin
# else remove the *.py

[[ $1 == "" ]] && cp *.py ~/.local/bin

if [[ $1 != "" ]]; then
  for file in *.py; do
    rm ~/.local/bin/${file}
  done
fi
