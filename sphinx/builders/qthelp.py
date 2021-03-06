"""
    sphinx.builders.qthelp
    ~~~~~~~~~~~~~~~~~~~~~~

    Build input files for the Qt collection generator.

    :copyright: Copyright 2007-2019 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import warnings

from sphinxcontrib.qthelp import QtHelpBuilder, render_file

import sphinx
from sphinx.deprecation import RemovedInSphinx40Warning, deprecated_alias

if False:
    # For type annotation
    from typing import Any, Dict  # NOQA
    from sphinx.application import Sphinx  # NOQA


deprecated_alias('sphinx.builders.qthelp',
                 {
                     'render_file': render_file,
                     'QtHelpBuilder': QtHelpBuilder,
                 },
                 RemovedInSphinx40Warning)


def setup(app):
    # type: (Sphinx) -> Dict[str, Any]
    warnings.warn('sphinx.builders.qthelp has been moved to sphinxcontrib-qthelp.',
                  RemovedInSphinx40Warning)

    app.setup_extension('sphinxcontrib.qthelp')

    return {
        'version': sphinx.__display_version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
