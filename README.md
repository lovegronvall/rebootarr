```
   .
           .                 .          .                               .
  _|__:                          .    . .      ·
_/ |·:|__:_|___________ :____|_  .      :      :        .....   :_______|_ _
\     |  | |·:\_______/_|    |:\ :____|_|      |_____ .::·  ·:. |   _   |:\_\_
 \    :  |     /      ·:|       \|    |:\   ________/_::   .:·  |  _/      / /
  \_     :    /         |      \ \       \_  ·:|      ·:..:·  .:·:.\______/ ·
    \______|_/________|_|______|\         /______       ·:::::· |.·  ·:|
         . |  .    .  | :      : \____|__/      \____|_/        :      :
           .          . :__|_  ·     ·|              |          ·      .
        _|____|_  _|____|  |:\ :     :.       .....  .
      _/ |    |:\/ |  ·:|     \|     |_____ .::·  ·:.
     /      :    \      :      \_ ________/_::   .:·
  · /    :  |     \______       /  ·:|      ·:..:·  .:·:.
_/_/     |__|_|____/    \____|_/_|____        ·:::::·  .·
\_\_|____|  : |              |   |   \_____|__/
    |    :    .              .   .         |
    .                                      .
```
# rebootarr
Reboot server by writing to a file (from for example a container)

Default file is /tmp/reboot and the content it should have for a reboot is simply 1

So for rebooting you can run:
```
echo 1 >tmp/reboot
```


## Installation (macOS)
In Terminal, go to the directory containing this repo and run the following code. It should activate after your next reboot:
```
sudo cp rebootarr.py /opt
sudo chown root:wheel /opt/rebootarr.py
sudo chmod 750 /opt/rebootarr.py

sudo cp com.rebootarr.autostart.plist /Library/LaunchDaemons/com.rebootarr.autostart.plist
sudo chown root:wheel /Library/LaunchDaemons/com.rebootarr.autostart.plist
sudo chmod 644 /Library/LaunchDaemons/com.rebootarr.autostart.plist
```


