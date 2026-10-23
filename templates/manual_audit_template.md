# Manual Accessibility Audit: [Product / Page Name]

| Field | Value |
|---|---|
| Auditor | [Name], DHS Trusted Tester (certification ID: [ ]) |
| Date | [YYYY-MM-DD] |
| Standard | WCAG 2.2 Level A/AA; Revised Section 508 (WCAG 2.0 A/AA by reference) |
| Test process | DHS Trusted Tester [version] / ICT Baseline |
| Scope (URLs / screens / documents) | [list] |
| Automated pre-scan | `a508` report: [link] |

## Test environment
| Assistive technology | Version | Browser / OS |
|---|---|---|
| JAWS | [ ] | Chrome [ ] / Windows [ ] |
| NVDA | [ ] | Firefox [ ] / Windows [ ] |
| VoiceOver (macOS) | macOS [ ] | Safari [ ] |
| VoiceOver (iOS) | iOS [ ] | Safari |
| Keyboard only | n/a | [ ] |
| Zoom / reflow | 200% / 400% at 1280px | [ ] |

Result key: **Pass** · **Fail** · **DNA** (Does Not Apply) · **NT** (Not Tested)

## 1. Keyboard and focus
| ID | Check | WCAG | Result | Notes |
|---|---|---|---|---|
| K-1 | Every function works with Tab / Shift+Tab / Enter / Space / arrow keys | 2.1.1 | | |
| K-2 | No keyboard trap; focus can always leave a component (modals, embeds) | 2.1.2 | | |
| K-3 | Focus order keeps meaning and operation | 2.4.3 | | |
| K-4 | Focus indicator is always visible | 2.4.7 | | |
| K-5 | Focused item is not hidden by sticky headers or footers | 2.4.11 (2.2) | | |
| K-6 | Single-key shortcuts can be turned off or remapped | 2.1.4 | | |
| K-7 | Focus and input don't cause unexpected context changes | 3.2.1, 3.2.2 | | |

## 2. Screen reader checks
Run each check in **JAWS + Chrome**, **NVDA + Firefox**, and **VoiceOver + Safari**.

| ID | Check | WCAG | JAWS | NVDA | VO | Notes |
|---|---|---|---|---|---|---|
| SR-1 | Page title is announced and describes the page | 2.4.2 | | | | |
| SR-2 | Headings list (Insert+F6 / NVDA+F7 / VO Rotor) shows a logical outline | 1.3.1, 2.4.6 | | | | |
| SR-3 | Landmarks (main, nav, banner, contentinfo) are present and labeled | 1.3.1, 2.4.1 | | | | |
| SR-4 | Images: meaningful ones have equivalent alt text, decorative ones are ignored | 1.1.1 | | | | |
| SR-5 | Form fields announce label, role, required state, and instructions | 1.3.1, 3.3.2, 4.1.2 | | | | |
| SR-6 | Errors are announced and linked to their fields; suggestions are given | 3.3.1, 3.3.3 | | | | |
| SR-7 | Custom widgets (tabs, menus, accordions, dialogs) announce name, role, and state changes | 4.1.2 | | | | |
| SR-8 | Status messages are announced without moving focus (live regions) | 4.1.3 | | | | |
| SR-9 | Data tables announce header and cell relationships | 1.3.1 | | | | |
| SR-10 | Links are meaningful in the links list | 2.4.4 | | | | |
| SR-11 | Language changes are announced or pronounced correctly | 3.1.1, 3.1.2 | | | | |
| SR-12 | Reading order (virtual cursor) matches the visual order | 1.3.2 | | | | |

## 3. Visual and sensory
| ID | Check | WCAG | Result | Notes |
|---|---|---|---|---|
| V-1 | Text contrast is ≥ 4.5:1 (≥ 3:1 for large text) | 1.4.3 | | |
| V-2 | UI component and graphic contrast is ≥ 3:1 | 1.4.11 | | |
| V-3 | Color is not the only way information is shown | 1.4.1 | | |
| V-4 | 200% zoom works without loss; content reflows at 320 CSS px | 1.4.4, 1.4.10 | | |
| V-5 | Text-spacing override causes no loss of content | 1.4.12 | | |
| V-6 | Targets are ≥ 24×24 CSS px or have enough spacing | 2.5.8 (2.2) | | |
| V-7 | Hover and focus content can be dismissed, hovered, and stays visible | 1.4.13 | | |

## 4. Multimedia and timing
| ID | Check | WCAG | Result | Notes |
|---|---|---|---|---|
| M-1 | Prerecorded video has accurate synchronized captions | 1.2.2 | | |
| M-2 | Audio description or a media alternative is provided | 1.2.3, 1.2.5 | | |
| M-3 | Auto-playing or moving content can be paused | 1.4.2, 2.2.2 | | |
| M-4 | Time limits can be adjusted or extended | 2.2.1 | | |
| M-5 | Nothing flashes more than 3 times per second | 2.3.1 | | |

## 5. WCAG 2.2 additions
| ID | Check | WCAG | Result | Notes |
|---|---|---|---|---|
| N-1 | Dragging has a single-pointer alternative | 2.5.7 | | |
| N-2 | Help mechanisms appear in a consistent location | 3.2.6 (A) | | |
| N-3 | Users aren't asked to re-enter information they already gave | 3.3.7 (A) | | |
| N-4 | Login doesn't depend on a cognitive function test (or offers an alternative) | 3.3.8 | | |

## 6. Documents (PDF / Office) linked from scope
| ID | Check | Result | Notes |
|---|---|---|---|
| D-1 | Tagged PDF, title, and language set; logical reading order | | |
| D-2 | Figures have alt text; artifacts are marked | | |
| D-3 | Tables have header cells; lists are tagged | | |

## Issue log
| # | Location | Description | Steps to reproduce | AT / browser | WCAG SC | TT test | Severity | Recommendation |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |

## Summary
- Criteria passed: [ ] · failed: [ ] · DNA: [ ]
- Overall conformance: [Supports / Partially Supports / Does Not Support]
- Key risks and remediation priorities: [ ]
