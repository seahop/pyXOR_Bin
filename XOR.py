import binascii 

key = bytes([0x41,0x41])

def xorFrom(key):
    combined = bytearray()
    with open("Some\\Path\\file.bin", "rb") as f:
        while (content := f.read(1)):
            result = [ chr(a ^ b) for (a,b) in zip(content,key) ]
            combined += bytes(result.pop(0), encoding='latin1')
    
    file = open("Some\\Path\\b.bin","wb")
    file.write(combined)
    
def xorTo(key):
    combined = bytearray()
    with open("Some\\Path\\beacon.bin", "rb") as f:
        while (content := f.read(1)):
            result = [ chr(a ^ b) for (a,b) in zip(content,key) ]
            combined += bytes(result.pop(0), encoding='latin1')
            
        #print(combined)
            
    file = open("Some\\Path\\a.bin","wb")
    file.write(combined)
    
    
xorTo(key)
xorFrom(key)