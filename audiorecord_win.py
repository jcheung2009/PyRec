import pyaudio 
import wave
import audioop
from collections import deque
import os
import time
import math



CHUNK = 256 # CHUNKS of bytes to read each time from mic
FORMAT = pyaudio.paInt16 #this is the standard wav data format (16bit little endian)
CHANNELS = 1# number of channels
RATE = 44100# sampling frequency
THRESHOLD = 10500 # amplitude threshold
SILENCE_LIMIT = 1 # amount of silence required to stop recording in seconds
PREV_AUDIO = 0.5 # Previous audio (in seconds) to prepend
MIN_DUR=1#minimum duration in seconds

def audio_int(num_samples=64):
 """ Gets max audio intensity for a bunch of chunks of data. useful for setting threshold.
 """
 print "Getting intensity values from mic."

 p = pyaudio.PyAudio()
 stream=p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
 
 #stream = aa.PCM(aa.PCM_CAPTURE,aa.PCM_NORMAL,'hw:1,0')
 #stream.setchannels(CHANNELS)
 #stream.setrate(RATE)
 #stream.setformat(FORMAT)
 #stream.setperiodsize(CHUNK)
 values = [math.sqrt(abs(audioop.max(stream.read(CHUNK), 4)))for x in range(num_samples)]
 values = sorted(values, reverse=True)
 r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
 print " Finished "
 print " max audio intensity is ", values
 stream.close()
 r=1
 return r
 
def record_song(threshold=THRESHOLD):

 p = pyaudio.PyAudio()    
 stream=p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
 #stream = aa.PCM(aa.PCM_CAPTURE,aa.PCM_NORMAL,'hw:1,0')
 #stream.setchannels(CHANNELS)
 #stream.setrate(RATE)
 #stream.setformat(FORMAT)
 #stream.setperiodsize(CHUNK)
    
 print "Listening"
 audio2send = []
 cur_data = '' # current chunk of audio data
 rel = RATE/CHUNK
 slid_win = deque(maxlen=SILENCE_LIMIT * rel) #amplitude threshold running buffer
 prev_audio = deque(maxlen=PREV_AUDIO * rel) #prepend audio running buffer
 started = False
 curr_data=stream.read(CHUNK)
 slid_win.append(math.sqrt(abs(audioop.max(cur_data, 4)))) 
 while (1):
#  if len(slid_win)>0:
#   print max(slid_win) #uncomment if you want to print intensity values
  cur_data = stream.read(CHUNK)
  slid_win.append(math.sqrt(abs(audioop.max(cur_data, 4))))
  if(sum([x > THRESHOLD for x in slid_win]) > 0):
   if(not started):
    print "recording"
    print time.ctime()
    started = True
   audio2send.append(cur_data)
  elif (started is True and len(audio2send)>MIN_DUR*rel):
   print "Finished"
   filename = save_audio(list(prev_audio) + audio2send)
   started = False
   slid_win = deque(maxlen=SILENCE_LIMIT * rel)
   prev_audio = deque(maxlen=0.5 * rel)
   print "Listening ..."
   audio2send=[]
  elif (started is True):
   print "duration criterion not met"
   started = False
   slid_win = deque(maxlen=SILENCE_LIMIT * rel)
   prev_audio = deque(maxlen=0.5 * rel)
   audio2send=[]
   print "Listening ..."
  else:
   prev_audio.append(cur_data)
 print "done recording"
 stream.close()

def save_audio(data):
 """ Saves mic data to  WAV file. Returns filename of saved
 file """
 filename = 'output_'+str(int(time.time()))
 # writes data to WAV file
 data = ''.join(data)
 wf = wave.open(filename + '.wav', 'wb')
 wf.setnchannels(1)
 wf.setsampwidth(4)
 wf.setframerate(RATE) 
 wf.writeframes(data)
 wf.close()
 return filename + '.wav'


if(__name__ == '__main__'):
 audio_int()
 record_song()
