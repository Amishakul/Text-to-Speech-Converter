# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
import pyttsx3

  
# import Os module to start the audio file
import os 
  
mytext = "Amidst the cacophony of bustling city streets, María, with her résumé in hand, walked into the café. The aroma of freshly brewed café au lait mingled with the scent of croissants, creating a delightful atmosphere. She was here for a job interview at Café de l'Artiste, a place known for its fusion of artistic expression and culinary expertise. As she waited, she admired the café's décor, which featured abstract paintings by local artists, adding an air of sophistication to the ambiance. María had a résumé filled with diverse experiences, from working as a sous chef in Paris to volunteering in São Paulo, and she hoped to become part of this creative and gastronomic community."
  
# Language we want to use 
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 

