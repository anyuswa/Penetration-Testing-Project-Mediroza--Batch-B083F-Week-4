# Data handling and evidence limitations

## Public material

This repository publishes analytical documentation, descriptions of the evidence, source hashes and aggregate results. It excludes original patient reports, laboratory result images, employee names and individual salaries, shareholder names, national IDs, phone numbers, email addresses, recovered passwords, password-verification hashes, session cookies, live target addresses and exploit payload strings.

The complete confidential report and all 64 original source files remain in the delivery package's separate reference folder. A public GitHub repository must contain only the `mediroza-pentest-portfolio` folder. GitHub web uploads do not enforce `.gitignore`; do not upload the entire delivery package.

## Evidence limitations

- No exported Burp project or complete raw HTTP transaction collection is supplied.
- A portal redirect and subsequent report-list screenshot support bypass; source code is needed to confirm the exact query implementation.
- No standalone original SQL backup is supplied. SQL text captures, screenshots and formatted tables support the data conclusions.
- SHA-256 hashes identify the uploaded artifacts at report preparation time; original collection-time custody is not established.
- The dump header dates the backup to August 2019, while employee joining dates include later dates through February 2020. The records do not establish current salaries or ownership.
- The earlier limited salary PDF is superseded by the complete SQL extract and full salary table PDF.
- AI conversation screenshots supply context and are not independent proof.
- Timestamps include multiple timezone offsets; no exact unified timeline is asserted.
- All findings are open; remediation or retest is not evidenced.

## Handling updates

Retain originals in restricted storage, preserve integrity hashes, and share confidential proof only with the client/instructor. Replace public evidence descriptions only after checking publication permission and removing sensitive content. Files committed in the past remain in Git history even after deletion.
