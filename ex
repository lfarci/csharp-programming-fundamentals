#!/usr/bin/env bash
# ./ex start A04 | ./ex check | ./ex run | ./ex next | ./ex list
cd "$(dirname "$0")" && exec dotnet run --project tools/ex -v q -- "$@"
