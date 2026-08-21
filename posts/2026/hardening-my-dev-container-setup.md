---
title: Hardening my Dev Container Setup
date: '2026-03-14T12:30:35+05:30'
categories:
- coding
- llms
description: I hardened my Docker dev-container setup by having Copilot update and run its tests, then fixed host/container confusion, conflicting mounts, and missing package paths. Readable test output made debugging easier.
tags: [ai-coding-agents, docker, software-testing]
---

![](https://files.s-anand.net/images/2026-03-14-hardening-my-dev-container-setup.avif) <!-- https://gemini.google.com/app/9162b7c405fcd5ee -->

I run AI coding agents inside a [Docker container](https://github.com/sanand0/scripts/blob/dbdf328bb0e960367d45f9f8580d921159be3e9e/dev.dockerfile) for safety.

The setup is

- [`dev.dockerfile`](https://github.com/sanand0/scripts/blob/dbdf328bb0e960367d45f9f8580d921159be3e9e/dev.dockerfile): builds the image
- [`dev.sh`](https://github.com/sanand0/scripts/blob/dbdf328bb0e960367d45f9f8580d921159be3e9e/dev.sh): launches the container with the right mounts and env vars
- [`dev.test.sh`](https://github.com/sanand0/scripts/blob/dbdf328bb0e960367d45f9f8580d921159be3e9e/dev.test.sh): verifies everything works.

I wrote them semi-manually and it had bugs. I had GitHub Copilot + GPT-5.4 High update tests and actually _run_ the commands to verify the setup.

Here's what I learned from the process.

**1. Make it easier to review**. The first run took long. I pressed <kbd>Ctrl</kbd>+<kbd>C</kbd>, told Copilot to "add colored output, timing, and a live status line". Then I re-ran. Instead of a bunch of `ERROR:` lines, I now got a color-coded output with timing + a live status line showing what's running.

<pre><div style='color: #cccccc; background-color: #000000; font-family: FiraCode Nerd Font, Maple Mono, Inconsolata, Consolas, monospace, monospace; font-size: 14px;'><div><span></span><span style='color: #0dbc79;'>PASS</span><span>   2.495s  markitdown --help</span></div><div><span></span><span style='color: #cd3131;'>FAIL</span><span>   0.003s  playwright --version</span></div><div><span></span><span style='color: #ffbc03;'>note</span><span> /home/sanand/code/scripts/dev.test.sh: line 148: playwright: command not found</span></div><div><span></span><span style='color: #cd3131;'>FAIL</span><span>   0.003s  copilot version</span></div><div><span></span><span style='color: #ffbc03;'>note</span><span> /home/sanand/code/scripts/dev.test.sh: line 148: copilot: command not found</span></div></div></pre>

**2. Run in the target environment**. Tests reported that `fd` and `node` were missing, though they were _obviously_ in the image. Why? The test script was running on _my laptop_, not in the container. It was checking the host, not the container. I didn't realize that.

Copilot added a check to see if we're already inside a container:

```bash
running_in_container() {
  [ -f /.dockerenv ] || grep -qaE '(docker|containerd|kubepods)' /proc/1/cgroup 2>/dev/null
}

if ! running_in_container; then
  exec bash "${SCRIPT_DIR}/dev.sh" -- "$SCRIPT_PATH" --inside-container
fi
```

**3. Check for conflicting commands**. `fd` and `node` were still missing. Why? `dev.sh` was mounting my host `mise` and `bin` directories, overshadowing the image

```bash
-v "$HOME/.local/share/mise:/home/vscode/.local/share/mise"
-v "$HOME/.local/bin:/home/vscode/.local/bin"
```

It doesn't matter what's installed in the container - only the host binaries are visible. Copilot removed the first line, and copied `mise` into `~/.local/overrides/` to override the `~/.local/bin` PATH.

**4. Use the right packages**. The default ImageMagick binary at `https://imagemagick.org/archive/binaries/magick` is an AppImage. It doesn't work in containers. So it hat to switch to `apt-get install -y imagemagick` instead.

**5. Use the right paths**. `npm install -g wscat playwright ...` ran but to add them to the PATH, you need to `mise reshum node`. Copilot added that.

---

These are good practices, but since agents can fix them, they're less important to learn.

**Vibe-coding good tests** enabled Copilot to fix them.\
**Making output easy to read** enabled me to steer Copilot.

That's what I'd recommend if you're trying to optimize setup / deployments.
