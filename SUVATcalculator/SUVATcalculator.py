#suvat calculator
#what are we working out
print("███████╗██╗   ██╗██╗   ██╗ █████╗ ████████╗")
print("██╔════╝██║   ██║██║   ██║██╔══██╗╚══██╔══╝")
print("███████╗██║   ██║██║   ██║███████║   ██║   ")
print("╚════██║██║   ██║╚██╗ ██╔╝██╔══██║   ██║  ┌─┐┌─┐┬  ┌─┐┬ ┬┬  ┌─┐┌┬┐┌─┐┬─┐")
print("███████║╚██████╔╝ ╚████╔╝ ██║  ██║   ██║  │  ├─┤│  │  │ ││  ├─┤ │ │ │├┬┘")
print("╚══════╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝   ╚═╝  └─┘┴ ┴┴─┘└─┘└─┘┴─┘┴ ┴ ┴ └─┘┴└─ By: Lucas Wharton")
print("Version: 1.0")
print("s = Distance m")
print("u = Initial Speed ms⁻¹")
print("v = Final Speed ms⁻¹")
print("a = Acceleration ms⁻²")
print("t = Time s")
answer = str(input("Please input what value you would like to work out: s, u, v, a, t "))
import math


#distance

if answer == "s":
    unknown_variable = str(input("Please input what value you do not have: u, v, a, t "))
    if unknown_variable == "u":
        v = float(input("Please input v value "))
        a = float(input("Please input a value "))
        t = float(input("Please input t value "))
        calculation = (v * t) - (0.5 * a * t ** 2)
    elif unknown_variable == "v":
        u = float(input("Please input u value "))
        a = float(input("Please input a value "))
        t = float(input("Please input t value "))
        calculation = (u * t) + (0.5 * a * t ** 2)
    elif unknown_variable == "a":
        u = float(input("Please input u value "))
        v = float(input("Please input v value "))
        t = float(input("Please input t value "))
        calculation = ((v + u) / 2) * t
    elif unknown_variable == "t":
        u = float(input("Please input u value "))
        a = float(input("Please input a value "))
        v = float(input("Please input v value "))
        calculation = (v ** 2 * u ** 2) / (2 * a)
    else:
        print("Invalid input. Please try again")
    
    print("your distance =", calculation, "m")

#initial speed

if answer == "u":
    unknown_variable = str(input("Please input what value you do not have: s, v, a, t "))
    if unknown_variable == "s":
        v = float(input("Please input v value "))
        a = float(input("Please input a value "))
        t = float(input("Please input t value "))
        calculation = v - (a * t)
    elif unknown_variable == "v":
        s = float(input("Please input s value "))
        a = float(input("Please input a value "))
        t = float(input("Please input t value "))
        calculation = (s - (0.5 * a * t**2)) / t
    elif unknown_variable == "a":
        s = float(input("Please input s value "))
        v = float(input("Please input v value "))
        t = float(input("Please input t value "))
        calculation = ((2 * s) / t) - v
    elif unknown_variable == "t":
        s = float(input("Please input s value "))
        a = float(input("Please input a value "))
        v = float(input("Please input v value "))
        calculation = math.sqrt((v ** 2) - (2 * a * s))
    else:
        print("Invalid input. Please try again")
    
    print("your initial speed =", calculation, "ms⁻¹")
    
#final speed

if answer == "v":
    unknown_variable = str(input("Please input what value you do not have: u, s, a, t "))
    if unknown_variable == "u":
        s = float(input("Please input s value "))
        a = float(input("Please input a value "))
        t = float(input("Please input t value "))
        calculation = (s + (0.5 * a * t ** 2)) / t
    elif unknown_variable == "s":
        u = float(input("Please input u value "))
        a = float(input("Please input a value "))
        t = float(input("Please input t value "))
        calculation = u + (a * t)
    elif unknown_variable == "a":
        u = float(input("Please input u value "))
        s = float(input("Please input s value "))
        t = float(input("Please input t value "))
        calculation = ((s * 2) / t) - u
    elif unknown_variable == "t":
        u = float(input("Please input u value "))
        a = float(input("Please input a value "))
        s = float(input("Please input s value "))
        calculation = math.sqrt((u ** 2) + (2 * a * s))
    else:
        print("Invalid input. Please try again")
    
    print("your final speed =", calculation, "ms⁻¹")

#acceleration

if answer == "a":
    unknown_variable = str(input("Please input what value you do not have: u, v, s, t "))
    if unknown_variable == "u":
        v = float(input("Please input v value "))
        s = float(input("Please input s value "))
        t = float(input("Please input t value "))
        calculation = (v * t) / (s + 0.5 * t ** 2)
    elif unknown_variable == "v":
        u = float(input("Please input u value "))
        s = float(input("Please input s value "))
        t = float(input("Please input t value "))
        calculation = (u * t) / (s + 0.5 * t ** 2)
    elif unknown_variable == "s":
        u = float(input("Please input u value "))
        v = float(input("Please input v value "))
        t = float(input("Please input t value "))
        calculation = (v - u) / t
    elif unknown_variable == "t":
        u = float(input("Please input u value "))
        s = float(input("Please input s value "))
        v = float(input("Please input v value "))
        calculation = (v ** 2 - u ** 2) / ( 2 * s)
    else:
        print("Invalid input. Please try again")

    print("your acceleration =", calculation, "ms⁻²")

#time

if answer == "t":
    unknown_variable = str(input("Please input what value you do not have: u, v, a, s "))
    if unknown_variable == "u":
        v = float(input("Please input v value "))
        a = float(input("Please input a value "))
        t = float(input("Please input s value "))
        calculation = (s * 2) / (v + math.sqrt(v ** 2 - 2 * a * s))
    elif unknown_variable == "v":
        u = float(input("Please input u value "))
        a = float(input("Please input a value "))
        t = float(input("Please input s value "))
        calculation = (s * 2) / (u + math.sqrt(u ** 2 + 2 * a * s))
    elif unknown_variable == "a":
        u = float(input("Please input u value "))
        v = float(input("Please input v value "))
        t = float(input("Please input s value "))
        calculation = (s * 2) / (v + u)
    elif unknown_variable == "s":
        u = float(input("Please input u value "))
        a = float(input("Please input a value "))
        v = float(input("Please input v value "))
        calculation = (v - u) / a
    else:
        print("Invalid input. Please try again")

    print("your time =", calculation, "s")