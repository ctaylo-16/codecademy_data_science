import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load rankings data here:
roller_coasters= pd.read_csv('roller_coasters.csv')
rankings_wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')

rankings_steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(roller_coasters.head())
print(rankings_wood.head())
print(rankings_steel.head())

# write function to plot rankings over time for 1 roller coaster here:
    #Write a function that will plot the ranking of a given roller coaster over time as a line. Your function should take a roller coaster’s name and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.

def rank_over_time(name, rankings_df):
    coaster_rankings = rankings_df[(rankings_df['Name']==name)]
    fig, ax =plt.subplots()
    ax.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'])
    ax.set_yticks(coaster_rankings['Rank'].values)
    ax.set_xticks(coaster_rankings['Year of Rank'].values)
    plt.title("{} Rankings".format(name))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.show()


rank_over_time('El Toro',rankings_wood)
plt.close('all')


# write function to plot rankings over time for 2 roller coasters here:

def ranks_over_time(name1,name2, rankings_df):
    coaster_rankings1 = rankings_df[(rankings_df['Name']==name1)]
    coaster_rankings2 = rankings_df[(rankings_df['Name']==name2)]
    fig, ax =plt.subplots()
    ax.plot(coaster_rankings1['Year of Rank'],coaster_rankings1['Rank'])
    ax.plot(coaster_rankings2['Year of Rank'],coaster_rankings2['Rank'])
    plt.title("{} Rankings".format([name1, name2]))
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.legend([name1,name2])
    plt.show()

 
ranks_over_time('El Toro','Boulder Dash',rankings_wood)




plt.clf()

# write function to plot top n rankings over time here:

plt.close('all')

rankings_wood['name_place'] = rankings_wood['Name'] + rankings_wood['Park']

top_n_rankings = rankings_wood[rankings_wood['Rank'] <= 3]
print(top_n_rankings)

top_coasters = rankings_wood[rankings_wood['name_place'].isin(top_n_rankings['name_place'].unique())]  
print(top_coasters)
print(top_coasters.sort_values(by='name_place'))

def top_ranks_time(n_rank,rankings_df):
    top_n_rankings = rankings_df[rankings_df['Rank'] <= n_rank]
    top_coasters = rankings_df[rankings_df['Name'].isin(top_n_rankings['Name'].unique())]    
    top_coasters_pivoted = top_coasters.pivot(index='Year of Rank', columns = 'name_place', values = 'Rank')
    fig, ax=plt.subplots()
    top_coasters_pivoted.plot(ax=ax)
    


top_ranks_time(7,rankings_wood)





plt.clf()

# load roller coaster data here:
roller_coasters= pd.read_csv('roller_coasters.csv')
print(roller_coasters.head())

# write function to plot histogram of any numeric columns values here:
    #speed,height,length, number of inversions

def make_hist(roller_coasters,variable):
    plt.hist(roller_coasters[variable])
    plt.title('Histogram of roller coaster {}'.format(variable))
    plt.xlabel(variable)
    plt.ylabel('Count')
    plt.show()

make_hist(roller_coasters,'length')




plt.clf()

# write function to plot inversions by coaster at a park here:
park = roller_coasters[roller_coasters['park'] == 'Parc Asterix']
print(park)
plt.bar(range(len(park['num_inversions'])),park['num_inversions'])
ax = plt.subplot()
ax.set_xticks(range(len(park['name'])))
ax.set_xticklabels(park['name'],rotation=90)
plt.show()
def funct_invert(roller_coasters,park_name):
    park = roller_coasters[roller_coasters['park'] == park_name]
    num_inversions = park['num_inversions']
    coasters = park['name']
    plt.bar(range(len(num_inversions)),num_inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(coasters)))
    ax.set_xticklabels(coasters,rotation=90)
    ax.set_yticks(num_inversions)
    plt.ylabel('Number of inversions')
    plt.xlabel('Roller coasters in {} '.format(park_name))
    plt.title('Number of inversions of each roller coaster in {} '.format(park_name))
    plt.show()



funct_invert(roller_coasters,'Parc Asterix')



plt.clf()

# write function to plot pie chart of operating status here:

def coasters_pie(roller_coasters):
    status_options =roller_coasters['status'].unique()
    status_count = roller_coasters['status'].value_counts().reset_index()
    plt.pie(status_count['status'], autopct='%0.1f%%', labels=status_options)
    plt.axis('equal')
    plt.title('Rollercoaster operating status')
    plt.show()
    
coasters_pie(roller_coasters)    
    




plt.clf()

# write function to create scatter plot of any two numeric columns here:




def coasters_scatter(roller_coasters,variable_1,variable_2):
    plt.scatter(roller_coasters[variable_1],roller_coasters[variable_2])
    plt.title('Relationship between variables: {} and {} '.format(variable_1,variable_2))
    plt.xlabel(variable_1)
    plt.ylabel(variable_2)
    plt.legend([variable_1,variable_2])
    plt.show()

coasters_scatter(roller_coasters,'height','length')


plt.clf()
