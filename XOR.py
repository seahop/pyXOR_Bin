import binascii 
import argparse
from datetime import datetime

    
def XOR(key,binary, clearkey):
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")

    combined = bytearray()
    with open(binary, "rb") as f:
        while (content := f.read(1)):
            result = [ chr(a ^ b) for (a,b) in zip(content,key) ]
            combined += bytes(result.pop(0), encoding='latin1')
                        
    file = open("encoded" + time + ".bin","wb")
    file.write(combined)
    print("XOR encrypted binary: " + binary)
    print("XOR encrypted with key: " + clearkey)
    print("Output file: " + "encoded" + time + ".bin")
    
def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", dest= "key", help="Key to XOR. Wrap in quotes to be safe. Doesnt like special characters.", required=True)
    parser.add_argument("-b", "--bin", dest= "path", help="Binary path. Should work with any binary.", required=True)
    args = parser.parse_args()

    toBytes = args.key.encode('latin1')
    XOR(toBytes, args.binary, args.key)

if __name__ == "__main__":
    main()
