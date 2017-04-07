#!/usr/bin/env python2

# Server edited from Lightning's "Edgy" GiTS 2014

import SocketServer
import sys
import socket
import threading
import thread
import tempfile
import subprocess
import os
import random
import time
import zlib
import pickle
import json

#base port for service
BasePort = 54444

def pickle_to_json(ifile, ofile):
    """Read in a pickle then print out the json of it

    Max pickle 4096 bytes
    WARNING: EXPLOITABLE
    """
    p = ifile.read(4096)
    d = pickle.loads(p)
    j = json.dumps(d)
    ofile.write("json:\n")
    ofile.write(j)

class servhandler(SocketServer.StreamRequestHandler):
                    
    def handle(self):

        # self.connection.settimeout(5)

        # self.wfile.write()
        # self.rfile.readline()

        try:
            # do things
            pickle_to_json(self.rfile, self.wfile)
            return True

        except Exception, ex:
            print ex
            pass

        return True

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

'''
def daemonize():
    if os.fork() != 0:
        os._exit(0)
     
    os.setsid()
     
    if os.fork() != 0:
        os._exit(0)
     
    os.chdir("/")
    os.umask(022)
    [os.close(i) for i in xrange(3)]
    os.open(os.devnull, os.O_RDWR)
    os.dup2(0, 1)
    os.dup2(0, 2)
'''

if __name__ == "__main__":

    #daemonize()

    #since we are threading make a general lock
    #ThreadLock = threading.Lock()
    
    #start the service
    server = ThreadedTCPServer(('', BasePort), servhandler)
    #t = threading.Thread(target=server.serve_forever)
    #t.setDaemon(False) # don't hang on exit
    print "Server Starting\n"
    #t.start()
    
    #server this forever
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
