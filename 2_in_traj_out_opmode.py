###########have to get col index of speed, acc
###input speed should be km/h, acc should be m/s2
###input traj should be vehicle specific

def vsp(speed, acc, g, grade, vsp_coef):
	vsp = (vsp_coef[0]*speed + vsp_coef[1]*(speed)**2 + vsp_coef[2]*(speed)**3 + (acc + g*sin(grade))*speed*vsp_coef[3])/vsp_coef[3]
	return vsp

def opmode_id(speed, acc_series, vsp):
	#speed in mph, acc_series includes the acceleration in the consecutive 3 seconds, according to the definition of OpMode by USEPA
	count = len(acc_series) #track the length of the driving trajectory. acc_series is an appending list of the acceleration
	if count >=2:
		if acc[count]< -2 or (acc[count]< -1 and acc[count-1]< -1 and acc[count-2]< -1):######problem here
			opmode = 0   ###Braking
		return opmode
		break
	else:
		if speed < 1 and speed >= 0:
			opmode = 1   ###idling
		elif vsp < 0: ###coast down
			if speed >= 1 and speed <= 25:
				opmode = 11
			elif speed >=25 and speed <50:
				opmode = 21
			elif speed >= 50:
				opmode = 33
		elif vsp <3 and vsp >= 0:
			if speed >= 1 and speed < 35:
				opmode = 12
			elif speed >= 25 and speed < 50:
				opmode = 22
			elif speed >= 50:
				opmode = 33
		elif vsp < 6 and vsp >= 3:
			if speed >= 1 and speed < 25:
				opmode = 13
			elif speed >= 25 and speed < 50:
				opmode = 23
			elif speed >= 50:
				opmode = 33
		elif vsp < 9 and vsp >= 6:
			if speed >= 1 and speed < 25:
				opmode = 14
			elif speed >= 25 and speed < 50:
				opmode = 24
			elif speed >= 50:
				opmode = 35
		elif vsp < 12 and vsp >= 9:
			if speed >= 1 and speed < 25:
				opmode = 15
	        elif speed >= 25 and speed < 50:
				opmode = 25
	        elif speed >= 50:
				opmode = 35
		elif vsp < 18 and vsp >= 12:
			if speed >= 1 and speed < 25:
				opmode=16
	        elif speed >= 25 and speed < 50:
				opmode=27
	        elif speed >= 50:
				opmode=37
		elif vsp < 24 and vsp >= 18:
			if speed >= 1 and speed < 25:
				opmode=16
	        elif speed >= 25 and speed < 50:
				opmode=28
	        elif speed >= 50:
				opmode = 38
		elif vsp < 30 and vsp >= 24:
			if speed >= 1 and speed < 25:
				opmode = 16
	        elif speed >= 25 and speed < 50:
				opmode = 29
	        elif speed >= 50:
				opmode = 39
		elif vsp >= 30:
	        if speed >= 1 and speed < 25:
				opmode = 16
	        elif speed >= 25 and speed < 50:
				opmode = 30
	        elif speed >= 50:
				opmode = 40
return opmode

def generate_acc_series(current_t, acc_record):
	#current_t records the current timestep of the whole trajectory
	#acc_record records all the acceleration in a time series
	if current_t >= 2:
		acc_series = [acc_record[current_t-2], acc_record[current_t-1], acc_record[current_t]]
	else:
		acc_series = acc_record[:current_t]
return acc_series
