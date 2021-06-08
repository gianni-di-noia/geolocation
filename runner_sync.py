"""Speedtest runner."""
import os
import time

import controller

PATH = os.path.dirname(os.path.realpath(__file__))


def speed_test():
    """Utility function to test unique IP."""
    start = time.perf_counter()

    ips = open(PATH + "/10K_ips.txt", "r").readlines()
    for ip_address in ips:
        country = controller.search_country(ip_address.replace("\n", ""))
        print(country)
    elapsed = time.perf_counter() - start
    print(f"10K executed in {elapsed:0.2f} seconds.")


if __name__ == "__main__":
    speed_test()
