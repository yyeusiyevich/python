"""
Module for preparing inverted indexes based on uploaded documents
"""
import json
import sys
import re
from typing import Dict, List
from argparse import ArgumentParser, FileType, ArgumentTypeError
from io import TextIOWrapper


DEFAULT_PATH_TO_STORE_INVERTED_INDEX = "inverted.index"
PATH_TO_STOP_WORDS = "stop_words_en.txt"

class EncodedFileType(FileType):
    """
    File encoder.
    """
    def __call__(self, string):
        # the special argument "-" means sys.std{in,out}
        if string == '-':
            if 'r' in self._mode:
                stdin = TextIOWrapper(sys.stdin.buffer, encoding=self._encoding)
                return stdin
            if 'w' in self._mode:
                stdout = TextIOWrapper(sys.stdout.buffer, encoding=self._encoding)
                return stdout
            msg = 'argument "-" with mode %r' % self._mode
            raise ValueError(msg)
        # all other arguments are used as file names
        try:
            return open(string, self._mode, self._bufsize, self._encoding,
                        self._errors)
        except OSError as exception:
            args = {'filename': string, 'error': exception}
            message = "can't open '%(filename)s': %(error)s"
            raise ArgumentTypeError(message % args)

    def print_encoder(self):
        """
        Printer of encoder.
        """
        print(self._encoding)


class InvertedIndex:
    """
    The inverted index is a dictionary where the keys are the terms and the values are the lists of document
    identifiers.
    """
    def __init__(self, words_ids: Dict[str, List[int]] = None):
        if words_ids:
            self.words_ids = words_ids
        else:
            self.words_ids = dict()

    def query(self, words: List[str]) -> List[int]:
        """
        Returns the list of relevant documents for the given query.
        Creates a set for each word in the query, containing the relevant documents for that word
        (or an empty set if the word is not in the index).
        Then finds the intersection of all these sets.
        """
        documents = [set(self.words_ids.get(word, [])) for word in words]
        result = set.intersection(*documents)
        return list(result)

    def dump(self, filepath: str) -> None:
        """
        Allow us to write inverted indexes documents to temporary directory or local storage
        :param filepath: path to file with documents
        :return: None
        """
        with open(filepath, 'w') as file:
            json.dump(self.words_ids, file)

    @classmethod
    def load(cls, filepath: str):
        """
        Allow us to upload inverted indexes from either temporary directory or local storage
        :param filepath: path to file with documents
        :return: InvertedIndex
        """
        with open(filepath) as file:
            index = json.load(file)
        return cls(index)


def load_documents(filepath: str) -> Dict[int, str]:
    """
    Allow us to upload documents from either tempopary directory or local storage
    :param filepath: path to file with documents
    :return: Dict[int, str]
    """
    with open(filepath, 'r', encoding='utf8') as dataset:
        documents = {}
        for line in dataset:
            doc_id, content = line.rstrip('\n').lower().split('\t', 1)
            documents[int(doc_id)] = content
    return documents


def build_inverted_index(documents: Dict[int, str]) -> InvertedIndex:
    """
    Builder of inverted indexes based on documents
    :param documents: dict with documents
    :return: InvertedIndex class.
    For each document in the input dictionary, the function tokenizes the content of the document into terms.
    Then removes duplicates from the list of terms and adds the document identifier to the posting list for each term.
    """
    inverted = InvertedIndex()
    # load stop_words file and process it
    with open(PATH_TO_STOP_WORDS, 'r', encoding='utf-8') as file_stop:
        stop_words = [stop_words.strip().lower() for stop_words in file_stop]
    for doc_id, content in documents.items():
        terms = re.split(r"\W+", content)
        filtered_terms = list(dict.fromkeys(terms))
        # remove stop words from terms
        for word in filtered_terms:
            if word not in stop_words:
                inverted.words_ids.setdefault(word, []).append(doc_id)
    return inverted


def callback_build(arguments) -> None:
    """
    Process build runner.
    """
    return process_build(arguments.dataset, arguments.output)


def process_build(dataset, output) -> None:
    """
    Function is responsible for running of a pipeline to load documents,
    build and save inverted index
    :param arguments: key/value pairs of arguments from 'build' subparser
    :return: None.
    """
    documents: Dict[int, str] = load_documents(dataset)
    inverted_index = build_inverted_index(documents)
    inverted_index.dump(output)


def callback_query(arguments) -> None:
    """
    Callback query runner.
    """
    process_query(arguments.query, arguments.index)


def process_query(queries, index) -> None:
    """
    Function is responsible for loading inverted indexes
    and printing document indexes for keywords from arguments.query
    :param arguments: key/value pairs of arguments from 'query' subparser
    :return: None.
    """
    inverted_index = InvertedIndex.load(index)
    for query in queries:
        print(query[0])
        if isinstance(query, str):
            query = query.strip().split()

        doc_indexes = ','.join(str(value) for value in inverted_index.query(query))
        print(doc_indexes)


def setup_subparsers(parser) -> None:
    """
    Initial subparsers with arguments.
    :param parser: Instance of ArgumentParser
    """
    subparser = parser.add_subparsers(dest='command')
    build_parser = subparser.add_parser(
        "build",
        help="this parser is need to load, build"
             " and save inverted index bases on documents"
    )
    build_parser.add_argument(
        '-d', '--dataset',
        required=True,
        help='You should specify path to file with documents. ',
    )
    build_parser.add_argument(
        '-o', '--output',
        default=DEFAULT_PATH_TO_STORE_INVERTED_INDEX,
        help='You should specify path to save inverted index. '
             'The default: %(default)s',
    )
    build_parser.set_defaults(callback=callback_build)

    query_parser = subparser.add_parser(
        "query",
        help="This parser is need to load and apply inverted index"
    )
    query_parser.add_argument(
        '--index',
        default=DEFAULT_PATH_TO_STORE_INVERTED_INDEX,
        help='specify the path where inverted indexes are. '
             'The default: %(default)s',
    )
    query_file_group = query_parser.add_mutually_exclusive_group(required=True)
    query_file_group.add_argument(
        '-q', '--query', dest='query',
        action='append',
        nargs="+",
        help='you can specify a sequence of queries to process them overall',
    )
    query_file_group.add_argument(
        '--query_from_file', dest='query',
        type=EncodedFileType("r", encoding='utf-8'),
        # default=TextIOWrapper(sys.stdin.buffer, encoding='utf-8'),
        help="query file to get queries for inverted index",
    )
    query_parser.set_defaults(callback=callback_query)


def main():
    """
    Starter of the pipeline.
    """
    parser = ArgumentParser(
        description="Inverted Index CLI is need to load, build,"
                    "process query inverted index"
    )
    setup_subparsers(parser)
    arguments = parser.parse_args()
    arguments.callback(arguments)


if __name__ == '__main__':
    main()
