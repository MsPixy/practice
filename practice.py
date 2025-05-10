print ("Hello Vim!")
#Data types: You use data types to make data structures. (things like character, array, interger, and floats are data types. Data structures are strings, ect.)
dt_character = 'v'
dt_character2 = '8'
dt_character3 = '$'
#All characters have an ASCII value assigned to them (they have a numberical value).
dt_integer = 1
dt_integer2 = -26
#Integer characters doesn't require a ' surrounding them like other characters; they cannot be decimals either.
#floats, or floating point numbers, are integers with decimals. Sometimes called double, they're only accurate to around 7 decimal places.
dt_float = 0.1
dt_float2 = 0.2
dt_float3 = dt_float + dt_float2
print(dt_float3)
#Booleans are "True or False" data types. They need a condition to resolve; they have a numerical value of "True is 1, and False is 0".
dt_boolean = True
dt_boolean2 = False
#Bytes is an address to something. They're started with "0b", and then the binary code for the desired output.
dt_binary = 0b01000001 #this is binary for "65".
print (dt_binary)
dt_byte = bytes([dt_binary]) #Use square brackets for 
print(dt_byte)
#dt_byte is going to show the character associated with the dt_binary; in this case "A". It'll show "b'a'", with the b saying it's a byte.
#Every ASCII character has a decimal equivalent. 
#Long data types are just "long integers". An integer only has 4 bytes, and longs have 8 bytes. You'd only use long if you really need a BIG ASS number. Python seems smart enough to auto turn ints into longs.
dt_int = 26
dt_long = 3000000000
print(int(3000000000))
print(dt_long)
#Arrays are building blocks in coding. They're used to store groups of information. It can break 3d, (1d, 2d, 3d, ect). Arrays have addresses as well called "index".
dt_array = [42, 21, 97, 69] #An array of integers
#If you want to find the address of an array, you COUNT FROM 0. for example, if you wanna find 97's index, it'd be 2. (42=0, 21=1, ect)
print(dt_array)
print(dt_array[2]) #The 2 in square brackets is the index for 97, so this should print "97".
# print(dt_array[4]) This is out of the index range, since the highest index is 3(69). This will error out.
