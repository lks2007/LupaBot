#!/bin/bash
clear
echo '
  __  __  ____  _   _ _____ _______ ____  _____      _____ ______ _______      ________ _____  
 |  \/  |/ __ \| \ | |_   _|__   __/ __ \|  __ \    / ____|  ____|  __ \ \    / /  ____|  __ \ 
 | \  / | |  | |  \| | | |    | | | |  | | |__) |  | (___ | |__  | |__) \ \  / /| |__  | |__) |
 | |\/| | |  | | . ` | | |    | | | |  | |  _  /    \___ \|  __| |  _  / \ \/ / |  __| |  _  / 
 | |  | | |__| | |\  |_| |_   | | | |__| | | \ \    ____) | |____| | \ \  \  /  | |____| | \ \ 
 |_|  |_|\____/|_| \_|_____|  |_|  \____/|_|  \_\  |_____/|______|_|  \_\  \/   |______|_|  \_\
                                                                                               
                                                                                               
'

cd ..

if [[ $EUID -ne 0 ]]; then
   echo "$( tput setaf 1 )$(tput bold)This script must be run as root$(tput setaf 5)$(tput sgr0)";
   exit 1
fi

if [[ $1 == "-r" ]]; then

    echo -e ':: Research to restart tools...

Tools (1) Daphne\n'

    read  -s -n 1 -p ':: Restart tools [Y/n]' response
    if [[ $response == 'Y' ]] || [[ $response == '' ]]; then

        sh -c 'sudo systemctl daemon-reload; sudo systemctl restart daphne_lks.service' &> /dev/null
        sh -c 'python log/daphne_log.py -r' &> /dev/null

        echo -ne '\n\ndaphne                    [##############----------------------------------------------] 23%\r'
        sleep 0.5
        echo -ne 'daphne                    [##################################--------------------------] 57%\r'
        sleep 0.5
        echo -ne 'daphne                    [############################################################] 100%\r'
        echo -ne '\n'
    else
        exit 1
    fi
else
    echo -e ':: Research tools...

Tools (4) Redis Postgresql Nginx Daphne\n'

    read  -s -n 1 -p ':: Start-up tools [Y/n]' response

    if [[ $response == 'Y' ]] || [[ $response == '' ]]; then
        sh -c 'docker start postgresql-container eloquent_khorana' &> /dev/null

        echo -ne '\n\nredis                     [##################------------------------------------------] 30%\r'
        sleep 0.5
        echo -ne 'redis                     [########################################--------------------] 67%\r'
        sleep 0.5
        echo -ne 'redis                     [############################################################] 100%\r'
        echo -ne '\n'
        echo -ne 'postgresql                [########################------------------------------------] 40%\r'
        sleep 0.5
        echo -ne 'postgresql                [#####################################################-------] 89%\r'
        sleep 0.5
        echo -ne 'postgresql                [############################################################] 100%\r'
        echo -ne '\n'

        sh -c 'sudo systemctl start nginx' &> /dev/null

        echo -ne 'nginx                     [##############----------------------------------------------] 23%\r'
        sleep 0.5
        echo -ne 'nginx                     [##################################--------------------------] 57%\r'
        sleep 0.5
        echo -ne 'nginx                     [############################################################] 100%\r'
        echo -ne '\n'


        sh -c 'sudo systemctl daemon-reload; sudo systemctl start daphne_lks.service' &> /dev/null
        exec python log/daphne_log.py

        echo -ne 'daphne                    [##############----------------------------------------------] 23%\r'
        sleep 0.5
        echo -ne 'daphne                    [##################################--------------------------] 57%\r'
        sleep 0.5
        echo -ne 'daphne                    [############################################################] 100%\r'
        echo -ne '\n'

    else
        exit 1
    fi
fi