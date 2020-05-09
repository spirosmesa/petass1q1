#! /bin/bash
#calls the shared... .py script in order to post a message on the mix,
#then downloads the logs in dir ./logs, 
#names them appropriately(entryLog1.txt, exitLog1.txt etc)
#counts the input messages, the output messages and then just outputs everything#on the screen for study 
port=$1

for i in $(seq 1 40); do
python3 shared*.py $i $port
wget -O ./logs/entry$i.txt https://pets.ewi.utwente.nl/log/16-T6Kf9FAyXasdNBOZPU+drvU82httJ93QUDyJL+0ynX0=/entry.txt

wget -O ./logs/exit$i.txt https://pets.ewi.utwente.nl/log/16-T6Kf9FAyXasdNBOZPU+drvU82httJ93QUDyJL+0ynX0=/exit.txt
done

