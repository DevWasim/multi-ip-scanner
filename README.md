<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Port Scanner</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 20px;
        }

        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>

<body>

    <h1>Port Scanner</h1>
    <p>A simple Python script for scanning open ports on a target system. The script utilizes the <code>socket</code> library for establishing connections, <code>termcolor</code> for colorful console output, and <code>tqdm</code> for a progress bar. Additionally, an ASCII art representation of a port scanner is printed at the beginning.</p>

    <h2>Prerequisites</h2>
    <p>Make sure you have the required libraries installed:</p>
    <pre>pip install termcolor tqdm</pre>

    <h2>Usage</h2>
    <p>Run the script by executing the following command:</p>
    <pre>python port_scanner.py</pre>
    <p>Follow the on-screen instructions to input the target(s), the number of ports to scan, and the desired output type.</p>

    <h2>Features</h2>
    <ul>
        <li>Scans specified ports on the target system.</li>
        <li>Displays the state (open/closed) and service/version information for each scanned port.</li>
        <li>Supports scanning multiple targets separated by commas.</li>
        <li>Allows the user to choose between scanning all open and closed ports or only open ports.</li>
    </ul>

    <h2>Disclaimer</h2>
    <p>This tool is intended for educational purposes only. Use it responsibly and only on systems you have explicit permission to scan.</p>

    <h2>ASCII Art</h2>
    <pre>&lt;ASCII art here&gt;</pre>

    <p><strong>Note:</strong> The ASCII art is displayed at the beginning of the execution for aesthetic purposes.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>

</html>
