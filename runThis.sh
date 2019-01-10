
cd /home/richard/Desktop/iiotstream/tools/
cp csv_grepper.sh data/
sh get.sh 2 
cd data
sh csv_grepper.sh reflowoven_vaf out.csv

cd /home/richard/Desktop/iiotstream/streaming/RF

python3 stateGen.py /home/richard/Desktop/iiotstream/tools/data/out_reflowoven_vaf.csv

#rm -R /home/richard/Desktop/newIoT/tools/data/*

cd /home/richard/Desktop/iiotstream/streaming
#echo "Completed RF state generation.."



