import sys


def calculateChecksum(checksumSize,fileName):
    #open the file in binary read mode, thanks python!
    try:
        with open(fileName,"rb") as file:
            text = file.read()
    except:
        print("Error reading file or file empty.",file = sys.stderr)
        sys.exit(1)
            
    #remove windows \r characters
    text = text.replace(b'\r', b'')        
    
    chars = len(text)
    paddingNeeded = chars % (checksumSize // 8)
    if paddingNeeded != 0:
        padSize = (checksumSize // 8) - paddingNeeded
        text += b'X' * padSize ### padding with binary X to make it divisble by checksumsize
    
    chars = len(text)
    ## print with padding debug
    #for i in range(0, len(text), 80):
    #   print(text[i:i + 80])
    #print("\n\n")
    
    checkSum = 0
    chunkSize = checksumSize // 8 ## converts it to bytes 1 byte is 8 bits
    
    ## add to sum till the end of text
    for i in range(0, chars, chunkSize):
        chunk = int.from_bytes(text[i:i + chunkSize], "big", signed= False)
        checkSum = (checkSum + chunk) & ((1 << checksumSize) - 1)
        
    ## take the two's complement
    ##checkSum = (~checkSum + 1) & (( 1 << checksumSize) - 1)

    return checkSum, chars, text 
    
        
def main():
    #arguments from command lines
    fileName = sys.argv[1]
    checkSumSize = int(sys.argv[2]) ## in bits 8 / 16 / 32
    if checkSumSize not in [8,16,32]:
        print("Valid checksum sizes are 8, 16, or 32\n",file = sys.stderr)    
        sys.exit(1) 

    #calculate checksum
    result, chars, newText = calculateChecksum(checkSumSize,fileName)
    result = hex(result)
    resultHex = result[2:]
    
    for i in range(0, len(newText), 80):
        line = newText[i:i + 80].decode('utf-8', errors='replace')  # Convert bytes to string
        print(line)
    
    print(f"{checkSumSize:2d} bit checksum is {resultHex:8} for all {chars:4d} chars\n")

if __name__ == "__main__":
    main()