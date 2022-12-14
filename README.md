# Frequency of letter pairs (bigrams)
A simple Python script which analyses a text file and returns a heatmap plot of bigrams occurrence. 

<p align="center">
<img src="https://i.imgur.com/jEsizl9.png" width=35% height=35%>
</p>
  
## What it does
This project aims to analyze the frequency of letter pairs, also known as bigrams, in a given piece of text. The frequency of bigrams can be useful in various ways, such as identifying common patterns in language or analyzing the security of a cipher.

## How it works
To find the frequency of bigrams in a piece of text, the program first splits the text into individual letters. It then groups the letters into pairs and counts the number of occurrences of each pair. The program then outputs the bigrams and their corresponding frequencies in a table.

## Installation

#### - Install the required dependencies
```
pip install -r requirements.txt
```
#### - Place the desired text in 'sample_text.txt' (sample already included for testing)


#### - Run the Python script
```
python pair_frequency.py
```
## License
MIT License; please read the LICENSE file in this repository.
