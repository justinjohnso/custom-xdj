# Agent Rules for VirtualDJ XDJ-480 Skin

This document outlines the strict technical constraints and design guidelines for LLMs and autonomous agents contributing to the `custom-xdj` skin project.

## 1. Resolution & Hardware Constraints
- **Target Display:** 8.8" stretched bar display at **1920x480** resolution.
- **Design Philosophy:** Minimalist, zero-clutter, hardware-centric layout. Emulate the Pioneer XDJ standalone workflow. Do not add standard software GUI elements (like window borders, excessive buttons, or standard drop-downs).
- **Visibility:** Consider high pixel density (~220 PPI). Avoid extremely small fonts or click targets, keeping in mind that the user will view this on a hardware-mounted display.

## 2. XDJ Workflow Emulation
- **Performance View:** Must feature edge-to-edge parallel stacked waveforms, track metadata, time, pitch, and key. 
- **Browser View:** A full-screen library browser.
- **Toggle Mechanism:** Switching between Performance and Browser views must be handled via a single hardware-style toggle, utilizing local state variables (e.g., `'$show_browser'`).

## 3. Legacy Engine Compliance (VDJ 8)
- **Engine Spec:** All XML code must be written strictly against the legacy **VirtualDJ 8** engine specification to guarantee stability on older, dedicated hardware setups.
- **Forbidden Syntax:** Do **not** use the modern `<group>` syntax introduced in VirtualDJ 2021+ engines.
- **Approved Syntax:** Rely exclusively on older `<panel>`, `<visual>`, and `<rectangle>` rendering hooks for constructing the interface geometry.

## 4. File Structure & Parser Requirements
- **Root Header Declaration:** The skin's XML file (e.g., `XDJ480.xml`) must declare a valid sprite sheet in its root header: `<Skin image="2Decks.png" ...>`.
- **Mandatory Sprite Sheet:** Even if all UI elements are rendered dynamically via XML, the `2Decks.png` file must physically exist in the skin's directory. Removing it or deleting the root declaration will cause a fatal parser crash.
- **Flat Architecture:** VirtualDJ's legacy parser is highly strict. Keep `XDJ480.xml` and `2Decks.png` in a single, flat directory. Do not place images or assets in subfolders.

## 5. Repository & Git Workflow
- **Commit Messages:** Commit messages must be written entirely in **lowercase**. They should be direct and descriptive, without conventional prefixes (like "feat:", "fix:"). Example: `fix ui ghosting and add play buttons`.
- **Artifacts:** Keep the root directory clean. Planning files, tasks, and scratchpads belong in the `.specs/` directory.
- **Temporary Scripts:** Any ad-hoc Python or shell scripts written by the AI to parse, edit, or validate files must be written directly to the `.specs/scripts/` directory. Do not write temporary scripts to the root directory.
