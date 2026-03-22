from dataclasses import dataclass, field
from typing import List, Optional, Dict

SEVERITY_ORDER = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
    "info": 4,
    "default": 5
}

SEVERITY_UI = {
    "critical": {"label" :"Critiical", "colour": "#6E0D25"},
    "high": {"label" :"High", "colour": "#DB4C40"},
    "medium": {"label" :"Medium", "colour": "#C36F09"},
    "low": {"label" :"Low", "colour": "#143642"},
    "info": {"label" :"Info", "colour": "#85877C"},
    "default": {"label" :"Default", "colour": "#5F6062"},
}

@dataclass
class Finding:
    category: str
    title: str
    detail: str
    severity: str

@dataclass
class Report:
    filename: str
    meta: Dict[str, str] = field(default_factory=dict)
    findings: List[Finding] = field(default_factory=list)
    def counts(self):
        counts = {sev: 0 for sev in SEVERITY_ORDER}
        for f in self.findings:
            counts[f.severity] += 1
        return counts