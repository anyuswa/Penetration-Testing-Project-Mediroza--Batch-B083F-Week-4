# Penetration Testing Report | Public Portfolio Edition

**Analyst:** Asanda Lloyd Nyuswa  
**Assignment:** Networkwalks B083, Week 4, Milestone 4  
**Evidence period:** 28-30 September 2026  
**Report date:** 1 October 2026  
**Version:** 1.0 | Sanitised  
**Overall assessed risk:** Critical

## 01 Executive Summary

The supplied evidence demonstrates a connected confidentiality exposure: a crafted patient-login input was followed by portal access, three encrypted patient reports were recovered using predictable passwords, and an internal PDF metadata note led to a public archived SQL backup. The supplied database records include 30 employees and 10 shareholders.

The strongest direct exposure is the archive, assessed Critical because it disclosed a bulk sensitive dataset through web delivery. Login bypass and recoverable PDF passwords are assessed High. Metadata leakage is assessed Medium because it assisted discovery but did not itself grant access.

Data reading and download are supported. Host takeover, remote code execution, database modification and a malicious third-party breach are not established. Findings remain open. Immediate containment should remove public archive delivery and correct login and report authorisation.

## 02 Scope and Methodology

The original brief states permission for a single educational target and excludes social engineering, denial of service and other systems. The planned duration is five days. The evidence covers reconnaissance, web request analysis, document recovery, metadata analysis and SQL interpretation. No new target requests were made for this repository.

See [scope](../docs/SCOPE.md), [methodology](../docs/METHODOLOGY.md) and [limitations](../docs/DATA_HANDLING.md). Two broader-subnet scan screenshots are explicitly excluded from the domain findings.

## 03 Findings and Proof of Exploitation

### F01 | SQL-style authentication bypass

**Risk:** High | **Milestone:** M1 | **Status:** Open

The Burp Intruder evidence records a POST to [patient login endpoint] with a crafted username (value withheld). The selected response is HTTP/2 302 Found with Location: [patient portal]. The later browser screenshot displays a report portal containing three pathology reports with Download buttons.

An unauthorised user could gain portal access and retrieve patient documents. Three report files are present in the submitted evidence. Broader account access, write access and arbitrary database extraction through this endpoint are not demonstrated.

Evidence: E15, E16. [Full finding](../findings/F01.md).

### F02 | Recoverable passwords on confidential PDFs

**Risk:** High | **Milestone:** M2 | **Status:** Open

The original artifacts use Standard PDF protection identified in ExifTool output as V2.3 (128-bit). Recovery screenshots show passwords for all three files. The copied qpdf output records decryption without errors after installation. During report preparation, each recovered password successfully decrypted its corresponding supplied PDF.

All three pathology reports became readable, exposing patient identities, birth dates, identifiers, laboratory results and referring clinicians. The report summaries below retain enough information to demonstrate recovery without repeating every personal field.

Evidence: E28, E30. [Full finding](../findings/F02.md).

### F03 | Internal backup location leaked in PDF metadata

**Risk:** Medium | **Milestone:** M3 | **Status:** Open

The third PDF contains an internal author identifier and an internal comment disclosing a legacy backup directory. This was recorded through metadata/string inspection and independently confirmed in the locally decrypted uploaded PDF. The clue led to the [legacy archive]/ directory response.

The leak reduced the effort required to locate the archive that contained HR and shareholder data. It does not itself grant server access; the separate public backup exposure is rated under F04.

Evidence: E38, E40. [Full finding](../findings/F03.md).

### F04 | Public directory index and confidential SQL backup

**Risk:** Critical | **Milestone:** M3 | **Status:** Open

The supplied curl output for [legacy archive]/ shows HTTP/2 200 and Index of [legacy archive]/, linking the SQL backup. Download evidence records 6,346 bytes; file inspection identifies ASCII text. The SQL excerpts show staff and shareholders tables with 30 employees and 10 shareholders.

Bulk disclosure includes names, jobs, departments, emails, phones, national IDs, monthly salaries, joining dates and ownership details. This is direct evidence of confidential data exposure, with no database credentials or host takeover demonstrated.

Evidence: E40, E32. [Full finding](../findings/F04.md).

The [evidence register](../evidence/EVIDENCE_INDEX.md) accounts for all 45 screenshots. Public entries describe original evidence; they are not replacement screenshots. Local parsing independently verified that all three supplied encrypted PDFs open with the recovered passwords and contain one page each.

## 04 Risk Rating

| Finding | Rating | Justification |
| --- | --- | --- |
| F01 | High | Portal access follows crafted login input; sensitive report access is supported, broader database control is not |
| F02 | High | All three patient files became readable with recovered predictable passwords; obtaining the files is a prerequisite |
| F03 | Medium | Internal metadata reduces discovery effort; separate archive controls cause the bulk disclosure |
| F04 | Critical | Direct web delivery exposes the supplied HR and shareholder dataset without authentication shown in the command evidence |

Ratings are qualitative, not CVSS. Overall risk follows the highest demonstrated impact rather than adding ratings. Service banners, failed WAF detection and failed ffuf attempts are observations, not additional validated findings.

## 05 Recommendations and Remediation

Immediately remove the backup from public origin/cache/deployment storage and correct login query handling and per-report authorisation. Replace exposed weakly protected reports and adopt secure document delivery. Strip operational metadata, implement backup/deployment safeguards and review access logs.

See the [actionable remediation plan](../docs/REMEDIATION.md) for owners, priorities and closure criteria. Retest the precise affected assets with authorised accounts and retain request/response proof. No finding is marked fixed until the acceptance criteria pass.

## Data summary

| Metric | Supplied dataset |
| --- | --- |
| Patient PDFs recovered | 3 |
| Employee records | 30 |
| Total monthly salaries | R2,027,000 |
| Mean monthly salary | R67,566.67 |
| Shareholders | 10 |
| Total ownership | 100% |
| Total shares | 1,000,000 |
| Ordinary / preferential shares | 880,000 / 120,000 |

These are historical training-dataset values. The backup's stated date conflicts with some joining dates. Individual identities, salaries, medical results and access material are excluded; the confidential report preserves the full required M3 schedules.

## Source and provenance

The Module 4 instructions require the five sections above. All 64 uploaded source files are listed in the [source inventory](../evidence/SOURCE_INVENTORY.md) and hashed in the manifest. AI conversations and the reusable guide are contextual material. Original SQL text and screenshots support record disclosure; no standalone SQL backup was supplied.
