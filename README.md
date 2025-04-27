<h1>🔍 Port Scanner Tool</h1>

<h2>Description</h2>
<p>
A lightweight Python script that performs fast and reliable port scans on one or multiple targets. <br>
This tool supports both single and multiple port inputs and conducts efficient SYN/CONNECT scans on specified hosts.
</p>

<h2>Installation</h2>
<pre>
git clone https://github.com/wizz117/Port-Scanner.git
cd Port-Scanner
python3 PortScanner.py
</pre>

<h2>Usage</h2>

<h3> Step 1: Enter Target IP(s)</h3>
<p>
Input the IP addresses you wish to scan, separated by commas.
</p>
<img src="https://user-images.githubusercontent.com/95639719/193258529-28775ac8-18ed-4d66-aa84-5af54bc5d740.png" alt="Start the script" width="600"/>

<h3> Step 2: Choose Scan Mode</h3>
<p>
You'll be prompted to scan a specific port. Enter <strong>Y</strong> (Yes) or <strong>N</strong> (No).<br>
If <strong>Y</strong>, enter one or multiple ports (comma-separated).
</p>
<img src="https://user-images.githubusercontent.com/95639719/193258868-6ffd1b37-1c88-4234-8d38-f0d4749740e4.png" alt="Specific port" width="600"/>

<h3> Step 3: Scan Multiple Ports</h3>
<p>
If you choose <strong>N</strong>, you'll be asked to enter the number of ports to scan.<br>
For example, entering <code>1100</code> scans ports from 0 to 1100.
</p>
<img src="https://user-images.githubusercontent.com/95639719/193259012-73cd3999-7c5f-4572-9ed3-7ae10419b8da.png" alt="Multiple ports" width="600"/>
