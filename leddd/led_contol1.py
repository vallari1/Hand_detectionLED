import pyfirmata

comport='COM5'

board=pyfirmata.Arduino(comport)


led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')
led_5=board.get_pin('d:12:o')
leds = [led_1,led_2,led_3,led_4,led_5]
def led(fingerUp):
    # for i in fingerUp:
    #     if (i==1):
    #         leds[i].write(1)
    #     else:
    #         leds[i].write(0)
    if fingerUp==[0,0,0,0,0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

    elif fingerUp==[0,0,0,0,1]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(1)
    elif fingerUp==[0,0,0,1,1]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(1)
        led_5.write(1)    
    # elif fingerUp==[0,0,1,0,0]:
    #     led_1.write(0)
    #     led_2.write(0)
    #     led_3.write(1)
    #     led_4.write(0)
    #     led_5.write(0)
    elif fingerUp==[0,0,1,1,0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp==[0,0,1,0,1]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        led_4.write(0)
        led_5.write(1)
    elif fingerUp==[0,0,1,1,1]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
    elif fingerUp==[0,1,0,0,0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[0,1,0,0,1]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(1)
    elif fingerUp==[0,1,0,1,0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp==[0,1,0,1,1]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
        led_4.write(1)
        led_5.write(1)
    elif fingerUp==[0,1,1,0,0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[0,1,1,1,0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp==[0,1,1,1,1]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
    elif fingerUp==[1,0,0,0,0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)

    elif fingerUp==[1,0,0,0,1]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(1)
    elif fingerUp==[1,0,0,1,1]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(1)
        led_5.write(1)    
    # elif fingerUp==[1,0,1,0,0]:
    #     led_1.write(1)
    #     led_2.write(0)
    #     led_3.write(1)
    #     led_4.write(0)
    #     led_5.write(0)
    elif fingerUp==[1,0,1,1,0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp==[1,0,1,0,1]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(1)
        led_4.write(0)
        led_5.write(1)
    elif fingerUp==[1,0,1,1,1]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
    elif fingerUp==[1,1,0,0,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[1,1,0,0,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(1)
    elif fingerUp==[1,1,0,1,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp==[1,1,0,1,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(1)
        led_5.write(1)
    elif fingerUp==[1,1,1,0,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp==[1,1,1,1,0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp==[1,1,1,1,1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)    
    