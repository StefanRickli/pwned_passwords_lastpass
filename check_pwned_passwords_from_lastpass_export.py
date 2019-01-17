## User variables

password_file_path = 'my_password_list.txt'
database_path = 'pwned-passwords-sha1-ordered-by-hash-v4.txt'


## Helper functions

import pandas as pd
import hashlib
import math

# Performs a binary search the password file
def db_find(db_path, key):
    #print(key.encode('utf-8'))
    fp = open(db_path, 'r')

    begin = 0
    fp.seek(0, 2) # go to end of file
    end = fp.tell()
    #print('EOF: {}'.format(end))
    
    entry = None
    while (begin < end) and begin >= 0:
        at = int((end + begin) / 2)
        #print('begin: {}, end: {}, middle: {}'.format(begin, end, at))
        fp.seek(at, 0)
        goto_line_start(fp)
        line_start = fp.tell()
        line = fp.readline()
        line_end = fp.tell()
        #print(line.encode('utf-8'))
        line_key = line.split(':')[0].rstrip('\n')
        if (key == line_key):
            #print('found key')
            return line.rstrip('\n').split(':')
        elif (key > line_key):
            #print('search_right\n')
            begin = line_end
        else:
            #print('search_left\n')
            end = line_start - 1
    
    #print('not found')
    return None


def goto_line_start(fp):
    at = fp.tell()
    while at != 0:
        if fp.read(1) != '\n':
            at -= 1
            fp.seek(at)
        else:
            return
    return


## Search the 'Pwned Passwords' database

pw_db = pd.read_csv(password_file_path, dtype = str).sort_values('password')

for index, row in pw_db.iterrows():
    if isinstance(row['password'], float) and math.isnan(row['password']):
        #print('NaN')
        continue
    
    encoder = hashlib.sha1()
    encoder.update(row['password'].encode('utf-8'))
    pw_hash = encoder.hexdigest().upper()
    db_entry = db_find(database_path, pw_hash)
    
    if db_entry is not None:
        print('Entry:\t\t{}'.format(row['name']))
        print('URL:\t\t{}'.format(row['url']))
        print('User:\t\t{}'.format(row['username']))
        print('Password:\t{}'.format(row['password']))
        print('Hash:\t\t{}'.format(pw_hash))
        print("==> {} entries in 'Pwned Passwords' database\n".format(db_entry[1]))

print('\nDone.\n')
