# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
# License: MIT
# Change for CudaLint: Alexey T.

from cuda_lint import Linter, util


class JSL(Linter):
    """Provides an interface to the jsl executable."""

    syntax = 'JavaScript'
    cmd = 'jsl -stdin -nologo -nosummary'

    version_args = ''
    version_re = r'^JavaScript Lint (?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.3.0, < 0.4.0'
    regex = r'''(?xi)
        # First line is (lineno): type: error message
        ^\((?P<line>\d+)\):.*?(?:(?P<warning>warning)|(?P<error>error)):\s*(?P<message>.+)$\r?\n

        # Second line is the line of code
        ^.*$\r?\n

        # Third line is a caret pointing to the position of the error
        ^(?P<col>[^\^]*)\^
    '''
    multiline = True
    error_stream = util.STREAM_STDOUT
    defaults = {
        '-conf:': None
    }
    selectors = {
        'html': 'source.js.embedded.html'
    }
