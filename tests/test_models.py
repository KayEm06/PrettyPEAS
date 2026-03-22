from prettypeas.models import Finding, Report

f1 = Finding(
    category="privesc",
    title = "Dangerous capabilities found on /usr/bin/python3.8",
    detail = "cap_setuid,cap_net_bind_service",
    severity = "high"
)

f2 = Finding(
    category="system",
    title = "Writable path: /var/tmp",
    detail = "/var/tmp can be written to by any user",
    severity = "low"
)

report = Report(filename="linpeas_report.out")

report.findings.append(f1)
report.findings.append(f2) 

print(report.counts())