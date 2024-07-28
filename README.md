# Interactly_task_Alok-Karn
The coding task given for data science intern position
The database setup was not necessary because the number of entries was 120, and for small data external db is not necessary. However, if there was a lot of data we would have to use elasticdb or FAISS or chroma;
The data is not much preprocessed because the data has multiple repeating names, but different email or skills. While it is crucial for a big data to be pre processed and do data wrangling, small data with mostly string based value may not need one.
Vector embedding was done using pre-trained model (hkunlp/instructor-large) from sentence transformer. One can use huggingface or openai api keys, however, sentence transformer is suitable in this case. Models like all-mpnet-base-v2 may not give higher accuracy in this case because it is a general purpose model whereas hkunlp/instructor-large is tuned for specific domains.
The query was easily prompted using command line. One can use API or front end frameworks for better UI UX.
