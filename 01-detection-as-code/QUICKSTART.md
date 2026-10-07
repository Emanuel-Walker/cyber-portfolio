# Quickstart - Detection-as-Code

## Zero-to-hero path

You can follow this even if you have never cloned a repo before.

### 1. Install Python

Google:

```text
Python download
```

Use the official site:

```text
https://www.python.org/downloads/
```

Install Python 3.10 or newer.

On Windows, check **Add Python to PATH** if the installer offers it.

Close and reopen Terminal or PowerShell.

Verify:

```bash
python --version
```

If your computer uses `python3` instead:

```bash
python3 --version
```

**PASS:** Python reports 3.10 or newer.

### 2. Get the project files

You do not need Git.

Beginner route:

```text
GitHub repository -> Code -> Download ZIP
```

Extract the ZIP.

Open:

```text
cyber-portfolio/01-detection-as-code/
```

Developer route, if you already use Git:

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio/01-detection-as-code
```

### 3. Open a terminal in that project folder

Windows:

- open the folder in File Explorer
- click the address bar
- type `powershell`
- press Enter

macOS:

- open Terminal
- type `cd `
- drag the project folder into Terminal
- press Enter

Verify the folder contains:

```text
README.md
QUICKSTART.md
code/
```

Then continue with the demo below.

## What you will build

You are going to prove one idea:

**A security detection rule should be tested like software before it reaches production.**

By the end, you will:

- install Python
- download the project files
- create an isolated Python environment
- install the project dependencies
- run six automated tests
- see positive and benign detection gates
- convert a Sigma rule into Elastic KQL
- intentionally break a rule and watch the test suite catch it

You do not need Git.

---

# Part 1 — Install Python

## Step 1. Google Python

Search:

```text
Python download
```

Use the official site:

```text
https://www.python.org/downloads/
```

Install Python 3.10 or newer.

### Windows

Run the Python installer.

If the installer shows:

```text
Add python.exe to PATH
```

enable it.

Then open **PowerShell**.

Run:

```powershell
py --version
```

If `py` is unavailable, try:

```powershell
python --version
```

### macOS

Install the current Python 3 release from python.org.

Open **Terminal**.

Run:

```bash
python3 --version
```

**PASS:** Python reports version 3.10 or newer.

---

# Part 2 — Get the project files

## Beginner method — Download ZIP

Open:

```text
https://github.com/Emanuel-Walker/cyber-portfolio
```

Click:

```text
Code -> Download ZIP
```

Extract the ZIP.

Open:

```text
cyber-portfolio-main/01-detection-as-code
```

## Developer method — Git clone

Optional:

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio/01-detection-as-code
```

Git is not required.

---

# Part 3 — Open a terminal in the project folder

## Windows

Open the `01-detection-as-code` folder in File Explorer.

Click the address bar.

Type:

```text
powershell
```

Press Enter.

PowerShell should open directly in that folder.

Verify:

```powershell
Get-Location
```

## macOS

Open Terminal.

Type:

```bash
cd 
```

including the space after `cd`.

Drag the `01-detection-as-code` folder from Finder into Terminal.

Press Enter.

Verify:

```bash
pwd
```

**PASS:** the terminal path ends in `01-detection-as-code`.

---

# Part 4 — Create an isolated Python environment

This keeps this project's packages separate from the rest of your computer.

## Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation for this session:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
```

## macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**PASS:** your terminal prompt usually starts with:

```text
(.venv)
```

---

# Part 5 — Install the dependencies

Run:

```bash
python -m pip install --upgrade pip
python -m pip install -r code/requirements.txt
```

On macOS, if `python` is unavailable inside the virtual environment, use:

```bash
python3 -m pip install -r code/requirements.txt
```

**PASS:** installation finishes without an error.

---

# Part 6 — Understand what you are about to test

Open:

```text
code/rules/
```

You should see Sigma YAML detection rules.

Open:

```text
code/tests/
```

The test suite checks three things:

1. a malicious/attack-like event must fire the rule
2. a benign event must stay quiet
3. the written detection strategy must exist

That is the dual gate.

```text
bad behavior -> MUST MATCH
normal behavior -> MUST NOT MATCH
```

---

# Part 7 — Run the tests

Run:

```bash
pytest code/tests/ -v
```

Expected result:

```text
6 passed
```

You should see tests similar to:

```text
test_rule_fires_on_atomic[...] PASSED
test_rule_silent_on_benign[...] PASSED
test_ads_spec_present[...] PASSED
```

**PASS:** all six tests pass.

If a benign test fails, the rule is too broad.

If a malicious test fails, the rule is too weak or incorrect.

---

# Part 8 — Convert the Sigma rule

Run:

```bash
python code/converters/sigma_to_elastic.py code/rules/suspicious_powershell_download.yml
```

The script should print an Elastic KQL query.

Example shape:

```text
process.name:"powershell.exe" and process.command_line:(...)
```

**PASS:** a KQL query prints without an exception.

The project currently demonstrates automated conversion to **Elastic KQL**.

Do not describe Splunk or another backend as implemented unless a tested converter exists.

---

# Part 9 — Break the rule on purpose

This is the useful part.

Open:

```text
code/rules/suspicious_powershell_download.yml
```

Make one detection condition intentionally too broad.

For example, temporarily change a specific command-line condition so that normal PowerShell activity is more likely to match.

Save the file.

Run:

```bash
pytest code/tests/ -v
```

Expected:

At least one test should turn red.

That demonstrates why the benign gate exists.

Undo your temporary change.

Run the tests again.

**PASS:**

```text
6 passed
```

---

# Part 10 — What you just built

You now have this pipeline:

```text
Sigma rule
   |
   +--> written strategy exists?
   |
   +--> malicious event fires?
   |
   +--> benign event stays quiet?
   |
   v
tests pass
   |
   v
Elastic KQL artifact
```

That is Detection-as-Code.

---

# Common problems

## `python` is not recognized

Windows:

```powershell
py --version
```

macOS:

```bash
python3 --version
```

If neither works, reinstall Python from python.org.

## `pytest` is not found

Make sure the virtual environment is activated.

Then:

```bash
python -m pip install -r code/requirements.txt
python -m pytest code/tests/ -v
```

## PowerShell will not activate the virtual environment

For the current PowerShell window:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
```

## Tests collect zero items

Confirm the terminal path ends in:

```text
01-detection-as-code
```

Then run:

```bash
python -m pytest code/tests/ -v
```

---

# Definition of done

- [ ] Python installed
- [ ] project files downloaded
- [ ] virtual environment active
- [ ] dependencies installed
- [ ] six tests pass
- [ ] Elastic KQL conversion works
- [ ] you broke a rule and saw a test catch it
- [ ] you restored the rule and returned to green

You now understand the project well enough to explain it in an interview.
