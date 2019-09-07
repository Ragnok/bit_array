''' Goals:
* Learn to not underestimate the effort involved multithreading.
* Learn procedures and techniques for doing it reliably.

RR1:  Get your app tested and debugged in a singled threaded mode first
      before you start threading.  Threading NEVER makes debugging easier.

RR2:  Testing cannot prove the absence of errors.  It is still useful,
      don't rely on it.  Many interest racing conditions don't reveal
      themselves in test environments.

RR3:  97.3% of threading problems are either race conditions or sequencing problems.
      Good news, these problems can be solved reliably.  Bad new, the remaining 2.7%
      of threading problems are hard.

RR4:  Locks don't lock anything.  They are just flags and can be ignored.
      It is a cooperative tool, not an enforced tool.

RR5:  The more locks you are acquire at one time, the more you lose
      the advantages of concurrency.


RFC 1000:
    ALL shared resources SHALL be run in EXACTLY ONE thread.
    ALL communication with that thread SHALL be done using an atomic message queue:
    typically the Queue module, email, message queues like RabbitMQ or ZeroMQ,
    interesting you can communicate via a database as well.

    Resources that need this technique:  global variables, user input, output devices,
    files, sockets, etc.

    Some resources that already have locks inside (thread-safe):  logging module,
    decimal module (thread local variables), databases (reader locks and writer locks),
    email (this is an atomic message queue).

RFC 1001:
    One category of sequencing problems is to make sure that step A
    and step B happen sequentially.  The solution is to put both in
    the same thread where all actions proceed sequentially.

RFC 1002:  To implement a "barrier" that waits for parallel threads to complete,
    just join() all of the threads.

RFC 1003:  You can't wait on daemon threads to complete (they are infinite loops).
    Instead, you join() on the queue itself.  It waits until all the requested
    tasks are marked as being done.

RFC 1004:  Sometimes you need a global variable to communicate between functions.
    Global variables work great for this purpose in a single threaded program.
    In multithreaded code, it mutable global state is a disaster.  The better
    solution is to use a threading.local() that is global WITHIN a thread but
    not without.

Fuzzing improves the reliability of testing.

'''

import threading
import Queue
import time
import random

#######################################################

FUZZ = True

def fuzz():
    if FUZZ:
        time.sleep(random.random())

#######################################################
# Isolate access to the shared global variable

counter = 0

counter_queue = Queue.Queue()               # Dedicated email channel to the counter manager

# Hire a manager of the resource with exclusive access to the resource

def counter_manager():
    'I EXCLUSIVE rights to update the counter.'
    global counter
    while True:
        increment = counter_queue.get()     # Sleeps until a requests arrives
        counter += increment
        print_queue.put([
            'The count is %d' % counter,
            '--------------',
        ])
        counter_queue.task_done()

t = threading.Thread(target=counter_manager)
t.daemon = True
t.start()
del t

#######################################################
# Isolate the print resource

print_queue = Queue.Queue()

def print_manager():
    'I have EXCLUSIVE rights to call the "print" keyword'
    while True:
        job = print_queue.get()             # Sleeps until a request is made
        for line in job:
            print line
        print_queue.task_done()

t = threading.Thread(target=print_manager)
t.daemon = True
t.start()
del t

#######################################################

def worker():
    counter_queue.put(1)

print_queue.put(['Starting up'])
# Guarantee:  'Starting up' request has been sent to the print manager

workers = []
for i in range(10):
    t = threading.Thread(target=worker)
    t.start()
    workers.append(t)
# Guarantee is ten workers have started

for t in workers:
    t.join()                            # Wait until a worker returns
# Guarantee is that all ten workers have finished sending an email
# the counter manager.

counter_queue.join()
# Guarantee is that the counter manager has opened all ten email
# requests and report that the work required for each of them is done.
# In particular, the global variable "counter" has been incremeneted
# ten times AND ten email requests have been sent to the print queue
# for a total of eleven.
    
print_queue.put(['Finished!'])
# Guarantee is that twelve print jobs were submitted.
# The first was "starting up" and the last was "finished"

print_queue.join()
# Guarantee is the print manager has opened all twelve print job
# requests and has reported that they've actually physically
# been printed.

# Now, it is okay to return control, either ending the program
# or letting IDLE print the >>> prompt.



