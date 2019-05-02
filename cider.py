

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
def formatToBinary(unformattedStringInput):
    counter = 0 
    formattedString = ""
    for i in unformattedStringInput:
        formattedString = formattedString + i

        ##### We want to test out the next number, as well as avoid zero's
        if((counter+1)%8==0 and (counter+1)!=len(unformattedStringInput)):
            formattedString = formattedString + "."
        counter = counter+1
    return formattedString

def convertToDecimalFormat(binaryMaskInput, subnetMaskInput):
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
    bitHolder = 0
    for i in block1:
        if(i=="1"):
            bitHolder = bitHolder + 2**counter
        counter = counter - 1
    decimalIP = decimalIP + str(bitHolder)
    decimalIP = decimalIP + "."

    counter = 7
    bitHolder = 0
    for i in block2:
        if(i=="1"):
            bitHolder = bitHolder + 2**counter
        counter = counter - 1
    decimalIP = decimalIP + str(bitHolder)
    decimalIP = decimalIP + "."

    counter = 7
    bitHolder = 0
    for i in block3:
        if(i=="1"):
            bitHolder = bitHolder + 2**counter
        counter = counter - 1
    decimalIP = decimalIP + str(bitHolder)
    decimalIP = decimalIP + "."

    counter = 7
    bitHolder = 0
    for i in block4:
        if(i=="1"):
            bitHolder = bitHolder + 2**counter
        counter = counter - 1
    decimalIP = decimalIP + str(bitHolder)
    return decimalIP


def convertToBinaryFormat(decimalInput):

    BinaryIP = ""

    maskSplitArray = re.search(r'(.*)\.(.*)\.(.*)\.(.*)', decimalInput)
    block1 = int(maskSplitArray.group(1))
    block2 = int(maskSplitArray.group(2))
    block3 = int(maskSplitArray.group(3))
    block4 = int(maskSplitArray.group(4))

    block1 = bin(block1)
    block2 = bin(block2)
    block3 = bin(block3)
    block4 = bin(block4)

    block1 = block1[2:]
    block2 = block2[2:]
    block3 = block3[2:]
    block4 = block4[2:]

    while(len(block1)<8):
        block1 = "0" + block1
    while(len(block2)<8):
        block2 = "0" + block2
    while(len(block3)<8):
        block3 = "0" + block3
    while(len(block4)<8):
        block4 = "0" + block4
    BinaryIP = BinaryIP + block1 + "." + block2 + "." + block3 + "." + block4

    return BinaryIP;



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

def getSubnetMask( subnetMaskInput):
    subnetMaskInput = int(subnetMaskInput)
    IPFormat = ""
    while(subnetMaskInput>0):
        IPFormat = IPFormat + "1"
        subnetMaskInput = subnetMaskInput - 1
    while(len(IPFormat)<32):
        IPFormat = IPFormat + "0"
    IPFormat = formatToBinary(IPFormat)
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
    binarysubMask = getSubnetMask(submask)
    binaryIPAddress = convertToBinaryFormat(IPAddress)
    # Find the IPBlocks Occupied
    # IPBlocks = getIPBlocks(int(submask))
    # subNetMasks(IPBlocks)


    ####### Start finding variables!
    print("\tNumber of Host bits: ", getHostBits(submask))
    print("\tTotal IPs in our Network: ", getTotalIPs(submask))
    print("\tAssignable IPs (-2): ", getAssignableIPs(submask))
    print("\tGet Subnet Mask: ", getSubnetMask(submask))
    print("\tConvert Subnet Mask to Decimal: ", convertToDecimalFormat(binarysubMask, submask))
    print("\tConvert OG to Binary: ", convertToBinaryFormat(IPAddress))
    print("\n\nNow in order to determine the range, aka the Network Address and Broadcast address, \nwe need to compare the Binary Subnet Mask with the Binary Original IP")
    print("\n\n")
    print("SubMask: \n\t", binarysubMask,"\nIP Address:","\n\t", binaryIPAddress)

if __name__ == "__main__":
    main()
