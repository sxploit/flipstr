#!/usr/bin/env python
import sys

def flipstr(wrd):
    return wrd[::-1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: flipstr <word>")
        sys.exit(1)
    
    flipstr_arg = sys.argv[1]
    print(flipstr(flipstr_arg))