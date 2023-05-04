nombre = int(input("Intodueix un nombre"))

for i in range (2,nombre):
        print ("Es divident", int(nombre), "/", int(i), "que dona: ", (nombre/i))
        if (nombre / i == 0):
                print ("No és primer")
                exit (0)
print ("És un nombre primer")