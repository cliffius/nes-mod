FILEPATH=$3
FILENAME=$(basename "${FILEPATH}")
GAMENAME=${FILENAME%% (*}

# pass (1) system name, (2) clean game name, (3) original file name
# append '&' to let script run in the background
python /opt/retropie/configs/all/sendToLCD.py "$1" "$GAMENAME" "$FILENAME" &
