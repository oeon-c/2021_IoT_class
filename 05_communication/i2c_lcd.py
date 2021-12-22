from lcd import drivers
import time

display = drivers.Lcd()

try:
    print('Writing to Display')
    display.lcd_display_string('Helllo, World!', 1)
    while True:
        display.lcd_display_string('** Welcome **', 2)
        time.sleep(2)
        display.lcd_display_string('   Welcome   ', 2)
        time.sleep(2)

finally:
    print('cleaning up')
    display.lcd_clear()