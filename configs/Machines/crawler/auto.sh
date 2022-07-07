sleep 5
python3 main.py

sleep 5
echo "honey1" > /tmp/trigger.txt 
rsync /tmp/trigger.txt root@10.0.5.1:~trigger.txt

sleep 5
rsync -a ~/mysite_folder_name root@10.0.0.10:/var/www/html

sleep 5
echo "honey2" > /tmp/trigger.txt 
rsync /tmp/trigger.txt root@10.0.5.1:~trigger.txt

sleep 5
rsync -a ~/mysite_folder_name root@10.0.0.10:/var/www/html

sleep 5
echo "legit" > /tmp/trigger.txt 
rsync /tmp/trigger.txt root@10.0.5.1:~trigger.txt