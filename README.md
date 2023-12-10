# Port Scanner

A simple Python script for scanning open ports on a target system. The script utilizes the `socket` library for establishing connections, `termcolor` for colorful console output, and `tqdm` for a progress bar. Additionally, an ASCII art representation of a port scanner is printed at the beginning.

## Prerequisites

Make sure you have the required libraries installed:

```bash
pip install termcolor tqdm
```

## Usage

Run the script by executing the following command:

```bash
python port_scanner.py
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
<ASCII art here>
```

**Note:** The ASCII art is displayed at the beginning of the execution for aesthetic purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
