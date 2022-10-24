#!/bin/bash

find . -type f | awk -F. '!a[$NF]++{print $NF}'
