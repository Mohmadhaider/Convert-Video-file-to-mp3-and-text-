import os
import speech_recognition as sr
import soundfile as sf

#Class for video to text
class Converter:

    file_name = ""
    path = ""
    output = "/music.wav"
    # convert_to_audio will convert mp4 video file to 3gp and after that 3gp to wav file
    # Lower size of file will give better performance
    def convert_to_audio(self, path, file_name):
        self.path = path # path to the video file
        self.file_name = file_name # name of the video file
        # convert mp4 video to 3gp video with 176x144 px using FFMPEG
        os.system('ffmpeg -y -i '+self.path+'/'+self.file_name+' -r 20 -s 176x144 -vb 400k -acodec aac -strict experimental -ac 1 -ar 8000 -ab 24k '+self.path+'/vid.3gp')
        # convert 3gp video file to wav file using FFMPEG
        os.system('ffmpeg -i '+self.path+'/vid.3gp -b:a 192K '+self.path+self.output)

    # Extract text form audio file with 85% accuracy
    def convert_audio_to_text(self):
        # create object of Recognizer
        r = sr.Recognizer()
        # Get audio file
        Audiofile = sr.AudioFile(self.path+self.output)
        # create object of sound file to define duration of audio file in seconds
        f = sf.SoundFile(self.path+self.output)
        #define seconds in sound file
        seconds = float(format(len(f) / f.samplerate))
        audio = [] # list to store chunks of audios
        i = 0.00

        with Audiofile as source:
            #Start = offset end = duration
            while i <= seconds:
                # add audio chunks to list
                audio.append(r.record(source, duration = 10))
                i+=20
                
        try:
            #iterate through all elements 
            for aud in audio:
                # using google recognizer extract all text from all  chunks  "Required High internet connection"
                # printing result, you can store it in any variable and also create lyrics******
                print(r.recognize_google(aud))

        except Exception as e:
            print(e)



Convert_obj = Converter()
Convert_obj.convert_to_audio('C:/Your/path/to/video','name_of_video.mp4')
Convert_obj.convert_audio_to_text()
