import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def load_data(filename: str) -> list:
    with open(filename) as f:
        return f.readlines()


def sentence_classification(sentence: str):
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)

    if ss['pos'] > 0.3 and ss['neg'] < 0.1:
        return 'Your comment is positive'
    elif ss['neg'] > 0.15:
        return 'Your comment is negative'
    else:
        return 'Your comment is neutral'


def select_analysis_file(arguments: list) -> str:
    for c, arg in enumerate(arguments):
        if 'filename' in arg:
            open(arguments[c + 1])
            return arguments[c + 1]
    raise ValueError('No filename provided')


def check_print_arg(arguments: list) -> bool:
    possible_print_args = ['-v', 'print', '-print', '-p']
    for arg in arguments:
        if arg in possible_print_args:
            return True
    return False


def main():
    input_args = sys.argv[1:]
    filename = select_analysis_file(input_args)
    will_print = check_print_arg(input_args)
    data = load_data(filename)
    print('Analysis Start')
    output = []
    for sentence in data:
        output.append((sentence.strip(), sentence_classification(sentence).strip()))
        if will_print:
            print(sentence.strip())
            print(sentence_classification(sentence).strip(), '\n')
    print('Analysis Complete')


if __name__ == '__main__':
    main()
