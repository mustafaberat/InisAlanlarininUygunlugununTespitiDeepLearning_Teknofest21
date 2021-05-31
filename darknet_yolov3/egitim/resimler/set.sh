for i in *.txt;
do 
  sed -i 's/^8/0/g' $i
done
