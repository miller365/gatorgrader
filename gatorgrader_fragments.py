"""Utility functions that count the contents of a file"""

from pathlib import Path
import re
import nltk

FILE_SEPARATOR = "/"

# References:
# https://stackoverflow.com/questions/18568105/how-match-a-paragraph-using-regex
# https://stackoverflow.com/questions/13531204/how-to-match-paragraphs-in-text-with-regx

PARAGRAH_RE = r'(.+?\n\n|.+?$)'
SECTION_MARKER = "#"


def get_paragraphs(contents, blank_replace=True):
    """Retrieves the paragraphs in the writing"""
    # use a replacement to handle a string with just spaces
    if blank_replace is True:
        contents = contents.replace(" ", "")
    pattern = re.compile(PARAGRAH_RE)
    paragraphs = pattern.findall(contents)
    matching_paragraphs = []
    # extract all of the section headers in markdown
    for paragraph in paragraphs:
        if paragraph.startswith(SECTION_MARKER) is False:
            matching_paragraphs.append(paragraph)
    return matching_paragraphs


def count_paragraphs(contents):
    """Counts the number of paragraphs in the writing"""
    replace_blank_inputs = True
    matching_paragraphs = get_paragraphs(contents, replace_blank_inputs)
    return len(matching_paragraphs)


def count_sentences(contents):
    """Counts the number of sentences in the writing"""
    replace_blank_inputs = False
    paragraphs = get_paragraphs(contents, replace_blank_inputs)
    print(paragraphs)
    sentence_counts = []
    for paragraph in paragraphs:
        paragraph = paragraph.replace("\n", "")
        sentences = nltk.sent_tokenize(paragraph)
        sentence_counts.append(len(sentences))
    return min(sentence_counts)


def count_specified_fragment(contents, fragment):
    """Counts the specified string fragment in the writing"""
    fragment_count = contents.count(fragment)
    return fragment_count


def specified_fragment_greater_than_count(given_file, containing_directory,
                                          chosen_fragment, expected_count,
                                          checking_function):
    """Determines if the fragment count is greater than expected"""
    file_fragment_count = count_fragments(given_file, containing_directory,
                                          chosen_fragment, checking_function)
    if file_fragment_count >= expected_count:
        return True
    return False


def count_fragments(given_file, containing_directory, chosen_fragment,
                    checking_function):
    """Counts fragments for the file in the directory and a fragment"""
    file_for_checking = Path(containing_directory + FILE_SEPARATOR +
                             given_file)
    file_contents_count = 0
    if file_for_checking.is_file():
        file_contents = file_for_checking.read_text()
        file_contents_count = checking_function(file_contents, chosen_fragment)
    return file_contents_count
