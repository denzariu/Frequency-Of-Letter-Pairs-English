import pandas as pd
from matplotlib import pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 8,8
from heatmap import heatmap

# How big the boxes will look on the plot
scale_factor = 2

## Plot the data
def heatmap(x, y, size):
    fig, ax = plt.subplots()

    # Mapping from column names to integer coordinates
    x_labels = [v for v in x.unique()]
    y_labels = [v for v in y.unique()]
    x_to_num = {p[1]:p[0] for p in enumerate(x_labels)} 
    y_to_num = {p[1]:p[0] for p in enumerate(y_labels)} 
    
    size_scale = 100 * scale_factor
    ax.scatter(
        x=x.map(x_to_num), # Use mapping for x
        y=y.map(y_to_num), # Use mapping for y
        s=size * size_scale, # Vector of square sizes, proportional to size parameter
        marker='s' # Use square as scatterplot marker
    )
    
    # Show column labels on the axes
    ax.set_xticks([x_to_num[v] for v in x_labels])
    ax.set_xticklabels(x_labels, rotation=45, horizontalalignment='right')
    ax.set_yticks([y_to_num[v] for v in y_labels])
    ax.set_yticklabels(y_labels)
    ax.set_xlabel('Y - The second letter (probability)')
    ax.set_ylabel('X - The first letter (reference)')
    
    plt.show()

## Count every pair of letters (next to eachother) in the text
def next_letter_probability(text):
    frequency_of_pair = {}
    text_length = len(text)
    for index, letter in enumerate(text):
        if index + 1 == text_length:
            continue
        pair_of_letters = letter + text[index + 1]
        if pair_of_letters in frequency_of_pair:
            frequency_of_pair[pair_of_letters] += 1
        else:
            frequency_of_pair[pair_of_letters] = 1
    return frequency_of_pair

## Format the data, create the data object and call the plot function
def create_heatmap(frequency_of_pair):

    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    x   = [] # x   = a b c... a b c... a b c...
    y   = [] # y   = a a a... b b b... c c c...
    val = [] # val = frequency / maximum frequency found in the given text of an element
    
    # Format the X-axis
    for i in range(len(alph)):
        for letter in alph:
            x.append(letter)
    
    # Format the Y-axis
    for letter in alph:
        for i in range(len(alph)):
            y.append(letter)
    
    # Format the values for (X,Y)
    max_prob = max(frequency_of_pair.values())
    for index in range(len(x)):
        pair_of_letters = y[index] + x[index]
        if pair_of_letters in frequency_of_pair:
            val.append(frequency_of_pair[pair_of_letters] / max_prob)
        else:
            val.append(0)

    # Space character on the X & Y axis replaced by 'spc'
    for index in range(len(x)):
        if x[index] == ' ':
            x[index] = 'spc'
        if y[index] == ' ':
            y[index] = 'spc'

    # Create and populate a dataframe using previous data
    data = {}
    data['x']   = x
    data['y']   = y
    data['val'] = val
    data = pd.DataFrame(data)

    # Create the heatmap with the given data
    heatmap(
        data['x'],
        data['y'],
        data['val']
    )

## Main function - read, format and plot
if __name__ == "__main__":
    # Read the text
    with open('sample_text.txt', 'r') as myfile:
        text = myfile.read()
    ## Format the text
    text = text.lower()
    # Remove some of the unwanted / irrelevant characters from the text
    text_to_replace = ['!', '.', ',', '\'', '"', '@', ':', '+', '\\', '?', '#', '$', '&', '(', ')', '[', ']']
    for character in text_to_replace:
        text.replace(character, '')
    
    """
    TEST IF IT IS CORRECTLY FORMATTED:
    print(text)
    """
    
    pair_frequency = next_letter_probability(text)
    create_heatmap(pair_frequency)