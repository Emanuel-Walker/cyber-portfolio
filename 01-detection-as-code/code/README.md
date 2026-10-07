# Code

This folder contains the working detection-as-code implementation.

## Folders

- `rules/` = Sigma detection source
- `converters/` = backend conversion code
- `tests/` = positive, benign, and contract tests

## First command

From the project root:

```bash
pytest code/tests/ -v
```

Then:

```bash
python code/converters/sigma_to_elastic.py code/rules/suspicious_powershell_download.yml
```

## Rule

A detection source file is not ready unless:
- strategy/spec exists
- malicious test fires
- benign test stays quiet
