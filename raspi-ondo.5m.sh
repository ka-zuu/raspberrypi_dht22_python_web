#!/bin/bash

curl http://raspi.local:8000/ |
awk NR==2
