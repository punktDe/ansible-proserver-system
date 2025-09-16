<!-- BEGIN_ANSIBLE_DOCS -->
<!--
Do not edit README.md directly!

This file is generated automatically by aar-doc and will be overwritten.

Please edit meta/argument_specs.yml instead.
-->

# ansible-proserver-system

system role for Proserver

## Supported Operating Systems

- Debian 12
- Ubuntu 24.04, 22.04
- FreeBSD [Proserver](https://infrastructure.punkt.de/de/produkte/proserver.html)

## Role Arguments



#### Options for `system`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `root_group` | Root group name (automatically determined based on OS) | str | no | {{ 'root' if ansible_os_family == 'Debian' else 'wheel' }} |
| `sshd` | SSH daemon configuration | dict of 'sshd' options | no | {} |
| `rsyslog` | Rsyslog configuration | dict of 'rsyslog' options | no | {} |
| `features` | Feature flags to enable/disable various role components | dict of 'features' options | no | {} |
| `prefix` | Path prefixes for various system components | dict of 'prefix' options | no | {} |
| `proserver_fact` | Proserver fact configuration | dict of 'proserver_fact' options | no | {} |
| `network` | Network configuration | dict of 'network' options | no | {} |
| `hostname` | Hostname configuration | str | no | None |
| `timezone` | System timezone | str | no | None |
| `netplan` | Netplan configuration | dict | no |  |
| `ufw` | UFW firewall configuration | dict of 'ufw' options | no | {} |
| `sysctl` | Sysctl kernel parameters | dict | no |  |
| `hosts` | /etc/hosts entries | dict | no |  |
| `environment` | System-wide environment variables | dict | no |  |
| `apt` | APT package management configuration | dict of 'apt' options | no | {} |
| `unattended_upgrades` | Unattended upgrades configuration | dict of 'unattended_upgrades' options | no | {} |
| `postfix` | Postfix mail server configuration | dict of 'postfix' options | no | {} |
| `sudoers` | Sudoers configuration files | dict | no |  |
| `groups` | System groups to create | dict | no |  |
| `users` | System users to create | dict | no |  |
| `users_delete` | List of users to delete | list of 'str' | no | [] |
| `motd` | Message of the day configuration | dict of 'motd' options | no | {} |

#### Options for `system.sshd`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `config` | SSH daemon configuration parameters | dict | no | {"MaxStartups": "100:30:100", "PasswordAuthentication": false, "PermitRootLogin": false} |

#### Options for `system.rsyslog`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `precise_timestamps` | Enable precise timestamps in rsyslog | bool | no | False |

#### Options for `system.features`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `rsyslog` | Enable rsyslog configuration | bool | no | {{ ansible_system == 'Linux' }} |
| `sshd` | Enable SSH daemon configuration | bool | no | {{ ansible_system == 'Linux' }} |
| `proserver_fact` | Enable proserver fact generation | bool | no | False |
| `hostname` | Enable hostname configuration | bool | no | True |
| `timezone` | Enable timezone configuration | bool | no | True |
| `netplan` | Enable netplan configuration | bool | no | {{ ansible_distribution == 'Ubuntu' }} |
| `systemd_resolved` | Enable systemd-resolved configuration | bool | no | False |
| `ufw` | Enable UFW firewall configuration | bool | no | {{ ansible_distribution == 'Ubuntu' }} |
| `sysctl` | Enable sysctl configuration | bool | no | {{ ansible_system == 'Linux' }} |
| `hosts` | Enable /etc/hosts configuration | bool | no | True |
| `environment` | Enable system-wide environment variables | bool | no | True |
| `apt` | Enable APT package management (Debian/Ubuntu only) | bool | no | {{ ansible_os_family == 'Debian' }} |
| `proserver_user` | Enable proserver user configuration | bool | no | False |
| `postfix` | Enable Postfix mail server configuration | bool | no | False |
| `users` | Enable user management | bool | no | True |
| `sudoers` | Enable sudoers configuration | bool | no | True |
| `authorized_keys` | Enable SSH authorized keys management | bool | no | True |
| `authorized_keys_delete` | Enable deletion of SSH authorized keys | bool | no | False |
| `motd` | Enable message of the day configuration | bool | no | True |
| `unattended_upgrades` | Enable unattended upgrades configuration (Debian/Ubuntu only) | bool | no | False |

#### Options for `system.prefix`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `sudoers` | Path prefix for sudoers configuration | str | no | {{ '/etc' if ansible_system == 'Linux' else '/usr/local/etc' }} |

#### Options for `system.proserver_fact`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `python` | Python interpreter path for proserver facts | str | no | {{ '/usr/bin/env python3.8' if (ansible_distribution == 'Ubuntu' and ansible_distribution_version == '18.04') else '/usr/bin/env python3' }} |

#### Options for `system.network`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `public_interfaces` | List of public network interfaces | list of 'str' | no | [] |
| `public_subnets` | List of public subnets | list of 'str' | no | [] |

#### Options for `system.ufw`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `reset` | Reset UFW to default state | bool | no | {{ system_ufw_reset | bool }} |
| `state` | UFW state (enabled/disabled) | str | no | None |
| `policy` | UFW default policy | str | no | None |
| `rules` | UFW firewall rules | dict of 'rules' options | no | {} |

#### Options for `system.ufw.rules`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `comment` | Comment for the UFW rule | str | no | None |
| `delete` | Whether to delete the UFW rule | bool | no | False |
| `direction` | Direction for the UFW rule (in/out) | str | no | None |
| `from_ip` | Source IP address for the UFW rule | str | no | any |
| `from_port` | Source port for the UFW rule | str | no | None |
| `interface` | Network interface for the UFW rule | str | no | None |
| `log` | Enable logging for the UFW rule | bool | no | False |
| `proto` | Protocol for the UFW rule (tcp/udp/any) | str | no | None |
| `route` | Apply the rule to routed/forwarded packets | bool | no | False |
| `rule` | Rule type (allow/deny/limit/reject) | str | no | None |
| `to_ip` | Destination IP address for the UFW rule | str | no | any |
| `to_port` | Destination port for the UFW rule | str | no | None |

#### Options for `system.apt`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `proxy` | APT proxy configuration | str | no | None |
| `packages` | APT packages to install (dict with package names as keys and boolean values) | dict | no |  |
| `version_locks` | APT package version locks (dict with package names as keys and version constraint values) | dict | no |  |

#### Options for `system.unattended_upgrades`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `config` | Unattended upgrades configuration parameters | dict | no | {"feature_updates": false, "auto_clean": true, "auto_reboot": {"enabled": false, "time": "03:00"}, "blacklist": [], "schedule": "20:00", "mail": {"enable": true, "only_on_error": true, "to": null}} |

#### Options for `system.postfix`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `prefix` | Postfix configuration path prefix | dict of 'prefix' options | no | {} |
| `hash_maps` | Postfix hash maps | dict | no |  |
| `main.cf` | Postfix main.cf configuration | dict | no |  |

#### Options for `system.postfix.prefix`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `config` | Postfix configuration directory path | str | no | {{ '/etc/postfix' if ansible_system == 'Linux' else '/usr/local/etc/postfix' }} |

#### Options for `system.motd`

|Option|Description|Type|Required|Default|
|---|---|---|---|---|
| `project` | Project name for MOTD | str | no | None |
| `banner_string` | Banner string for MOTD | str | no | punkt.de        ____
 _ __  _ __ ___/ ___|  ___ _ ____   _____ _ __
| '_ \| '__/ _ \___ \ / _ \ '__\ \ / / _ \ '__|
| |_) | | | (_) |__) |  __/ |   \ V /  __/ |
| .__/|_|  \___/____/ \___|_|    \_/ \___|_|
|_| |
| `details` | Additional details for MOTD | str | no | {{ (((dehydrated | default({})).domains | default({})).keys() | list + ((dehydrated | default({})).domains | default({})).values() | list | sum(start=[])) | reject('eq', inventory_hostname) | reject('eq', ansible_nodename) | system_motd_sort_fqdns }} |

## Dependencies

None.

## Installation

Add this role to the requirements.yml of your playbook as follows:

```yaml
roles:
  - name: ansible-proserver-system
    src: https://github.com/punktDe/ansible-proserver-system
```

Afterwards, install the role by running `ansible-galaxy install -r requirements.yml`

## Example Playbook

```yaml
- hosts: all
  roles:
    - name: system
```

<!-- END_ANSIBLE_DOCS -->
