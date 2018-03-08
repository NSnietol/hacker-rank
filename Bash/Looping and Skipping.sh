##Your task is to use for loops to display only odd natural numbers from 1 to 99
##Input Format ->There is no input.

X=1
while [ $X -le 99 ]
do
	echo $X
	X=$((X+2))
done