#source: https://www.tecmint.com/install-wordpress-with-nginx-in-ubuntu-20-04/

#download wordpress
wget -c http://wordpress.org/latest.tar.gz
tar -xzvf latest.tar.gz

#copy contents
sudo cp -R wordpress/ /var/www/html/mysite.com
sudo chown -R www-data:www-data /var/www/html/mysite.com
sudo chmod -R 775 /var/www/html/mysite.com
#remove contents
sudo rm -fr latest.tar.gz
sudo rm -fr wordpress/

#configure wordpress
sudo mv /var/www/html/mysite.com/wp-config-sample.php /var/www/html/mysite.com/wp-config.php

#copy configuration file (go back to repo)
sudo cp mysite.com.conf /etc/nginx/conf.d/

#remove the default
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/default

#create database,user,password
#run commands of "wordpress.sql"
#sudo mysql -u root -p 

#restart nginx
sudo nginx -t
sudo systemctl restart nginx