import cyberpi, mbot2
import time
import math, random

_trackWidth = 11.5
_circumference = 20.420352248333657
_diffPortsSwapped = False


def run():
    while True:
        cyberpi.console.println("Robotul nu face nimic")
        cyberpi.led.on((255, 0, 0)[0], (255, 0, 0)[1], (255, 0, 0)[2], 1)
        cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 2)
        if cyberpi.controller.is_press("up"):
            mbot2.drive_speed(30, -(30))
            cyberpi.console.println("Robotul merge in fata")
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 1)
            cyberpi.led.on((51, 102, 255)[0], (51, 102, 255)[1], (51, 102, 255)[2], 2)
        else:
            cyberpi.console.println("Robotul nu face nimic")
            cyberpi.led.on((255, 0, 0)[0], (255, 0, 0)[1], (255, 0, 0)[2], 1)
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 2)
        if cyberpi.controller.is_press("down"):
            mbot2.drive_speed(-(30),30)
            cyberpi.console.println("Robotul merge in spate")
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 1)
            cyberpi.led.on((51, 102, 255)[0], (51, 102, 255)[1], (51, 102, 255)[2], 2)
        else:
            cyberpi.console.println("Robotul nu face nimic")
            cyberpi.led.on((255, 0, 0)[0], (255, 0, 0)[1], (255, 0, 0)[2], 1)
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 2)
        if cyberpi.controller.is_press("left"):
            mbot2.drive_speed(-(30), -(30))
            cyberpi.console.println("Robotul face curba la stanga")
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 1)
            cyberpi.led.on((51, 102, 255)[0], (51, 102, 255)[1], (51, 102, 255)[2], 2)
        else:
            cyberpi.console.println("Robotul nu face nimic")
            cyberpi.led.on((255, 0, 0)[0], (255, 0, 0)[1], (255, 0, 0)[2], 1)
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 2)
        if cyberpi.controller.is_press("right"):
            mbot2.drive_speed(30, 30)
            cyberpi.console.println("Robotul face curba la dreapta")
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 1)
            cyberpi.led.on((51, 102, 255)[0], (51, 102, 255)[1], (51, 102, 255)[2], 2)
        else:
            cyberpi.console.println("Robotul nu face nimic")
            cyberpi.led.on((255, 0, 0)[0], (255, 0, 0)[1], (255, 0, 0)[2], 1)
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 2)
        if cyberpi.controller.is_press("A"):
            cyberpi.console.println("Buna ziua! Acesta este un program intuitiv realizat \u00EEn Open Roberta Lab, care este simplu de utilizat. Am creat acest program intuitiv pentru copii care \u00EEnva\u021B\u0103 logica, sa-\u0219i imagineze \u00EEn mintea lor ce pot face, astfel \u00EEnc\u00E2t s\u0103 \u00EEl poat\u0103 reprograma sau s\u0103 \u00EEl avanseze \u00EEn python sau scratch.")
            cyberpi.led.on((255, 0, 0)[0], (255, 0, 0)[1], (255, 0, 0)[2], 1)
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 2)
        if cyberpi.controller.is_press("B"):
            cyberpi.console.println("Robotul Lumineaza")
            cyberpi.led.on((255, 255, 51)[0], (255, 255, 51)[1], (255, 255, 51)[2], 1)
            cyberpi.led.on((204, 102, 204)[0], (204, 102, 204)[1], (204, 102, 204)[2], 2)
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 3)
            cyberpi.led.on((51, 102, 255)[0], (51, 102, 255)[1], (51, 102, 255)[2], 4)
            cyberpi.led.on((255, 153, 255)[0], (255, 153, 255)[1], (255, 153, 255)[2], 5)
            time.sleep(5000/1000)
            cyberpi.led.off("all")
            time.sleep(100/1000)
            cyberpi.console.println("Robotul nu face nimic")
            cyberpi.led.on((255, 0, 0)[0], (255, 0, 0)[1], (255, 0, 0)[2], 1)
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 2)
        else:
            cyberpi.console.println("Robotul nu face nimic")
            cyberpi.led.on((255, 0, 0)[0], (255, 0, 0)[1], (255, 0, 0)[2], 1)
            cyberpi.led.on((51, 255, 51)[0], (51, 255, 51)[1], (51, 255, 51)[2], 2)

def main():
    try:
        run()
    except Exception as e:
        cyberpi.display.show_label("Exeption on Mbot 2", 16, int(8 * 0 + 5), int(17 * 0))
        cyberpi.display.show_label(e, 16, int(8 * 0 + 5), int(17 * 1))
        raise
    finally:
        mbot2.motor_stop("all")
        mbot2.EM_stop("all")
main()