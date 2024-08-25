import np

##find emission rate from the er_list_file
##er_list_file should in csv/table file type
#the colnmae of emiss rate file should include: opmode, vehtype, vehyear, modelyear
#emission type of the emission rate file should include co2, co, so2, no, pm25, pm10, fuel
def emis_rate(erfile_name, opmode, vehtype, vehyear, modelyear):
    #co2, co, so2, nox, pm25, pm10, fuel = 0, 0, 0, 0, 0, 0, 0
    #erfile = open(erfile_name, 'r')
    # Read the Excel file
    er_file = pd.read_excel(erfile_name)
    co2 = er_file.loc[(df['opmode'] == opmode) & (df['vehtype'] == vehtype) & (df['vehyear'] == vehyear) &(df['modelyear'] = mmodelyear), 'co2'].iloc[0]
    co = er_file.loc[(df['opmode'] == opmode) & (df['vehtype'] == vehtype) & (df['vehyear'] == vehyear) &(df['modelyear'] = mmodelyear), 'co'].iloc[0]
    so2 = er_file.loc[(df['opmode'] == opmode) & (df['vehtype'] == vehtype) & (df['vehyear'] == vehyear) &(df['modelyear'] = mmodelyear), 'so2'].iloc[0]
    nox = er_file.loc[(df['opmode'] == opmode) & (df['vehtype'] == vehtype) & (df['vehyear'] == vehyear) &(df['modelyear'] = mmodelyear), 'nox'].iloc[0]
    pm25 = er_file.loc[(df['opmode'] == opmode) & (df['vehtype'] == vehtype) & (df['vehyear'] == vehyear) &(df['modelyear'] = mmodelyear), 'pm25'].iloc[0]
    pm10 = er_file.loc[(df['opmode'] == opmode) & (df['vehtype'] == vehtype) & (df['vehyear'] == vehyear) &(df['modelyear'] = mmodelyear), 'pm10'].iloc[0]
    fuel = er_file.loc[(df['opmode'] == opmode) & (df['vehtype'] == vehtype) & (df['vehyear'] == vehyear) &(df['modelyear'] = mmodelyear), 'fuel'].iloc[0]

    return co2, co, so2, nox, pm25, pm10, fuel
    
