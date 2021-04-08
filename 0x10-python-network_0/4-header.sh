#!/bin/bash
# This script sends a GET request to the URL and display body response
curl -s GET -H 'X-holbertonSchool-User-Id: 98' "$1" ; echo ""
