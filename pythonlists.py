bicycles=['trek', 'cannodale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[-1].title())

motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' #replace to list
print(motorcycles)

motorcycles.append('ducati') #insert to list
print(motorcycles)

motorcycles.insert(0, 'kwasaki')
print(motorcycles)

del motorcycles[1]
print(motorcycles)
print(motorcycles.pop()) #last one popped 
print(motorcycles)




