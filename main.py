"""

modra sviti
zluta sviti
oranzova sviti
fialova nesviti
seda nesviti
zelena nesviti
cerna nesviti
cervena nesviti

"""

def on_button_press(index):
    if ledky[index] == 0:
        ledky[index] = 1
        tm1638.setLED_on(index)
    else:
        ledky[index] = 0
        tm1638.setLED_off(index)
tm1638.on_button_press_event(on_button_press)

def vytvor_seznam_ledky():
    global ledky
    ledky = []
    for pořadí in range(9):
        ledky[pořadí] = 0
ledky: List[number] = []
vytvor_seznam_ledky()
sekund_do_vybuchu = 600
tm1638.init(DigitalPin.P0, DigitalPin.P1, DigitalPin.P2)
while not (sekund_do_vybuchu == 0 or ledky[1] == 0 and ledky[2] == 0 and ledky[3] == 0 and ledky[4] == 1 and ledky[5] == 0 and ledky[6] == 1 and ledky[7] == 1 and ledky[8] == 0):
    sekund_do_vybuchu += -1
    basic.pause(1000)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    tm1638.show_number_left(sekund_do_vybuchu / 60)
    tm1638.show_number_right(sekund_do_vybuchu % 60)
music.play(music.builtin_playable_sound_effect(soundExpression.slide),
    music.PlaybackMode.UNTIL_DONE)
basic.show_icon(IconNames.SKULL)
basic.pause(1000)
basic.clear_screen()
while True:
    basic.show_string("game over")