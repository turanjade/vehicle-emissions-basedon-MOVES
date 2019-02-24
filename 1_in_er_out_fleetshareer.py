######input: dir&filename of fleetshare; category of ER file 
######category of the ER: model year, pt/pc; summerorwinter; gasoline/diesel
import numpy as np

def fleetshare_er(fleetsharedir, fleetsharename, erdir, year, summerorwinter, gasolineordiesel):
	
	#####read files
	fleetfile = open(fleetsharedir + '/' + fleetsharename + '.csv','r') ###fleet share file
	pc=str(erdir + '/' + year + '_' + summerorwinter + '_' + 'pc' + '.csv')
	pt=str(erdir + '/' + year + '_' + summerorwinter + '_' + 'pt' + '.csv')
	movespcfile = open(pc, 'r')
	movesptfile = open(pt, 'r')
	print(movespcfile)
	next(movespcfile)
	next(movesptfile)
	
	fleet = []
	#####generate fleet list
	for line in fleetfile:
		cols = [x.rstrip() for x in line.split(',')]
		fleet.append(cols)
	
	pcer = []
	#####generate er list
	for line in movespcfile:
		cols = [x.rstrip() for x in line.split(',')]
		pcer.append(cols)
		
	pter = []
	#####generate er list
	for line in movesptfile:
		cols = [x.rstrip() for x in line.split(',')]
		pter.append(cols)
	
	fleetfile.close()
	movespcfile.close()
	movesptfile.close()
	
	fleet = np.asarray(fleet)
	pcer = np.asarray(pcer)
	pter = np.asarray(pter)
	
	opmode = np.unique(pcer[:,1])
	vehyear = np.unique(pcer[:,0])

	aggregateder = []
	for i in opmode:
		i = str(i)
#		print(i)
		co2, co, so2, nox, pm25, pm10, fuel = 0, 0, 0, 0, 0, 0, 0
		for year in vehyear:
			year = str(year)
#			print(year)
			pcyearshare = float(fleet[np.argwhere(np.logical_and(fleet[:,1]==year, fleet[:,0]=='21'))[0],3])
			ptyearshare = float(fleet[np.argwhere(np.logical_and(fleet[:,1]==year, fleet[:,0]=='31'))[0],3])
			
			co2=co2+pcyearshare*float(pcer[np.argwhere(np.logical_and(pcer[:,0]==year, pcer[:,1]==i))[0],2])+\
				ptyearshare*float(pter[np.argwhere(np.logical_and(pter[:,0]==year, pter[:,1]==i))[0],2])
				
			co=co+pcyearshare*float(pcer[np.argwhere(np.logical_and(pcer[:,0]==year, pcer[:,1]==i))[0],3])+\
				ptyearshare*float(pter[np.argwhere(np.logical_and(pter[:,0]==year, pter[:,1]==i))[0],3])
				
			so2=so2+pcyearshare*float(pcer[np.argwhere(np.logical_and(pcer[:,0]==year, pcer[:,1]==i))[0],4])+\
				ptyearshare*float(pter[np.argwhere(np.logical_and(pter[:,0]==year, pter[:,1]==i))[0],4])
				
			nox=nox+pcyearshare*float(pcer[np.argwhere(np.logical_and(pcer[:,0]==year, pcer[:,1]==i))[0],5])+\
				ptyearshare*float(pter[np.argwhere(np.logical_and(pter[:,0]==year, pter[:,1]==i))[0],5])
				
			pm25=pm25+pcyearshare*float(pcer[np.argwhere(np.logical_and(pcer[:,0]==year, pcer[:,1]==i))[0],6])+\
				ptyearshare*float(pter[np.argwhere(np.logical_and(pter[:,0]==year, pter[:,1]==i))[0],6])
				
			pm10=pm10+pcyearshare*float(pcer[np.argwhere(np.logical_and(pcer[:,0]==year, pcer[:,1]==i))[0],7])+\
				ptyearshare*float(pter[np.argwhere(np.logical_and(pter[:,0]==year, pter[:,1]==i))[0],7])	
				
			fuel=fuel+pcyearshare*float(pcer[np.argwhere(np.logical_and(pcer[:,0]==year, pcer[:,1]==i))[0],8])+\
				ptyearshare*float(pter[np.argwhere(np.logical_and(pter[:,0]==year, pter[:,1]==i))[0],8])	
		
		aggregateder.append([i, co2, co, so2, nox, pm25, pm10, fuel])
	
	return aggregateder
	
#er = fleetshare_er('E:/PhD/Research/EF_TABLES', 'ON_2017Share','E:/PhD/Research/EF_TABLES/opmode_Ef','2017','summer','gasoline')
#print(er)