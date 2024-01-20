input.onButtonPressed(Button.A, function () {
    datalogger.log(
    datalogger.createCV("A", 1),
    datalogger.createCV("B", 0)
    )
    basic.showLeds(`
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    datalogger.log(
    datalogger.createCV("A", 1),
    datalogger.createCV("B", 1)
    )
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
})
input.onButtonPressed(Button.B, function () {
    datalogger.log(
    datalogger.createCV("B", 1),
    datalogger.createCV("A", 0)
    )
    basic.showLeds(`
        . . # # #
        . . # # #
        . . # # #
        . . # # #
        . . # # #
        `)
})
datalogger.includeTimestamp(FlashLogTimeStampFormat.Minutes)
datalogger.setColumnTitles(
"A",
"B"
)
