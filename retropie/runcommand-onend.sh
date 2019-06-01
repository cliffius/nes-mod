# reset screen
python /opt/retropie/configs/all/sendToLCD.py "END" "END"

# calculate timestamp
FILEPATH=$3
FILENAME=$(basename "${FILEPATH}")
GAMENAME=${FILENAME%% (*}

START=$(cat "/home/pi/RetroPie-Save/${GAMENAME}.log")
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "$DIFF ($(date +%x_%H:%M:%S))" >> "/home/pi/RetroPie-Save/${GAMENAME}-time.log"
rm "/home/pi/RetroPie-Save/${GAMENAME}.log"

# backup save file
SAVELOC="${FILEPATH%/*}/saves"
FILENAME_NOEXT=${FILENAME%.*}
SAVEFILE="/home/pi/RetroPie-Save/${FILENAME_NOEXT}.srm"
STATEFILE="/home/pi/RetroPie-Save/${FILENAME_NOEXT}.state"

if test -f "$SAVEFILE"; then
   # -v is verbose, -p preserves file attributes
   echo $SAVEFILE
   cp -v -p $SAVEFILE $SAVELOC
fi

# backup state files
for i in {0..9}
do
   if [ $i = 0 ]
   then
      if test -f "$STATEFILE"; then
         echo $STATEFILE
         cp -v -p $STATEFILE $SAVELOC
   else
      STATEFILE_TEMP="$STATEFILE$i"
      if test -f "$STATEFILE_TEMP"; then
         echo $STATEFILE_TEMP
         cp -v -p $STATEFILE_TEMP $SAVELOC
   fi
done
