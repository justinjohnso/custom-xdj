# VirtualDJ Skin Architecture Modernization Research

This document addresses the research and strategic plan for migrating the `custom-xdj` skin from the VirtualDJ 8 legacy XML spec to the modern VirtualDJ 2026 engine spec.

## 1. Why was the XML built to the VirtualDJ 8 legacy spec?
According to the project's foundational documents (`IDEA.md` and `README.md`), the skin was deliberately built against the VDJ 8 engine spec to ensure absolute stability and compatibility on older, dedicated hardware builds. By utilizing legacy `<panel>` rendering hooks, local variables (e.g., `'$show_browser'`), and flat absolute coordinates, the skin bypassed modern CPU/GPU-heavy layout engines, ensuring it ran flawlessly on underpowered embedded processors driving 8.8" stretched displays.

## 2. What trade-offs are we currently making due to this version limitation?
By conforming to the VDJ 8 spec, the project suffers from several severe architectural constraints:
* **Rigid Absolute Positioning:** Without modern container tags, every element is anchored to global X/Y coordinates. Moving a deck or shifting the browser view requires manually recalculating and updating the coordinates of every single child element.
* **Lack of `<group>` Tags & Relative Scaling:** We cannot group logical UI blocks (e.g., `<group name="leftdeck">`) to apply offsets (`x="+50"`), relative positioning, or simple mathematical scaling (e.g., `x="1920/2+10"`). 
* **SVG Deficiencies:** Legacy skins rely on a raster PNG spritesheet (`2Decks.png`). It cannot dynamically scale without pixelation and blocks us from using crisp, vector-based SVG graphics for high-PPI displays.
* **Poor Conditional Logic:** We are stuck using legacy `<panel visibility="...">` hacks to toggle UI states (like the browser view), leading to verbose XML structures.
* **Lack of Native Stems & PadFX:** Legacy XML predates VirtualDJ's Real-Time Stems 2.0 (2020-2026). It lacks native support for `stem_pad`, `padfx`, and `ModernEQ` mappings out of the box.

## 3. What becomes possible by broadening our syntax to the modern spec (VDJ 2021+)?
Upgrading to the modern skin architecture unlocks several high-end capabilities:
* **`<group>` and `<define>` Tags:** We can create DRY (Don't Repeat Yourself) XML. We can declare reusable classes (`<define class="stem_button">`) and group elements into logical, relatively positioned containers (`<group name="leftdeck" x="+0">`).
* **Native SVG Rendering:** We can strip out the `2Decks.png` dependency and use XML-embedded or linked SVG files. UI elements (knobs, faders, stems pads) will be endlessly scalable and razor-sharp on 220+ PPI stretched displays.
* **Native Stems & ModernEQ UI:** We can introduce Stems 2.0 UI components, allowing the user to view and trigger Stem separations (Vocals, Instrumental, Bass, Kick, HiHat) directly from the skin.
* **Advanced Stems FX (PadFX):** We can embed FX chains targeted at specific stems (e.g., `padfx "echo out" 80% 1bt "stemfx:vocal"`), emulating advanced standalone hardware features.

## 4. Brainstorm & Refactoring Plan Loop
**Goal:** Provide an uncompromising XDJ/standalone experience with Stems, FX, and native VDJ 2026 functionality on an 8.8" stretched display.

* **Step 1: Containerization (The `<group>` Refactor)**
  * Break down the monolithic absolute XML into structured `<group>` nodes: `LeftDeck`, `RightDeck`, `CenterMixer`, and `BrowserView`. 
  * Convert global absolute X/Y positions to relative `x="+..." y="+..."` coordinates inside their respective groups.
* **Step 2: Vectorization (SVG Integration)**
  * Deprecate the `2Decks.png` spritesheet.
  * Implement `<svg>` backgrounds, waveforms, and button states to guarantee ultra-crisp UI rendering on the high-density display.
* **Step 3: Stems Performance Pad Integration**
  * Introduce a minimalistic "Stems" panel below the waveforms or track metadata.
  * Map on-screen Stems toggle buttons using VDJ 2026 script logic (e.g., `stem_pad 'vocal'` to isolate/mute vocals and `stem_pad 'instru'` for instrumentals).
* **Step 4: Hardware-Style Stems FX (PadFX)**
  * Add dedicated "Vocal Echo" and "Instru Echo" buttons mapped to `deck 1 padfx "Echo" 50% "stemfx:vocal" smart_pressed`.
  * Ensure these elements fit the minimalist "XDJ" aesthetic without cluttering the screen.
* **Step 5: ModernEQ Routing**
  * Map the skin's EQ visual feedback to display VDJ's ModernEQ (where high/mid/low knobs dynamically control stems instead of traditional frequencies).

*(This plan will be appended to `.specs/PLAN.md` as Phase 8).*