---
title: Linux
#subtitle: 
#description: 
#icon: 
#status:
tags: 
  - TODO
  - resource
#template: 
---

# Linux

## Network

### Eduroam using [`iwd`](https://archive.kernel.org/oldwiki/iwd.wiki.kernel.org/)

As root, create a file `eduroam.8021x` at the default location [`/var/lib/iwd`](https://wiki.archlinux.org/title/Iwd#Network_configuration):

``` { .cfg .copy title="/var/lib/iwd/eduroam.8021x" hl_lines="6 7" }
[Security]
EAP-Method=PEAP
EAP-Identity=anonymous@stud.aho.no
EAP-Phase2-Method=MSCHAPV2
EAP-PEAP-Phase2-Method=MSCHAPV2
EAP-PEAP-Phase2-Identity=MY_AHO_USERNAME@stud.aho.no
EAP-PEAP-Phase2-Password=MY_AHO_PASSWORD

[Settings]
AutoConnect=true
```

Change `MY_AHO_USERNAME` (in format _sXXXYYY_) and `MY_AHO_PASSWORD` accordingly.
