# Ansible Automation Platform Upgrade Protector
The `aap-protector` is a `dnf-plugin`, written to take care of unwanted package upgrades to Ansible Automation Platform when perform operating system upgrades.
The solution is based on [Red Hat Solution 4566711.](https://access.redhat.com/solutions/4566711)


## Installation
Copy the files from Repository into correct location on your system.
```
/etc/dnf/plugins/aap-protector.conf
/etc/dnf/plugins/aap-protector.list
```

### Configuration file and Package List
Place the configuration file into `dnf-plugin` directory.
```
/etc/dnf/plugins/aap-protector.conf
```

The package list need to be placed at location `/etc/dnf/plugins` under the name `aap-protector.list`.
In the `repo/package_lists` subdirectory, pre-configured lists available, based on the [Red Hat Solution](https://access.redhat.com/solutions/4566711). Store the matching list to your system at the correct location.


### RHEL8
The python file need to be placed in following path.
```
/usr/lib/python3.6/site-packages/dnf-plugins/aap-protector.py
```

### RHEL9
The python file need to be placed in following path.
```
/usr/lib/python3.9/site-packages/dnf-plugins/aap-protector.py
```

## Usage

## Enable the plugin
```
# sed -i 's/enabled = 0/enabled = 1/' /etc/dnf/plugins/aap-protector.conf
```

## Disable the plugin
```
# sed -i 's/enabled = 1/enabled = 0/' /etc/dnf/plugins/aap-protector.conf
```

## Disable the plugin during runtime
```
# dnf <command> --disableplugin aap-protector <package>
```

## Verbose / troubleshooting

Use DNF’s own debug level when you need more detail (timers, repo metadata, plugin load order, etc.), for example:

```
dnf -d 10 <command>
```

The plugin logs its summary at INFO (`Reading AAP protector configuration`, excluded count, and the upgrade warning when anything is excluded). Each excluded package is also logged at DEBUG (`--* Excluded PKG: …`); there is no config flag for that. Showing DEBUG from the plugin logger may require DNF logging settings beyond `dnf -d` alone.


## LICENSE
This project is licensed under the MIT
