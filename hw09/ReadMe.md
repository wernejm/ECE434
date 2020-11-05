James Werne
ECE434 hw09
ReadMe.md

Project Timeline: 

Our group plans to complete the following milestones by the given dates:

11/6/2020: Write patterns to LED strip\
11/9/2020: Update eLinux page with project info. Post project on other sites (effectively completing hw10)\
11/13/2020: Research how to extract intensity of certain frequencies in an mp3/wav file\
11/16/2020: Apply research to have LEDs react to music (similar to an equalizer)


Logging in Sheets: 


I decided to record values from the two TMP101 sensors into a google sheets form. To record the current temperature, navigate to the subdirectory "/sheets" and run ./setup.sh to configure the TMP101 sensors, then run ./tempread.py in the command line to read and record the temperatures. 

The link to the google sheet with my temp info is shown below: 

https://docs.google.com/spreadsheets/d/1WDUkZMWWFjqkyZ2v3483UQqmKmDF-dYwOA_jITEOOO4/edit?usp=sharing 


Logging in ThingSpeak: 


Similarly, I recorded values from the two TMP101 sensors into a Thingspeak channel. To record the current temperature, navigate to the subdirectory "/thingspeak", run ./tempread.sh to configure the sensors, type "source setup.sh" in the command line to set up the thingspeak API, and run ./temp.py to read and record the temperature. 

The link to the thingspeak page with the temp info is shown below: 

https://thingspeak.com/channels/1220211/private_show  
