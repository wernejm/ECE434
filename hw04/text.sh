# Here's how to use imagemagick to display text
# Make a blank image
# James Werne
SIZE=240x240		# edited dimensions to make rotated version legible
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
      -size $SIZE \
      label:'ImageMagick\nJames Werne' \
      -draw "text 0,200 'Hi Dr. Yoder!'" \
      $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE

# convert -list font
