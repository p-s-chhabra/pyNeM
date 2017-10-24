from socket import *
from datetime import *
from sys import *


# -------------------------------------------- Input ---------------------------------------------------
remoteServer    = raw_input("Please Enter Remote Host to scan: ")
inputport = raw_input("Please specify port/s to scan: ")
remoteServerIP  = gethostbyname(remoteServer)
#------------------------------------------------------------------------------------------------------
# Print a nice banner with information on which host we are about to scan
print '\n'
print "-" * 80
print "Scanning remote host", remoteServer
print "Remote host IP", remoteServerIP
print "-" * 80
print '\n'


#Port input checking and port scanning
if str(inputport.isdigit()) == 'True':
    # Main port scanning with some error handling
    t1 = datetime.now() #Time of scan initiation

    try:
        for port in range(1,1025):  
            sock = socket(AF_INET, SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            sock.close()

    except KeyboardInterrupt:
        print "Keyboard Interrupt Detected"
        exit()

    except gaierror:
        print 'Hostname could not be resolved. Exiting'
        exit()

    except error:
        print "Unable to connect to server"
        exit()
    
else if str(inputport.isdigit()) == 'False'
    print "F"




# Calculates the time difference, for execution time
t2 = datetime.now() #Get current time
total =  t2 - t1

# Printing execution time
print '\n'
print 'Scanning Completed in: ', total
print '\n'