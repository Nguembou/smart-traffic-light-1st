input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 9; index++) {
        counter += -1
        basic.pause(500)
        if (counter == 0) {
            basic.showLeds(`
                . . # . .
                # # # # #
                . . # . .
                . # # # .
                # . . . #
                `)
            GREEN()
            basic.pause(5000)
        }
    }
    counter = 10
    for (let index = 0; index < 9; index++) {
        counter += -1
        basic.showNumber(counter)
        basic.pause(500)
        if (counter == 1) {
            basic.showLeds(`
                . # # # .
                # # . . #
                # . # . #
                # . . # #
                . # # # .
                `)
            ORANGE()
            basic.pause(500)
            RED()
        }
    }
    counter = 9
})
function RED () {
    range = strip.range(0, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Red))
    range = strip.range(1, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Black))
    range = strip.range(2, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Black))
}
function GREEN () {
    range = strip.range(2, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Green))
    range = strip.range(1, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Black))
    range = strip.range(0, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Black))
}
input.onButtonPressed(Button.AB, function () {
	
})
input.onButtonPressed(Button.B, function () {
    music.playTone(784, music.beat(BeatFraction.Whole))
    for (let index = 0; index < 9; index++) {
        counter += -1
        basic.pause(500)
        if (counter == 0) {
            music.playTone(698, music.beat(BeatFraction.Whole))
            basic.showLeds(`
                . . # . .
                # # # # #
                . . # . .
                . # # # .
                # . . . #
                `)
            GREEN()
            basic.pause(5000)
        }
    }
    counter = 10
    for (let index = 0; index < 9; index++) {
        music.playTone(659, music.beat(BeatFraction.Whole))
        counter += -1
        basic.showNumber(counter)
        basic.pause(500)
        if (counter == 1) {
            music.playTone(587, music.beat(BeatFraction.Whole))
            basic.showLeds(`
                . # # # .
                # # . . #
                # . # . #
                # . . # #
                . # # # .
                `)
            ORANGE()
            basic.pause(500)
            RED()
        }
    }
    counter = 9
})
function ORANGE () {
    range = strip.range(1, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Orange))
    range = strip.range(2, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Black))
    range = strip.range(0, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Black))
}
let distance = 0
let range: neopixel.Strip = null
let counter = 0
let strip: neopixel.Strip = null
basic.showLeds(`
    . # # # .
    # # . . #
    # . # . #
    # . . # #
    . # # # .
    `)
strip = neopixel.create(DigitalPin.P16, 3, NeoPixelMode.RGB)
strip.setBrightness(90)
RED()
counter = 9
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P1, 0)
    control.waitMicros(2)
    pins.digitalWritePin(DigitalPin.P1, 1)
    control.waitMicros(10)
    pins.digitalWritePin(DigitalPin.P1, 0)
    distance = pins.pulseIn(DigitalPin.P0, PulseValue.High) / 58
    basic.pause(2000)
    if (distance == 0) {
    	
    }
})
