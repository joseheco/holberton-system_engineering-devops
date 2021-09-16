# header response, but with Puppet.

exec { 'setting up nginx':
  command  => 'sudo apt-get -y update;
                sudo apt-get -y upgrade;
                sudo apt-get -y install nginx;
                echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html;
                sudo sed -i "/server_name _;/ a \\\trewrite ^/redirect_me https://www.google.com permanent;" /etc/nginx/sites-available/default
                sudo sed -i "11i \\\t add_header X-Served-By $HOSTNAME always;\n" /etc/nginx/nginx.conf;
                sudo service nginx restart',
  provider => shell,
}
