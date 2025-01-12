# This is responsible for running thread and updating the ui
# whenever there is a change on the state
# [for example: trigger from the physical button]
import threading
import time


class AppThread:
    def __init__(self):
        self.running = True
        self.thread = threading.Thread(target=self.run_thread)
        self.thread.daemon = True
        print('starting thread')

    def run_thread(self):
        while self.running:
            self.run()
            time.sleep(5)

    def start(self):
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def run(self):
        print('running')
        # reading the state of the button and updating the ui
