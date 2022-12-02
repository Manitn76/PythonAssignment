cursing = 33000;
currentalt = 0;
pilotsugg = 5000;  #The input from the pilot
currentalt = cursing - pilotsugg;
print("Current altitude - ",+currentalt);
if currentalt > 10000:
	print("Go Around..");
elif currentalt > 5000:
	print("Bring down the plane to 1000");
