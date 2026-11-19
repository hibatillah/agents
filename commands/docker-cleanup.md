---
description: Prune Docker build cache, then compact the Docker Desktop (WSL2) VHDX so freed disk space returns to Windows
disable-model-invocation: true
---

Docker Desktop on Windows does not shrink `docker_data.vhdx` after a prune. A prune frees space inside the VHDX only; the space returns to Windows once the VHDX is compacted.

Run the steps in order. Each step ends when its stated condition holds.

1. **Measure the starting state** (PowerShell). Done when you hold all three numbers:
   - Size of `$env:LOCALAPPDATA\Docker\wsl\disk\docker_data.vhdx` in GB. If the file is missing, search `$env:LOCALAPPDATA\Docker\wsl` for `*.vhdx` and use that path as `-VhdxPath` in step 4.
   - Free space on C: `(Get-PSDrive C).Free / 1GB`.
   - `docker system df` output (skip it when Docker is not running).

2. **Prune (only when Docker is running).** Show the `docker system df` result, then ask the user which scope to prune. Done when the user has chosen a scope and the prune has run, or the user has chosen to skip it.
   - Safe default: `docker builder prune -f --filter until=168h` (build cache older than 7 days).
   - More aggressive: `docker builder prune -a -f` or `docker image prune -a -f`.
   - Volumes hold data such as databases. Run `docker volume prune` or `docker system prune --volumes` only after the user approves it explicitly.

3. **Ask the user to quit Docker Desktop** from the tray icon; quitting it themselves stops the containers cleanly, which `Stop-Process` would not. Done when `Get-Process 'Docker Desktop'` returns nothing.

4. **Compact:**
   ```powershell
   powershell -NoProfile -File "${CLAUDE_PLUGIN_ROOT}/scripts/docker-reclaim.ps1"
   ```
   The script asks for UAC (the user must click Yes), runs `wsl --shutdown`, starts the `vds` service, then runs `diskpart compact vdisk`. It deletes no data. Done when the script prints `VHDX: <before> GB -> <after> GB`.

5. **Report** the VHDX size and free C: space, before and after, as measured numbers. When the VHDX did not shrink, say so and give the likely reason (nothing was pruned, or the prune freed little).

## When it fails
- `Virtual Disk Service error: The service failed to initialize`: restart Windows without opening Docker Desktop, then repeat step 4.
- Windows 11 Home has no `Optimize-VHD` (Hyper-V module), so `diskpart` is the route.
- Leave sparse VHD (`--allow-unsafe`) off; Microsoft flags it as a data-corruption risk.

## Prevention
Cap the build cache in Docker Desktop → Settings → Docker Engine:
```json
{ "builder": { "gc": { "enabled": true, "defaultKeepStorage": "10GB" } } }
```
