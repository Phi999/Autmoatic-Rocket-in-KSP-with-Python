import krpc
import time


conn = krpc.connect(name='Controller')
vessel = conn.space_center.active_vessel
vessel.control.sas = True








def altitudine(a):
    mean_altitude = conn.get_call(getattr, vessel.flight(), 'mean_altitude')

    expr = conn.krpc.Expression.greater_than(
        conn.krpc.Expression.call(mean_altitude),
        conn.krpc.Expression.constant_double(a))
    vessel.control.sas = True

    event = conn.krpc.add_event(expr)
    with event.condition:
        event.wait()
    print('Got to ' + str(a))
def altitudine1(a):
    mean_altitude = conn.get_call(getattr, vessel.flight(), 'mean_altitude')

    expr = conn.krpc.Expression.less_than(
        conn.krpc.Expression.call(mean_altitude),
        conn.krpc.Expression.constant_double(a))
    vessel.control.sas = True

    event = conn.krpc.add_event(expr)
    with event.condition:
        event.wait()
    print('Booster   separation')





print(vessel.name)
print("\nReady!\n")
time.sleep(10)
vessel.control.sas = True

vessel.auto_pilot.target_pitch_and_heading(90, 0)
vessel.control.throttle = 1
vessel.auto_pilot.engage()

time.sleep(1)

print('Launch!')



vessel.control.activate_next_stage()
vessel.control.sas = True

altitudine(2000)
vessel.control.activate_next_stage()
vessel.control.activate_next_stage()

print('Succesfull!')



time.sleep(2)

altitudine(5000)

print('Gravity turn')

vessel.auto_pilot.target_pitch_and_heading(90, 60)


time.sleep(3)


vessel.control.sas = True




#vessel.control.activate_next_stage()

time.sleep(3)



# 3
altitudine(10000)
print("Jos al doilea motor")
vessel.control.activate_next_stage()
print("pornim al doilea motor")
vessel.control.activate_next_stage()

print('al doilea motor 0.1')
vessel.control.throttle = 0.1

print('Gravity turn + sas(nu merge me reu)')
vessel.control.sas = True
vessel.auto_pilot.target_pitch_and_heading(90, 60)
vessel.auto_pilot.target_pitch_and_heading(90, 60)

vessel.auto_pilot.engage()
time.sleep(2)

time.sleep(3)
print('Succesfull!')
altitudine(20000)
vessel.control.throttle = 0
altitudine1(15000)
vessel.auto_pilot.target_pitch_and_heading(90, 60)






altitudine1(3000)
print("parachuta")
vessel.control.activate_next_stage()
vessel.control.throttle = 0.45


vessel.auto_pilot.engage()
altitudine1(1900)
vessel.control.activate_next_stage()

vessel.auto_pilot.engage()
time.sleep(1)
print("Succesfull!!")


#mai lucreaza la ultima parte
altitudine1(1500)
vessel.control.throttle = 0.5


altitudine1(900)
vessel.control.throttle = 0.1
altitudine1(100)
vessel.control.throttle = 0
altitudine1(370)
vessel.control.throttle = 0.1
altitudine1(360)
vessel.control.throttle = 0.0
altitudine1(365)
vessel.control.throttle = 0.1
altitudine1(355)
vessel.control.throttle = 0.0
altitudine1(350)
vessel.control.throttle = 0.1
altitudine1(340)
vessel.control.throttle = 0.0


altitudine1(150)
print("suucces!!!!!!!!!!!!")



#PUNE ALTITUDINEA PE MARE CA SA MEARGA, ALTFEL E PREA JOS CAND DESCHIDE PARASUTA







