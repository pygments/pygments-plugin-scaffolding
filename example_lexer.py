"""An example plugin lexer for Pygments."""

from pygments.lexer import RegexLexer
from pygments.token import Keyword, Text

class ExampleLexer(RegexLexer):
    # This should be the human-readable name of the language.  In this example,
    # doing
    #
    #   pygments.lexers.find_lexer_class("Pygments Plugin Example Language")
    #
    # will return the ExampleLexer class.
    name = "Pygments Plugin Example Language"

    # This is a list of names that can be used to select the language.
    # In this example, we can call the pygmentize command as
    #
    #   pygmentize -l example-lang
    #
    # Also, doing
    #
    #   pygments.lexers.find_lexer_class_by_name("example-lang")
    #
    # in Python will find the lexer class. This is what many documentation or
    # site generation tools implicitly do with code blocks, e.g., this in Sphinx
    # reST:
    #
    #   .. code-block:: example-lang
    #
    #      your code here
    #
    # or this in Markdown:
    #
    #   ```example-lang
    #   your code here
    #   ```
    #
    aliases = ["example-lang"]

    # This is a list of file patterns that will automatically be highlighted
    # with this lexer. In this example, calling
    #
    #   pygmentize file.exmpl
    #
    # will automatically highlight file.exmpl with this lexer, without needing
    # to pass `-l example-lang`. Similarly,
    #
    #   pygments.lexers.find_lexer_class_for_filename("file.exmpl")
    #
    # will return the ExampleLexer class.
    filenames = ["*.exmpl"]

    # This is a list of MIME types for the language. In this example,
    #
    #   pygments.lexers.get_lexer_for_mimetype("text/x-exmpl")
    #
    # will return the ExampleLexer class.
    mimetypes = ["text/x-exmpl"]

    # This lexer highlights lines that read "foo".
    tokens = {
        'root': [
            (r'foo\n', Keyword),
            (r'.*\n', Text),
        ]
    }
