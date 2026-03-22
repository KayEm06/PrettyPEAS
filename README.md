# PrettyPEAS
PrettyPEAS is a command-line tool written in Python designed to take raw LinPEAS output and generate clean, structured, web-ready reports.

The purpose of PrettyPEAS is to remove all noise from default and informational findings that obfuscate vulnerabilities deserving of attention.

PrettyPEAS has been written with sensitive regex rules to minimise output with false positives and rank findings to minimise false negatives.

## Features (WIP)

- Import any LinPEAS report through the CLI.
- HTML reports are strucutred on a hierarchy displaying Crtitical, High, Medium, Low, Info, and Default-severity findings respectively.
- Findings are assigned corresponding colour-coded markers based on severity classification.
- Option to hide Low, Info, and Default findings to focus on medium and high-severity findings.
- Collapse and expand sections to follow a systematic approach for privilege escalation.
- Export reports to PDF for easy, future reference.
