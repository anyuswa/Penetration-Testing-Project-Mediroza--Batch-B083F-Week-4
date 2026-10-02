# Mediroza Hospital | Penetration Testing Portfolio

**An authorised educational assessment documented from reconnaissance through client reporting.**

![Assessment: educational](https://img.shields.io/badge/Assessment-Educational-167e8c)
![Milestones: M1-M4](https://img.shields.io/badge/Milestones-M1--M4-132d49)
![Publication: sanitised](https://img.shields.io/badge/Publication-Sanitised-22863a)

| Project field | Details |
| --- | --- |
| Analyst | Asanda Lloyd Nyuswa |
| Programme | Networkwalks, Cybersecurity Internship |
| Batch / assignment | B083 / Week 4 |
| Engagement | Educational black-box web application assessment |
| Evidence period | 28-30 September 2026 |
| Report date | 1 October 2026 |
| Publication | Sanitised portfolio; confidential originals excluded |

## Project overview

The supplied assessment evidence supports patient-portal access following crafted login input, recovery of three password-protected reports, and discovery of an exposed archived SQL backup. The recovered dataset contains 30 employee salary records and 10 shareholder records. This portfolio explains the evidence, business impact, remediation and limitations without publishing the sensitive records or reusable access material.

**Overall assessed risk: Critical.** Ratings are qualitative, based on this exercise's evidence. They are not CVSS scores and do not establish an actual malicious breach.

## Read the project

- [Complete sanitised report](reports/REPORT.md)
- [Scope and authorisation boundaries](docs/SCOPE.md)
- [Methodology and tool coverage](docs/METHODOLOGY.md)
- [Evidence register](evidence/EVIDENCE_INDEX.md)
- [Findings](findings/README.md)
- [Remediation and retest plan](docs/REMEDIATION.md)
- [Milestone outcomes](docs/MILESTONES.md)
- [Data handling and limitations](docs/DATA_HANDLING.md)
- [GitHub upload instructions](docs/GITHUB_SETUP.md)

## Findings at a glance

| ID | Finding | Risk | Milestone | Status |
| --- | --- | --- | --- | --- |
| [F01](findings/F01.md) | SQL-style authentication bypass | High | M1 | Open |
| [F02](findings/F02.md) | Recoverable passwords on confidential PDFs | High | M2 | Open |
| [F03](findings/F03.md) | Internal backup location leaked in PDF metadata | Medium | M3 | Open |
| [F04](findings/F04.md) | Public directory index and confidential SQL backup | Critical | M3 | Open |

## Demonstrated skills

Web reconnaissance, HTTP interpretation, Burp Suite request analysis, evidence preservation, protected-document analysis, metadata investigation, SQL record interpretation, risk assessment and professional reporting.

## Milestone outcomes

| Milestone | Required outcome | Evidence-based result |
| --- | --- | --- |
| M1 | Retrieve three confidential PDFs | Files supplied; login response and portal screenshots support access |
| M2 | Recover the contents of all three PDFs | Recovery screenshots and successful local password verification |
| M3 | Find employee salaries and shareholder details | Archive index/download evidence and complete supplied SQL extracts |
| M4 | Produce a professional client report | Five-section report with evidence, risk ratings and remediation |

## Repository layout

| Path | Purpose |
| --- | --- |
| `reports/` | Sanitised professional report |
| `findings/` | Four individual finding records |
| `docs/` | Scope, methodology, milestones, remediation and publishing guide |
| `evidence/` | Screenshot index and inventory covering all 64 source files |
| `data/` | Aggregate outcomes and remediation CSV files |
| `scripts/` | Offline repository and artifact-integrity checks |
| `.github/` | Validation workflow and finding/retest issue templates |

## Local checks

Python 3.11 or later; no third-party packages or target network access required.

```bash
python scripts/check_repository.py
```

The integrity utility can compare the original supplied folder against the source manifest locally. Run it only on your own local evidence copy; no upload is performed.

```bash
python scripts/verify_evidence.py /path/to/Project
```

## Evidence and publication

Every supplied source artifact is accounted for in the inventory. Original screenshots, patient PDFs, salary/name tables, password hashes, raw requests and the confidential client PDF are deliberately outside this public repository. The downloadable delivery package preserves these in a separate confidential reference folder.

The assignment brief establishes educational testing permission. It does not establish permission to publish confidential data. Public evidence is therefore represented by descriptions, aggregate results and file integrity references. No retest has been performed and findings remain open.

## Licence

Original documentation and offline scripts in this repository are licensed under the MIT licence. The licence does not cover the client's data, original project brief, third-party tools, trademarks, screenshots or confidential source artifacts.
