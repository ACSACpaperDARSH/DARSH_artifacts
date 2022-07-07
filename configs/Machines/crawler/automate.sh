sleep 10
python3 main.py

# for scp without pass
# configure /etc/ssh/sshd_config ->
#
# PasswordAuthentication no
# ChallengeResponseAuthentication no
# UsePAM no
#
# then do ->
# sudo systemctl restart ssh
# sudo systemctl restart sshd

sleep 30
scp -r ~/mysite_folder_name root@10.0.0.10:/var/www/html

sleep 30
scp -r ~/mysite_folder_name root@10.0.0.10:/var/www/html