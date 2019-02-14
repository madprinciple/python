cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort() #sorted alphebatically
print(cars) 
cars.sort(reverse=True) #sorted alphebatically reverse order
print(cars) 

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars) #original
print(sorted(cars)) #tempererly sorted
print(cars) #original again
cars.reverse()
print(cars) #reverse
