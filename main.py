def on_button_press(index):
    tm1638.setLED_on(index)
tm1638.on_button_press_event(on_button_press)

sekund_do_vybuchu = 10
tm1638.init(DigitalPin.P0, DigitalPin.P1, DigitalPin.P2)
while sekund_do_vybuchu > 0:
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

def on_forever():
    pass
basic.forever(on_forever)
