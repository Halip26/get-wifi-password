import subprocess
import os
import re
from collections import namedtuple

# import configparser


def get_windows_saved_ssids():
    """Mengembalikan daftar SSID yang disimpan di mesin Windows menggunakan perintah netsh"""
    # dapatkan semua profil wifi yang disimpan di PC
    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = []
    profiles = re.findall(r"All User Profile\s(.*)", output)
    for profile in profiles:
        # untuk setiap SSID, hilangkan spasi dan titik dua
        ssid = profile.strip().strip(":").strip()
        # tambahkan ke daftar
        ssids.append(ssid)
    return ssids


# Fungsi untuk mendapatkan Key wifi yang disimpan OS windows
def get_windows_saved_wifi_passwords(verbose=1):
    # Menjalankan command untuk mendapatkan rincian SSID
    ssids = get_windows_saved_ssids()
    Profile = namedtuple("Profile", ["ssid", "ciphers", "key"])
    profiles = []
    for ssid in ssids:
        ssid_details = subprocess.check_output(
            f"""netsh wlan show profile "{ssid}" key=clear"""
        ).decode()
        # Mendapatkan tipe enkripsi dari rincian SSID
        ciphers = re.findall(r"Cipher\s(.*)", ssid_details)
        # kosongkan spaces and colon
        ciphers = "/".join([c.strip().strip(":").strip() for c in ciphers])
        # mendapatkan Wi-Fi password
        key = re.findall(r"Key Content\s(.*)", ssid_details)
        # Menghapus spasi dan titik dua
        try:
            key = key[0].strip().strip(":").strip()

        except IndexError:
            key = "None"
        # Membuat named tuple Profile untuk SSID yang sedang diproses
        profile = Profile(ssid=ssid, ciphers=ciphers, key=key)
        # Menampilkan rincian SSID jika verbose >= 1
        if verbose >= 1:
            print_windows_profile(profile)
        profiles.append(profile)
    return profiles


# Fungsi untuk menampilkan rincian SSID
def print_windows_profile(profile):
    """Mencetak lebih dari satu profil di Windows"""
    print(f"{profile.ssid:32}{profile.ciphers:15}{profile.key:50}")


def print_windows_profiles(verbose):
    """Mencetak semua SSID yang diekstraksi beserta Key di Windows"""
    print("SSID                 \t\tCIPHER(S)      KEY")
    print("-" * 60)
    get_windows_saved_wifi_passwords(verbose)


# # Fungsi untuk mendapatkan Key wifi yang disimpan OS Linux
# def get_linux_saved_wifi_passwords(verbose=1):
#     network_connections_path = "/etc/NetworkManager/system-connections/"
#     fields = ["ssid", "auth-alg", "key-mgmt", "psk"]
#     Profile = namedtuple("Profile", [f.replace("-", "_") for f in fields])
#     profiles = []
#     for file in os.listdir(network_connections_path):
#         data = {k.replace("-", "_"): None for k in fields}
#         config = configparser.ConfigParser()
#         config.read(os.path.join(network_connections_path, file))
#         for _, section in config.items():
#             for k, v in section.items():
#                 if k in fields:
#                     data[k.replace("-", "_")] = v
#         profile = Profile(**data)
#         if verbose >= 1:
#             print_linux_profile(profile)
#         profiles.append(profile)
#     return profiles


# # untuk menampilkan password pada os linux
# def print_linux_profile(profile):
#     """Prints a single profile on Linux"""
#     print(
#         f"{str(profile.ssid):32}{str(profile.auth_alg):6}{str(profile.key_mgmt):10}{str(profile.psk):50}"
#     )


# def print_linux_profiles(verbose):
#     """Mencetak semua SSID yang diekstrak beserta Key (PSK) di Linux"""
#     print("SSID                     AUTH KEY-MGMT  PSK")
#     print("-" * 50)
#     get_linux_saved_wifi_passwords(verbose)


def print_profiles(verbose=1):
    if os.name == "nt":
        print_windows_profiles(verbose)
    elif os.name == "posix":
        print_linux_profiles(verbose)
    else:
        raise NotImplemented("Code only works for either Linux or Windows")


if __name__ == "__main__":
    print_profiles()
