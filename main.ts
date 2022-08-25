music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(1000)
    basic.showIcon(IconNames.No)
    basic.pause(1000)
})
