led.enable(False)
pin_LS = DigitalPin.P1
pin_LP = DigitalPin.P2
pin_PP = DigitalPin.P9
wall_const = 0
speed = 30

def main():
    LS = pins.digital_read_pin(pin_LS) #Levý Střední
    LP = pins.digital_read_pin(pin_LP) #Levý Přední
    PP = pins.digital_read_pin(pin_PP) #Pravý Přední
    if LS == wall_const: #levý senzor detekuje stěnu
        if PP == wall_const or LP == wall_const:
            while LP == wall_const:
                motor_run(speed, -speed, speed, -speed) #rotate right

                LP = pins.digital_read_pin(pin_LP)
        else: #přední senzory nedetekují stěnu
            motor_run(speed, speed, speed, speed) #go forward

    else:
        if LP == wall_const: #auto je v průběhu otáčení a levý senzor nedetekuje stěnu
            while LS != wall_const:
                motor_run(speed, -speed, speed, -speed) #rotate right
                if LP != wall_const:
                    motor_run(-speed, speed, speed, -speed) #go left

                LS = pins.digital_read_pin(pin_LS)
                LP = pins.digital_read_pin(pin_LP)
        else:
            motor_run(0, speed, 0, speed) #rotate left
forever(main)

def motor_run(UpL = 0, UpR = 0, LwL = 0, LwR = 0):
    mecanumRobot.Motor(LR.Upper_left, MD.FORWARD, Math.constrain(UpL, -100, 100))
    mecanumRobot.Motor(LR.Upper_right, MD.FORWARD, Math.constrain(UpR, -100, 100))
    mecanumRobot.Motor(LR.Lower_left, MD.FORWARD, Math.constrain(LwL, -100, 100))
    mecanumRobot.Motor(LR.Lower_right, MD.FORWARD, Math.constrain(LwR, -100, 100))