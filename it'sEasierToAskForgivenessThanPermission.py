# process file: LBYL

import os

p = '/path/to/datafile.dat'

if os.path.exists(p):
  process_file(p)
else:
  print(f'No such files as{p}')  

try:
    process_file(f)
except OSError as e:
    print(f'error:{e}')    