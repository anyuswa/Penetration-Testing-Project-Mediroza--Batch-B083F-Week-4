# Screenshot evidence register

All 45 original screenshots are retained in the confidential reference package. Public copies are withheld because screenshots contain patient records, personal data, passwords or session values. IDs match the confidential report.

| ID | Original source path | Evidence role |
| --- | --- | --- |
| E01 | `Milstone1&2/Screenshot 1.png` | WHOIS output: domain reconnaissance. |
| E02 | `Milstone1&2/Screenshot 10.png` | Nmap: open 80/443; service and TLS observations. |
| E03 | `Milstone1&2/Screenshot 11.png` | Nmap HTTP headers and TLS output. |
| E04 | `Milstone1&2/Screenshot 12.png` | HTTP/HTTPS header response observations. |
| E05 | `Milstone1&2/Screenshot 13.png` | HTTP response and redirect/challenge checks. |
| E06 | `Milstone1&2/Screenshot 14.png` | ffuf failed because the specified wordlist was absent. |
| E07 | `Milstone1&2/Screenshot 16.png` | Staff login form HTML inspection. |
| E08 | `Milstone1&2/Screenshot 17.png` | Burp request preparation for staff login; no successful staff access established. |
| E09 | `Milstone1&2/Screenshot 18.png` | Burp request configuration; preparation only. |
| E10 | `Milstone1&2/Screenshot 19.png` | Burp and patient login HTML inspection. |
| E11 | `Milstone1&2/Screenshot 2.png` | whatweb: LiteSpeed fingerprint and 403/redirect observations. |
| E12 | `Milstone1&2/Screenshot 20.png` | Patient portal login form source. |
| E13 | `Milstone1&2/Screenshot 21.png` | Intruder payload configuration; preparation evidence. |
| E14 | `Milstone1&2/Screenshot 22.png` | Intruder results: response variation for crafted inputs. |
| E15 | `Milstone1&2/Screenshot 23.png` | F01: crafted username with 302 and Location: [patient portal]. |
| E16 | `Milstone1&2/Screenshot 24.png` | M1/F01: portal lists the three downloadable reports. |
| E17 | `Milstone1&2/Screenshot 25.png` | Login page containing crafted username; corroborating context. |
| E18 | `Milstone1&2/Screenshot 3.png` | nslookup: target resolved to 199.188.201.16. |
| E19 | `Milstone1&2/Screenshot 4.png` | HTTP header redirect observation. |
| E20 | `Milstone1&2/Screenshot 5.png` | wafw00f failed on name resolution; no reliable WAF conclusion. |
| E21 | `Milstone1&2/Screenshot 6.png` | DNS reconnaissance output. |
| E22 | `Milstone1&2/Screenshot 7.png` | Zenmap subnet scan: broader than domain scope; other-host results excluded. |
| E23 | `Milstone1&2/Screenshot 8.png` | Zenmap subnet topology: scope limitation, not a reported vulnerability. |
| E24 | `Milstone1&2/Screenshot 9.png` | Nmap service scan. |
| E25 | `Milstone1&2/p1.png` | M2: readable first patient pathology report. |
| E26 | `Milstone1&2/p2.png` | M2: readable second patient pathology report. |
| E27 | `Milstone1&2/p3.png` | M2: readable third patient pathology report. |
| E28 | `Milstone1&2/passwordhash1_p1.png` | M2/F02: first PDF password recovery success. |
| E29 | `Milstone1&2/passwordhash2_p2.png` | M2/F02: second PDF password recovery success. |
| E30 | `Milstone1&2/passwordhash3_p3.png` | M2/F02: third PDF password recovery success. |
| E31 | `Milstone3/1.png` | Original encrypted PDF metadata inspection. |
| E32 | `Milstone3/10.png` | F04: download, ASCII file identification and table inspection. |
| E33 | `Milstone3/12.png` | SQL sections showing staff and shareholder fields. |
| E34 | `Milstone3/13.png` | M3: complete staff salary extract and shareholder data. |
| E35 | `Milstone3/14.png` | M3: complete shareholder extract. |
| E36 | `Milstone3/2.png` | AI guidance on metadata inspection; contextual advice only. |
| E37 | `Milstone3/3.png` | qpdf installation and document decryption commands. |
| E38 | `Milstone3/4.png` | F03: strings inspection reveals [legacy archive]/ backup comment. |
| E39 | `Milstone3/5.png` | AI discussion of metadata clue; not independent proof. |
| E40 | `Milstone3/6.png` | F04: HTTP 200 [legacy archive]/ autoindex links the SQL backup. |
| E41 | `Milstone3/7.png` | AI interpretation of archive clue; not independent proof. |
| E42 | `Milstone3/8.png` | F04: curl download completion, 6,346 bytes. |
| E43 | `Milstone3/9.1.png` | SQL: remaining staff records and shareholder schema. |
| E44 | `Milstone3/9.2.png` | SQL: ownership records and end of dump. |
| E45 | `Milstone3/9.png` | Downloaded SQL: header, staff schema and initial records. |
