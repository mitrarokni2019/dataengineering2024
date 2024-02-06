import matplotlib.pyplot as plt

# Initialize a dictionary to store letter counts
letter_counts = {}

# Read the letter counts file
with open('letter_counts.txt', 'r') as file:
    for line in file:
        letter, count = line.strip().split()
        # Only include alphabetic characters
        if letter.isalpha():
            letter_counts[letter] = int(count)

# Sort the counts by letter
letters = sorted(letter_counts.keys())
counts = [letter_counts[letter] for letter in letters]

# Create a bar chart
plt.figure(figsize=(10, 8))
plt.bar(letters, counts, color='skyblue')
plt.xlabel('Letters')
plt.ylabel('Counts')
plt.title('Letter Counts from Hadoop Output')
plt.savefig('letter_counts_plot.png')
plt.close()
