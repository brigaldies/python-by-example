# Exit if an example fails.
set -e

examples=("type_hints" "async_io" "generators" "decorators" "sql_database" "interface")

for i in "${examples[@]}"
do
  echo "*****************************"
  echo "Running example $i:"
  poetry run python main.py --example "$i" --debug true
  exitcode=$?
  echo "Example $i exit code: $exitcode"
done