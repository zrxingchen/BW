#!c:\users\���\desktop\root\bwonline\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'future==0.18.2','console_scripts','pasteurize'
__requires__ = 'future==0.18.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('future==0.18.2', 'console_scripts', 'pasteurize')()
    )