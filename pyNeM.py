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

#--------------------------------------------- Scan Single Port -----------------------------------------------------------
if str(inputport.isdigit()) == 'True':                  
    # Main port scanning with some error handling
    t1 = datetime.now() #Time of scan initiation
    
    if int(inputport) <= 65535:
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((remoteServerIP, int(inputport)))
            if result == 0:
                print "Port {}: 	 Open".format(inputport)
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
    else:
        print "Invalid port number. Port not in range"
       

#-------------------------------------------------------------------------------------------------------------------------

#------------------------------------------ Scan Specified Range of Ports ------------------------------------------------

else:
    if str(inputport).find('-') != -1:   #
        ports = str(inputport).split('-')   #Store minimum and maximum port number in this list
        minport = int(ports[0])
        maxport = int(ports[1])
        if (minport > maxport) or (minport <=0) or (maxport > 65535) or (minport == maxport): #Error check
            print "Invalid port range."
        else:
            t1 = datetime.now() #Time of scan initiation
            try:
                for inputport in range(minport,maxport):    
                    sock = socket(AF_INET, SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((remoteServerIP, inputport))
                    if result == 0:
                        print "Port {}: 	 Open".format(inputport)
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
    
    
#---------------------------------------------- Default Ports ----------------------------------------------------    
    else: 
        try:
            t1 = datetime.now() #Time of scan initiation
            for inputport in range(1,1000):
                sock = socket(AF_INET, SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((remoteServerIP, int(inputport)))
                if result == 0:
                    print "Port {}: 	 Open".format(inputport)
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
        

# Calculates the time difference, for execution time
t2 = datetime.now() #Get current time
total =  t2 - t1

# Printing execution time
print '\n'
print 'Scanning Completed in: ', total
print '\n'