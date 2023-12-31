#!/usr/bin/python3

# doi --- DOI to Sci-Hub
# needed to set `sci` for sci-hub search engine 

import os
import re

fifo = open(os.getenv("QUTE_FIFO"), "w")

mode = os.getenv("QUTE_MODE")

text = None

if mode == "hints":
    text = os.getenv("QUTE_URL").strip()
elif mode == "command":
    text = os.getenv("QUTE_SELECTED_TEXT").strip()

# DOI syntax: https://www.doi.org/doi_handbook/2_Numbering.html#2.2.
#
# Note that this probably matches a subset of possible DOIs, as it
# seems that there’s no practical limitation on neither the length nor
# the contents of the DOI.  But IMHO this is a healthy subset.
doi_re = re.compile(
    # match possible URI prefix
    r"(?P<blah>((https?)?://)?doi\.org/)?"
    # match actual DOI
    r"(?P<meat>[a-zA-Z0-9\./\-_]+)"
)

match = doi_re.match(text)

if match is None:
    fifo.write(f"message-warning \"`{text}' is probably not a DOI, or update regexp\"")

else:
    doi = match['meat']
    fifo.write(f"open -t sci {doi}")

fifo.flush()
