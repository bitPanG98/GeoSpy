# Quack Toolkit

![quack](https://user-images.githubusercontent.com/54115104/74247189-c04a9300-4cf6-11ea-982a-2222329215bd.jpeg)

<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a>
  <a href="https://github.com/entynetproject/quack/releases">
    <img src="https://img.shields.io/github/release/entynetproject/quack.svg">
  </a>
  <a href="https://wikipedia.org/wiki/Python_(programming_language)">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/entynetproject/quack/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/quack.svg">
  </a>
  <a href="https://github.com/entynetproject/quack/wiki">
      <img src="https://img.shields.io/badge/wiki%20-quack-lightgrey.svg">
 </a>
  <a href="https://twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
</p>

***

# About Quack Toolkit

    Quack Toolkit is a set of a Denial of Service 
    attack methods. Quack includes SMS attack method, 
    TCP attack method and many other attack methods.

***

# Getting started

## Quack installation

> cd quack

> chmod +x install.sh

> ./install.sh

## Quack uninstallation

> cd quack

> chmod +x uninstall.sh

> ./uninstall.sh

***

# Quack Toolkit execution

> quack -h

```

usage: quack [-h] [--target <IP:PORT, URL, PHONE>]
             [--method [SMS|NTP|TCP|UDP|SYN|POD|SLOWLORIS|MEMCACHED|HTTP|NJRAT]]
             [--time TIME] [--threads THREADS] [-u]

optional arguments:
  -h, --help            show this help message and exit
  --target <IP:PORT, URL, PHONE>
                        Target IP:port, URL or phone.
  --method [SMS|NTP|TCP|UDP|SYN|POD|SLOWLORIS|MEMCACHED|HTTP|NJRAT]
                        Attack method.
  --time TIME           Time in secounds.
  --threads THREADS     Threads count.
  -u, --update          Update Quack Toolkit.
```
  
***
  
# Quack Toolkit examples

> Example of the SMS attack method
    
    quack --method SMS --target +<phone> --time <time> --threads <threads>

***

# Quack Toolkit disclaimer

    Usage of the Quack Toolkit for attacking targets without prior mutual consent is illegal. 
    It is the end user's responsibility to obey all applicable local, state, federal, and international laws. 
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.

***

# Quack Toolkit license

    MIT License

    Copyright (C) 2019, Entynetproject. All Rights Reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
