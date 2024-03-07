import threading
from time import sleep

class Screwdriver:

    def __init__(self, id):
        self.id = id
        self.lock = threading.Lock()

    def pick_up(self):
        sleep(0.3)
        self.lock.acquire()

    def put_down(self):
        sleep(0.3)
        self.lock.release()


class Doctor(threading.Thread):
    def __init__(self, id: int, l_scr, r_scr) -> None:
        super().__init__()
        self.state = 0
        self.id = id
        self.l_scr = l_scr
        self.r_scr = r_scr

    def run(self):
        self.l_scr.pick_up()
        self.r_scr.pick_up()
        sleep(1)
        print(f"Doctor {self.id}: BLAST!")
        self.l_scr.put_down()
        self.r_scr.put_down()


if __name__ == '__main__':
    start_id = 9
    n = 5
    screwdrivers = [Screwdriver(i) for i in range(start_id, start_id + n)]
    doctors = [Doctor(start_id + i, screwdrivers[i], screwdrivers[i + 1]) for i in range(n - 1)]
    last_doctor = Doctor(start_id + n - 1, screwdrivers[n - 1], screwdrivers[0])

for doctor in doctors:
        doctor.start()
for t in doctors:
    t.join()
last_doctor.start()
