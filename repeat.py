import mouse, keyboard, sys, winsound

num_images = int(sys.argv[1])
dur = 500
freq = 440

while True:
    mouse_events = []

    keyboard.wait('a')

    mouse.hook(mouse_events.append)

    keyboard.wait('a')

    mouse.unhook(mouse_events.append)

    events = []

    for i in range(num_images - 1):
        mouse.play(mouse_events, speed_factor=10)

    mouse.move(615, 804, absolute=True)
    mouse.click()
    winsound.Beep(freq, dur)