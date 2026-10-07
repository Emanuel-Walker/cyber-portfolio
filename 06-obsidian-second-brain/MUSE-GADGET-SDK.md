# Muse Gadget SDK integration

Upstream:

```text
https://github.com/facebookincubator/muse-gadget-sdk
```

Pinned research revision:

```text
b139b45064b4dcecf7bfe97e75bc7f99c10c28b6
```

License: Apache-2.0, with upstream-noted exceptions for certain third-party/avatar files.

## Why it matters

Meta's Muse Gadget SDK can turn:

- an ESP32 board into a Muse-connected gadget
- a Raspberry Pi or Linux computer into a Muse-connected tool host

That overlaps directly with the Second Brain / Muse architecture.

The Linux SDK exposes commands including:
- `device.health`
- `file.read`
- `file.write`
- `system.run`

It also lets developers add their own narrower commands.

## Security rule

Do **not** start by installing it under your normal admin account.

The upstream installer warns that Muse gets the same permissions as the account selected with `--run-as`.

Our beginner path creates a dedicated account:

```text
museagent
```

That account should:
- have no sudo rights
- have its own home folder
- only receive the context/files you intentionally expose

## 1. Pull the pinned SDK

From this project:

```bash
bash integrations/muse-gadget/bootstrap.sh
```

**PASS:** the script clones the pinned SDK and stops before installation.

## 2. Get a Muse Gadget SDK token

The upstream project currently requires an SDK token from:

```text
https://gadgets.muse.ai/settings/sdk-tokens
```

Read the upstream Gadget SDK Terms before using it.

Do not commit the token.

## 3. Install with least privilege

Set the token in your shell:

```bash
export MUSE_GADGET_SDK_TOKEN="[YOUR_MUSE_GADGET_SDK_TOKEN]"
```

Then:

```bash
bash integrations/muse-gadget/bootstrap.sh --install
```

The script:
1. creates `museagent` if needed
2. creates `/home/museagent/muse-share`
3. installs the pinned Linux SDK
4. tells the upstream installer to run Muse commands as `museagent`

## 4. Pair

Follow the terminal instructions.

In the Muse app:
1. enable Developer mode
2. add a device
3. choose the `MuseGadget...` device

## 5. First safe test

Run locally:

```bash
sudo musegadget info
sudo systemctl status musegadget
```

Then ask Muse for the device health.

**PASS:** Muse reports uptime, load, memory, disk, or temperature.

Do not test arbitrary shell execution first.

## 6. Expose only selected context

Put intentionally shared files under:

```text
/home/museagent/muse-share/
```

Example:

```bash
sudo -u museagent tee /home/museagent/muse-share/README.md >/dev/null <<'EOF'
# Muse shared context

Only files intentionally copied into this folder are available to the device-side agent account.
EOF
```

Do not point this account at `Legacy/`, credentials, private keys, or your entire home directory.

## Better long-term design

The Linux SDK is extensible.

Instead of relying forever on:

```text
system.run
```

add narrow commands such as:

```text
muse.project_status
muse.focus_mode
muse.dashboard_scene
muse.vault_summary
```

A narrow command is easier to test and safer to grant.

## ESP32 path

The ESP32 SDK supports multiple boards, including **M5Stack CoreS3**.

That makes it relevant to future Muse body experiments.

Do not replace a working StackChan integration immediately.

Use the SDK when it removes a real integration problem.

## What this integration proves

- local files can remain the canonical memory layer
- a physical device can become a controlled tool/interface
- device permissions can be separated from the model itself

It does **not** prove that a cloud-connected companion is private by default.

Review what data leaves the device before exposing sensitive context.
