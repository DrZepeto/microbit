music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
        5000,
        0,
        255,
        0,
        500,
        SoundExpressionEffect.NONE,
        InterpolationCurve.LINEAR),
    SoundExpressionPlayMode.UNTIL_DONE)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(1000)
    basic.show_icon(IconNames.NO)
    basic.pause(1000)
basic.forever(on_forever)
