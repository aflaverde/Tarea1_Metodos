##PUNTO 1 Bash
##ANDRES FELIPE LAVERDE MARTINEZ
mkdir Temperaturas
cd Temperaturas
wget https://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt
wget https://raw.githubusercontent.com/aflaverde/Tarea1_Metodos/master/tempdata.txt

awk '{if($2<-30 && length($2)!=0 || ($3<-30 && length($3)!=0) || ($4<-30 && length($4)!=0) || ($5<-30 && length($5)!=0) || ($6<-30 && length($6)!=0) || ($7<-30 && length($7)!=0) || ($8<-30 && length($8)!=0) || ($9<-30 && length($9)!=0) || ($10<-30 && length($10)!=0) || ($11<-30 && length($11)!=0) || ($12<-30 && length($12)!=0) || ($13<-30 && length($13)!=0)) print $1}' tempdata.txt > menorque30.txt

awk '{if($2<-6 && length($2)!=0 || ($3<-6 && length($3)!=0) || ($4<-6 && length($4)!=0) || ($5<-6 && length($5)!=0) || ($6<-6 && length($6)!=0) || ($7<-6 && length($7)!=0) || ($8<-6 && length($8)!=0) || ($9<-6 && length($9)!=0) || ($10<-6 && length($10)!=0) || ($11<-6 && length($11)!=0) || ($12<-6 && length($12)!=0) || ($13<-6 && length($13)!=0)) print $1}' tempdata.txt > menorque6.txt

awk '{print $7}' tempdata.txt > junio.txt

awk '{if($14>-15) print $1}' tempdata.txt

rm tempdata.txt
##ANDRES FELIPE LAVERDE MARTINEZ
