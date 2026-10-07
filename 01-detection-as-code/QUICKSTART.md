# Quickstart - Detection-as-Code


## Get the project files

You can read this walkthrough without Git.

To run the demo, get the files one of two ways.

### Beginner option: Download ZIP

On the GitHub repository page:

```text
Code -> Download ZIP
```

Extract the ZIP.

Open the folder for this project.

### Developer option: Git clone

If you already use Git:

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio
```

Then enter this project's folder when the walkthrough tells you to.

Git is optional. The project files are not.


> [!info] Plain English
> This project treats security detection rules like software. You write a rule, write two tests (one that proves it catches the bad thing, one that proves it stays quiet on normal activity), and a pipeline blocks the merge if either test fails. You will see six tests pass and a detection rule convert into a working Elastic query. Takes about 5 minutes.

## 5-minute demo

BLUF. You will run the dual-gate pytest suite and the Sigma to Elastic converter. If the tests go green and the converter prints a KQL query, the project works.

Prerequisites.

```bash
python --version   # need 3.10 or newer
pip install pytest pyyaml jsonschema
```

Step 1 - setup.

```bash
cd 01-detection-as-code
pip install -r code/requirements.txt
```

What you see. Pip resolves and installs `pyyaml`, `jsonschema`, and `pytest`. The final line reads `Successfully installed ...` with no errors.

Step 2 - run the dual gate.

```bash
pytest code/tests/ -v
```

What you see. Pytest discovers `test_detection_coverage.py` and prints one line per test. Expect `6 passed` at the bottom. Each rule has a positive test (must fire) and a benign test (must not fire). Both gates have to pass or the rule is rejected.

```
test_detection_coverage.py::test_rule_fires_on_atomic[credential_dump_lsass] PASSED
test_detection_coverage.py::test_rule_silent_on_benign[credential_dump_lsass] PASSED
test_detection_coverage.py::test_rule_fires_on_atomic[suspicious_powershell_download] PASSED
test_detection_coverage.py::test_rule_silent_on_benign[suspicious_powershell_download] PASSED
test_detection_coverage.py::test_ads_spec_present[credential_dump_lsass] PASSED
test_detection_coverage.py::test_ads_spec_present[suspicious_powershell_download] PASSED
======= 6 passed in 0.4s =======
```

Step 3 - run the converter.

```bash
python code/converters/sigma_to_elastic.py code/rules/suspicious_powershell_download.yml
```

What you see. The script prints a working Elastic KQL query derived from the Sigma rule. Something like `process.name:"powershell.exe" and process.command_line:(*DownloadString* or *IEX*)`. Copy that into Kibana and it runs.

Step 3b - validate.

Both gates green means merge is allowed. If either fails, the PR blocks. That is the whole point. Try breaking a rule in `code/rules/*.yml` and rerunning pytest. The benign test should flip red.

## What this proves

- Detection engineering treated like software with CI gates, not a wiki page of regexes.
- Dual-gate testing (positive + benign) catches rules that fire on legitimate admin work before prod does.
- Sigma keeps the source detection logic portable while this project demonstrates automated conversion to Elastic KQL.

## Add screenshots here

Capture these while running the demo and drop them in a `screenshots/` folder next to this file.

- `screenshots/01-pytest-green.png` - terminal showing 6 passed
- `screenshots/02-pytest-broken-rule.png` - benign test failing after rule is loosened
- `screenshots/03-converted-kql.png` - converter output printed to terminal
- `screenshots/04-ads-spec.png` - a `.ads.md` file open next to its `.yml` rule
- `screenshots/05-pr-blocked.png` - a mocked PR view with the red CI check

## Common issues

- `ModuleNotFoundError: No module named 'yaml'`. The `pyyaml` install did not land in the active interpreter. Run `python -m pip install pyyaml` instead of plain `pip`.
- Pytest reports `collected 0 items`. You ran it from the repo root. Either run from `01-detection-as-code/` or pass the full path `pytest 01-detection-as-code/code/tests/ -v`.
- Converter prints a Sigma field name with no translation. The field is not in the Elastic mapping table. Add it to the converter's `FIELD_MAP` dict and rerun.
