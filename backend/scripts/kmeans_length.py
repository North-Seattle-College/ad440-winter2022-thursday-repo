from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import json
import pandas as pd
import numpy as np
import sys
import os

MAX_CLUSTERS = 10
INERTIA_THRESHOLD = 1


def get_conversation_length(sentences: dict) -> list:
    out = []
    for key in sentences:
        out.append([len(key), 0])
    return out


def get_cluster_count(conversations: list) -> int:
    inertia_values = []
    for i in range(1, MAX_CLUSTERS + 1):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(conversations)
        inertia_values.append(kmeans.inertia_)

    counter = 0
    previous_value = inertia_values[0]

    for c, value in enumerate(inertia_values):
        if previous_value > value > INERTIA_THRESHOLD:
            previous_value = value
            counter = c

    return counter + 1


def check_response_count(sentences: list):
    if len(sentences) < MAX_CLUSTERS:
        raise ValueError('Sentence count less than ' + str(MAX_CLUSTERS))


def get_kmean_summary(conversation_length: list, kmeans_labels: list) -> pd.DataFrame:
    df = pd.DataFrame({'conversation_length': [i[0] for i in conversation_length], 'cluster_id': kmeans_labels})
    conversation_length = df.pivot_table(values='conversation_length', index='cluster_id', aggfunc=np.average)[
        'conversation_length']
    table = df.pivot_table(values='conversation_length', index='cluster_id', aggfunc=np.count_nonzero)
    table['length'] = conversation_length
    table.columns = ['count', 'length']

    return table


def output_plot(df: pd.DataFrame):
    fig, ax = plt.subplots()
    ax.bar(df['length'], df['count'])
    ax.set_title('Conversation Clusters Length and Count')
    ax.set_ylabel('Count')
    ax.set_xlabel('Avg Length of Conversation (response & reply)')
    plt.savefig('k_means_plot.png')


def get_filename_from_input_args(args: list) -> str:
    files_in_dir = os.listdir(os.getcwd())

    if len(args) < 2:
        raise FileNotFoundError('Need to input file, e.g. run "python file.json"')
    elif args[1] is None or args[1] == '':
        raise ValueError('Input empty filename')
    elif args[1] not in files_in_dir:
        raise FileNotFoundError('File not found')

    return args[1]


def main():
    # Get filename and read JSON object
    filename = get_filename_from_input_args(sys.argv)
    conversations = json.load(open(filename))

    # Calculate conversation lengths
    conversation_length = get_conversation_length(conversations)
    check_response_count(conversations)

    # Get clusters
    number_clusters = get_cluster_count(conversation_length)
    kmeans = KMeans(n_clusters=number_clusters)
    kmeans.fit(conversation_length)

    # Generate summary table
    table = get_kmean_summary(conversation_length, kmeans.labels_)

    # Generate plot
    output_plot(table)


if __name__ == '__main__':
    main()
