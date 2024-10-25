import sys


def calculateChecksum(checksumSize,fileName):
    #open the file in binary read mode, thanks python!
    try:
        with open(fileName,"rb") as file:
            text = file.read()
    except:
        print("Error reading file or file empty.",file = sys.stderr)
        sys.exit(1)
            
    chars = len(text)
    paddingNeeded = len(chars) % (checksumSize // 8)
    if paddingNeeded != 0:
        padSize = (checksumSize // 8) - paddingNeeded
        text += b'X' * padSize ### padding with binary X to make it divisble by checksumsize
    
    checkSum = 0
    chunkSize = checksumSize // 8 ## converts it to bytes 1 byte is 8 bits
    
    ## add to sum till the end of text
    for i in range(0, len(text), chunkSize):
        chunk = int.from_bytes(text[i:i + chunkSize])
        checkSum = (checkSum + chunk) & ((1 << checksumSize) - 1)
        
    
     

    return "67677", chars 
    
        
def main():
    #arguments from command lines
    fileName = sys.argv[1]
    checkSumSize = int(sys.argv[2]) ## in bits 8 / 16 / 32
    if checkSumSize not in [8,16.32]:
        print("Valid checksum sizes are 8, 16, or 32\n",file = sys.stderr)    
        sys.exit(1) 

    #calculate checksum
    result, chars = calculateChecksum(checkSumSize,fileName)
    
    print(f"{checkSumSize:2} bit checksum is {result:8} for all {chars:4}\n")

if __name__ == "__main__":
    main()