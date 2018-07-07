#!/bin/bash

python3 convert.py
sudo ibus-table-createdb -n /usr/share/ibus-table/tables/myInputTable.db -s ibusTable
sudo cp symbol_input_icon.png /usr/share/ibus-table/icons/
ibus-daemon -drx

