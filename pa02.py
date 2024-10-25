import sys


def calculateChecksum(checksumSize,fileName):
    #open the file in binary read mode, thanks python!
    with open(fileName,"rb") as file:
        text = file.read()
        if not text:
            print("Error reading file or file empty.",file = sys.stderr)
            sys.exit(1)
    chars = len(text)

    return "67677", chars 
    
        
def main():
    #arguments from command lines
    file = sys.argv[1]
    checkSumSize = int(sys.argv[2]) ## in bits 8 / 16 / 32
    if checkSumSize not in [8,16.32]:
        print("Valid checksum sizes are 8, 16, or 32\n",file=sys.stderr)    
        sys.exit(1) 

    #calculate checksum
    result, chars = calculateChecksum(checkSumSize,file)
    
    print(f"{checkSumSize:2} bit checksum is {result:8} for all {chars:4}\n")

if __name__ == "__main__":
    main()