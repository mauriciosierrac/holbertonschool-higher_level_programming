#!/bin/bash
# this script capture the length of content from body msg
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
