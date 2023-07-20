#!/usr/bin/env python
# coding: utf-8

# # PANDAS

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


df=pd.read_csv("C:\\Users\\jayde\\IPL Matches 2008-2020.csv")
data="C:\\Users\\jayde\\IPL Matches 2008-2020.csv"


# In[21]:


df


# In[ ]:





# # Data Analysis

# In[14]:


df=pd.read_excel("ipl.xlsx")
data="ipl.xlsx"
df


# In[19]:


type(df["date"])


# In[20]:


# DataFrame ma sauthee pahela "date" valee column ne parse_dates(" ") thee change karavee

x=pd.read_excel("ipl.xlsx", parse_dates=['date'])
x.head()


# In[21]:


type(df["date"])           # DataFrame ma sauthee pahela "date" valee column ne parse_dates(" ") thee change karavee


# In[22]:


y=x[x['date']>'2016-05-29 00:00:00']
y.head()


# In[ ]:





# #  Find info of DataFrame

# In[24]:


#  df.info
#  df.descibe
#  df.head()
#  df.tail
#  df.sample
#  nrows
#  skiprows
#  usecols[1,5,2]
#  index_col=2
#  header=10
#  header=None
#  names


# In[53]:


data.info()   # data ni info janavaa
              # data type= DataFrame
              # Range index= rows
              # total column
              # column name with detail


# In[55]:


data.describe()


# In[23]:


df.head()       # data ni top 5 vaalue bataave


# In[399]:


df.head(2)       # data ni top 2 value bataave


# In[400]:


df.tail()        # data ni last 5 value bataave


# In[23]:


# nrows
pd.read_excel(data, nrows=10)       # nrows=10 (first 10 rows aape)


# In[411]:


#skip rows

df = pd.read_excel(data, skiprows=[1,4,8,30,50]) # skiprows ma aapel rows DataFrame mathee skip thase
df


# In[ ]:


#print specific columns using usecol parameters
 
df = pd.read_csv(data, usecols=[0,3,5])      # usecols thee DataFrame mathee selected column male


# In[413]:


#use columns as a index

df = pd.read_excel(data, index_col=2)        #index_col=2("city") --> "city column"  index bane
df


# In[415]:


# make any rows as a header

df = pd.read_excel(data, header=25)        # 25 mee row header banee
df


# In[418]:


df = pd.read_excel(data, header=None)      # (header=None) thee column name nee badle index value aape
df


# In[423]:


df = pd.read_excel(data, names=["A","B","C","D","E","F","G","H","I"])     # LAST COLUMN THEE NAME AAPE
df


# In[ ]:





# # Handel Missing Value

# In[ ]:


# isnull
# notnull

# na_value

# dropna
# dropna(how="all")
# dropna(axis=1)
# drop_duplicates
 
# fillna(0)
# fillna(method="ffill")
# fillna(method="bfill")
# fillna(method="ffill"/"bfill", limit=1/2/3)

# interpolate
# interpolate("time")


# In[ ]:


# missing values saathe deal karavaa
# machine learning ma duplicate data thee algorithm ni efficiency ghate 6


# In[5]:


data=pd.read_excel("ipl.xlsx")
data.head()


# In[54]:


data.info()   # data ni info janavaa
              # data type= DataFrame
              # Range index= rows
              # total column
              # column name with detail


# ### isnull & notnull

# In[6]:


data.isnull()  # "null" value DataFrame ma check kare


# In[8]:


data.isnull().sum()    # every column ma rahel "null" value=data count kare


# In[9]:


data.isnull().sum().sum()   # DataFrame ma rahel "Total null" value=data count kare


# In[10]:


data.notnull()


# In[11]:


data.notnull().sum()    # every column ma rahel "notnull" value=data count kare


# In[12]:


data.notnull().sum().sum()  # DataFrame ma rahel Total "notnull" value=data count kare


# ### dropna

# In[ ]:


# DataFrame mathee "missing value" ne drop=remove karvaa useful


# In[13]:


data.dropna()    #DataFrame mathee null value valee rows remove kare


# In[19]:


data.shape


# In[14]:


data.dropna().shape  # here all rows have some null value so shape=(0,20)


# In[15]:


data.dropna(axis=1)  # null value column wisw check kare ane (null value valee column remove kare)


# In[17]:


data.dropna(axis=1).shape  # 20 mathee 10 column j bakee rahee


# In[16]:


data.dropna(how="all")  # je row ma badhee value "null" hoy tevee row j remove kare


# In[18]:


data.dropna(how="all").shape   # DataFrame ma aakhee row no data missing hoy tevee koi row nathee
                               #how="all" ---> row ma badhee column null hoy to tene remove kare


# In[20]:


data.shape


# In[21]:


data.dropna(how="any")  # je row ma ek pan null value hoy to te remove thase


# In[22]:


data.dropna(thresh=19)  # je row ma 19 ke tethee vadhu "notnull" value hoy tena sivaay nee row remove thase
                        # thresh=19 (notnull values>=19) tevee rows


# In[24]:


data.dropna(thresh=19).shape


# In[23]:


data.dropna(thresh=18)  # (notnull values>=18) hoy tevee rows


# In[25]:


data.dropna(thresh=18).shape


# In[ ]:





# ### fillna

# In[28]:


# missing value drop karavaathee important data pan remove thay 6
# aathee dropna ne badle fillna vadhu saaree method 6


# In[30]:


data.fillna(0)   # DataFrame ma null value "0" thee fill kare
                 # categorial data ma pan "0" aave aathee column wise fillna vadhu saaree method 6


# In[32]:


data.fillna(0, limit=2)     # limit=2 (column ma 2 thee vadhu null value fill no thay)
                            # missing value fill karavaa par limit muke
                            


# In[34]:


data.fillna({"id":1000,"city":"Bhuj","player_of_match":"Robinhood"}) 

 # dictionary ma aapel column name same nee value te column ma missing value ne replace karse


# In[35]:


data.fillna(method="ffill")   # missing data tenee uparanee column no data thee fill thase
                              # 1st row ma missing data hoy to te fill thase nahee


# In[41]:


data.fillna(method="bfill")   # missing data tenee nichenaa column no data thee fill thase
                              # last row ma missing data hoy to te fill thase nahee


# In[42]:


data.fillna(method="ffill", axis=1)   # missing data tenee left row no data thee fill thase
                                     # 1st column  ma missing data hoy to te fill thase nahee


# In[43]:


data.fillna(method="bfill", axis=1)   # missing data tenee right row no data thee fill thase
                                      # last column  ma missing data hoy to te fill thase nahee


# In[ ]:





# ### interpolate

# In[45]:


data.interpolate()    # interpolate missing data ne upper & lower value nee (mean) thee fill thase


# In[48]:


data.interpolate(type="time")  # "Time" base data hoy tyaare interpolate(type="time") best fill method 6


# In[ ]:





# ### drop_duplicates

# In[51]:


data.drop_duplicates(subset=["city"])    # "city" column ma rahel duplicates remove kare
                                         #  "keep=first" default hovathee only first row j baakee rahe
                                         #  "keep=last" aapvaathee DataFrame ma Duplicates data nee last row bakee rahe


# In[50]:


data.drop_duplicates(subset=["city"]).shape  # duplicate value remove thavaathee 32 rows rahee


# In[52]:


data.drop_duplicates(subset=["city","season"]).shape   # city & season bane "sathe" hoy teva duplicate remove kare


# In[ ]:





# ### row / column fetch karva

# In[66]:


df=pd.read_csv("facebook.csv")
data="facebook.csv"
df


# In[67]:


df["App"]


# In[68]:


df[["App","Category"]]


# In[ ]:





# In[69]:


data=pd.read_excel("ipl.xlsx")


# In[70]:


data["city"]  # koi particular column call karava


# In[71]:


type(data["city"] )   # DataFrame mathi koi particular "column" athava "ROW" fetch karavamaa aave to te Series bANE


# In[72]:


data[["team1","team2","winner"]]  # ek thi vadhare column call karava


# In[ ]:





# # row/column ne index value thee show karavaa

# In[15]:


data.iloc[0]  # data mathi row melavavaa
               # loc= label "id","season" thee call karay
               # iloc= index value thee call karay [0],[1:5],[1:3,4:6]


# In[16]:


data.iloc[0:4]  # data mathi ek thi vadhare row kadhava


# In[17]:


data.iloc[[1,4,8,45]]   # koi random row fetch karavaa


# In[18]:


data.iloc[:,[4,5,10]]  # 4,5,10 mee column data mathi fetch karavaa


# In[ ]:





# # masking operation

# In[19]:


mask=data["city"]=="Hyderabad"     #  masking =  fitering mate condtion use karavama aave
                                  


# In[20]:


mask                                #  answer boolian Series maLe 6
                                   # jene normal data ma covert karavaa masking karavu pade


# In[21]:


data[mask]         # jene normal data ma covert karavaa masking karavu pade


# In[22]:


data[mask].shape      # row=49 (ketala match thaya te bataave 6)  COUNT


# In[24]:


data[mask].shape[0]  # shape[0] row = tyaa ketala match thaya te bataave


# In[ ]:





# # value_count using function

# In[28]:


def get_city_match_count(city):
    mask=data["city"]==city             #  data scientist analysis mate function banavi mostly use kare 6
    return data[mask].shape[0]


# In[26]:


get_city_match_count("Rajkot")          # rajkot ma thayel match ni value aape 6


# In[27]:


get_city_match_count("Pune")            # pune ma thayel match ni value aape 6


# In[28]:


get_city_match_count("Hyderabad")       # hyderabad ma thayel match ni value aape 6


# In[ ]:





# ## value_count

# In[ ]:


#  value_count data categorise column mate use thay 6


# In[73]:


data.head()


# In[58]:


data["winner"]


# In[59]:


data["winner"].value_counts()  # column ni team ketala match haju sudheema jeetee 6 tenee value batave


# In[60]:


import matplotlib.pyplot as plt


# In[61]:


data["winner"].value_counts().plot(kind="bar")    #winner team na data parathee visualization mate plot function


# In[62]:


data["winner"].value_counts().head().plot(kind="bar")  # only top 5 value no chart melavavaa head() no use


# In[ ]:





# In[65]:


data.head()


# In[66]:


data["toss_decision"]


# In[67]:


data["toss_decision"].value_counts()   # filter karee toss_decision ne sub_class ma convert kare
                                        # toss_decision ek categorial column 6 (tema "field" ane "bat" category hovathee)


# In[68]:


data["toss_decision"].value_counts().plot()


# In[69]:


data["toss_decision"].value_counts().plot(kind="pie")      # toss_decision ne pie chart thee visualize kare
                                                           # category mate pie chart no use thay
                                                           # numeric value represent karava histogram use thay


# In[70]:


data["win_by_runs"].plot(kind="hist")


# In[71]:


###  Series    (DataFrame ni single column= Series)


# In[72]:


data["winner"].value_counts()      # Series ma left side=index & right side=value jova male 6
                                   # mumbai indians=index  , 92=value


# In[73]:


type(data["winner"].value_counts())   


# In[74]:


a=data["winner"].value_counts()


# In[75]:


a.values    # a Series ma rahel badhee value aapase


# In[76]:


a["Delhi Daredevils"]  # index call karavathee teni value male


# In[ ]:





# In[77]:


# mumbai indians naa badha match count karava


# In[78]:


data["team1"].value_counts()


# In[79]:


data["team2"].value_counts()


# In[80]:


# be Series ma "same index" hoy to tene aapasama add karee sakaay


# In[81]:


a=data["team1"].value_counts()+data["team2"].value_counts()

a


# In[ ]:





# ## value ne sort karavee

# In[76]:


a=data["winner"].value_counts()
a


# In[83]:


a.sort_values()   #default ASCENDING order ma j sort kare


# In[84]:


a.sort_values(ascending=False)  #ascending=False aapavathee Descending order ma sort thase


# In[89]:


a.sort_values().head(3) # sort karyaa baad top 3 jova mate


# In[ ]:





# In[86]:


data.head()


# In[317]:



data.sort_values("season").head()  #DataFrame "city" column mujab ascending way ma sort thai jase


# In[318]:


data.sort_values("season", ascending=False).head() ##DataFrame "city" column mujab descending way ma sort thai jase


# In[100]:


data.sort_values(["city", "date"])


# In[319]:


data.shape


# In[320]:


data.sort_values(["city", "date"]).shape


# In[ ]:





# ## darek IPL no winner gotvo

# In[107]:


# darek season no last match finale hoy
# ane last match=finale jeete te season no winner bane


# In[108]:


data.drop_duplicates("season")  #by default keep=first rakhe 6


# In[109]:


data.drop_duplicates("season").shape


# In[110]:


data.drop_duplicates("season",keep="last")   # season no last match 


# In[111]:


data.drop_duplicates("season")[["season","winner"]]      # data mathee season & winner kadhava


# In[112]:


data.drop_duplicates("season")[["season","winner"]].sort_values("season") # season wise sort karava


# In[ ]:





# In[ ]:





# ## groupby

# In[324]:


winner=data.groupby("winner")
winner


# In[325]:


winner.groups   # similar data ne group ma convert kare
                # dictionary return kare... jema value tenee id 6


# In[326]:


winner.get_group("Kolkata Knight Riders") #get_group thee groupby "winner=Kolkata Knight Riders" no DataFrame male


# In[328]:


season=data.groupby("season")
season


# In[118]:


season.sum()  ## DataFrame ma rahel numerical column ma "sum function" apply kare
               # win by run -- total 


# In[333]:


season.agg(["mean","sum","max","min"])  # numerical data na agg=min,max,mean,sum find kare


# In[119]:


season.sum().sum()  ## aakhee season no sum aape


# In[120]:


len(data)


# In[121]:


len(season)  # 637 row ne 10 group ma convert karee


# In[122]:


season.size()   # dar varse ramaayelee "IPL match" nee value aape


# In[123]:


season.size().sort_values(ascending=False)  # highest match kya saal maa ramaai te bataave


# In[124]:


season.size().sort_values(ascending=False).head(3)  # hihest mastch played (top 3 )


# In[125]:


season.first()  # dar varse first  "ipl match" nee value aape


# In[126]:


season.last()  # dar varse ramayelee last "ipl match" bataave (je "IPL finale" hase) ("finale winner= ipl winner")
               # IPL winner no data male


# In[ ]:





# # IPL TOP 5 Batsman

# In[129]:


data=pd.read_csv("deliveries.csv")


# In[130]:


data


# In[131]:


# ipl ma top 5 highest scorer batsman


# In[132]:


runs=data.groupby("batsman")
runs


# In[133]:


runs.get_group("V Kohli")   # virat kohli e ipl ma rameli "match" nu list


# In[134]:


runs.get_group("V Kohli").shape


# In[135]:


runs["batsman_runs"].sum()  # IPL ma player na total runs


# In[136]:


runs["batsman_runs"].sum().sort_values(ascending=False)  # IPl player list acording highest runs


# In[137]:


runs["batsman_runs"].sum().sort_values(ascending=False).head()   #top 5 player


# In[ ]:





# ## IPL ma 6? 4?

# In[138]:


mask=data["batsman_runs"]==4     #IPl ma 4
strike=data[mask]
strike.shape[0]


# In[139]:


mask=data["batsman_runs"]==6     #IPl ma 6
strike=data[mask]
strike.shape[0]


# In[140]:


mask=data["batsman_runs"]==3    #IPl ma 3
strike=data[mask]
strike.shape[0]


# In[ ]:





# In[142]:


strike.groupby("batsman")["batsman_runs"].count()  # batsman ketala 6 marela te bataave


# In[143]:


strike.groupby("batsman")["batsman_runs"].count().sort_values(ascending=False)  #highest 6  karnar player


# In[ ]:





# In[145]:


strike.groupby("batsman")["batsman_runs"].count().sort_values(ascending=False)  #highest 3 runs lenar   player


# In[ ]:





# ##  kohli e last 10 years ma kai team same highest run karya

# In[147]:


data["batsman"]=="V Kohli"


# In[148]:


kohli=data[data["batsman"]=="V Kohli"]


# In[149]:


kohli.groupby("bowling_team")["batsman_runs"].sum().sort_values(ascending=False).head(3)

# kohli e "Chennai Super Kings=706"     same highest runs karela 6


# In[ ]:





# ## highest runs by player agaist which team  "FUNCTION"

# In[151]:


def run_scored(batsman_name):
    kohli=data[data["batsman"]==batsman_name]
    return kohli.groupby("bowling_team")["batsman_runs"].sum().sort_values(ascending=False).head(3)
    
    


# In[152]:


run_scored("V Kohli")  #kohli highest runs=706 is against "Chennai Super Kings"


# In[153]:


run_scored("MS Dhoni") #MS DHONI  highest runs=608 is against "Royal Challengers Bangalore"


# In[154]:


run_scored("G Gambhir") # G Gambhir highest runs=671 is against "Kings XI Punjab"


# In[ ]:





# # isin()

# In[156]:


#  Most death striker (batsman runs*100)/over
# min 200 balls
# 16-20 over


# In[157]:


data=pd.read_csv("deliveries.csv")
data


# In[158]:


strike=data[data["over"]>15] # 16 thee 20 over


# In[159]:


data.groupby("batsman")["batsman_runs"].count()  # balls played by batsman


# In[160]:


strike.groupby("batsman")["batsman_runs"].count()  #data ni badle strike par groupby karavathee last 5 over ni strike rate malse


# In[161]:


a=strike.groupby("batsman")["batsman_runs"].count()


# In[162]:


a[a>200]  # 200 thee vadhu runs vala batsman


# In[163]:


a[a>200].index


# In[164]:


batsman_list=a[a>200].index.tolist()
batsman_list


# In[165]:


# run scored by all these 43 player
# balls played by these 43 batsman


# In[166]:


data["batsman"].isin(batsman_list)


# In[167]:


data[data["batsman"].isin(batsman_list)]


# In[168]:


finale=data[data["batsman"].isin(batsman_list)]


# In[169]:


balls=finale.groupby("batsman")["batsman_runs"].count()


# In[170]:


runs=finale.groupby("batsman")["batsman_runs"].sum()


# In[171]:


strike_rate=(runs*100)/(balls/6)


# In[172]:


strike_rate   # strike rate of batsman


# In[173]:


strike_rate.sort_values(ascending=False)  # strike rate of top batsman


# In[174]:





# ## Ipl ma lagela 6 nu list

# In[332]:


data.head()


# In[176]:


data["batsman_runs"]==6               # Ipl ma lagela 6 nu list
six=data[data["batsman_runs"]==6]       
six.head()


# In[177]:


six.shape   # ipl ma atyaar sudhee ma 6523 ((6)) lagya 


# In[ ]:





# # Pivot Table

# In[178]:


six.pivot_table(index="over",columns="batting_team",values="batsman_runs",aggfunc="count")  
# ipl nee badhee team e ketla 6 marelaa te batave


# In[179]:


pt=six.pivot_table(index="over",columns="batting_team",values="batsman_runs",aggfunc="count")  


# In[180]:


import seaborn as sns


# In[181]:


sns.heatmap(pt)


# In[ ]:





# # co relation function

# In[182]:



# machine learning ma useful 6
# two numeric values no relation aape


# In[183]:


match=pd.read_csv("matches.csv")


# In[184]:


match


# In[185]:


match.corr()   # only "numeric" column par j perform thaay
               # co-relation (+) or (-) jova male
               # 1 nee najik hoy tevee value mate co-relation strong manaay 6 (+) ane (-) banemaa
               # 0.5 ke tethee lesser value mate co-relation weak manaay 6
               


# In[186]:


sns.heatmap(match.corr())


# In[ ]:





# In[187]:


# Rename column
# csv import karva time j column nu name badalee sakaay
# repeatedly use thatee column ne easy rename aapavaa


# In[188]:


match


# In[189]:


match.rename(columns={"city":"place","date":"dom"})


# In[190]:


# set_index & reset_index


# In[191]:


data.head(2)


# In[192]:


data.set_index("match_id")  #column ne index banava


# In[ ]:





# # Replace 

# In[352]:


df


# In[354]:


df.replace("Ironman","bhoot")  # single str replacement


# In[356]:


df.replace(["tiger","Ironman"],["Iden","mnsw"])  # DataFrame ma multiple value ne replace karava


# In[357]:


df.replace(to_replace=[0,1,2,3,4,5,6,7,8,9,10],value=125) 


# In[360]:


df.replace(to_replace=[4642044,1245897,6306064],value=125)  #(index=0,2,4,5)


# In[362]:


df.replace({"RATING":9},456)


# In[364]:


df.replace("[A-Za-z]","!",regex=True)    # categorial data badalva  (regex=True) aapvu pade
                                         # numerical data mate regex nee jaroor nathee


# In[ ]:





# #  merge function

# In[ ]:


# symmetrical data merging (same no. of row/column,index)


# In[292]:


df1=pd.DataFrame({"ID":[1,2,3,4,5],"class":[11,22,33,44,55]}) # 
df1


# In[291]:


df2=pd.DataFrame({"ID":[1,2,3,4,5],"name":[11,22,33,44,55]})
df2


# In[293]:


pd.merge(df1,df2,on="ID")  # on="ID" (df1 ane df2 Dataframe "ID" common column thee merge thay)


# In[307]:


pd.merge(df1,df2,left_index=True,right_index=True)  # df1 ane df2 nee seprate "ID"=column jova male


# In[303]:


pd.merge(df1,df2,on="ID", how="inner")  # on="ID" (df1 ane df2 ma common data merge thase)


# In[ ]:





# In[ ]:


#  unsymmetrical data merging  (different no. of rows/column, index)


# In[312]:


df1=pd.DataFrame({"ID":[1,2,3,4,5],"class":[11,22,33,44,55]}) # 
df1


# In[295]:


df3=pd.DataFrame({"ID":[1,2,3,5],"name":["a","b","c","e"]})
df3


# In[296]:


pd.merge(df1,df3,on="ID",how="inner")  #(df1 ane df3 ma "common" data merge thase)


# In[297]:


pd.merge(df1,df3,on="ID",how="outer")  #(df1 ane df3 ma "tamaam" data merge thase)


# In[298]:


pd.merge(df1,df3,on="ID",how="left")  #(df1 ane df3 ma "left"=df1 no tamaam data consider thase)
                                      # merging ma df3 no data df1 mujab adjust thase 


# In[305]:


pd.merge(df1,df3,on="ID",how="right")  #(df1 ane df3 ma "right"=df3 no tamaam data consider thase)
                                       # merging ma df1 no data df3 mujab adjust thase 


# In[311]:


pd.merge(df1,df3,how="cross") # df1 ane df3 no data loop wise jova male


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




