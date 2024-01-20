def on_button_pressed_a():
    datalogger.log(datalogger.create_cv("A", 1), datalogger.create_cv("B", 0))
    basic.show_leds("""
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    datalogger.log(datalogger.create_cv("A", 1), datalogger.create_cv("B", 1))
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    datalogger.log(datalogger.create_cv("B", 1), datalogger.create_cv("A", 0))
    basic.show_leds("""
        . . # # #
        . . # # #
        . . # # #
        . . # # #
        . . # # #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

datalogger.include_timestamp(FlashLogTimeStampFormat.MINUTES)
datalogger.set_column_titles("A", "B")