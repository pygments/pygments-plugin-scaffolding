# Pygments plugin examples

This repository contains an example of the project scaffolding needed to write a
plugin lexer/formatter/style/filter for the [Pygments](https://pygments.org)
syntax highlighter.

Roadmap:

```
.
├── example_filter.py    # An example filter
├── example_formatter.py # An example formatter
├── example_lexer.py     # An example lexer
├── example_style.py     # An example style
├── pyproject.toml       # The Python package metadata file
├── README.md            # You are here
└── test.exmpl           # A test file in the mockup language of the example lexer
```

To be usable, plugins must be installed. If you are running the `pygmentize`
command, you probably want to use a
[virtual environment](https://docs.python.org/3/library/venv.html)
to avoid installing packages globally. For example, here is how to create
a virtual environment and install this set of plugins into it:

```
python -m venv venv/
venv/bin/pip install . # install the project in current directory into the virtual environment
venv/bin/pygmentize ... # use the pygmentize command from the virtual environment
```

Alternatively, since this example uses the [Hatch](https://hatch.pypa.io)
tool, you may use

```
hatch run pygmentize ...
```

If you are using Pygments from Python, possibly through a tool like Sphinx,
mkdocs, etc., then you just need to install the plugin in the same environment
as the one where you installed Pygments.

If you want to distribute your plugin on PyPI, you should read the
[packaging user guide](https://packaging.python.org/en/latest/tutorials/packaging-projects).


#### License for this template

There isn't much copyrightable content here, but if you are worried about reuse:

Copyright (C) 2023 by Jean Abou Samra <jean@abou-samra.fr>

Permission to use, copy, modify, and/or distribute this software for any purpose
with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
THIS SOFTWARE.
