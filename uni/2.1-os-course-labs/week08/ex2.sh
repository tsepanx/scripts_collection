#!/bin/bash

gcc -w ex2.c
./a.out &

vmstat 1
