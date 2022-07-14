red_line_stops = ["Howard", "Jarvis", "Morse", "Loyola", "Granville", "Thorndale", "Bryn Mawr", "Argyle", "Wilson", "Sheridan", "Addison", "Belmont", "Fullerton", "North/Clybourn", "Clark/Division", "Chicago", "Grand", "Lake", "Monroe", "Jackson", "Harrison", "Roosevelt", "Cermak-Chinatown", "Sox-35th", "47th", "Garfield", "63rd", "69th", "79th", "87th", "95th/Dan Ryan"]

def find_position(station,train_line):
    for s in range(len(train_line)):
        if train_line[s] == station:
            return s 

print (find_position ("Loyola", red_line_stops))

def distance(s1, s2, tl):
    return abs(find_position(s1, tl) - find_position(s2, tl))
        
print (distance ("Morse", "Thorndale", red_line_stops))

def run(train_line):
    var= input("station 1")
    var2= input ("station 2")
    print(distance(var, var2, train_line))

red_line_stops = ["Howard", "Jarvis", "Morse", "Loyola", "Granville", "Thorndale", "Bryn Mawr", "Argyle", "Wilson", "Sheridan", "Addison", "Belmont", "Fullerton", "North/Clybourn", "Clark/Division", "Chicago", "Grand", "Lake", "Monroe", "Jackson", "Harrison", "Roosevelt", "Cermak-Chinatown", "Sox-35th", "47th", "Garfield", "63rd", "69th", "79th", "87th", "95th/Dan Ryan"]
run(red_line_stops)
