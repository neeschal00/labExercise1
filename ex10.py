"""Write a Python program to convert seconds to day, hour, minutes and seconds."""
tsec=int(input("Enter a time in second:"))
tmin=tsec//60
thr=tsec//(60**2)
print("The time in minutes from second is:",tmin)
print("The time in hour from second is:",thr)