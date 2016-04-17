#!/usr/bin/env bash
DIR=$(dirname "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")")
exec "${DIR}/lab" login

