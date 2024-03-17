#!/bin/bash

# Error if unbound variable
set -u

examples=("type_hints" "async_io" "generators" "decorators" "sql_database" "interface")

for i in "${examples[@]}"
do
  echo "*****************************"
  echo "Running example $i:"
  set -x
  poetry run python main.py --example "$i" --debug true
  exitcode=$?
  set +x
  if [ $exitcode -eq 0 ]
  then
    echo "Example $i ran successfully"
  else
    echo "Example $i failed with exit code $exitcode"
    exit 1
  fi
done