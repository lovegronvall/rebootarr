# rebootarr
Reboot mac server by writing to a file (from for example a container)

Default file is /tmp/reboot and the content it should have for a reboot is simply 1

So for rebooting you can run:
```
echo 1 >tmp/reboot
```


## Installation (macOS)
```
sudo cp rebootarr.py /opt
sudo chown root:wheel /opt/rebootarr.py
sudo chmod 644 /opt/rebootarr.py

sudo cp com.rebootarr.autostart.plist /Library/LaunchDaemons/com.rebootarr.autostart.plist
sudo chown root:wheel /Library/LaunchDaemons/com.rebootarr.autostart.plist
sudo chmod 644 /Library/LaunchDaemons/com.rebootarr.autostart.plist
```


