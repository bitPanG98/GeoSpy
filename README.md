Geolocation Spy (GeoSpy)
========

```
  _______             ______             
 / ______)           / _____)            
| |   ___ _____  ___( (____  ____  _   _ 
| |  (_  | ___ |/ _ \\____ \|  _ \| | | |
| |____) | ____| |_| |____) ) |_| | |_| |
 \______/|_____)\___(______/|  __/ \__  |
                            |_|   (____/ 
```

---
GeoSpy is an **OSINT** analysis and research tool, which allows people to track and execute intelligent **social engineering** attacks in real time. It was created with the aim of teaching the world how large Internet companies could obtain **confidential information** such as the status of sessions of their websites or services and control their users through their browser, without their knowlege, but It evolves with the aim of helping **government** organizations, companies and **researchers** to track the cybercriminals.

***

Some benefits
-----------
* **LOCATOR OPTIMIZATION** Trace the path between you and the target you're tracking. Each time you make a move, the path will be updated, the location of the target is obtained silently through a bypass made in the browsers, allowing you to skip the location request on the victim's side, and at the same time maintain a precision of **99%** in the locator.

* **APPROACH** When you're close to the target, GeoSpy will tell you.

* **REST API** Generates an API (random or custom), and through this you can control and monitor other Web sites on the Internet remotely, getting the traffic of all visitors.

* **PROCESS HOOKS** Manages social engineering attacks or processes in the target's browser.
    
* **SEVERAL** You can issue a phishing attack of any domain or service in real time as well as send malicious files to compromise the device of a target.
    
* **INJECT JS** You keep the JavaScript code running free in real time, so you can manage the execution of a **keylogger** or your own custom functions in JS which will be reflected in the target's browser.
    
* **SPEECH** A process of audio creation is maintained which is played in the browser of the target, by means of this you can execute personalized messages in different voices with languages in Spanish and English.

* **PUBLIC NETWORK TUNNEL** GeoSpy has its own **API** that is linked to **ngrok.com** to allow the automatic management of public network tunnels; So you can publish the content of your GeoSpy server which is executed locally to the Internet, to manage hooks or public attacks.

* **CLICK ATTACK TO GET CREDENTIALS** Automatically obtains the target credentials, recognizing your connection availability on a social network or Internet service.

* **NETWORK** You can get information about the user's network.

* **SPEED** Viewing the target's network speed. (Ping, download, upload, type connection)

* **HOSTS OR DEVICES** Here you can get a scan of all the devices that are connected in the target network automatically.

* **PROFILE** Brief summary of the target's behavior and important additional information about your device.

***

30 sessions recognition
-------
Session recognition is one of GeoSpy most interesting attractions, since you as a researcher can know remotely what service the target is connected to.

* **USABILITY** You can delete logs and view alerts for each process or action you run against each target.

***

GeoSpy in work
-------

* **INSTALLATION**

```
cd GeoSpy
chmod +x install.sh
./install.sh
```

* **EXECUTION**

```
geospy --url http://example.com --port 8080
```

* **USAGE**

```
usage: geospy -u <URL> -p <PORT> [-h] [-v] [-u URL] [-p PORT]
                                 [-ak ACCESSKEY] [-l LOCAL] [-n]
                                 [-ic INJC] [-ud]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -u URL, --url URL     Put the web page url to clone.
  -p PORT, --port PORT  Insert your port.
  -ak ACCESSKEY, --accesskey ACCESSKEY
                        Insert your custom key access.
  -l LOCAL, --local LOCAL
                        Insert your home file.
  -n, --ngrok           Insert your ngrok Authtoken.
  -ic INJC, --injectcode INJC
                        Insert your custom REST API path.
  -ud UPDATE, --update UPDATE
                        Update GeoSpy to the latest version.
```

   **--url**  In this option you add the URL you want to clone, which works as a decoy.

   **--port**  Here you insert the port, where you are going to run the  **GeoSpy server**.

   **--accesskey**  You enter a custom key for the  **GeoSpy panel**, if you do not insert it will generate an  **automatic key**.

   **--injectcode**  GeoSpy contains a  **REST API**  to play anywhere, using this option you can customize the name of the file to include, if it does not, generates a random name allusive to a token.

   **--local**  Using this option you can call a local **HTML file**, this is the replacement of the  **--url**  option made to run a local lure in GeoSpy.

   **--ngrok**  In this option you can enter a token, to run at the time of a process. This would replace the token saved in configurations.

   **--version**  You can see the version number of GeoSpy.

   **--update**  Option used to upgrade to the latest version of **GeoSpy**.

   **--help**  It is used to see all the above options, from the executable.

***

Disclaimer
-------
This tool has been published educational purposes. It is intended to teach people how bad guys could track them, monitor them or obtain information from their credentials, we are not responsible for the use or the scope that someone may have through this project.
We are totally convinced that if we teach how vulnerable things really are, we can make the Internet a safer place.

***

GeoSpy apache license
-------

    Copyright (C) 2016 - 2018 Entynetproject, Inc.

    Licensed under the Apache License, Version 2.0 (the "License"); you may not
    use the software except in compliance with the License.

    You may obtain a copy of the License at:

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations under
    the License.

    Disclaimer:
    This tool has been published educational purposes. It is intended to teach 
    people how bad guys could track them, monitor them or obtain information from 
    their credentials, we are not responsible for the use or the scope that someone 
    may have through this project. We are totally convinced that if we teach how 
    vulnerable things really are, we can make the Internet a safer place.

***

Thats all!
-------
