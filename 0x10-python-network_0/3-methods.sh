#!/bin/bash
# This script show all Http methods the server will accept
curl -sI "$1" | grep "Allow: "
