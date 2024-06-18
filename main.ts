// modra sviti
// zluta sviti
// oranzova sviti
// fialova nesviti
// seda nesviti
// zelena nesviti
// cerna nesviti
// cervena nesviti
tm1638.onButtonPressEvent(function (index) {
    if (ledky[index] == 0) {
        ledky[index] = 1
        tm1638.setLED_on(index)
    } else {
        ledky[index] = 0
        tm1638.setLED_off(index)
    }
})
function vytvor_seznam_ledky () {
    ledky = []
    for (let pořadí = 0; pořadí <= 8; pořadí++) {
        ledky[pořadí] = 0
    }
}
let ledky: number[] = []
music.setVolume(60)
vytvor_seznam_ledky()
let sekund_do_vybuchu = 900
tm1638.init(DigitalPin.P0, DigitalPin.P1, DigitalPin.P2)
while (!(sekund_do_vybuchu == 0 || ledky[1] == 0 && ledky[2] == 0 && ledky[3] == 0 && ledky[4] == 1 && ledky[5] == 0 && ledky[6] == 1 && ledky[7] == 1 && ledky[8] == 0)) {
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
