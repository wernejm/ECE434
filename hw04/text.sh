# Here's how to use imagemagick to display text
# Make a blank image
SIZE=240x240
TMP_FILE=/tmp/frame.png
#TMP_FILE=~/ECE434_repo/hw04/boris.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
      -size $SIZE \
      label:'ImageMagick\nJames Werne' \
      -draw "text 0,200 'Bottom of Display'" \
      magick display boris.jpg
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

# convert -list font
