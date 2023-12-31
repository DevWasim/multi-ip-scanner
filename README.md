# Port Scanner

A simple Python script for scanning open ports on a target system. The script utilizes the `socket` library for establishing connections, `termcolor` for colorful console output, and `tqdm` for a progress bar. Additionally, an ASCII art representation of a port scanner is printed at the beginning.

## Prerequisites

Make sure you have the required libraries installed:

```bash
pip3 install termcolor tqdm
```

## Usage

Run the script by executing the following command:

1 For better UI and some extra Features but slow scanning speed :
```bash
python3 slow_scanner.py
```

2 For super fast speed scanning speed:
```bash
python3 fast_scanner.py
```



Follow the on-screen instructions to input the target(s), the number of ports to scan, and the desired output type.

## Features

- Scans specified ports on the target system.
- Displays the state (open/closed) and service/version information for each scanned port.
- Supports scanning multiple targets separated by commas.
- Allows the user to choose between scanning all open and closed ports or only open ports.

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and only on systems you have explicit permission to scan.

## ASCII Art

```
 #   #          ##     #       #            ###   ####           ###                                            
 #   #           #     #                     #    #   #         #   #                                           
 ## ##  #   #    #    ####    ##             #    #   #         #       ###    ###   # ##   # ##    ###   # ##  
 # # #  #   #    #     #       #             #    ####           ###   #   #      #  ##  #  ##  #  #   #  ##  # 
 #   #  #   #    #     #       #             #    #                 #  #       ####  #   #  #   #  #####  #     
 #   #  #  ##    #     #  #    #             #    #             #   #  #   #  #   |  #   |  |   |  #      %
 #   #   ## #   ###     ##    ###           ###   #              ###    ###    ####  #   #  #   #   ###   #     by wasim khan
```

**Note:** The ASCII art is displayed at the beginning of the execution for aesthetic purposes.

---

## 🌱 Empower dedication with your generosity
#### Every single coffee boosts towards greater motivation, turning compassion into action. Show your kind support with just a little click! 😃

<a href="https://www.buymeacoffee.com/developerwasim" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


