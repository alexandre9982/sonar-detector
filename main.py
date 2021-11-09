distance = 0

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    if distance < 5:
        basic.show_leds("""
            # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    elif distance < 10:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    elif distance < 15:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        . . . . .
                        . . . . .
        """)
    elif distance < 20:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        . . . . .
        """)
    elif distance < 25:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
basic.forever(on_forever)
