# What's up everybody? Welcome to this new session on Python with the Panda. Today, we're going 
# to look at the last immutable data type: Tuples. We've looked at Numbers and Strings already.
# So let's get started right away.

# Now Tuples are pretty easy to grasp. There's really not much to worry about. Basically,
# Tuples are a list, or rather a sequence of Python objects.

# Here's what a Tuple looks like:
Tuple_001 = (1, 2, 3);
print('Tuple 001: ' + str(Tuple_001) + '\n');      # The output for this line is Tuple 001: (1, 2, 3)

# The most basic form of a Tuple is seen during value assignment. Have a look at this:
firstName, lastName, age = 'Kevin', 'Sequeira', 25;     # This line here is what we commonly called an 'Implicit Tuple'.
print('Full Name: ' + firstName + ' ' + lastName);
print('Age: ' + str(age) + '\n');

# If you look closely, you'll notice that a Tuple can hold objects of different data types.
# Also, the kind of data stored in a Tuple can be a bit complicated. Have a look:
deviceName001, devicePrice001, deviceDimensions001 = ('Samsung Galaxy S', 29000, [360, 640, 0.5]);
Tuple_device001 = (deviceName001, devicePrice001, deviceDimensions001);
print('Device Data: ' + str(Tuple_device001));
print('Device Name: ' + deviceName001);
print('Device Price: Rs. ' + str(devicePrice001) + '/-');
print('Device Dimensions: ' + str(deviceDimensions001[0]) + ' x ' + str(deviceDimensions001[1]) + ' x ' + str(deviceDimensions001[2]) + '\n');

# Here's the output for the above code:
# Device Data: ('Samsung Galaxy S', 29000, [360, 640, 0.5])
# Device Name: Samsung Galaxy S
# Device Price: 29000
# Device Dimensions: 360 x 640 x 360

# You can see that apart from having String and Integer data, the Tuple also consists of
# a List within itself. This is what makes Tuples special. As we go ahead, we'll see how 
# Tuples add value to Python Dictionaries: the King of Python Data Types, by acting as keys
# for these dictionaries. Now if you're asking me, "What's this dictionaries stuff?" don't worry.
# We'll get to that as we go ahead in our course.

# Let's look at some more stuff that you can do with Tuples...
# Remember, Tuples are Immutable Data Types, which means that the data within a Tuple cannot be
# re-written at any point in the course of the program, but the data can be cloned into another
# Tuple.

deviceName002, devicePrice002, deviceDimensions002 = ('Moto G4 Plus', ) + Tuple_device001[1:];
Tuple_device002 = (deviceName002, devicePrice002, deviceDimensions002);
print('Device Data: ' + str(Tuple_device002));
print('Device Name: ' + deviceName002);
print('Device Price: Rs. ' + str(devicePrice002) + '/-');
print('Device Dimensions: ' + str(deviceDimensions002[0]) + ' x ' + str(deviceDimensions002[1]) + ' x ' + str(deviceDimensions002[2]) + '\n');

# Here's the output for the above given lines of code:
# Device Data: ('Moto G4 Plus', 29000, [360, 640, 0.5])
# Device Name: Moto G4 Plus
# Device Price: Rs. 29000/-
# Device Dimensions: 360 x 640 x 0.5

# Well, it's pretty clear that the data from Tuple_device001 has been successfully cloned into
# Tuple_device002 as intended.

# And finally, before we close this session, there's one more important thing that we need to
# consider. A Tuple can also be declared with just one object within it. But one needs to be
# careful avout the syntax. Check out the followin two objects:

object001 = 2;      # Object declaration without a comma after the first object value.
object002 = 2, ;    # Object declaration with a comma after the first object value.
print('Type of Object 1: ' + str(type(object001)));     
print('Type of Object 2: ' + str(type(object002)));

# Here's what we get:
# Type of Object 1: <class 'int'>
# Type of Object 2: <class 'tuple'>
# An single object can only be declared as a Tuple if the object value is followed by a
# comma, as seen in the above examples.

# Well guys, that's all for this session on Tuples. Going ahead, we're going to explore
# Mutable Data Types.
