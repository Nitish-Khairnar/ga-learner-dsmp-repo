# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#path of the data file- path
data=pd.read_csv(path)
#print(data.head())
#Code starts here 
data['Gender'].replace('-','Agender', inplace=True)
gender_count=data.Gender.value_counts()
gender_count.plot(kind='bar')



# --------------
#Code starts here
alignment=data.Alignment.value_counts()
#pie_labels='Character Alignment'
explode=(0.1,0,0)
plt.pie(alignment, explode=explode, labels= alignment.index)
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here
sc_df=data[['Strength', 'Combat']]
#print(sc_df.head())
#mean_strength=round(data.Strength.mean(),2)
#mean_combat=round(data.Combat.mean(),2)
#diff_strength=round(data.Strength-mean_strength,2)
#diff_combat=round(data.Combat-mean_combat,2)
#summation=round((diff_strength*diff_combat).sum(),2)
sc_covariance=round(sc_df.cov().iloc[0,1],2)
#print(sc_covariance)
sc_strength=sc_df['Strength'].std()
sc_combat=sc_df['Combat'].std()


#sc_covariance=round(summation/len(sc_df),2)
#print(sc_covariance)
#now calculate the SD
#strength_Distance=(data.Strength-mean_strength)**2
#sc_strength=(strength_Distance.sum()/len(strength_Distance))**(1/2)
#similarly for combat
#combat_Distance=(data.Combat-mean_combat)**2
#sc_combat=(combat_Distance.sum()/len(combat_Distance))**(1/2)
sc_pearson=sc_covariance/(sc_strength*sc_combat)
#print(sc_pearson)
#now we will do the same for Intelligence and combat columns
ic_df=data[['Intelligence', 'Combat']]
#print(ic_df.head())
#mean_intelligence=data.Intelligence.mean()
#diff_Intelligence=data.Intelligence-mean_intelligence
#summation_ic=(diff_Intelligence*diff_combat).sum()
#ic_covariance=summation_ic/len(ic_df)
ic_covariance=round(ic_df.cov().iloc[0,1],2)
ic_intelligence=ic_df['Intelligence'].std()
ic_combat=ic_df['Combat'].std()
#print(ic_covariance)
#Intelligence_Distance=(data.Intelligence-mean_intelligence)**2
#ic_intelligence=(Intelligence_Distance.sum()/len(Intelligence_Distance))**(1/2)
ic_pearson=ic_covariance/(ic_intelligence*ic_combat)




# --------------
#Code starts here
total_high=data['Total'].quantile(q=0.99)
#print(total_high)
super_best=data[data['Total']>total_high]
super_best_names=list(super_best['Name'])

print(super_best_names)
#print(super_best.head())


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3)=plt.subplots(1,3, figsize=(20,8))
ax_1.boxplot(super_best['Intelligence'])
ax_1.set(title='Intelligence')
ax_2.boxplot(super_best['Speed'])
ax_2.set(title='Speed')
ax_3.boxplot(super_best['Power'])
ax_3.set(title='Power')


