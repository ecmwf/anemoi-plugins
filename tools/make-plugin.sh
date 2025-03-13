#!/bin/bash
set -eu
package=$1
kind=$2

# Fail if package is not in the list
valid_packages=("transform" "datasets" "inference")
if [[ ! " ${valid_packages[@]} " =~ " ${package} " ]]; then
    echo "Error: [$package] is not a valid package. Must be one of: ${valid_packages[*]}."
    exit 1
fi

# Fail if kind ends with an 's'
if [[ $kind == *s ]]; then
  echo "Error: [$kind] should not end with an 's'"
  exit 1
fi



class=$(echo $kind | awk '{print toupper(substr($0, 1, 1)) tolower(substr($0, 2))}')

here=$(cd $(dirname $0); /bin/pwd)
top=$here/..

cd $here

for file in $(find plugins -type f); do

    echo $file
    path=$(echo $file | sed -e "
    s/CLASS/$class/g
    s/KIND/$kind/g
    s/PACKAGE/$package/g")
    echo $path
    mkdir -p $(dirname $top/$path)
    sed -e "
    s/CLASS/$class/g
    s/KIND/$kind/g
    s/PACKAGE/$package/g" $file > $top/$path

done

# sed -e "s/PLUGIN_NAME/${package}/g" $here/plugin_example/CMakeLists.txt > CMakeLists.txt
