# Automated Accessibility Audit: file:///.../samples/broken.html

- **Scanned:** 2026-10-23T20:25:26.955Z
- **Engine:** axe-core 4.14.0, WCAG 2.2 A/AA tag set
- **Violations:** 7 rules (critical: 3, serious: 4)
- **Needs manual review (axe incomplete):** 0

> Automated testing finds only part of the WCAG failures on a page. Use this report alongside the manual Trusted Tester / screen reader checks in `templates/manual_audit_template.md`.

## Findings

| # | Rule | Impact | WCAG 2.2 SC | Section 508 | Trusted Tester | Elements |
|---|---|---|---|---|---|---|
| 1 | [button-name](https://dequeuniversity.com/rules/axe/4.14/button-name?application=axeAPI) | critical | 4.1.2 Name, Role, Value (A) | Yes | 5.C, 9.A | 1 |
| 2 | [image-alt](https://dequeuniversity.com/rules/axe/4.14/image-alt?application=axeAPI) | critical | 1.1.1 Non-text Content (A) | Yes | 6.A | 1 |
| 3 | [select-name](https://dequeuniversity.com/rules/axe/4.14/select-name?application=axeAPI) | critical | 4.1.2 Name, Role, Value (A) | Yes | 5.C, 9.A | 1 |
| 4 | [color-contrast](https://dequeuniversity.com/rules/axe/4.14/color-contrast?application=axeAPI) | serious | 1.4.3 Contrast (Minimum) (AA) | Yes | 7.C | 1 |
| 5 | [document-title](https://dequeuniversity.com/rules/axe/4.14/document-title?application=axeAPI) | serious | 2.4.2 Page Titled (A) | Yes | 10.A | 1 |
| 6 | [html-has-lang](https://dequeuniversity.com/rules/axe/4.14/html-has-lang?application=axeAPI) | serious | 3.1.1 Language of Page (A) | Yes | 11.A | 1 |
| 7 | [target-size](https://dequeuniversity.com/rules/axe/4.14/target-size?application=axeAPI) | serious | 2.5.8 Target Size (Minimum) (AA) | No (WCAG 2.1/2.2 only) | - | 1 |

## Details

### 1. button-name: Buttons must have discernible text

- `button`

### 2. image-alt: Images must have alternative text

- `img`

### 3. select-name: Select element must have an accessible name

- `#course`

### 4. color-contrast: Elements must meet minimum color contrast ratio thresholds

- `p`

### 5. document-title: Documents must have <title> element to aid in navigation

- `html`

### 6. html-has-lang: <html> element must have a lang attribute

- `html`

### 7. target-size: All touch targets must be 24px large, or leave sufficient space

- `.main > a`
