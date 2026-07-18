# VirtualDJ XDJ-480

A hardware-focused, minimalist VirtualDJ skin tailored specifically for 8.8" (1920x480) stretched bar displays. Designed to strip away the software GUI and emulate the parallel waveform workflow of a Pioneer XDJ standalone unit.

### Features
*   **Hardware-Centric Layout:** Zero-clutter interface featuring track metadata, time, pitch, key, and edge-to-edge parallel stacked waveforms.
*   **XDJ Workflow:** A dedicated hardware-style toggle swaps the entire UI between the performance view and a full-screen library browser.
*   **Legacy Engine Compliance:** Built against the VDJ 8 engine spec to ensure stability on older, dedicated hardware builds.

---

### Installation

VirtualDJ's legacy skin parser is notoriously strict regarding archive structures and image mapping. Do not compress these files into a nested `.zip` archive, or the engine will throw an `Impossible to open skin` exception.

1. Clone or download this repository. Ensure `XDJ480.xml` and `2Decks.png` remain in the same flat directory (e.g., `XDJ480/`).
2. Move the entire folder into your active VirtualDJ skins directory:
   * **Windows:** `Documents\VirtualDJ\Skins` (or `%USERPROFILE%\AppData\Local\VirtualDJ\Skins` on newer clean installs).
   * **Mac:** `~/Documents/VirtualDJ/Skins` (or `~/Library/Application Support/VirtualDJ/Skins`).
3. Launch VirtualDJ, navigate to **Settings > Interface**, and select `XDJ 480 Hardware`.

---

### Display & Configuration Requirements

8.8" stretched displays have a very high pixel density (~220 PPI). You must configure your OS and VDJ to prevent rendering conflicts.

*   **Lock OS Scaling:** Go to your Windows/macOS display settings and force the scaling for the 8.8" monitor to exactly **100%**. If the OS auto-scales it to 125% or 150%, VirtualDJ will render the skin off-canvas.
*   **Legible Browser Text:** VDJ's default library text will look microscopic at this resolution. Open VDJ **Settings > Options**, search for `browserTextSize`, and increase the integer value until the track list is legible from your normal mixing position.

---

### Development Notes

This skin utilizes the `<panel>` rendering hooks and local variables (e.g., `'$show_browser'`) specific to the VDJ 8 parser, bypassing the modern `<group>` syntax of the 2021+ engines. 

The `2Decks.png` file must remain in the directory. Even though the UI geometry is generated strictly via XML `<visual>` and `<rectangle>` nodes, the legacy engine requires a valid sprite sheet declared in the `<Skin image="...">` root header. Stripping it will cause a fatal parser crash.