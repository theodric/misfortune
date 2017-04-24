#!/bin/bash
# yomama
cat $1 | perl -p -e 's/^\n/%/g' | sed 's/^%/%\n/g'
