import pandas as pd
import numpy as np
!pip install sentence_transformers
from sentence_transformers import SentenceTransformer
!pip install --upgrade pip 
!pip install nltk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
df=pd.read_csv('/kaggle/input/recruterpilot-candidate-sample/RecruterPilot candidate sample input dataset - Sheet1.csv')
hashmap={}
stoppers={',': 1, ';':2 , '.': 3}
for i in range(len(df)):
    txt=(df['Job Skills'][i]+df['Projects'][i]+df['Comments'][i])
    hashmap[i]=''.join([items for items in txt if items not in stoppers])
model=SentenceTransformer("hkunlp/instructor-large")
x=[]
for i in hashmap.values():
    x+=[model.encode(i)]
df['Embedding']=x
def query_to_embedding(query):
    words=word_tokenize(query)
    stop_words=set(stopwords.words('english'))
    q=[items for items in words if items.lower() not in stop_words]
    return model.encode(q)
def query_process(embd, df, top_n):
    embd1=query_to_embedding(embd)
    df['Similarity']=df['Embedding'].apply(lambda x: np.linalg.norm(embd1 - x))
    df_sorted=df.sort_values(by='Similarity', ascending= True)
    x=df_sorted.drop(['Embedding'], axis=1)
    return x
!pip install openpyxl
Query= str(input("Enter the query for the candidate analysis"))
top_n= input("Enter the number of candidates you want")
main_df=(query_process(Query, df, top_n))
for i in range(int(top_n)):
    print(main_df.iloc[i])
x=main_df.iloc[0:i]
len(x)
new=x.to_excel('TheResult.xlsx')
