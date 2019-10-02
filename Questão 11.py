celsius = 0
for farnht in range(100,151):
celsius = (5/9) * (farnht-32)
print ('{} °F = {:.2f} °C '.format (farnht, celsius))