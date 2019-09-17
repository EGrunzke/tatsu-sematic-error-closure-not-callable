from gen.bug_parser import BugParser
from gen.bug_model import BugModelBuilderSemantics
import tatsu


if __name__ == '__main__':
    text = "(test)"

    # Works
    with open("bug.peg") as file:
        grammar = file.read()
        tatsu.compile(grammar).parse(text)

    # Works
    parser = BugParser()
    parser.parse(text)

    # Fails
    semantics = BugModelBuilderSemantics()
    parser.parse(text, semantics=semantics)
