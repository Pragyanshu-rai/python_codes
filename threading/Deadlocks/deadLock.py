from threading import Thread, Lock
from time import sleep


# using the resource locks to lock the resource using the specific thread
resourceLockOne = Lock()
resourceLockTwo = Lock()


def resourceOne(threadName, threadId) -> None:
    """
        Given the threadName and threadId this resource when invoked by the respected
        thread will be allocated to that thread.
    """

    print(
        f"This resource(One) has been allocated to {threadId} - {threadName}")


def resourceTwo(threadName, threadId) -> None:
    """
        Given the threadName and threadId this resource when invoked by the respected
        thread will be allocated to that thread.
    """

    print(
        f"This resource(Two) has been allocated to {threadId} - {threadName}")


class ProcessThreadOne(Thread):

    def __init__(self, threadName, threadId) -> None:
        Thread.__init__(self)
        self.threadName = threadName
        self.threadId = threadId

    def run(self):
        # locking the resourceOne
        resourceLockOne.acquire()
        resourceOne(self.threadName, self.threadId)

        # waiting for the other thread to lock the resourceTwo
        sleep(2)

        # locking the resourceTwo
        resourceLockTwo.acquire()
        resourceTwo(self.threadName, self.threadId)

        # releasing all the resources
        resourceLockOne.release()
        resourceLockTwo.release()


class ProcessThreadTwo(Thread):

    def __init__(self, threadName, threadId) -> None:
        Thread.__init__(self)
        self.threadName = threadName
        self.threadId = threadId

    def run(self):
        # locking the resourceTwo
        resourceLockTwo.acquire()
        resourceTwo(self.threadName, self.threadId)

        # waiting for the other thread to lock the resourceTwo
        sleep(2)

        # locking the resourceOne
        resourceLockOne.acquire()
        resourceOne(self.threadName, self.threadId)

        # releasing all the resources
        resourceLockOne.release()
        resourceLockTwo.release()


class ProcessThreadTwoSafe(Thread):

    def __init__(self, threadName, threadId) -> None:
        Thread.__init__(self)
        self.threadName = threadName
        self.threadId = threadId

    def run(self):
        # locking the resourceOne
        resourceLockOne.acquire()
        resourceOne(self.threadName, self.threadId)

        # waiting for the other thread to lock the resourceTwo
        sleep(2)

        # locking the resourceTwo
        resourceLockTwo.acquire()
        resourceTwo(self.threadName, self.threadId)

        # releasing all the resources
        resourceLockOne.release()
        resourceLockTwo.release()


if __name__ == "__main__":

    startWithDeadLock = input(
        "Enter 'yes' to start the process in deadlock\n>")

    if startWithDeadLock == 'yes':
        print("Ok >>> starting with deadlock")
        t1 = ProcessThreadOne("ThreadOne", "1234")
        t2 = ProcessThreadTwo("ThreadTwo", "5678")

    else:
        print("Ok >>> starting without deadlock")
        t1 = ProcessThreadOne("Threadone", "1234")
        t2 = ProcessThreadTwoSafe("ThreadTwo", "5678")
    
    t1.start()
    t2.start()

    sleep(10)

    if t1.is_alive() == True and t2.is_alive() == True:
        print("The process went into DEADLOCK!!!")

    t1.join()
    t2.join()

    print("The process ended without a DEADLOCK")
