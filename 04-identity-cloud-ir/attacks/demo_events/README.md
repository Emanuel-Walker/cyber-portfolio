# Demo events

Synthetic AWS-style events for the offline detection demo.

Current pair:

```text
create_access_key.json -> should match
list_buckets.json      -> should not match
```

Run from the project root:

```bash
python3 detections/demo_iam_detection.py attacks/demo_events/create_access_key.json
python3 detections/demo_iam_detection.py attacks/demo_events/list_buckets.json
```

No AWS account is used.
