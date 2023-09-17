# Get Saved WiFi Passwords

A Python script to retrieve saved WiFi passwords from Windows and Linux operating systems.

## Installation

To use this script, you need to have Python installed on your system. Additionally, the `subprocess`, `os`, `re`, `collections`, and `configparser` modules are required. These modules can be installed using `pip`:

```bash
pip install subprocess
pip install os
pip install re
pip install collections
pip install configparser

```

## Usage

To retrieve saved WiFi passwords, simply execute the script get_saved_wifi_passwords.py. The passwords will be displayed in the console output.

```bash
python get_saved_wifi_passwords.py
```

## Supported Operating Systems

This script supports the following operating systems:

- Windows
- Linux

Please note that the script may not work on other operating systems.

## LICENSE

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. ```

## Explanations

  """
  Extracts saved Wi-Fi passwords saved in a Windows machine, this function extracts data using netsh
  command in Windows
  Args:
      verbose (int, optional): whether to print saved profiles real-time. Defaults to 1.
  Returns:
      [list]: list of extracted profiles, a profile has the fields ["ssid", "ciphers", "key"]
  """

"""Extracts saved Wi-Fi passwords saved in a Linux machine, this function extracts data in the
    `/etc/NetworkManager/system-connections/` directory
    Args:
        verbose (int, optional): whether to print saved profiles real-time. Defaults to 1.
    Returns:
    [list]: list of extracted profiles, a profile has the fields ["ssid", "auth-alg", "key-mgmt", "psk"]
"""
