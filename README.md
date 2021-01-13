<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Extracting emotion through Machine Learning
*Anna Fonte Farré*

*Data Analytics, Barcelona October 2020*

## Table of contents
- [Project Description](#project-description)
- [Database](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
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
[Slides](https://docs.google.com/presentation/d/10LCIiAuPLG4-P7wrC38O9okiwDCNUKRk8AQqAoWBjno/edit?usp=sharing)  
[Trello](https://trello.com/b/SHjpqP3b/finalproject)  
