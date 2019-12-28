# Geolocation Spy (GeoSpy)

<h3 align="center"><img src="https://user-images.githubusercontent.com/54115104/65831192-89cc2880-e2bf-11e9-936c-792dcf56407c.png"></h3>
<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a> 
  <a href="https://github.com/entynetproject/geospy/releases">
    <img src="https://img.shields.io/github/release/entynetproject/geospy.svg">
  </a>
  <a href="https://github.com/entynetproject/geospy/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/geospy.svg">
  </a>
  <a href="https://github.com/entynetproject/geospy/wiki">
      <img src="https://img.shields.io/badge/wiki%20-geospy-lightgrey.svg">
 </a>
  <a href="https://twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
</p>

***

# About Geolocation Spy

    Geolocation Spy (GeoSpy) is an OSINT analysis and research tool that is used to track and execute 
    intelligent social engineering attacks in real time. It was created with the aim of teaching the world 
    show large Internet companies could obtain confidential information such as the status of sessions of their 
    websites or services and control their users through their browser, without their knowlege, but It evolves 
    with the aim of helping government organizations, companies and researchers to track the cybercriminals.

***

# Getting started

## GeoSpy installation

> cd geospy

> chmod +x install.sh

> ./install.sh

## GeoSpy uninstallation

> cd geospy

> chmod +x uninstall.sh

> ./uninstall.sh

***

# Geolocation Spy execution

> geospy -h

```
usage: geospy [-h] [-v] [-u URL] [-p PORT] [-ak ACCESSKEY] [-l LOCAL] [-n] 
              [-ic INJC] [-ud]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Put the web page URL to clone.
  -p PORT, --port PORT  Insert your port.
  -ak ACCESSKEY, --accesskey ACCESSKEY
                        Insert your custom Access Key.
  -n, --ngrok           Insert your ngrok Authtoken.
  -ic INJC, --injectcode INJC
                        Insert your custom REST API path.
  -ud, --update         Update GeoSpy to the latest version.
```

***

# Geolocation Spy disclaimer

    INFO: Usage of the Geolocation Spy for attacking targets without prior mutual consent is illegal. 
    It is the end user's responsibility to obey all applicable local, state, federal, and international laws. 
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.

***

# Geolocation Spy license

    Copyright (C) 2016 - 2019 Entynetproject

    Licensed under the Apache License, Version 2.0 (the "License"); you may not
    use the software except in compliance with the License.

    You may obtain a copy of the License at:

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    License for the specific language governing permissions and limitations under
    the License.
