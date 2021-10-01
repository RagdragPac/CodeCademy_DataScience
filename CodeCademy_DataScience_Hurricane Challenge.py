# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


#code_start_here
#update the damages, convert Millions and Billions
def convert_damages(damages):

  conversion = {"M": 1000000, "B": 1000000000}
  updated_damages = []

  for eachdamage in damages:
    if eachdamage == "Damages not recorded":
      updated_damages.append(eachdamage)
    if eachdamage[-1] == 'M':
      updated_damages.append(float(eachdamage.strip('M'))*conversion["M"])
    if eachdamage[-1] == 'B':
      updated_damages.append(float(eachdamage.strip('B'))*conversion["B"])

  return updated_damages

updated_damages = convert_damages(damages)
print(updated_damages)
print()


#create dictionary for hurricane data
#hurricane names as key and hurricane data details as value
def hurricane_dictionary(names, months,years,max_sustained_winds,areas_affected,damages,deaths):
  
  hurricane = {}
  hurricane_count = len(names)

  for i in range(hurricane_count):
    hurricane[names[i]] = {"Name": names[i], 
                           "Month": months[i], 
                           "Year": years[i], 
                           "Max Sustained Wind": max_sustained_winds[i], 
                           "Areas Affected": areas_affected[i], 
                           "Damage": damages[i],
                           "Death": deaths[i]}
  return hurricane

hurricane = hurricane_dictionary(names, months,years,max_sustained_winds,areas_affected,damages,deaths)
print(hurricane)
print()



#Create new dictionary (same as hurricane_dictionary above)
#but instead of using name as the key, try use year as the key
hur_years_dict = {}
hurricane_count = len(names)
for i in range(hurricane_count):
    hur_years_dict[years[i]] = {"Name": names[i], 
                           "Month": months[i], 
                           "Year": years[i], 
                           "Max Sustained Wind": max_sustained_winds[i], 
                           "Areas Affected": areas_affected[i], 
                           "Damage": damages[i],
                           "Death": deaths[i]}

print(hur_years_dict)
print()



#Count how many times hurricane happen in each area
areas_count={}

for areas in areas_affected:
    for i in areas:
        if i not in areas_count:
            areas_count[i] = 1
        else:
            areas_count[i] += 1

print(areas_count)
print()


#Function that finds the most affected area
def areas_max_affected():
  max_key_areas = max(areas_count, key=areas_count.get)
  max_value_areas = max(areas_count.values())
  return max_key_areas, max_value_areas

max_key_areas, max_value_areas = areas_max_affected()
print("The most affected area : " + max_key_areas + "\nCount : " 
      + str(max_value_areas) + " times.")
print()


#Count the most death
def max_death():
  max_death_data = dict(zip(names,deaths))
  max_key_death = max(max_death_data, key=max_death_data.get)
  max_value_death = max(max_death_data.values())
  return max_key_death, max_value_death

max_key_death, max_value_death = max_death()
print("The most death : \nHurricane Name : " + max_key_death
      + "\nDeath Count : " + str(max_value_death))
print()


#Rate the hurricane using mortality_scale (based on death count)
#mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
#8
def mortality(hurricane):
  mortality_rates = {0:[], 1:[], 2:[], 3:[], 4:[]}

  for i in hurricane:
    rate = 0
    death_count = hurricane[i]["Death"]
    if death_count < 100:
      rate = 0
    elif death_count >= 100 and death_count < 500:
      rate = 1
    elif death_count >= 500 and death_count < 1000:
      rate = 2
    elif death_count >= 1000 and death_count < 10000:
      rate = 3
    else:
      rate = 4
    
    if rate not in mortality_rates:
       mortality_rates[rate] = hurricane[i]
    else:
      mortality_rates[rate].append(hurricane[i])
  
  return mortality_rates

mortality_rates = mortality(hurricane)
print(mortality_rates)
print()



#Print each mortality_rates data (name,death) for every rate
