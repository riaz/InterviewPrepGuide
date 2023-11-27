from threading import Semaphore
from threading import Barrier
from typing import Callable

class H2O:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.bar_assembling = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        with self.sem_h:
            self.bar_assembling.wait()

            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        with self.sem_o:
            self.bar_assembling.wait()

            releaseOxygen()


def printMole(mole):
    print(mole)

if __name__ == '__main__':
    water = 'HOH'
    h = H2O()
    


