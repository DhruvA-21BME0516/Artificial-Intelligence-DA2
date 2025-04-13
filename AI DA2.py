def m_state(vib1, temp1, curr1):
   
    if vib1 and temp1 and curr1:
        return "Immediatly Shutdown"
    elif vib1 and temp1:
        return "Overheating and vibration"
    elif curr1 and (vib1 or temp1):
        return "High load used"
    elif vib1:
        return "Vibration High"
    elif temp1:
        return "Temperature High"
    elif curr1:
        return "High Power Used"
    else:
        return "Normal"

test = [
    (False, False, False),
    (True, False, False),
    (False, True, True),
    (True, True, True)
    ]

print("Machine State:")
print("-----------------------")
for vib, temp, curr in test:
    state = m_state(vib, temp, curr)
    sensor = []
    if vib: sensor.append("Vibration")
    if temp: sensor.append("Temperature")
    if curr: sensor.append("Current")
    
    if sensor:
        print(f"High reading: {', '.join(sensor)}")
    else:  
        print("Normal State")
        print(f"Machine state: {state}\n")