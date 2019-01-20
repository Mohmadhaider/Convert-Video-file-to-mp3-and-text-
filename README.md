# Convert-Video-file-to-mp3-and-text-

-----FIRST---- you need to insall following things
ffmpeg you can download it from https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20190119-32fb83e-win64-static.zip

after that Extract that zip file

copy C:\Users\path to\Desktop\ffmpeg-20190117-aceb913-win64-static\bin
and add this path to system variable under environment variable.

after that you can check  it by 
open command prompt
type C:\Users>ffmpeg
if No errors then ok else you need to go to that path using command prompt ex (cd C:\Users\path to\Desktop\ffmpeg-20190117-aceb913-win64-static\bin)
and execute ffmpeg command or write ffmpeg again it will definetly work but for these you also need to give the ffmpeg path in python script so it will work fine

-----SECOND---- you need to install dependences using pip 
for that write follwing command in cmd

C:\Users>pip install SoundFile
and

C:\Users>pip install SpeechRecognition

------THIRD---- after that you need to clone this and run speect_to_text.py file 

#########################################################################################3
This can also user to convert video to audio and audio to text.

By using python 3.6 and google recognizer and ffmpeg it will convert video file like mp4 to audio file like mp3 and also convert 3gp file to wav file for text convert. Using speect recognize it will extract text form audio 
