#!/bin/bash
docker image history -H timeservice | grep -v \<missing\> | sort 
