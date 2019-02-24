###########have to get col index of speed, acc
###input speed should be km/h, acc should be m/s2
###input traj should be vehicle specific
def veh_opmode(traj, speedcol, acccol, vehidcol, linkidcol, timecol):
	count=0
	acc=[]
	for line in traj:
		cols = [float(x) for x in traj]
		acc.append(cols[acccol]*3.6/1.6)
		speedm=cols[speedcol]/3.6 
		speedi=cols[speedcol]/1.6

		pcvsp = (0.156461*speedm+0.00200193*(speedm)**2+0.000492646*(speedm)**3+cols[4]*speedm*1.4788)/1.4788

		if count>=2:
			if acc[count]< -2 or (acc[count]< -1 and acc[count-1]< -1 and acc[count-2]< -1):######problem here
				pcopmode=0
				###########Braking
			elif speedi<1 and speedi>=-1:
				pcopmode=1
			###########Idle
			elif pcvsp < 0:
				if speedi>=1 and speedi<25:
					pcopmode=11
				elif speedi>=25 and speedi<50:
					pcopmode=21
				elif speedi>=50:
					pcopmode=33
			###########Coast
			elif pcvsp<3 and pcvsp>=0:
				if speedi>=1 and speedi<25:
					pcopmode=12
				elif speedi>=25 and speedi<50:
					pcopmode=22
				elif speedi>=50:
					pcopmode=33
			elif pcvsp<6 and pcvsp>=3:
				if speedi>=1 and speedi<25:
					pcopmode=13
				elif speedi>=25 and speedi<50:
					pcopmode=23
				elif speedi>=50:
					pcopmode=33
			elif pcvsp<9 and pcvsp>=6:
				if speedi>=1 and speedi<25:
					pcopmode=14
				elif speedi>=25 and speedi<50:
					pcopmode=24
				elif speedi>=50:
					pcopmode=35
			elif pcvsp<12 and pcvsp>=9:
				if speedi>=1 and speedi<25:
					pcopmode=15
				elif speedi>=25 and speedi<50:
					pcopmode=25
				elif speedi>=50:
					pcopmode=35
			elif pcvsp<18 and pcvsp>=12:
				if speedi>=1 and speedi<25:
					pcopmode=16
				elif speedi>=25 and speedi<50:
					pcopmode=27
				elif speedi>=50:
					pcopmode=37
			elif pcvsp<24 and pcvsp>=18:
				if speedi>=1 and speedi<25:
					pcopmode=16
				elif speedi>=25 and speedi<50:
					pcopmode=28
				elif speedi>=50:
					pcopmode=38
			elif pcvsp<30 and pcvsp>=24:
				if speedi>=1 and speedi<25:
					pcopmode=16
				elif speedi>=25 and speedi<50:
					pcopmode=29
				elif speedi>=50:
					pcopmode=39
			elif pcvsp>=30:
				if speedi>=1 and speedi<25:
					pcopmode=16
				elif speedi>=25 and speedi<50:
					pcopmode=30
				elif speedi>=50:
					pcopmode=40
					
		elif count<2:
			if speedi<1 and speedi>=-1:
				pcopmode=1
			###########Idle
			elif pcvsp < 0:
				if speedi>=1 and speedi<25:
					pcopmode=11
				elif speedi>=25 and speedi<50:
					pcopmode=21
				elif speedi>=50:
					pcopmode=33
			###########Coast
			elif pcvsp<3 and pcvsp>=0:
				if speedi>=1 and speedi<25:
					pcopmode=12
				elif speedi>=25 and speedi<50:
					pcopmode=22
				elif speedi>=50:
					pcopmode=33
			elif pcvsp<6 and pcvsp>=3:
				if speedi>=1 and speedi<25:
					pcopmode=13
				elif speedi>=25 and speedi<50:
					pcopmode=23
				elif speedi>=50:
					pcopmode=33
			elif pcvsp<9 and pcvsp>=6:
				if speedi>=1 and speedi<25:
					pcopmode=14
				elif speedi>=25 and speedi<50:
					pcopmode=24
				elif speedi>=50:
					pcopmode=35
			elif pcvsp<12 and pcvsp>=9:
				if speedi>=1 and speedi<25:
					pcopmode=15
				elif speedi>=25 and speedi<50:
					pcopmode=25
				elif speedi>=50:
					pcopmode=35
			elif pcvsp<18 and pcvsp>=12:
				if speedi>=1 and speedi<25:
					pcopmode=16
				elif speedi>=25 and speedi<50:
					pcopmode=27
				elif speedi>=50:
					pcopmode=37
			elif pcvsp<24 and pcvsp>=18:
				if speedi>=1 and speedi<25:
					pcopmode=16
				elif speedi>=25 and speedi<50:
					pcopmode=28
				elif speedi>=50:
					pcopmode=38
			elif pcvsp<30 and pcvsp>=24:
				if speedi>=1 and speedi<25:
					pcopmode=16
				elif speedi>=25 and speedi<50:
					pcopmode=29
				elif speedi>=50:
					pcopmode=39
			elif pcvsp>=30:
				if speedi>=1 and speedi<25:
					pcopmode=16
				elif speedi>=25 and speedi<50:
					pcopmode=30
				elif speedi>=50:
					pcopmode=40

		count = count + 1
		if count % 100000 == 0:
			print (count)
			
		trajwithopmode = [cols[vehidcol], cols[linkidcol], cols[timecol], cols[speedcol], cols[acccol], pcopmode]
	return trajwithopmode