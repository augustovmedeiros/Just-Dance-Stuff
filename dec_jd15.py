import os
import sys
import json
import struct
#DTAPE
def dec_dtape(dtapefile, entry_mapname):#Start DTape Conversion
    f = open(dtapefile, "rb")
    arq = open("raw_dtape.dec", "w")
    arq.write('{')
    arq.write('"__class":"Tape",')
    arq.write('"Clips":[')
    #Header
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)#timeline ver
    timeline_ver = struct.unpack('>I', byte)[0]
    #Header
    #Infos
    byte = f.read(4)#Entries
    entries = struct.unpack('>I', byte)[0]
    total = entries
    #Infos
    for x in range(entries):
        byte = f.read(4)#unknown
        entry_unknown = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#class_id
        entry_class = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#id
        entry_id = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#trackid
        entry_trackid = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#isactive
        entry_isactive = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#starttime
        entry_starttime = struct.unpack('>I', byte)[0]

        byte = f.read(4)#duration
        entry_duration = struct.unpack('>I', byte)[0]
        
        if(entry_class == 108 or entry_class == 112 or entry_class == 56):
            byte = f.read(4)#namelength
            entry_namelength = struct.unpack('>I', byte)[0]

            byte = f.read(entry_namelength)#name
            entry_name = byte.decode("utf-8")

            byte = f.read(4)#pathlength
            entry_pathlength = struct.unpack('>I', byte)[0]

            byte = f.read(entry_pathlength)#path
            entry_path = byte.decode("utf-8")

            byte = f.read(4)#atlindex
            entry_atlindex = struct.unpack('>I', byte)[0]

            byte = f.read(4)#unknown2
            entry_unknown2 = struct.unpack('>I', byte)[0]
            
            if(entry_class == 108 or entry_class == 112):

                byte = f.read(4)#goldmove
                entry_goldmove = struct.unpack('>I', byte)[0]

                byte = f.read(4)#coachid
                entry_coachid = struct.unpack('>I', byte)[0]

                byte = f.read(4)#movetype
                entry_movetype = struct.unpack('>I', byte)[0]
                #Useless stuff
                #Colors
                byte = f.read(4)#color1
                byte = f.read(4)#color2
                byte = f.read(4)#color3
                byte = f.read(4)#color4
                #Colors
                #Pointing
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                byte = f.read(4)
                #Useless stuff
                arq.write("{")
                arq.write('"__class":"MotionClip",')
                arq.write('"Id":' +  str(entry_id) + ',')
                arq.write('"TrackId":' + str(entry_trackid) + ',')
                arq.write('"IsActive":' + str(entry_isactive) + ',')
                arq.write('"StartTime":' + str(entry_starttime) + ',')
                arq.write('"Duration":' + str(entry_duration) + ',')
                arq.write('"ClassifierPath":"' + entry_path.replace("jd2015", "maps") + entry_name + '",')
                arq.write('"GoldMove":' + str(entry_goldmove) + ',')
                arq.write('"CoachId":' + str(entry_coachid) + ',')
                arq.write('"MoveType":' + str(entry_movetype) + ',')
                arq.write('"Color":[')
                arq.write('1,')
                arq.write('0.968628,')
                arq.write('0.164706,')
                arq.write('0.552941')
                arq.write('],')
                arq.write('"MotionPlatformSpecifics":{')
                arq.write('"X360":{')
                arq.write('"__class":"MotionPlatformSpecific",')
                arq.write('"ScoreScale":1,')
                arq.write('"ScoreSmoothing":0,')
                arq.write('"ScoringMode":0')
                arq.write('},')
                arq.write('"ORBIS":{')
                arq.write('"__class":"MotionPlatformSpecific",')
                arq.write('"ScoreScale":1,')
                arq.write('"ScoreSmoothing":0,')
                arq.write('"ScoringMode":0')
                arq.write('},')
                arq.write('"DURANGO":{')
                arq.write('"__class":"MotionPlatformSpecific",')
                arq.write('"ScoreScale":1,')
                arq.write('"ScoreSmoothing":0,')
                arq.write('"ScoringMode":0')
                arq.write('}')
                arq.write('}')
            elif(entry_class == 56):
                byte = f.read(4)#coachcount
                entry_coachcount = struct.unpack('>I', byte)[0]
                arq.write("{")
                arq.write('"__class":"PictogramClip",')
                arq.write('"Id":' +  str(entry_id) + ',')
                arq.write('"TrackId":' + str(entry_trackid) + ',')
                arq.write('"IsActive":' + str(entry_isactive) + ',')
                arq.write('"StartTime":' + str(entry_starttime) + ',')
                arq.write('"Duration":' + str(entry_duration) + ',')
                arq.write('"PictoPath":"' + entry_path.replace("jd2015", "maps") + entry_name + '",')
                arq.write('"CoachCount":' + str(entry_coachcount))    
        elif(entry_class == 28):
            byte = f.read(4)#effecttype
            entry_effecttype = struct.unpack('>I', byte)[0]
            arq.write("{")
            arq.write('"__class":"GoldEffectClip",')
            arq.write('"Id":' +  str(entry_id) + ',')
            arq.write('"TrackId":' + str(entry_trackid) + ',')
            arq.write('"IsActive":' + str(entry_isactive) + ',')
            arq.write('"StartTime":' + str(entry_starttime) + ',')
            arq.write('"Duration":' + str(entry_duration) + ',')
            arq.write('"EffectType":' + str(entry_effecttype))
        else:
            print("New entry class found:", entry_class)
        if(total == 1):
            arq.write('}')
        else:
            arq.write('},')
        total = total - 1
    
    arq.write('],')
    arq.write('"TapeClock":0,')
    arq.write('"TapeBarCount":1,')
    arq.write('"FreeResourcesAfterPlay":0,')
    arq.write('"MapName":"' + entry_mapname + '"')
    arq.write('}')
    f.close()
    arq.close()
    dtapejson = json.load(open("raw_dtape.dec", "r"))
    os.remove("raw_dtape.dec")
    return dtapejson
    #DTape Ending
#KTAPE
def dec_ktape(ktapefile, entry_mapname):#Start DTape Conversion
    f = open(ktapefile, "rb")
    arq = open("raw_ktape.dec", "w", encoding="utf8")
    arq.write('{')
    arq.write('"__class":"Tape",')
    arq.write('"Clips":[')
    #Header
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)#timeline ver
    timeline_ver = struct.unpack('>I', byte)[0]
    #Header
    #Infos
    byte = f.read(4)#Entries
    entries = struct.unpack('>I', byte)[0]
    total = entries
    #Infos
    for x in range(entries):
        byte = f.read(4)#unknown
        entry_unknown = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#class_id
        entry_class = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#id
        entry_id = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#trackid
        entry_trackid = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#isactive
        entry_isactive = struct.unpack('>I', byte)[0]
        
        byte = f.read(4)#starttime
        entry_starttime = struct.unpack('>I', byte)[0]

        byte = f.read(4)#duration
        entry_duration = struct.unpack('>I', byte)[0]

        byte = f.read(4)#pitch
        entry_pitch = struct.unpack('>f', byte)[0]

        byte = f.read(4)#lyricslength
        entry_lyricslength = struct.unpack('>I', byte)[0]

        byte = f.read(entry_lyricslength)#lyrics
        entry_lyrics = byte.decode("utf-8")

        byte = f.read(4)#isendofline
        entry_isendofline = struct.unpack('>I', byte)[0]

        #Maybe some kind of karaoke pointing shit
        byte = f.read(4)
        byte = f.read(4)
        byte = f.read(4)
        byte = f.read(4)

        arq.write("{")
        arq.write('"__class":"KaraokeClip",')
        arq.write('"Id":' +  str(entry_id) + ',')
        arq.write('"TrackId":' + str(entry_trackid) + ',')
        arq.write('"IsActive":' + str(entry_isactive) + ',')
        arq.write('"StartTime":' + str(entry_starttime) + ',')
        arq.write('"Duration":' + str(entry_duration) + ',')
        arq.write('"Pitch":' + str(entry_pitch) + ',')
        arq.write('"Lyrics":"' + entry_lyrics + '",')
        arq.write('"IsEndOfLine":' + str(entry_isendofline) + ',')
        arq.write('"ContentType":0,"StartTimeTolerance":4,"EndTimeTolerance":4,"SemitoneTolerance":5')
        if(total == 1): 
            arq.write('}')
        else:
            arq.write('},')
        total = total - 1

    arq.write('],')
    arq.write('"TapeClock":0,')
    arq.write('"TapeBarCount":1,')
    arq.write('"FreeResourcesAfterPlay":0,')
    arq.write('"MapName":"' + entry_mapname + '"')
    arq.write('}')
    f.close()
    arq.close()
    ktapejson = json.load(open("raw_ktape.dec", "r"))
    os.remove("raw_ktape.dec")
    return ktapejson

def dec_sd_15(sdfile, ver):
    entry_mapnamealtsd = None
    f = open(sdfile, "rb")
    arq = open("raw_songdesc.dec", "w")
    f.read(56)
    entry_mpnamelengthsd = struct.unpack('>I', f.read(4))[0]
    entry_mapnamesd = f.read(entry_mpnamelengthsd).decode("utf-8")
    f.read(8)
    entry_isalt = struct.unpack('>I', f.read(4))[0]
    if(entry_isalt == 1):
        entry_mpnamealtlengthsd = struct.unpack('>I', f.read(4))[0]
        entry_mapnamealtsd = f.read(entry_mpnamealtlengthsd).decode("utf-8")
    entry_messquantity = struct.unpack('>I', f.read(4))[0]
    f.read(16)
    entry_localeid = struct.unpack('>I', f.read(4))[0]
    f.read(32)
    if(entry_messquantity == 2):
        f.read(52)
    entry_artistlengthsd = struct.unpack('>I', f.read(4))[0]
    entry_artistsd = f.read(entry_artistlengthsd).decode("utf-8")
    f.read(18)
    entry_titlelengthsd = struct.unpack('>I', f.read(4))[0]
    entry_titlesd = f.read(entry_titlelengthsd).decode("utf-8")
    entry_numcoach = struct.unpack('>I', f.read(4))[0]
    f.read(4)
    entry_diff = struct.unpack('>I', f.read(4))[0]
    entry_backgroundtype = struct.unpack('>I', f.read(4))[0]
    entry_lyricstype = struct.unpack('>I', f.read(4))[0]
    if(entry_isalt != 1):
        f.read(20)
        entry_previewentry = struct.unpack('>I', f.read(4))[0]
        f.read(12)
        entry_previewLoopStart = struct.unpack('>I', f.read(4))[0]
        entry_previewLoopEnd = struct.unpack('>I', f.read(4))[0]
    else:
        f.read(12)
        entry_previewentry = 0
        entry_previewLoopStart = 0
        entry_previewLoopEnd = 100
    if(ver == "jd17" or ver == "jd18" or ver == "jd19"):
        f.read(28)
    else:
        f.read(8)
    entry_lyricscolor3 = struct.unpack('>f', f.read(4))[0]
    entry_lyricscolor2 = struct.unpack('>f', f.read(4))[0]
    entry_lyricscolor1 = struct.unpack('>f', f.read(4))[0]
    entry_lyricscolor0 = struct.unpack('>f', f.read(4))[0]
    arq.write('''{
   "__class":"Actor_Template",
   "WIP":0,
   "LOWUPDATE":0,
   "UPDATE_LAYER":0,
   "PROCEDURAL":0,
   "STARTPAUSED":0,
   "FORCEISENVIRONMENT":0,
   "COMPONENTS":[
      {
         "__class":"JD_SongDescTemplate",
         "MapName":"''' + entry_mapnamesd + '''",
         "JDVersion":2019,
         "OriginalJDVersion":2019,
         "Artist":"''' + entry_artistsd + '''",
         "DancerName":"Unknown Dancer",
         "Title":"''' + entry_titlesd + '''",
         "NumCoach":''' + str(entry_numcoach) + ''',
         "MainCoach":-1,
         "Difficulty":2,
         "SweatDifficulty":2,
         "backgroundType":0,
         "LyricsType":''' + str(entry_lyricstype) + ''',
         "Tags":[
            "main"
         ],
         "Status":3,
         "LocaleID":''' + str(entry_localeid) + ''',
         "MojoValue":0,
         "CountInProgression":1,
         "DefaultColors":{
            "songcolor_2a":[
               0,
               0,
               0,
               0
            ],
            "lyrics":[
               ''' + str(entry_lyricscolor0) + ''',
               ''' + str(entry_lyricscolor1) + ''',
               ''' + str(entry_lyricscolor2) + ''',
               ''' + str(entry_lyricscolor3) + '''
            ],
            "theme":[
               1,
               1,
               1,
               1
            ],
            "songcolor_1a":[
               0,
               0,
               0,
               0
            ],
            "songcolor_2b":[
               0,
               0,
               0,
               0
            ],
            "songcolor_1b":[
               0,
               0,
               0,
               0
            ]
         },
         "VideoPreviewPath":""
      }
   ]
}''')
    arq.close()
    f.close()
    sdjson = json.load(open("raw_songdesc.dec", "r"))
    os.remove("raw_songdesc.dec")
    return sdjson, entry_previewentry, entry_previewLoopStart, entry_previewLoopEnd, entry_mapnamealtsd
    

#MUSICTRACK
def dec_mt_15(mtfile, timeline_ver):#Start DTape Conversion
    f = open(mtfile, "rb")
    arq = open("raw_musictrack.dec", "w")
    arq.write('{')
    arq.write('"__class":"Actor_Template",')
    arq.write('"WIP":0,')
    arq.write('"LOWUPDATE":0,')
    arq.write('"UPDATE_LAYER":0,')
    arq.write('"PROCEDURAL":0,')
    arq.write('"STARTPAUSED":0,')
    arq.write('"FORCEISENVIRONMENT":0,')
    arq.write('"COMPONENTS": [{')
    arq.write('"__class": "MusicTrackComponent_Template",')
    arq.write('"trackData": {')
    arq.write('"__class": "MusicTrackData",')
    arq.write('"structure": {')
    arq.write('"__class": "MusicTrackStructure",')
    #Header
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)#timeline ver
    timeline_version = struct.unpack('>I', byte)[0]
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    #Header

    byte = f.read(4)#Markers
    markers = struct.unpack('>I', byte)[0]
    beats = []
    
    for x in range(markers):
        byte = f.read(4)#beat
        beat = struct.unpack('>I', byte)[0]
        beats.append(beat)
    arq.write('"markers":' + str(beats).replace(" ", "") + ',')

    byte = f.read(4)#signatures
    signatures = struct.unpack('>I', byte)[0]
    arq.write('"signatures": [')    
    for x in range(signatures):
        byte = f.read(4)#class
        byte = f.read(4)#marker
        sig_marker = struct.unpack('>I', byte)[0]
        byte = f.read(4)#beat
        sig_beat = struct.unpack('>I', byte)[0]
        arq.write('{')
        arq.write('"__class": "MusicSignature",')
        arq.write('"marker":' + str(sig_marker) + ',')
        arq.write('"beats":'+ str(sig_beat))
        if(signatures-x == 1):
            arq.write('}')
        else:
            arq.write('},')
    arq.write('],')

    byte = f.read(4)#sections
    sections = struct.unpack('>I', byte)[0]
    arq.write('"sections": [')

    for x in range(sections):
        byte = f.read(4)#class
        byte = f.read(4)#marker
        sec_marker = struct.unpack('>I', byte)[0]
        byte = f.read(4)#sectiontype
        sec_sectiontype = struct.unpack('>I', byte)[0]
        byte = f.read(4)#commentlength
        commentlength = struct.unpack('>I', byte)[0]
        byte = f.read(commentlength)
        arq.write('{')
        arq.write('"__class": "MusicSection",')
        arq.write('"marker":' + str(sec_marker) + ',')
        arq.write('"sectionType":'+ str(sec_sectiontype) + ',')
        arq.write('"comment":""')
        if(sections-x == 1):
            arq.write('}')
        else:
            arq.write('},')
    arq.write('],')
        
    #MUSICTRACK Ending
    byte = f.read(4)#startbeat
    startbeat = struct.unpack('>i', byte)[0]

    byte = f.read(4)#endbeat
    endbeat = struct.unpack('>I', byte)[0]

    if(timeline_ver == "jd18" or timeline_ver == "jd19"):
        #UNKNOWN
        byte = f.read(4)
        byte = f.read(6)
        #UNKNOWN

    byte = f.read(4)#videostarttime
    videostarttime = struct.unpack('>f', byte)[0]
    
    byte = f.read(4)
    
    byte = f.read(4)#wavlength
    wavlength = struct.unpack('>I', byte)[0]
    byte = f.read(wavlength)
    wav = byte.decode("utf-8")

    byte = f.read(4)#pathlength
    wavpathlength = struct.unpack('>I', byte)[0]
    byte = f.read(wavpathlength)
    wavpath = byte.decode("utf-8")

    arq.write('"startBeat":' + str(startbeat) + ',')
    arq.write('"endBeat":' + str(endbeat) +',')
    arq.write('"videoStartTime":' + str(videostarttime) + ',')
    arq.write('"previewEntry":' + str(int(endbeat/2)) + ',')
    arq.write('"previewLoopStart":' + str(int(endbeat/2)) + ',')
    arq.write('"previewLoopEnd":' + str(endbeat) + ',')
    arq.write('"volume":0')
    arq.write('},')
    arq.write('"path":"' + wavpath + wav + '",')
    arq.write('"url":""')
    arq.write('}}]}')
    
    byte = f.read(4)
    byte = f.read(4)
    byte = f.read(4)
    arq.close()
    f.close()
    mtjson = json.load(open("raw_musictrack.dec", "r"))
    os.remove("raw_musictrack.dec")
    return mtjson
    #MUSICTRACK Ending

