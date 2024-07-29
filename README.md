# Interactly_task_Alok-Karn

## Code Documentation: Candidate Analysis with Sentence Transformers

**Task:** This Python script performs candidate analysis for a data science intern position using a pre-trained sentence transformer model.
I used Kaggle or Jupyter notebook for the process.

**Data Preprocessing:**

* **Data Source:** The script assumes a CSV file named "RecruterPilot candidate sample input dataset - Sheet1.csv" located in the `/kaggle/input/recruterpilot-candidate-sample` directory.
* **Minimal Preprocessing:** Due to the small dataset size (120 entries), extensive preprocessing wasn't necessary. However, the script removes basic punctuation (',', ';', and '.') from the combined text of "Job Skills", "Projects", and "Comments" columns.
* **Stop Word Removal:** The script uses NLTK to remove stop words (common, unimportant words) from the query text entered by the user.

**Vector Embedding:**

* **Sentence Transformer:** The script utilizes the pre-trained model "hkunlp/instructor-large" from Sentence Transformers. This model is specifically chosen for its ability to handle various domains, which is beneficial for candidate analysis tasks.
* **Encoding:** The script generates vector embeddings for both the candidate information (combined text) and the user-provided query. Each embedding represents the semantic meaning of the text in a high-dimensional space.

**Similarity Search:**

* **Query Processing:** The script prompts the user to enter a query string related to the desired candidate skills or experience.
* **Similarity Calculation:** It computes the cosine similarity between the query embedding and each candidate embedding. Cosine similarity reflects how similar the two texts are semantically.
* **Top N Retrieval:** The script retrieves and displays the top N candidates (specified by the user) with the highest similarity scores to the query.

**Output:**

* **Command Line Results:** The script displays the top N most relevant candidates based on the query using the command line interface.
* **Optional Excel Export:** The script additionally creates an Excel file named "TheResult.xlsx" containing the top N candidate information (excluding the embeddings) for further analysis.

**Additional Notes:**

* For larger datasets, consider using external databases like Elasticsearch or FAISS for efficient retrieval.
* Extensive data cleaning techniques might be required for bigger datasets with inconsistencies or noise.
* Alternative pre-trained models like "all-mpnet-base-v2" might perform differently depending on the specific domain and task.
* This script demonstrates a basic implementation. APIs and front-end frameworks can be integrated for a more user-friendly interface.
* OpenAI or huggingface API were not used because of small datasets and specific domain, however, for large real time data such API may be useful in query retrieval.
