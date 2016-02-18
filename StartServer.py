import os,sys,glob,re

username = r'{NMUserName}'
password = r'{NMPassWord}'
Host = r'{Host}'
our_str = r"{ServerName}"
NMPort = r'{NMPort}'
DomainName = r'{DomainName}'
DomainDir = r'{DomainDir}'
NMType = r'{NMType}'

if not username:
	print '!!!! Error...NMUserName cannot be empty !!!!'
	sys.exit(1)

if not password:
	print '!!!! Error...NMPassWord cannot be empty !!!!'
	sys.exit(1)

if not Host:
	print '!!!! Error...Host cannot be empty !!!!'
	sys.exit(1)

if not our_str:
	print '!!!! Error...ServerName cannot be empty !!!!'
	sys.exit(1)	

if not NMPort:
	print '!!!! Error...NMPort cannot be empty !!!!'
	sys.exit(1)

if not DomainName:
	print '!!!! Error...DomainName cannot be empty !!!!'
	sys.exit(1)	

if not DomainDir:
	print '!!!! Error...No DomainDir selected !!!!'
	sys.exit(1)

if not NMType:
	print '!!!! Error...No NMType given !!!!'
	sys.exit(1)	

sers= []

#Splitting by |
ser_all = our_str.split("|")

#Getting the true values
for val in ser_all:
	if '[true]' in val:
		newstr = val.replace("[true]","",1)
		sers.extend([newstr])

if not sers:
	print '!!!! Error...ServerName cannot be empty !!!!'
	sys.exit(1)	
	
try:
	print('\n')
	connect( '{tool.UserName}', '{tool.PassWord}', '{tool.AdminURL}')
	nmConnect(Username,Password,Host,nmPort,domainName,domainDir,nmType)
	print ''
	print '========================================================='
	print 'Connected to NODE MANAGER Successfully...!!!'
	print '========================================================='
	print ''

	print('\n')
	for c in sers:
		try:
			nmStart(c)
			print('\n')
			print '===================================================='
			print '===> Server started ', c, '  <==='
			print '===================================================='
			print('\n')
				
		except:
			print('\n')
			print ' !!! Error while starting the server '+c+' ..!!!! '
			sys.exit(1)	

except Exception, e:
	print ' !!!! Error while Connecting to Nodemanager !!!!',e
	sys.exit(1)	

print('\n')
print ('=============================================================')
print ('------------------- State of the servers --------------------')
print ('=============================================================')
print('\n\n')
for c in sers:
	try:
		state(c,"Server")
	except Exception, e:
		print ' !!! Error while getting the state !!!! ', e
		sys.exit(1)	

print('\n\n')
print ('=============================================================')	

#Disconnecting from weblogic
disconnect()
exit()
