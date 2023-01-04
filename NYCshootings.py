import pandas as pd
import numpy as np
import datetime as dt 
import matplotlib.pyplot as plt
import folium
import datetime as dt


if __name__ == '__main__':
    shooting_df = pd.read_csv('NYPD_Shooting_Incident_Data__Historic_.csv')
    shooting_df = shooting_df[['OCCUR_DATE','OCCUR_TIME','BORO','STATISTICAL_MURDER_FLAG','VIC_AGE_GROUP','VIC_SEX','VIC_RACE','Latitude','Longitude']]
    shooting_df = shooting_df[shooting_df['BORO'].str.contains('MANHATTAN')] #filter the dataframe to only have shootings from queens
    shooting_df['OCCUR_DATE'] = pd.to_datetime(shooting_df['OCCUR_DATE']) #convert the occur_date column to datetime objects
    shooting_df['OCCUR_DATE'] = pd.DatetimeIndex(shooting_df['OCCUR_DATE']).year #filter the dataframe to only have shootings from 2021
    years = [2020]
    shooting_df= shooting_df[shooting_df['OCCUR_DATE'].isin(years)]
    shooting_df = shooting_df.reset_index(drop = True)
    #calls_df = calls_df.dropna(subset = )
    my_map3 = folium.Map(location = [40.74169, -74.003], zoom_start = 7)
    for ind in shooting_df.index:
        folium.Marker([shooting_df['Latitude'][ind], shooting_df['Longitude'][ind]], popup = shooting_df['VIC_RACE'][ind] + ' ' + shooting_df['VIC_AGE_GROUP'][ind], icon = folium.Icon(color = 'red', icon = 'info_sign')).add_to(my_map3)

    my_map3.save("NycshootingsManhattan2020.html")
    print(shooting_df.head)
    """plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()"""
