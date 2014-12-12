## Licensed under the Apache License, Version 2.0 (the "License"); you may not
## use this file except in compliance with the License. You may obtain a copy of
## the License at
##
##   http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
## WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
## License for the specific language governing permissions and limitations under
## the License.

import datetime
import os
import re
import sys

sys.path.insert(0, os.path.abspath('../ext'))

extensions = ["sphinx.ext.todo", "sphinx.ext.extlinks", 'github',
              'httpdomain', 'configdomain']


nitpicky = True

version = '1.0'
release = '1.0.0'

# General information about the project.
project = u'rcouch'
copyright = u'2014, The refuge project'


highlight_language = "json"



primary_domain = "http"

pygments_style = "sphinx"

html_theme = "couchdb"

html_theme_path = ['../templates']

templates_path = ["../templates"]

html_static_path = ["../static"]

html_title = ' '.join([
    project,
    version,
    'Documentation'
])

html_style = "rtd.css"

html_logo = "../images/logo.png"

html_favicon = "../images/favicon.ico"

html_use_index = False

html_additional_pages = {
    'download': 'pages/download.html',
    'index': 'pages/index.html'
}

html_context = {
    "ga_code": "UA-658988-6"
}

html_sidebars = {
    "**": [
        "searchbox.html",
        "localtoc.html",
        "relations.html",
        "utilities.html",
        "help.html",
        "tracking.html",
    ]
}

text_newlines = "native"

latex_documents = [(
    "contents",
    "CouchDB.tex",
    project,
    "",
    "manual",
    True
)]

latex_elements = {
    "papersize": "a4paper"
}

texinfo_documents = [(
    "contents",
    "CouchDB",
    project,
    "",
    "CouchDB",
    "The Apache CouchDB database",
    "Databases",
    True
)]

extlinks = {
        'issue': ('%s-%%s' % "http://", 'COUCHDB-'),
    'commit': ('https://git-wip-us.apache.org/repos/asf?p=couchdb.git;a=commit;h=%s', '#')
}

github_project = 'apache/couchdb'

html_context['git_branch'] = github_branch = '1.x.x'

github_docs_path = 'share/doc/src'

