import os
import struct

cwd = os.getcwd()

def makeHashList(inputipk):
    ipkhashs = [] #hash list
    with open(inputipk, "rb") as f: #Start Reading IPK
        for i in range(4): 
            byte = f.read(4) #unused bytes
        
        byte = f.read(4)
        numfiles = struct.unpack('>I', byte)[0]
    
        for i in range(10): 
            byte = f.read(4) #unused bytes
    
        for i in range(numfiles):
            for i in range(4):
                byte = f.read(4)#unused bytes
            
            byte = f.read(4)#namelength
            entry_namelength = struct.unpack('>I', byte)[0]
            
            byte = f.read(entry_namelength)#name
            entry_name = byte.decode("utf-8")
        
            byte = f.read(4)#pathlength
            entry_pathlength = struct.unpack('>I', byte)[0]
            
            byte = f.read(entry_pathlength)#path
            entry_path = byte.decode("utf-8")
        
            byte = f.read(4)#hash
            ipkhashs.append(byte)
            
            for i in range(4):
                byte = f.read(4) #unused bytes
                
    return ipkhashs

denc = open("secure_fat.gf", "wb")
denc.write((1431520852).to_bytes(4, byteorder="big", signed=False))
denc.write((526312495).to_bytes(4, byteorder="big", signed=False))
denc.write((1).to_bytes(4, byteorder="big", signed=False))
ipkid = 0
allhashs = []

for nome in os.listdir(cwd):
    if(".ipk" in nome):
        allhashs = allhashs + makeHashList(nome)
denc.write((len(allhashs)).to_bytes(4, byteorder="big", signed=False))

for nome in os.listdir(cwd):       
    if(".ipk" in nome):
        ipkhash = makeHashList(nome)
        for hashfile in ipkhash:
            denc.write(hashfile)
            denc.write((1).to_bytes(4, byteorder="big", signed=False))
            denc.write((ipkid).to_bytes(1, byteorder="big", signed=False))
        ipkid = ipkid + 1
        
denc.write((ipkid).to_bytes(4, byteorder="big", signed=False))
ipkid = 0

for nome in os.listdir(cwd):       
    if(".ipk" in nome):
        ipkname = nome.lower().replace(".ipk","").replace("_wiiu","").replace("_wii","").replace("_x360","").replace("_pc","").replace("_orbis","").replace("_durango","").replace("_nx","")
        denc.write((ipkid).to_bytes(1, byteorder="big", signed=False))
        denc.write((len(ipkname.encode('utf8'))).to_bytes(4, byteorder="big", signed=False))
        denc.write(ipkname.encode('utf8'))
        ipkid = ipkid + 1
        
denc.close()
        

    
    
