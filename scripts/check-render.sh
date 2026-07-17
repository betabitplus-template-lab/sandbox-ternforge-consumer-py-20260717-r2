#!/usr/bin/env bash
set -euo pipefail
test ! -e _components
! find -L . -type l -print -quit | grep -q .
! grep -RIlE '^(<<<<<<<|=======|>>>>>>>)' . >/dev/null

