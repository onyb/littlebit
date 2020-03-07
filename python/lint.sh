#!/usr/bin/env bash

# Ledger Bluestar
# Copyright 2020 Ledger
# Author: @YBadiss

set -euxo pipefail

target="./"
check=
while getopts ":t:c" opt; do
  case ${opt} in
    t )
      target=$OPTARG
      ;;
    c )
      check=true
      ;;
    \? ) echo "Usage: lint [-c] [-t]"
      ;;
  esac
done

if [[ -n "$check" ]]; then
    autoflake -c -r --remove-unused-variables --remove-all-unused-imports $target
    isort -rc -c $target
    black --check $target
    # mypy $target
else
    autoflake --in-place -r --remove-unused-variables --remove-all-unused-imports $target
    isort -rc $target
    black --fast $target
fi

