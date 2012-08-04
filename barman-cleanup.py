#!/usr/local/python27/bin/python2.7

from subprocess import Popen, PIPE
import sys

backuplist = Popen(["barman", "list-backup", "pgx-test"], stdout=PIPE)

i = 0

for line in backuplist.stdout:
        try:
                backup, date, size, wsize = line.split(' - ')
                i += 1
                if i > 2:
                        #print "Deleting " + backup
                        server, backupid = backup.split()
                        deleteit = Popen(["barman", "delete", server, backupid])
        except:
                sys.write.stderr("Unable to split line due to incorrect number of values.\n")
                sys.write.stderr(line + "\n")
                
