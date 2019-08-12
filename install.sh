RSA="\033[31m"
YSA="\033[1;93m"
CEA="\033[0m"
WHS="\033[0;97m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
    echo -e ""$RSA"[-]"$WHS" [Errno 1] Failed to copy files: Operation not permitted"$CEA""
    exit
exit
fi

if [[ -d ~/GeoSpy ]]
then
cd ~/GeoSpy
{
cp bin/GeoSpy /usr/local/bin
chmod +x /usr/local/bin/GeoSpy
cp bin/GeoSpy /bin
chmod +x /bin/GeoSpy
} &> /dev/null
else
cd ~
{
git clone https://github.com/entynetproject/GeoSpy.git
cd  ~/GeoSpy
cp bin/GeoSpy /usr/local/bin
chmod +x /usr/local/bin/GeoSpy
cp bin/GeoSpy /bin
chmod +x /bin/GeoSpy
} &> /dev/null
fi
