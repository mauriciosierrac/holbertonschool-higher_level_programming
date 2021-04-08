#!/bin/bash
# This script send POST request to the passed, and display the body of the response
curl -s -X POST -d "email=hr@holbertonschool&subject=I will always be here for PLD" "$1"
