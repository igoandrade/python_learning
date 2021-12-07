# ================== #
# Import Libraries 
# ================== #

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# ================== #
# Page Title
# ================== #

image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app cout the nucleotide composition of query DNA!

***
""")

# ================== #
# Input Text Box
# ================== #

st.header('Enter DNA sequence')

sequence_input = ">DNA Query\ncgggtcgactagcagaccgtaccagttagcagttatttcaacatcctggcaaggggatag\ngcagcattctagcattgagcctgaacgttgatgatgctcaatcgttacttccaaaacgcg\natttactgtccatgcactgttggagataggcattctgtacttctagatcggcgccgacca\ntaacatcacgaagctttagacggcctccttcgggagagatcaccctgccgagattgtgga\nctgactctcaataatgtttacaaggcaggcccaatacgtctgacgtcattctcttcgagt"

sequence = st.text_area("Sequence input:", sequence_input.upper(), height=200)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
***
""")

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# 1. Compute dicitionary
dna_nucleotides = {
    'A': 'adenine',
    'T': 'thymine',
    'G': 'guanine',
    'C': 'cytosine'
}

def dna_nucleotice_count(seq):
    d = {}
    for key in dna_nucleotides.keys():
        d[key] = seq.count(key)
    return d

X = dna_nucleotice_count(sequence)

X_label = list(X)
X_values = list(X.values())


# 1. Print result
st.subheader('1. Print text result')
for k, v in dna_nucleotides.items():
    st.write(f"There are {X[k]} {v} ({k}).")

# 2. Display dataframe
st.subheader('2. Display dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

# 3. Displau Bar Chart using Atair
st.subheader('3. Displau Bar Chart using Atair')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)

st.write(p)

