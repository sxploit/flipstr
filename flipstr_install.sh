#!/bin/bash
FLIPSTR="flipstr.py"
FLIPSTR_ALIAS="flipstr"

chmod +x "$FLIPSTR"
sudo cp "$FLIPSTR" "/usr/local/bin/$FLIPSTR_ALIAS"