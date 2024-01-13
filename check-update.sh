#!/bin/sh
# NOTE: github repository is not always synced to the latest version
curl -L "https://www.spinellis.gr/sw/textproc/bib2xhtml/" 2>/dev/null |sed -ne 's,.*bib2xhtml-v\(.*\).tar.gz.*,\1,p'
