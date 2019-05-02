

import re
import sys



###### 0. Get the User Input
def getInput():
	txt = ""
	try:
		txt = input("IP Address: \n")
		return txt
	except:
		print("moving on")
		return; 

def getArgs():
	if(len(sys.argv))>1:
		IPInput = sys.argv[1]
		return IPInput
	else:
		IPInput = getInput()
		return IPInput

def cleanInput(textInput):
	search = re.search(r'(.*)/(.*)', textInput)
	return search

### https://stackoverflow.com/questions/10974932/split-string-based-on-a-regular-expression
### () you are capturing the group

###### 1. Get the IP Address and Port
def getIPBlocks(submaskInput):
	ipBlocks = int(submaskInput/8)
	print("\n\tNumber of IP blocks Occupied: ", ipBlocks)
	print("\tNumber of IP blocks Available: ", 4 - ipBlocks)
	return ipBlocks

def getSubnets(submaskInput):
	subnets = int(submaskInput%8)
	print("\n\tNumber of Subnets: ", subnets)
	return subnets


###### 2. Some Cleaning
def changeToBinaryFormat(unformattedStringInput):
	counter = 0 
	formattedString = ""
	## define IP Block 1
	for i in unformattedStringInput:
		formattedString = formattedString + i
		if(counter%8==0 and counter!=0):
			formattedString = formattedString + "."
		counter = counter+1
	return formattedString

def convertToDecimalFormat(IPinput, binaryMaskInput, subnetMaskInput):
	block1 = ""
	block2 = ""
	block3 = ""
	block4 = ""

	decimalIP = ""

	maskSplitArray = re.search(r'(.*)\.(.*)\.(.*)\.(.*)', binaryMaskInput)
	block1 = maskSplitArray.group(1)
	block2 = maskSplitArray.group(2)
	block3 = maskSplitArray.group(3)
	block4 = maskSplitArray.group(4)
	
	counter = 7
	bitHolder = 0;
	for i in block1:
		if(i=="1"):
			bitHolder = bitHolder + 2**counter
		print(counter)
		counter = counter - 1
	decimalIP = decimalIP + str(bitHolder)



	return decimalIP


###### 3. Get to work
def getHostBits(maskInput):
	hostBits = 32 - int(maskInput)
	return hostBits

def getTotalIPs(maskInput):
	hostBits = getHostBits(maskInput)
	assignableIPs = 2**hostBits
	return assignableIPs

def getAssignableIPs(maskInput):
	hostBits = getHostBits(maskInput)
	assignableIPs = 2**hostBits - 2
	return assignableIPs

def getSubnetMask(IPinput, subnetMaskInput):
	subnetMaskInput = int(subnetMaskInput)
	IPFormat = ""
	while(subnetMaskInput>0):
		print("in get subnetMask")
		print(subnetMaskInput)
		IPFormat = IPFormat + "1"
		subnetMaskInput = subnetMaskInput - 1
	while(len(IPFormat)<32):
		IPFormat = IPFormat + "0"
	IPFormat = changeToBinaryFormat(IPFormat)
	return IPFormat

def getNetworkAddress():

	return;

######







def main():
    UserInput = getArgs()
    AddressArray = cleanInput(UserInput)
    print("\nYou entered: ", AddressArray.groups())

    ## Determine Variables to use for next block below
    IPAddress = AddressArray.group(1)
    submask = AddressArray.group(2)
    binarysubMask = getSubnetMask(IPAddress,submask)
    # Find the IPBlocks Occupied
    # IPBlocks = getIPBlocks(int(submask))
    # subNetMasks(IPBlocks)


	####### Start finding variables!
    print("\tNumber of Host bits: ", getHostBits(submask))
    print("\tTotal IPs in our Network: ", getTotalIPs(submask))
    print("\tAssignable IPs (-2): ", getAssignableIPs(submask))
    print("\tGet Subnet Mask: ", getSubnetMask(IPAddress,submask))
    
    print("\tGet Subnet Mask: ", convertToDecimalFormat(IPAddress, binarysubMask, submask))


if __name__ == "__main__":
    main()
