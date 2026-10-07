# Quickstart - Prompt-Injection-Hardened LLM Triage

## What you will build

This project tests a simple security question:

**What happens when attacker-controlled alert text tries to manipulate the AI reading it?**

By the end, you will:

- install Python
- download the project
- run an offline sanitizer demo
- see attacker text wrapped as untrusted data
- optionally install Ollama
- run a local model
- triage a synthetic security alert
- execute the 16-case injection harness
- compare your result with the included sample run

You do not need Git.

You do not need Ollama for the first half.

---

# Part 1 — Install Python

Google:

```text
Python download
```

Use:

```text
https://www.python.org/downloads/
```

Install Python 3.10 or newer.

## Windows

Open PowerShell:

```powershell
py --version
```

If needed:

```powershell
python --version
```

## macOS

Open Terminal:

```bash
python3 --version
```

**PASS:** Python 3.10+ prints.

---

# Part 2 — Get the project files

## Beginner method

Open:

```text
https://github.com/Emanuel-Walker/cyber-portfolio
```

Choose:

```text
Code -> Download ZIP
```

Extract it.

Open:

```text
cyber-portfolio-main/02-llm-triage-hardened
```

## Developer method

Optional:

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio/02-llm-triage-hardened
```

---

# Part 3 — Open a terminal in the project

## Windows

Open the project folder in File Explorer.

Click the address bar.

Type:

```text
powershell
```

Press Enter.

## macOS

Open Terminal.

Type:

```bash
cd 
```

Drag the project folder into Terminal.

Press Enter.

Verify:

```bash
pwd
```

or on Windows:

```powershell
Get-Location
```

**PASS:** the path ends in `02-llm-triage-hardened`.

---

# Part 4 — Create a virtual environment

## Windows

```powershell
py -m venv .venv
Set-ExecutionPolicy -Scope Process Bypass
.\.venv\Scripts\Activate.ps1
```

## macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r code/requirements.txt
```

**PASS:** dependencies install without an error.

---

# Part 5 — Run the offline injection demo

You are going to inspect a synthetic alert containing attacker-controlled text.

Open:

```text
data/sample_alerts/injected_user_agent.json
```

Notice the `user_agent.original` field.

It contains text that tries to give instructions to the AI.

Now run:

```bash
python code/demo_sanitizer.py data/sample_alerts/injected_user_agent.json
```

Expected shape:

```text
Detected injection signals:
  - user_agent.original: ...
```

You may see more than one signal.

**PASS:** the sanitizer identifies the suspicious instruction-style text.

---

# Part 6 — See what the model would receive

Run:

```bash
python code/triage_agent.py \
  --input data/sample_alerts/injected_user_agent.json \
  --dry-run
```

The script should print the prompt/input without calling Ollama.

Look for the alert data inside:

```text
<untrusted_field>
...
</untrusted_field>
```

**PASS:** attacker-controlled text is treated as data, not trusted system instruction.

That is the first security boundary.

---

# Part 7 — Understand the pipeline

The project works like this:

```text
alert JSON
   |
   v
sanitize strings
   |
   v
wrap untrusted fields
   |
   v
local LLM
   |
   v
validate JSON output
   |
   v
log provenance
```

Open:

```text
code/hardening/
```

That folder contains the main controls.

---

# Part 8 — Optional: install Ollama

Now you will run the local model.

Google:

```text
Ollama download
```

Use:

```text
https://ollama.com/download
```

Install the version for your operating system.

Close and reopen the terminal if necessary.

Verify:

```bash
ollama --version
```

**PASS:** Ollama prints a version number.

---

# Part 9 — Pull the model

Run:

```bash
ollama pull llama3.1:8b
```

This downloads the model.

The download can take time and several gigabytes of storage.

When it finishes:

```bash
ollama list
```

**PASS:** `llama3.1:8b` appears in the installed model list.

---

# Part 10 — Start Ollama

Run:

```bash
ollama serve
```

Leave that terminal window open.

If Ollama says the service is already running, that is fine.

Open a **second terminal** in the project folder.

Activate the virtual environment again.

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### macOS

```bash
source .venv/bin/activate
```

---

# Part 11 — Triage a real synthetic alert

Run:

```bash
python code/triage_agent.py \
  --input data/sample_alerts/suspicious_powershell.json
```

Expected result:

The model returns structured JSON that passes the project's output schema.

Look for fields such as:
- severity
- reasoning
- recommended action
- or the equivalent schema fields implemented by the project

**PASS:** the command returns validated structured output instead of free-form prose.

---

# Part 12 — Run the attack harness

Now test the defense instead of trusting it.

Run:

```bash
python code/attacks/run_attacks.py \
  --out code/attacks/results.md
```

The harness injects 16 payload families.

When complete, open:

```text
code/attacks/results.md
```

Also compare it with:

```text
code/attacks/results_sample.md
```

The included sample run blocked 12 of 16 payload families.

Your number may be different.

That is expected.

Model versions and behavior change.

---

# Part 13 — Read the failures

Do not skip the failures.

The sample project documents bypass classes such as:

- Unicode/confusable tricks
- indirect severity manipulation
- context flooding
- benign-looking framing

The point is not:

```text
"I made prompt injection impossible."
```

The point is:

```text
"I built controls, attacked them, measured them, and documented what still fails."
```

That is a much stronger security claim.

---

# Common problems

## `ModuleNotFoundError`

Activate the virtual environment.

Then:

```bash
python -m pip install -r code/requirements.txt
```

## `ollama_error`

Check that Ollama is running.

```bash
ollama list
```

Then:

```bash
ollama serve
```

## Model not found

Run:

```bash
ollama pull llama3.1:8b
```

## Your score is not 12/16

That is okay.

Record:
- model version
- Ollama version
- date
- your actual score

Do not force your result to match the sample.

---

# Definition of done

- [ ] Python installed
- [ ] project files downloaded
- [ ] virtual environment active
- [ ] sanitizer flags the poisoned field
- [ ] dry-run shows untrusted-field wrapping
- [ ] Ollama installed, if using full mode
- [ ] local model returns structured output
- [ ] 16-case harness runs
- [ ] you reviewed at least one failure

You now understand both the project and its limitations.
