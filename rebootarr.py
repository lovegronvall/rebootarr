#!/usr/bin/env python3

import os
import time

reboot_file = "/tmp/reboot"
reboot_command = "/sbin/reboot"
reboot_password = "1"
sleep_time = 60

def main():

    # Lets not get stuck in endless reboot cycle:
    os.remove(reboot_file)

    while True:

        try:
            with open(reboot_file, "r") as f:
                content = f.read().strip()
            if content == reboot_password:
                print(f"File content is {reboot_password}, time to reboot: {reboot_command}")
                os.system(reboot_command)
            else:
                print(f"File found, but incorrect password")
        except FileNotFoundError:
            print(f"File not found: {reboot_file}")
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(sleep_time)

if __name__ == "__main__":
    main()

