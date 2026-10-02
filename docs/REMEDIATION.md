# Remediation and retest plan

| Finding | Priority | Suggested owner | Corrective action | Closure evidence |
| --- | --- | --- | --- | --- |
| F04 | Immediate | Web operations and data owner | Remove archive from public storage; deny direct delivery; disable listing; review caches and logs | Known URL inaccessible; backup excluded from deployment artifacts |
| F01 | Immediate | Application team | Parameterised account queries, secure password verification, session renewal and per-report authorisation | Invalid login fails; cross-account report access rejected |
| F02 | Within 7 days | Clinical/application systems | Secure authenticated delivery; replace exposed copies; strong unique secrets if needed | File access and password-generation review pass |
| F03 | Within 7 days | Document platform owner | Metadata allowlist, internal comment removal and historical-file review | Generated documents contain no operational hints |
| All | Within 30 days | Security and operations | Backup retention and deployment exposure checks | Controls documented and verified |

Preserve access logs and investigate historical downloads to determine the exposure window. The client's privacy/legal functions should assess any necessary notifications; this evidence review does not establish a third-party breach.

## Retest recording

Use authorised test accounts and approved assets. Record date, tester, affected finding, test inputs, observed responses and outcome. Mark a finding fixed only after its acceptance criteria pass. Configuration changes alone are insufficient closure proof.
