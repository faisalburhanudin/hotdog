#!/bin/bash
docker run --rm -it -p 8888:8888 -p 6006:6006 -v `pwd`:/root/workspace -m 4g faisalburhanudin/dl bash
