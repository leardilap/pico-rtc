pico-rtc

first download the most recent micropython.uf2 from the website, 
currently it is `rp2-pico-20220117-v1.18.uf2`

press the boot button and plug the pico, then drag the .uf2 to it.

reboot


send files to the pico 
`rshell --buffer-size=512 -p /dev/ttyACM1`

this creates a /pyboard folder on to one can copy the main.py file

`cp *.py /pyboard/`

control-D to disconnect

reboot and the file will be executed

connect to pico terminal and use python interactively
`screen /dev/ttyACM1`


for example:
`>>> print("Hello, Pico!")`

to issue a soft reset do control+d, then all python libraries are available to use interactively.

