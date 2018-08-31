##PUNTO 1
mkdir Temperaturas
cd Temperaturas
wget https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt
awk '{if($2<-30 || $3<-30 || $4<-30 || $5<-30 || $6<-30 || $7<-30 || $8<-30 || $9<-30 || $10<-30 || $11<-30 || $12<-30 || $13<-30) print $1}' tempdata.txt > menorque30.txt



##f
awk '{print $7}' tempdata.txt > junio.txt
##g
awk '{if($14>-15) print $1}' tempdata.txt
