# Fuzzy Auto Complete Words
This Project about suggesting Auto Complete word based on Ranking of the words specified in the dataset.
To start with need to install django and the libraries used in the projects.

Please follow the link for Django installation Steps:
https://docs.djangoproject.com/en/2.2/topics/install/

Here i've used the dataset of csv file. For the file reading purpose used pandas.
To install pandas run : pip install pandas
(To read .tsv file for dataset, add the sep= '\t' in pandas csv read method)

//Begin with Project Demo:
On successful running of Djnago project, hit the ur : http://127.0.0.1:8000/ , which lands on the UI for user search of word.

User Can enter a word to search, on entering each key, it shows the suggested list of auto complete words. On the list user can select the words.

On clicking of Submit button, return the response showing the words based on the ranks.
