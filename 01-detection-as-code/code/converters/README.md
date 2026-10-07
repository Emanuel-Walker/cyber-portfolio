# Converters

Backend conversion code lives here.

## Current implemented backend

```text
Elastic KQL
```

Run:

```bash
python code/converters/sigma_to_elastic.py code/rules/suspicious_powershell_download.yml
```

Do not claim a backend is supported until a converter and test exist for it.

Splunk and Microsoft Sentinel are future work unless implemented later.
