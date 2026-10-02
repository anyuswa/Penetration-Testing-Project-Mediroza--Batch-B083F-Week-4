# Methodology

| Stage | Activity | Tools evidenced | Result / qualification |
| --- | --- | --- | --- |
| Reconnaissance | Domain, DNS and technology review | WHOIS, nslookup, whatweb, curl, dnsrecon | DNS and HTTP/service observations captured |
| Service review | Web port and TLS inspection | Nmap / Zenmap | Web services observed; banners alone do not prove vulnerabilities |
| WAF review | Fingerprinting attempt | wafw00f | Failed on DNS resolution; no reliable WAF conclusion |
| Enumeration | Content discovery attempt | ffuf | Log shows nonexistent wordlist; success not claimed |
| Authentication | Form inspection and input-response comparisons | Browser source, Burp Suite Intruder | Crafted login input, portal redirect and portal screenshot |
| Document recovery | Protected-file analysis | PDF recovery interface, supplied hash artifacts, qpdf | Three files opened with recovered passwords |
| Metadata | Properties and embedded-file inspection | ExifTool, pdfinfo, pdfdetach, strings | Internal backup clue; no embedded files reported |
| Archive analysis | Index, download and local SQL review | curl, file, grep, sed | Staff and shareholder data disclosed |
| Reporting | Evidence correlation and calculations | Local Python tools | PDF recovery verified and totals recalculated |

## Evidence chain

Authentication input variation led to portal access and three report downloads. Local password recovery made the reports readable. Metadata in the third report disclosed a legacy archive location. The directory index revealed an SQL file, which contained HR and shareholder records.

## Accuracy constraints

The password recovery interface is evidenced, but the screenshots do not prove John the Ripper or Hashcat was used. A sqlmap launcher icon is insufficient evidence of a sqlmap run. The general assignment guide contains examples and is not a log of executed steps.

HTTP technology and certificate outputs differ across requests. Challenge responses, request routing and time may explain this, but the cause is unverified. Do not turn these variations into unsupported security findings.
