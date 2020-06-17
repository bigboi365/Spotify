"""forTrendYesterday['day'] = forTrendToday['day'] 
forTrendYesterday['month'] = forTrendToday['month'] 
forTrendYesterday['year'] = forTrendToday['year'] 
forTrendYesterday['pressureValue'] = forTrendToday['pressureValue']
forTrendToday['pressureCount'] = 0 
forTrendToday['humidityValue'] = 0 
forTrendToday['humidityCount'] = 0 
tempName = os.path.join(basePath, 'fty.temp') 
with open(tempName, 'w') as outfile: json.dump(forTrendYesterday, outfile)"""
