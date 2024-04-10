"""See Exercise: mile to kilometer.

Put this code into a function called convert(miles), and make sure to call it several times with different values.

Example output:

8 miles is 12.8 kilometers
12 miles is 19.200000000000003 kilometers
131 miles is 209.60000000000002 kilometers"""

#Function
def convert(miles):
    miles_km = 1.6*miles
    return miles_km

miles = int(input("Enter miles:"))

convert_miles = convert(miles)

print(miles, "Miles is", convert_miles, "kilometers")