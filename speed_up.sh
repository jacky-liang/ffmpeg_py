INPUT_FILE=$1
OUTPUT_FILE=$2
INV_SPEED_FACTOR=$3

ffmpeg -i $1 -filter_complex "[0:v]setpts=$INV_SPEED_FACTOR*PTS[v]" -map "[v]" $2