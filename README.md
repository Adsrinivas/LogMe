<h1 align="center">
LogMe
</h1>
<h4 align="center">LogMe.py is a Python script that fetches and filters logcat logs for a specified Android application. It automatically retrieves the package name and process ID (PID) using frida-ps and captures logcat output related to the application.</h4>

 <p align="center">
    <a href="https://x.com/S_Alluru_">
      <img src="https://img.shields.io/twitter/follow/S_Alluru_.svg?logo=twitter" alt="Follow on Twitter">
    </a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python Badge">
    <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey.svg" alt="Platform Badge">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License Badge">
  </p>

### ✨ **Key Features**
- 📦 **Automatic Package and PID Detection:** Retrieves the package name and PID using `frida-ps`.  
- 🎯 **Targeted Log Capture:**  
   - Saves all log lines except for those containing `"is beyond type entryCount"`.  
   - **Limits to saving only the first three instances** of logs containing `"is beyond type entryCount"`.  
- 🖥️ **NOX ADB Support:** Falls back to NOX ADB if standard ADB is unavailable.  
- 📄 **Log Saving:** Saves logs to a file named `<package_name>_logcat.txt`.  
- 🟥 **Enhanced Visibility:** Displays logs in red for better readability.  

---

## **Prerequisites**
Make sure you have the following installed:
- 🐍 **Python 3.x**  
- 📱 **ADB (Android Debug Bridge)** — Installed and added to your system PATH.  
- 🛠️ **Frida** — Install via pip:  
   ```sh
   pip install frida
   ```
- (Optional) `nox_adb.exe` for NOX emulator support.

---

## **Installation**
1. **Clone this repository:**
   ```sh
   git clone https://github.com/Adsrinivas/LogMe.git
   cd LogMe
   ```

2. **Install required dependencies:**
   ```sh
   pip install frida
   ```

---

## **Usage**
Run the script with the application's short name as an argument:
```sh
python LogMe.py <app_short_name>
```

### **Example**
```sh
python LogMe.py facebook
```
**This will:**
- Find the package name and PID of Facebook.  
- Start logcat filtering for that PID.  
- Save logs to `com.facebook.katana_logcat.txt`.  
- **Capture only the first three instances** of logs containing `"is beyond type entryCount"` and save the rest as usual.

---

## **Help Menu**
To display usage information:
```sh
python LogMe.py -h
```

---

## **Troubleshooting**
- **Device not detected:**  
   Ensure your device is connected and recognized by running:
   ```sh
   adb devices
   ```
- **Frida not found:**  
   Install Frida using pip:
   ```sh
   pip install frida
   ```

---

## **Contributing**
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-branch`).  
3. Commit your changes (`git commit -m 'Add some feature'`).  
4. Push to the branch (`git push origin feature-branch`).  
5. Create a Pull Request.

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Author**
👤 **ADSrinivas**  
- GitHub: [@S_Alluru_](https://github.com/Adsrinivas)  

Feel free to open an issue if you find a bug or have a feature request! 🎉

---

## **Support**
⭐ If you find this project useful, please consider starring it on GitHub!  
🐞 For any issues, check the [Issues](https://github.com/Adsrinivas/LogMe/issues) section or open a new one.
