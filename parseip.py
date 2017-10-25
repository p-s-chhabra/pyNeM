#!/usr/bin/python
# take in network input, output a list of IP addresses.

from sys import argv

def dectoip(decimal):
	ip_t = []
	for i in range(0,4):
		ip_t.append(str((decimal & (255 << (3-i)*8)) >> (3-i)*8))

	return '.'.join(ip_t)

def iptodec(ip_t):
	ip = 0
	for i in range(0,4):
		ip = ip + (int(ip_t[i]) << (3-i)*8)

	return ip

def parseip(network):
	if "/" in network:
		mask = network.split('/')[1]
		ip_t = network.split('/')[0].split('.')

		ip = iptodec(ip_t)
		baseip = (ip & ((2**32)-1) << (32-int(mask))) & ((2**32) -1)

		addresses = []
		for offset in range(2**(32-int(mask))):
			addresses.append(dectoip(baseip + offset))

		return addresses

	if "-" in network:
		ip_t = network.split('.')
		addresses = []
		for each in ip_t:
			if '-' in each:
				iprange = each.split('-')

		for offset in range(int(iprange[0]),int(iprange[1])+1):
			address = ""
			for i in range(0,4):
				if '-' not in ip_t[i]:
					if i == 0:
						address = ip_t[0]
					else:
						address = address + "." + ip_t[i]

				else:
					if i == 0:
						address = str(offset)
					else:
						address = address + "." + str(offset)

			addresses.append(address)
		
		return addresses

	else:
		return network

if __name__ == '__main__':
	if len(argv) != 2:
		print "Error, input IP i.e. 190.2.3.0/24."
		exit()

	print parseip(argv[1])