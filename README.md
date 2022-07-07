# NYPD-Shooting-Incidents
"""PURPOSE OF THIS PROJECT AND HOW I IMPLEMENTED IT"""
The purpose of this project was to create an interactive map that would visualize the data of NYPD shooting incidents. This map would be able to give insights on shootings
in New York City such as where might more shootings be clustered around, what is the most common demographic of shooting victims, and more. I first downloaded a csv file 
'NYPD_Shooting_Incident_Data__Historic_.csv' containing NYPD recorded shooting incidents from 2003 and onward. I then read this file using pandas into 
a dataframe and then filtered this dataframe to contain specific features being 'OCCUR_DATE','OCCUR_TIME','BORO','STATISTICAL_MURDER_FLAG','VIC_AGE_GROUP','VIC_SEX','VIC_RACE','Latitude','Longitude'
I then filtered the dataframe even further to only contain shootings at manhattan in 2020. With this new dataframe it now contained all recorded shooting incidents at 
manhattan in the year 2020. I used the folium library to plot each and every shooting incident in manhattan on an interactive map. This interactive map is saved in a 
separate html file "NycshootingsManhattan2020.html"

"""HOW TO USE AND VIEW INTERACTIVE MAP"""
You can view this interactive map by entering in the link: file:///C:/Users/johnl/OneDrive/Desktop/Python%20Projects/NycshootingsManhattan2020.html 
You can click on the markers or icons to view the victims demographic and age group
