<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Extracting emotion through Machine Learning
*Anna Fonte Farré*

<<<<<<< HEAD
*Data Analytics, Barcelona October 2020*

## Table of contents
- [Project Description](#project-description)
- [Database](#rules)
=======
*[Data Analytics FT, Barcelona & October 2020]*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
>>>>>>> 348778e947fbdda5069723fb16d59809b588abbb
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
<<<<<<< HEAD
Spotify is one of the major music streaming platforms, with over 191 million active users, 40 million songs, and 2 billion playlists. A key feature of Spotify is the song recommendations that populate your homepage, but in fact, every music streaming service has some kind of music recommendation algorithm. Each music service provider is competing to give their listeners the joy of discovering new music, and there are a wide array of algorithmic approaches companies are taking. 
This third project of the bootcamp got me familiar with Machine Learning, through the use of web scraping techniques, APIs and modelling methods such as the K-Means method. 

## Database
In order to create a large dataset to base the recommendations on, the Spotify API has been used in order to retreive data, covering the following parameters of the song: Title, URI, Artist, Popularity and its audio features (danceability, energy, key, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duratin in ms and time signature. 

## Workflow
* Web scraping the TripAdvisor website
![Flowchart of the program](/Images/workflow.png)

## Organization
The project has been outlined and organized through the tool Trello. For developing the workflow of the program, pencil and paper have been used. 

The repository containing the program contains a README file, a .gitignore file and the following folders:
* Notebooks: this folder contains four documents, including the web scraping process of the Hot 100 Billboard; the creation of the first prototype; the database creation and clustering process using spotify API and Spotipy library; and the final prototype of the program. 
* Datasets: this folder also includes four csv files, containing the data coming from the Hot 100 Billboard web scraping, the main playlist dataset with more than 50k songs retreived via Spotify API, and two datasets with the song features from the playlist datasets. 
* Images: the folder contais the image of the flowchart of the program. 

## Links
[Repository](https://github.com/annafonte/nlp-tripadvisor)
=======
The development of Web 2.0 has led to an important amount of user generated content online. Users are now free to express their opinions about products, places and events. This project is aimed at introducing sentiment analysis into touristic attractions. To begin with, reviews from Sagrada Família were collected using a TripAdvisor scraper. Afterwards, two sentiment labels were created: the human sentiment which is the rate of the reviewer; and the machine sentiment which is extracted from the library NLTK. After that, classification models are built so as to predict polarity sentiments. Finally, a subgroup discovery analysis was performed so as to extract valuable information about negative reviews.

## Questions & Hypotheses
The main objective of the project is creating a first attempt for Sentiment Analysis for tourist attractions, as mostly of the research has been only done in the hospitality industry.

## Dataset
As noted above, the data has been collected by scrapping TripAdvisor with a driver. Arround 55K opinions have been collected from 2010 to 2020. The main information that contains the dataset is related to the date of the visit, the location of the reviewer, the review title and the review body. 

## Workflow
- Firstly, some research was done in order to find interesting questions and get a solid background about the topic. 
- Then, data was collected using Selenium and ChromeDriver from TripAvisor website.
- For labelling the data, the human sentiment and machine sentiment approached were considered, as explained before. 
- Afterwards, the data cleaning and wrangling was performed, adapting all the features from the dataset and its types.
- To continue, some operations were in place in order to deal with the categorical features: the text was preprocessed in order to use the NLP methods. 
- Finally, analysis was conducted in order to find correlation between the two different label approaches and also to discover interesting patterns in the negative subgroup.

## Organization
All the steps of the project were organized with Trello (find the link attached below). 
Regarding the repository, it contains three main folders: the first one with the data used in the project and the second contains the notebooks for data collection, data cleaning, data analysis & data preprocessing and modelling. 

## Links
[Repository](https://github.com/annafonte/nlp-tripadvisor)  
>>>>>>> 348778e947fbdda5069723fb16d59809b588abbb
[Slides](https://docs.google.com/presentation/d/10LCIiAuPLG4-P7wrC38O9okiwDCNUKRk8AQqAoWBjno/edit?usp=sharing)  
[Trello](https://trello.com/b/SHjpqP3b/finalproject)  
