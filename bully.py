#raspberry pi users, paste in terminal;
#sudo apt-get install espeak;
#sudo pip3 install num2words

#requires openai libraries

#set the volume in 'alsamixer' in the terminal
#select f6 and choose your output
#change the volume with the arrow keys.

#openai
import openai
from gtts import gTTS

#tts
from num2words import num2words
from subprocess import call

#input your openai api key here
openai.api_key = "your-openai-key"

#commands - change the directory
cmd_beg= 'espeak '
cmd_end= ' | aplay /home/adam-cotton/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
cmd_out= '--stdout > /home/adam-cotton/Desktop/Text.wav ' # To store the voice file

while True:
    def generate_response(prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    prompt = input("\nFeel free to ask anything? \n >> ")
    action = " answer in the most rude, insulting and sarcastic way possible making me feel stupid, swearing as much as possible, use common jokes to also insult. keep the answer on one line. Use no grammar."
    response = generate_response(prompt + action)
    ttsresp = response.replace(' ', '_')
    ttsresp = response.replace('\'', '_') #attempt to remove you're

    print("\n" + response)
    
    #Replacing ' ' with '_' to identify words in the text entered

    print(ttsresp)

    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+cmd_out+ttsresp+cmd_end], shell=True)
    

