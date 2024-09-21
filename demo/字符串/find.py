path = 'https://raw.githubusercontentgy_euhigrfegfjergf.com'

i = path.find('_')

print(i)
image = path[i+1:]
print(image)

# rfind
i = path.rfind('.')
hou = path[i+1:]
print(hou)


num = path.count('.')
print(num)