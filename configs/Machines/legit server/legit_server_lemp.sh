#source: https://www.tecmint.com/install-lemp-with-phpmyadmin-in-ubuntu-20-04/
#update ubuntu
sudo apt update

#install nginx
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx 

#install php (check version if gets error)
sudo apt install php php-mysql php-fpm -y
sudo systemctl start php8.1-fpm
$ sudo systemctl enable php8.1-fpm

#install phpmyadmin (ESC (for nginx)-> yes -> set pass)
sudo apt install phpmyadmin

#install mariadb
sudo apt install mariadb-server mariadb-client -y
sudo systemctl start mariadb
sudo systemctl enable mariadb
#enter->all y
sudo mysql_secure_installation
