#!/bin/bash

thisdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pushd "${thisdir}" >/dev/null 2>&1

make clean >/dev/null 2>&1

python scrape.py >${thisdir}/scrape.log 2>&1
python announce.py >${thisdir}/announce.log 2>&1

popd >/dev/null 2>&1
