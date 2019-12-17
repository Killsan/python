servers = ['CS30', 'CS50', 'CS70']
print('I need to protect', len(servers), 'servers')
print("Servers:", end=' ')
for item in servers:
	print(item, end=' ')
print('I forger about one server')
servers.append('CS90')
print('Here is the full list of servers:', servers)
print("We need to sort our list")
# servers.sort()
# print("now it looks better:", servers)
		#^^This function sort list with
		#^^the help of alphabet
print("The first one server will be", servers[0])
#del servers[0]