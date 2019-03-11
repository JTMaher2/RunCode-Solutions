#!/usr/bin/env python3

import queue
import threading
import subprocess
import sys

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

def getOutput(outQueue):
    outStr = ''
    try:
        while True: #Adds output from the Queue until it is empty
            outStr+=outQueue.get_nowait()

    except queue.Empty:
        return outStr

url = sys.argv[1]
port = sys.argv[2]
		
p = subprocess.Popen("nc " + url + " " + port, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, universal_newlines=True)

outQueue = queue.Queue()
errQueue = queue.Queue()

outThread = threading.Thread(target=enqueue_output, args=(p.stdout, outQueue))
errThread = threading.Thread(target=enqueue_output, args=(p.stderr, errQueue))

outThread.daemon = True
errThread.daemon = True

outThread.start()
errThread.start()

someInput = input("Input: ")

p.stdin.write(someInput)
errors = getOutput(errQueue)
output = getOutput(outQueue)