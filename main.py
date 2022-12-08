def on_received_number(receivedNumber):
    if receivedNumber == 4:
        GREEN()
    elif receivedNumber == 6:
        RED()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global counter
    for index in range(9):
        counter += -1
        basic.pause(500)
        if counter == 0:
            basic.show_leds("""
                . . # . .
                                # # # # #
                                . . # . .
                                . # # # .
                                # . . . #
            """)
            GREEN()
            basic.pause(5000)
    counter = 10
    for index2 in range(9):
        counter += -1
        basic.show_number(counter)
        basic.pause(500)
        if counter == 1:
            basic.show_leds("""
                . # # # .
                                # # . . #
                                # . # . #
                                # . . # #
                                . # # # .
            """)
            ORANGE()
            basic.pause(500)
            RED()
    counter = 9
input.on_button_pressed(Button.A, on_button_pressed_a)

def RED():
    global range2
    range2 = strip.range(0, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.RED))
    range2 = strip.range(1, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    range2 = strip.range(2, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
def GREEN():
    global range2
    range2 = strip.range(2, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.GREEN))
    range2 = strip.range(1, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    range2 = strip.range(0, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))

def on_button_pressed_ab():
    pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global counter
    music.play_tone(831, music.beat(BeatFraction.WHOLE))
    for index3 in range(9):
        counter += -1
        basic.pause(500)
        if counter == 0:
            music.play_tone(698, music.beat(BeatFraction.WHOLE))
            basic.show_leds("""
                . . # . .
                                # # # # #
                                . . # . .
                                . # # # .
                                # . . . #
            """)
            GREEN()
            basic.pause(5000)
    counter = 10
    for index4 in range(9):
        counter += -1
        music.play_tone(698, music.beat(BeatFraction.WHOLE))
        basic.show_number(counter)
        basic.pause(500)
        if counter == 1:
            music.play_tone(831, music.beat(BeatFraction.WHOLE))
            basic.show_leds("""
                . # # # .
                                # # . . #
                                # . # . #
                                # . . # #
                                . # # # .
            """)
            ORANGE()
            basic.pause(500)
            RED()
    counter = 9
input.on_button_pressed(Button.B, on_button_pressed_b)

def ORANGE():
    global range2
    range2 = strip.range(1, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.ORANGE))
    range2 = strip.range(2, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    range2 = strip.range(0, 1)
    range2.show_color(neopixel.colors(NeoPixelColors.BLACK))
distance = 0
range2: neopixel.Strip = None
counter = 0
strip: neopixel.Strip = None
radio.set_group(79)
basic.show_leds("""
    . # # # .
        # # . . #
        # . # . #
        # . . # #
        . # # # .
""")
strip = neopixel.create(DigitalPin.P16, 3, NeoPixelMode.RGB)
strip.set_brightness(90)
RED()
counter = 9

def on_forever():
    global distance
    pins.digital_write_pin(DigitalPin.P1, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P1, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P1, 0)
    distance = pins.pulse_in(DigitalPin.P0, PulseValue.HIGH) / 58
    basic.pause(2000)
    if distance == 0:
        pass
basic.forever(on_forever)
