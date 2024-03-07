import itertools
import time
from threading import Event, Thread

def spin(msg: str, done: Event) -> None:
    for char in itertools.cycle('\|/-'):
        status = f'\r{char}{msg}'
        print(status, end='', flush=True)
        if done.wait(.1): # we need the animation to happen at 10 fps
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    time.sleep(3)
    return 42

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
    print(f'spinner object {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer {result}')

if __name__ == '__main__':
    main()
    


