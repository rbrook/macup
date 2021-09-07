#!/usr/bin/env python
import time
import sys

from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KController, Key

active = len(sys.argv) == 2 and sys.argv[1] == 'click'
if active:
    print("active mode on!")
    kb = KController()

step = 1 if active else 9
sleep_interval = 4*60+30 if not active else 10  # 10 secs for active, 4.5 mins for pasive

start_time = time.time()


msg="""

#########################################################################
#########################################################################
#########################################################################

!!!!! SET YOURSELF AS 'ACTIVE' ON SLACK !!!!!!

#########################################################################
#########################################################################
#########################################################################
"""

print(msg)
time.sleep(5)

while True:
    time.sleep(sleep_interval)
    mouse = Controller()
    cur_mouse_pos = mouse.position  # get mouse position
    print("mins since launch:", (time.time()-start_time)/60)
    mouse.position = (cur_mouse_pos[0] + step, cur_mouse_pos[1] + step)
    if active:
        print('clicking..')
        #mouse.click(Button.left, 2)
        kb.type('.')
        time.sleep(1)
        kb.press(Key.backspace)
        kb.release(Key.backspace)

    step *= -1  # move forward and backward, to avoid standing still in the corner
