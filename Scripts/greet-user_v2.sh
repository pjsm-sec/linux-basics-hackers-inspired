#! /bin/bash

# This script is inspired by an example from the book Linux Basics for Hackers

echo "Hi! What's your name?"

read name

echo "And how old are you?"

read age

if [ $age -lt 12 ]; then 
echo "Hey, $name this is not Minecraft. Don't use your parents' laptop without permission!"
elif [ $age -ge 12 ] && [ $age -lt 18 ]; then
echo "Welcome to scripting, $name!"
elif [ $age -ge 18 ] && [ $age -lt 25 ]; then
echo "Hello, $name!"
else
echo "It's never too late to learn how to script!"
fi