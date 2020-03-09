#!/usr/bin/env python
import subprocess
import time
from time import sleep


def get_logs():
    result = subprocess.run(['docker', 'logs', 'rabbitmq'],
                            stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8', 'ignore')


def main():
    start = time.time()
    while "server startup complete" not in get_logs().lower():
        sleep(0.1)  # sleep for 100 ms
    end = time.time()
    execution_time = end - start
    print(f"blocking took {execution_time:.3f} seconds.")


if __name__ == '__main__':
    main()
