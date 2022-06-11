led.enable(False)
pin_LS = DigitalPin.P7
pin_LP = DigitalPin.P2
pin_PP = DigitalPin.P1
#pin_PS = DigitalPin.P9
wall_const = 0
speed = 50
pause_length = 200

#wheel offset
UpR_offset = 0.9
LwR_offset = 0.9

def main():
    LS = pins.digital_read_pin(pin_LS) #Levý Střední
    LP = pins.digital_read_pin(pin_LP) #Levý Přední
    PP = pins.digital_read_pin(pin_PP) #Pravý Přední
    if LS == wall_const: #levý senzor detekuje stěnu
        if PP == wall_const or LP == wall_const:
            while LP == wall_const:
                motor_run(speed, -speed, speed, -speed) #rotate right

                LP = pins.digital_read_pin(pin_LP)
                basic.pause(pause_length)
        else: #přední senzory nedetekují stěnu
            motor_run(speed, speed, speed, speed) #go forward

    else:
        if LP == wall_const: #auto je v průběhu otáčení a levý senzor nedetekuje stěnu
            while LS != wall_const:
                
                if LP != wall_const:
                    motor_run(-speed, speed, speed, -speed) #go left
                else:
                    motor_run(speed, -speed, speed, -speed) #rotate right
                    basic.pause(pause_length)

                LS = pins.digital_read_pin(pin_LS)
                LP = pins.digital_read_pin(pin_LP)
                
        else:
            motor_run(0, speed, 0, speed) #rotate left

def motor_run(UpL = 0, UpR = 0, LwL = 0, LwR = 0):
    mecanumRobot.Motor(LR.Upper_left,  MD.FORWARD if UpL >= 0 else MD.BACK, Math.abs(UpL))
    mecanumRobot.Motor(LR.Upper_right, MD.FORWARD if UpR >= 0 else MD.BACK, Math.constrain(Math.abs(UpR * UpR_offset), 0, 100))
    mecanumRobot.Motor(LR.Lower_left,  MD.FORWARD if LwL >= 0 else MD.BACK, Math.abs(LwL))
    mecanumRobot.Motor(LR.Lower_right, MD.FORWARD if LwR >= 0 else MD.BACK, Math.constrain(Math.abs(LwR * LwR_offset), 0, 100))

forever(main)