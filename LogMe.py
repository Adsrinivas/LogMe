#!/usr/bin/env python3

import subprocess
import sys
import platform
import os

# Banner
def print_banner():
    banner = r"""
                            _                __  __      
                            | |    ___   __ _|  \/  | ___ 
                            | |   / _ \ / _` | |\/| |/ _ \
                            | |__| (_) | (_| | |  | |  __/
                            |_____\___/ \__, |_|  |_|\___|
                                        |___/             
                                    Made By ADSrinivas 
                            Github/X - Adsrinivas/@S_Alluru_                                            
"""
    print(banner)
print_banner()

def print_usage():
    print("Usage: python LogMe.py <app_short_name>")
    print("Options:")
    print("  -h, --help    Show this help message and exit")

def get_adb_command():
    """Return the appropriate adb command for the environment."""
    if platform.system() == "Windows":
        nox_adb = os.path.join(os.getcwd(), "nox_adb.exe")
        if os.path.exists(nox_adb):
            return [nox_adb, "logcat"]
    return ["adb", "logcat"]

def get_package_info(app_short_name):
    """Find the package name and PID based on a short app name using frida-ps."""
    result = subprocess.run(["frida-ps", "-Uai"], capture_output=True, text=True)
    
    for line in result.stdout.splitlines():
        if app_short_name.lower() in line.lower():
            parts = line.split()
            if len(parts) >= 2:
                pid = parts[0]
                package_name = parts[-1]
                return pid, package_name
    
    return None, None

def adb_logcat_pkg(app_short_name):
    if not app_short_name:
        print_usage()
        return 1
    
    pid, pkg_name = get_package_info(app_short_name)
    
    if not pkg_name:
        print(f"[-] No package found for application: {app_short_name}")
        return 1
    
    log_file = f"{pkg_name}_logcat.txt"
    
    print(f"\033[91m[+] Package: {pkg_name}, PID: {pid}\033[0m")
    
    if pid:
        cmd_logcat = ["adb", "logcat", "-b", "all", "-v", "color", "--pid", pid]
    else:
        print(f"[-] No PID found for package: {pkg_name}, using NOX ADB instead.")
        cmd_logcat = get_adb_command()
    
    match_count = 0  # Track the count of specific log lines

    with open(log_file, "w", encoding="utf-8") as f:
        process = subprocess.Popen(cmd_logcat, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            red_line = f"\033[91m{line.strip()}\033[0m"  # Make text red
            
            # Check for the specific log line
            if "is beyond type entryCount" in line:
                if match_count < 3:  # Capture only the first 3 matches
                    print(red_line)
                    f.write(line + "\n")
                    f.flush()
                    match_count += 1
            else:
                # Save the rest of the log as usual
                print(red_line)
                f.write(line + "\n")
                f.flush()
    
    print(f"[+] Logs saved to {log_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
    
    if sys.argv[1] in ("-h", "--help"):
        print_usage()
        sys.exit(0)
    
    adb_logcat_pkg(sys.argv[1])
