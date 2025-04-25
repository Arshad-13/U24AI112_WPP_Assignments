# Write a class called Converter. The user will pass a length and a unit when declaring an object
# from the class—for example, c = Converter(9,'inches'). The possible units are inches, feet,
# yards, miles, kilometers, meters, centimeters, and millimeters. For each of these units there
# should be a method that returns the length converted into those units. For example, using the
# Converter object created above, the user could call c.feet() and should get 0.75 as the result.

#1 feet = 12 inches
#1 feet = 0.3333 yards
#1 feet = 0.00018939 miles
#1 feet = 304.8 millimeters
#1 feet = 30.48 centimeters
#1 feet = 0.3048 meters
#1 feet = 0.0003048 kilometers
feet = 1
inches = 12
yards = 0.3333
miles = 0.00018939
millimeters = 304.8
centimeters = 30.48
meters = 0.3048
kilometers = 0.0003048

class Converter:

    def __init__(self, length, unit):
        self.len = length
        self.unit = unit
        
    def common(self, unit):
        if unit == 'inches':
            return self.len/12
        elif unit == 'feet':
            return self.len
        elif unit == 'yards':
            return self.len/0.3333
        elif unit == 'miles':
            return self.len/0.00018939
        elif unit == 'milimeters':
            return self.len/304.8
        elif unit == 'centimeters':
            return self.len/30.48
        elif unit == 'meters':
            return self.len/0.3048
        elif unit == 'kilometers':
            return self.len/0.0003048
        else:
            print("Invalid or out of scope unit emtered ")
            

def main():
    feets = int(input("Enter the length: "))
    convert = [inches, feet, yards, miles, millimeters, centimeters, meters, kilometers]
    conversions = ["inches", "feet", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]
    print(conversions)
    conversion = int(input("Enter the unit: "))
    user = Converter(feets, conversions[conversion-1])
    x = user.common(conversions[conversion-1])
    print(conversions)
    z = int(input("Enter the conversion: "))
    print("The length in", conversions[z - 1], "is", x*convert[z - 1])
    
if __name__ == "__main__":
    main()
    