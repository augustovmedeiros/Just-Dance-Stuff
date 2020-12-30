import os
import struct

for nome in os.listdir("input//"):
    os.mkdir("input//temp")
    if(".mp4" in nome and ".ckd" not in nome):
        os.system('ffmpeg -i input//' + nome + ' -ar 32000 -filter:a "volume=12dB" -map_channel 0.1.0 input//temp//left.wav -ar 32000 -filter:a "volume=12dB" -map_channel 0.1.1 input//temp//right.wav')
    if(".wav" in nome and ".ckd" not in nome or ".ogg" in nome):
        os.system("ffmpeg -i input//" + nome + " -ar 32000 -map_channel 0.0.0 input//temp//left.wav -ar 32000 -map_channel 0.0.1 input//temp//right.wav")
    if(".ckd" not in nome):
        os.system("VGAudioCli input//temp//left.wav input//temp//left.dsp")
        os.system("VGAudioCli input//temp//right.wav input//temp//right.dsp")
        rightbytes = []
        leftbytes = []
        filesize = (os.path.getsize("input//temp//left.dsp") - 96)
        leftcoefs = b''
        rightcoefs = b''

        with open("input//temp//left.dsp", "rb") as f:
            leftcoefs = f.read(96)
            for i in range(int(filesize/8)): 
                byte = f.read(8)
                leftbytes.append(byte)

        with open("input//temp//right.dsp", "rb") as f:
            rightcoefs = f.read(96)
            for i in range(int(filesize/8)): 
                byte = f.read(8)
                rightbytes.append(byte)
        
        os.remove("input//temp//left.wav")
        os.remove("input//temp//right.wav")
        os.remove("input//temp//left.dsp")
        os.remove("input//temp//right.dsp")
        os.rmdir("input//temp")

        nome = nome.replace(".ogg", ".wav")
        offsetinfo = 320
        denc = open("output//" + nome + ".ckd", "wb")
        denc.write(b'\x52\x41\x4B\x49\x00\x00\x00\x09\x57\x69\x69\x20\x61\x64\x70\x63\x00\x00\x01\x2E\x00\x00\x01\x40\x00\x00\x00\x05\x00\x00\x00\x00\x66\x6D\x74\x20\x00\x00\x00\x5C\x00\x00\x00\x12\x64\x73\x70\x4C\x00\x00\x00\x6E\x00\x00\x00\x60\x64\x73\x70\x52\x00\x00\x00\xCE\x00\x00\x00\x60\x64\x61\x74\x4C\x00\x00\x01\x40')
        denc.write((len(leftbytes)*8).to_bytes(4, 'big'))
        denc.write(b'\x64\x61\x74\x52')
        denc.write((offsetinfo + (len(leftbytes)*8)).to_bytes(4, 'big'))
        denc.write((len(rightbytes)*8).to_bytes(4, 'big'))
        denc.write(b'\x00\x02\x00\x02\x00\x00\x7D\x00\x00\x00\xFA\x00\x00\x02\x00\x10\x00\x00')
        denc.write(leftcoefs)
        denc.write(rightcoefs)
        denc.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        for i in range(int(filesize/8)):
            denc.write(leftbytes[i])
        for i in range(int(filesize/8)):
            denc.write(rightbytes[i])   
        denc.close()
        print("DONE: " + nome + ".ckd")
