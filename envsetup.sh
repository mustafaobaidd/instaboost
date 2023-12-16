#!/bin/sh

echo "setting up python"

python -m venv .env
source .env/bin/activate
pip install instagrapi Pillow

echo "Done!"

echo "Exporting env variables"

export INSTAUSERNAME="insert username here"
echo $INSTAUSERNAME
export INSTAPASSWORD="insert password here"
echo $INSTAPASSWORD
echo "Done"
