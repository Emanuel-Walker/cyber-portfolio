#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
UPSTREAM="$ROOT/.upstream/muse-gadget-sdk"
PIN="b139b45064b4dcecf7bfe97e75bc7f99c10c28b6"
ACTION="${1:-prepare}"

mkdir -p "$ROOT/.upstream"

if [ ! -d "$UPSTREAM/.git" ]; then
  git clone https://github.com/facebookincubator/muse-gadget-sdk.git "$UPSTREAM"
fi

git -C "$UPSTREAM" fetch --all --tags --prune
git -C "$UPSTREAM" checkout --detach "$PIN"

echo "PASS: muse-gadget-sdk pinned at $PIN"

if [ "$ACTION" != "--install" ]; then
  echo
  echo "PREPARE ONLY. Nothing was installed."
  echo
  echo "Next:"
  echo 'export MUSE_GADGET_SDK_TOKEN="[YOUR_MUSE_GADGET_SDK_TOKEN]"'
  echo "bash integrations/muse-gadget/bootstrap.sh --install"
  exit 0
fi

if [ -z "${MUSE_GADGET_SDK_TOKEN:-}" ]; then
  echo "STOP: MUSE_GADGET_SDK_TOKEN is not set." >&2
  exit 2
fi

if ! id museagent >/dev/null 2>&1; then
  sudo useradd --create-home --shell /bin/bash museagent
fi

if sudo -n -l -U museagent 2>/dev/null | grep -qE '\(ALL( : ALL)?\) (NOPASSWD: )?ALL'; then
  echo "STOP: museagent has broad sudo rights. Remove them before continuing." >&2
  exit 3
fi

sudo install -d -m 0750 -o museagent -g museagent /home/museagent/muse-share

bash "$UPSTREAM/linux/install.sh"   --from "$UPSTREAM/linux"   --run-as museagent   --sdk-token "$MUSE_GADGET_SDK_TOKEN"

echo
echo "PASS: Muse Gadget SDK installed with commands running as museagent."
echo "Shared folder: /home/museagent/muse-share"
echo
echo "Check:"
echo "sudo musegadget info"
echo "sudo systemctl status musegadget"
