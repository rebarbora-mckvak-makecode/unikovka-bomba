tm1638.onButtonPressEvent(function (index) {
    tm1638.setLED_on(index)
})
let sekund_do_vybuchu = 10
tm1638.init(DigitalPin.P0, DigitalPin.P1, DigitalPin.P2)
while (sekund_do_vybuchu > 0) {
    sekund_do_vybuchu += -1
    basic.pause(1000)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    tm1638.showNumberLeft(sekund_do_vybuchu / 60)
    tm1638.showNumberRight(sekund_do_vybuchu % 60)
}
music.play(music.builtinPlayableSoundEffect(soundExpression.slide), music.PlaybackMode.UntilDone)
basic.showIcon(IconNames.Skull)
basic.pause(1000)
basic.clearScreen()
while (true) {
    basic.showString("game over")
}
