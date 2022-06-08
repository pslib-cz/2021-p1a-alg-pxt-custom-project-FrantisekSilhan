let pin_LS = DigitalPin.P1
let pin_LP = DigitalPin.P2
let pin_PP = DigitalPin.P9
let wall_const = 0
let speed = 30
// rotate left
forever(function main() {
    let LS = pins.digitalReadPin(pin_LS)
    // Levý Střední
    let LP = pins.digitalReadPin(pin_LP)
    // Levý Přední
    let PP = pins.digitalReadPin(pin_PP)
    // Pravý Přední
    if (LS == wall_const) {
        // levý senzor detekuje stěnu
        if (PP == wall_const || LP == wall_const) {
            while (LP == wall_const) {
                motor_run(speed, -speed, speed, -speed)
                // rotate right
                LP = pins.digitalReadPin(pin_LP)
            }
        } else {
            // přední senzory nedetekují stěnu
            motor_run(speed, speed, speed, speed)
        }
        
    } else if (LP == wall_const) {
        // auto je v průběhu otáčení a levý senzor nedetekuje stěnu
        while (LS != wall_const) {
            motor_run(speed, -speed, speed, -speed)
            // rotate right
            if (LP != wall_const) {
                motor_run(-speed, speed, speed, -speed)
            }
            
            // go left
            LS = pins.digitalReadPin(pin_LS)
            LP = pins.digitalReadPin(pin_LP)
        }
    } else {
        motor_run(0, speed, 0, speed)
    }
    
})
function motor_run(UpL: number = 0, UpR: number = 0, LwL: number = 0, LwR: number = 0) {
    mecanumRobot.Motor(LR.Upper_left, MD.Forward, Math.constrain(UpL, -100, 100))
    mecanumRobot.Motor(LR.Upper_right, MD.Forward, Math.constrain(UpR, -100, 100))
    mecanumRobot.Motor(LR.Lower_left, MD.Forward, Math.constrain(LwL, -100, 100))
    mecanumRobot.Motor(LR.Lower_right, MD.Forward, Math.constrain(LwR, -100, 100))
}

