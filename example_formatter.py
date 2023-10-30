"""An example plugin formatter for Pygments."""

from pygments.formatter import Formatter

class ExampleFormatter(Formatter):
    # This should be the human-readable name of the format.
    name = "Pygments Plugin Example Format"

    # This is a list of names that can be used to select the formatter.
    # In this example, we can call the pygmentize command as
    #
    #   pygmentize -f example-format
    #
    # Also, doing
    #
    #   pygments.formatters.find_formatter_class("example-format")
    #
    # in Python will find the formatter class.
    aliases = ["example-format"]

    # This is a list of file patterns that the formatter will
    # typically be used to produce. In this example, calling
    #
    #   pygmentize -o out.exmplfmt
    #
    # will automatically select this formatter based on the output
    # file name. Similarly,
    #
    #   pygments.formatters.get_formatter_for_filename("out.exmplfmt")
    #
    # will return an instance of this formatter class.
    filenames = ["*.exmplfmt"]

    def format_unencoded(self, tokensource, out):
        # This formatter writes each token as [<color>]<string> .
        for ttype, value in tokensource:
            while not self.style.styles_token(ttype):
                ttype = ttype.parent
            color = self.style.style_for_token(ttype)['color']
            out.write("[" + (color or "black") + "]")
            out.write(value)
