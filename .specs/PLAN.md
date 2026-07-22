# VirtualDJ Skin Refactor Plan (`virtualdj-skin.xml`)
**Target Resolution:** 1920x480
**Syntax Constraint:** Legacy VDJ 8 XML (`<panel>`, `<visual>`, `<rectangle>`, `<text>`, `<textzone>`)

## Phase 1: Preparation & Core Structure
- [ ] **1.1. Backup Existing File:** Create a copy of the current `virtualdj-skin.xml` before making changes.
- [ ] **1.2. Define Base Dimensions:** Ensure the root `<skin>` node has `width="1920"` and `height="480"`.
- [ ] **1.3. Global Variables Initialization:** Add startup actions to initialize view states (e.g., `$show_performance=1`, `$show_browser=0`, `$show_settings=0`).
- [ ] **1.4. Calculate Width Adjustments:** Account for the new 100px left sidebar. 
  - *Remaining horizontal space:* 1820px. 
  - *Updated Bottom Section distribution:* Deck 1 (650px), Mixer/Center (520px), Deck 2 (650px) instead of 700/520/700 to fit perfectly.

## Phase 2: Auxiliary Sidebar Navigation
- [ ] **2.1. Left Sidebar Background:** Create a `<rectangle>` or graphic at `x="0" y="0" width="100" height="480"`.
- [ ] **2.2. Navigation Buttons:** Add 3 vertical buttons (Performance, Browser, Settings).
- [ ] **2.3. View Toggling Logic:** Attach `<action>` scripts to the buttons to set the respective variable to `1` and the others to `0`.

## Phase 3: Main Performance View (Condition: `$show_performance=1`)
- [ ] **3.1. Waveform Restructuring (Top):**
  - Move stacked horizontal waveforms (Deck 1 and Deck 2) to `x="100" y="0" width="1820" height="240"`.
  - Wrap in a `<panel>` or apply visibility logic tied to `$show_performance`.
- [ ] **3.2. Deck 1 Info (Bottom Left):**
  - Create elements at `x="100" y="240" width="650" height="240"`.
  - Add Deck 1 `<text>` components for Time, BPM, Key, and Title.
- [ ] **3.3. Center/Mixer Info (Bottom Center):**
  - Create elements at `x="750" y="240" width="520" height="240"`.
  - Add Global/Mixer elements (crossfader, master volume, or Hotcues if desired).
- [ ] **3.4. Deck 2 Info (Bottom Right):**
  - Create elements at `x="1270" y="240" width="650" height="240"`.
  - Add Deck 2 `<text>` components for Time, BPM, Key, and Title.

## Phase 4: Browser View (Condition: `$show_browser=1`)
- [ ] **4.1. Browser Container:** Create a `<panel>` at `x="100" y="0" width="1820" height="380"` (leaving bottom 100px for mini-decks).
- [ ] **4.2. Folders View:** Add a `<folder>` node targeting folders (e.g., `x="110" y="10" width="500" height="360"`).
- [ ] **4.3. Songs View:** Add a `<browser>` node targeting tracks/songs (e.g., `x="620" y="10" width="1290" height="360"`).
- [ ] **4.4. Mini-Decks Integration:** Add a persistent `<panel>` at `y="380" height="100"` that is visible during `$show_browser=1` or `$show_settings=1`, displaying simplified track info (Title, BPM, Key, Time, and a mini Rhythmwave/playback bar) for both decks.

## Phase 5: Settings View (Condition: `$show_settings=1`)
- [ ] **5.1. Settings Container:** Create a `<panel>` at `x="100" y="0" width="1820" height="380"`.
- [ ] **5.2. Background & Text:** Add a `<rectangle>` for background and static `<text>` titles.
- [ ] **5.3. Setting Toggles:** Implement buttons mapped to skin options (e.g., toggle vinyl mode, show/hide key match).

## Phase 6: Polish & Legacy Syntax Compliance
- [ ] **6.1. Validation:** Ensure no modern VDJ `<group>` tags are used; rely solely on `<panel>` and direct visibility parameters (`visibility="$show_browser"`).
- [ ] **6.2. Z-Index Checking:** Confirm `<panel>` ordering so navigation sits above or below views correctly.
- [ ] **6.3. Live Test:** Load skin in VirtualDJ windowed at 1920x480 and verify toggles and layout alignment.