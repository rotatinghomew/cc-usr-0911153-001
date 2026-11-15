from __future__ import annotations

import math
from typing import Any, Callable, Mapping

from orchard_grade.contracts.batches import DomainRecord, RuleResult, bounded, finite_number, normalized_text

RuleFunction = Callable[[DomainRecord, Mapping[str, Any]], RuleResult]

def _number(record: DomainRecord, field: str) -> float:
    value = record.payload.get(field)
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    if isinstance(value, (int, float)):
        return finite_number(value)
    text = normalized_text(value)
    if not text:
        return 0.0
    try:
        return finite_number(text)
    except ValueError:
        return float(sum(ord(ch) for ch in text) % 101)

def _context_number(context: Mapping[str, Any], key: str, default: float) -> float:
    try:
        return finite_number(context.get(key, default))
    except ValueError:
        return default

def _result(code: str, value: float, threshold: float, higher_is_better: bool, message: str, evidence: dict[str, Any]) -> RuleResult:
    distance = (value - threshold) if higher_is_better else (threshold - value)
    passed = distance >= 0
    scale = max(1.0, abs(threshold))
    score = bounded(0.5 + distance / (2.0 * scale))
    severity = 'info' if passed else ('critical' if score < 0.2 else 'error')
    return RuleResult(code, passed, score, severity, message, evidence)

def check_sweetness_brix_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_sweetness_brix_presence_threshold', 10.333)
    return _result('check_sweetness_brix_presence', adjusted, threshold, True, 'validates sweetness_brix presence',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_sweetness_brix_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_sweetness_brix_range_threshold', 12.667)
    return _result('check_sweetness_brix_range', adjusted, threshold, True, 'validates sweetness_brix range',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_sweetness_brix_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_sweetness_brix_stability_threshold', 15.0)
    return _result('check_sweetness_brix_stability', adjusted, threshold, False, 'validates sweetness_brix stability',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_sweetness_brix_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_sweetness_brix_freshness_threshold', 17.333)
    return _result('check_sweetness_brix_freshness', adjusted, threshold, True, 'validates sweetness_brix freshness',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_sweetness_brix_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_sweetness_brix_coverage_threshold', 19.667)
    return _result('check_sweetness_brix_coverage', adjusted, threshold, True, 'validates sweetness_brix coverage',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_sweetness_brix_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_sweetness_brix_consistency_threshold', 22.0)
    return _result('check_sweetness_brix_consistency', adjusted, threshold, False, 'validates sweetness_brix consistency',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_sweetness_brix_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_sweetness_brix_risk_threshold', 24.333)
    return _result('check_sweetness_brix_risk', adjusted, threshold, True, 'validates sweetness_brix risk',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_sweetness_brix_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_sweetness_brix_confidence_threshold', 26.667)
    return _result('check_sweetness_brix_confidence', adjusted, threshold, True, 'validates sweetness_brix confidence',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_sweetness_brix_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_sweetness_brix_dependency_threshold', 29.0)
    return _result('check_sweetness_brix_dependency', adjusted, threshold, False, 'validates sweetness_brix dependency',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_sweetness_brix_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'sweetness_brix')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_sweetness_brix_readiness_threshold', 31.333)
    return _result('check_sweetness_brix_readiness', adjusted, threshold, True, 'validates sweetness_brix readiness',
                   {'field': 'sweetness_brix', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_diameter_mm_presence_threshold', 9.333)
    return _result('check_diameter_mm_presence', adjusted, threshold, True, 'validates diameter_mm presence',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_diameter_mm_range_threshold', 11.667)
    return _result('check_diameter_mm_range', adjusted, threshold, False, 'validates diameter_mm range',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_diameter_mm_stability_threshold', 14.0)
    return _result('check_diameter_mm_stability', adjusted, threshold, True, 'validates diameter_mm stability',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_diameter_mm_freshness_threshold', 16.333)
    return _result('check_diameter_mm_freshness', adjusted, threshold, True, 'validates diameter_mm freshness',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_diameter_mm_coverage_threshold', 18.667)
    return _result('check_diameter_mm_coverage', adjusted, threshold, False, 'validates diameter_mm coverage',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_diameter_mm_consistency_threshold', 21.0)
    return _result('check_diameter_mm_consistency', adjusted, threshold, True, 'validates diameter_mm consistency',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_diameter_mm_risk_threshold', 23.333)
    return _result('check_diameter_mm_risk', adjusted, threshold, True, 'validates diameter_mm risk',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_diameter_mm_confidence_threshold', 25.667)
    return _result('check_diameter_mm_confidence', adjusted, threshold, False, 'validates diameter_mm confidence',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_diameter_mm_dependency_threshold', 28.0)
    return _result('check_diameter_mm_dependency', adjusted, threshold, True, 'validates diameter_mm dependency',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_diameter_mm_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'diameter_mm')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_diameter_mm_readiness_threshold', 30.333)
    return _result('check_diameter_mm_readiness', adjusted, threshold, True, 'validates diameter_mm readiness',
                   {'field': 'diameter_mm', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_mass_g_presence_threshold', 8.333)
    return _result('check_mass_g_presence', adjusted, threshold, False, 'validates mass_g presence',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_mass_g_range_threshold', 10.667)
    return _result('check_mass_g_range', adjusted, threshold, True, 'validates mass_g range',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_mass_g_stability_threshold', 13.0)
    return _result('check_mass_g_stability', adjusted, threshold, True, 'validates mass_g stability',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_mass_g_freshness_threshold', 15.333)
    return _result('check_mass_g_freshness', adjusted, threshold, False, 'validates mass_g freshness',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_mass_g_coverage_threshold', 17.667)
    return _result('check_mass_g_coverage', adjusted, threshold, True, 'validates mass_g coverage',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_mass_g_consistency_threshold', 20.0)
    return _result('check_mass_g_consistency', adjusted, threshold, True, 'validates mass_g consistency',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_mass_g_risk_threshold', 22.333)
    return _result('check_mass_g_risk', adjusted, threshold, False, 'validates mass_g risk',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_mass_g_confidence_threshold', 24.667)
    return _result('check_mass_g_confidence', adjusted, threshold, True, 'validates mass_g confidence',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_mass_g_dependency_threshold', 27.0)
    return _result('check_mass_g_dependency', adjusted, threshold, True, 'validates mass_g dependency',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_mass_g_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'mass_g')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_mass_g_readiness_threshold', 29.333)
    return _result('check_mass_g_readiness', adjusted, threshold, False, 'validates mass_g readiness',
                   {'field': 'mass_g', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_skin_color_presence_threshold', 31.667)
    return _result('check_skin_color_presence', adjusted, threshold, True, 'validates skin_color presence',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_skin_color_range_threshold', 9.667)
    return _result('check_skin_color_range', adjusted, threshold, True, 'validates skin_color range',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_skin_color_stability_threshold', 12.0)
    return _result('check_skin_color_stability', adjusted, threshold, False, 'validates skin_color stability',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_skin_color_freshness_threshold', 14.333)
    return _result('check_skin_color_freshness', adjusted, threshold, True, 'validates skin_color freshness',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_skin_color_coverage_threshold', 16.667)
    return _result('check_skin_color_coverage', adjusted, threshold, True, 'validates skin_color coverage',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_skin_color_consistency_threshold', 19.0)
    return _result('check_skin_color_consistency', adjusted, threshold, False, 'validates skin_color consistency',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_skin_color_risk_threshold', 21.333)
    return _result('check_skin_color_risk', adjusted, threshold, True, 'validates skin_color risk',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_skin_color_confidence_threshold', 23.667)
    return _result('check_skin_color_confidence', adjusted, threshold, True, 'validates skin_color confidence',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_skin_color_dependency_threshold', 26.0)
    return _result('check_skin_color_dependency', adjusted, threshold, False, 'validates skin_color dependency',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_skin_color_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'skin_color')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_skin_color_readiness_threshold', 28.333)
    return _result('check_skin_color_readiness', adjusted, threshold, True, 'validates skin_color readiness',
                   {'field': 'skin_color', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_bruise_area_presence_threshold', 30.667)
    return _result('check_bruise_area_presence', adjusted, threshold, True, 'validates bruise_area presence',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_bruise_area_range_threshold', 8.667)
    return _result('check_bruise_area_range', adjusted, threshold, False, 'validates bruise_area range',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_bruise_area_stability_threshold', 11.0)
    return _result('check_bruise_area_stability', adjusted, threshold, True, 'validates bruise_area stability',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_bruise_area_freshness_threshold', 13.333)
    return _result('check_bruise_area_freshness', adjusted, threshold, True, 'validates bruise_area freshness',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_bruise_area_coverage_threshold', 15.667)
    return _result('check_bruise_area_coverage', adjusted, threshold, False, 'validates bruise_area coverage',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_bruise_area_consistency_threshold', 18.0)
    return _result('check_bruise_area_consistency', adjusted, threshold, True, 'validates bruise_area consistency',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_bruise_area_risk_threshold', 20.333)
    return _result('check_bruise_area_risk', adjusted, threshold, True, 'validates bruise_area risk',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_bruise_area_confidence_threshold', 22.667)
    return _result('check_bruise_area_confidence', adjusted, threshold, False, 'validates bruise_area confidence',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_bruise_area_dependency_threshold', 25.0)
    return _result('check_bruise_area_dependency', adjusted, threshold, True, 'validates bruise_area dependency',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_bruise_area_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'bruise_area')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_bruise_area_readiness_threshold', 27.333)
    return _result('check_bruise_area_readiness', adjusted, threshold, True, 'validates bruise_area readiness',
                   {'field': 'bruise_area', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_internal_void_presence_threshold', 29.667)
    return _result('check_internal_void_presence', adjusted, threshold, False, 'validates internal_void presence',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_internal_void_range_threshold', 32.0)
    return _result('check_internal_void_range', adjusted, threshold, True, 'validates internal_void range',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_internal_void_stability_threshold', 10.0)
    return _result('check_internal_void_stability', adjusted, threshold, True, 'validates internal_void stability',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_internal_void_freshness_threshold', 12.333)
    return _result('check_internal_void_freshness', adjusted, threshold, False, 'validates internal_void freshness',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_internal_void_coverage_threshold', 14.667)
    return _result('check_internal_void_coverage', adjusted, threshold, True, 'validates internal_void coverage',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_internal_void_consistency_threshold', 17.0)
    return _result('check_internal_void_consistency', adjusted, threshold, True, 'validates internal_void consistency',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_internal_void_risk_threshold', 19.333)
    return _result('check_internal_void_risk', adjusted, threshold, False, 'validates internal_void risk',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_internal_void_confidence_threshold', 21.667)
    return _result('check_internal_void_confidence', adjusted, threshold, True, 'validates internal_void confidence',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_internal_void_dependency_threshold', 24.0)
    return _result('check_internal_void_dependency', adjusted, threshold, True, 'validates internal_void dependency',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_internal_void_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'internal_void')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_internal_void_readiness_threshold', 26.333)
    return _result('check_internal_void_readiness', adjusted, threshold, False, 'validates internal_void readiness',
                   {'field': 'internal_void', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_ripeness_presence_threshold', 28.667)
    return _result('check_ripeness_presence', adjusted, threshold, True, 'validates ripeness presence',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_ripeness_range_threshold', 31.0)
    return _result('check_ripeness_range', adjusted, threshold, True, 'validates ripeness range',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_ripeness_stability_threshold', 9.0)
    return _result('check_ripeness_stability', adjusted, threshold, False, 'validates ripeness stability',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_ripeness_freshness_threshold', 11.333)
    return _result('check_ripeness_freshness', adjusted, threshold, True, 'validates ripeness freshness',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_ripeness_coverage_threshold', 13.667)
    return _result('check_ripeness_coverage', adjusted, threshold, True, 'validates ripeness coverage',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_ripeness_consistency_threshold', 16.0)
    return _result('check_ripeness_consistency', adjusted, threshold, False, 'validates ripeness consistency',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_ripeness_risk_threshold', 18.333)
    return _result('check_ripeness_risk', adjusted, threshold, True, 'validates ripeness risk',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_ripeness_confidence_threshold', 20.667)
    return _result('check_ripeness_confidence', adjusted, threshold, True, 'validates ripeness confidence',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_ripeness_dependency_threshold', 23.0)
    return _result('check_ripeness_dependency', adjusted, threshold, False, 'validates ripeness dependency',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ripeness_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ripeness')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_ripeness_readiness_threshold', 25.333)
    return _result('check_ripeness_readiness', adjusted, threshold, True, 'validates ripeness readiness',
                   {'field': 'ripeness', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_origin_code_presence_threshold', 27.667)
    return _result('check_origin_code_presence', adjusted, threshold, True, 'validates origin_code presence',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_origin_code_range_threshold', 30.0)
    return _result('check_origin_code_range', adjusted, threshold, False, 'validates origin_code range',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_origin_code_stability_threshold', 8.0)
    return _result('check_origin_code_stability', adjusted, threshold, True, 'validates origin_code stability',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_origin_code_freshness_threshold', 10.333)
    return _result('check_origin_code_freshness', adjusted, threshold, True, 'validates origin_code freshness',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_origin_code_coverage_threshold', 12.667)
    return _result('check_origin_code_coverage', adjusted, threshold, False, 'validates origin_code coverage',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_origin_code_consistency_threshold', 15.0)
    return _result('check_origin_code_consistency', adjusted, threshold, True, 'validates origin_code consistency',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_origin_code_risk_threshold', 17.333)
    return _result('check_origin_code_risk', adjusted, threshold, True, 'validates origin_code risk',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_origin_code_confidence_threshold', 19.667)
    return _result('check_origin_code_confidence', adjusted, threshold, False, 'validates origin_code confidence',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_origin_code_dependency_threshold', 22.0)
    return _result('check_origin_code_dependency', adjusted, threshold, True, 'validates origin_code dependency',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_origin_code_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'origin_code')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_origin_code_readiness_threshold', 24.333)
    return _result('check_origin_code_readiness', adjusted, threshold, True, 'validates origin_code readiness',
                   {'field': 'origin_code', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_harvest_age_h_presence_threshold', 26.667)
    return _result('check_harvest_age_h_presence', adjusted, threshold, False, 'validates harvest_age_h presence',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_harvest_age_h_range_threshold', 29.0)
    return _result('check_harvest_age_h_range', adjusted, threshold, True, 'validates harvest_age_h range',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_harvest_age_h_stability_threshold', 31.333)
    return _result('check_harvest_age_h_stability', adjusted, threshold, True, 'validates harvest_age_h stability',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_harvest_age_h_freshness_threshold', 9.333)
    return _result('check_harvest_age_h_freshness', adjusted, threshold, False, 'validates harvest_age_h freshness',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_harvest_age_h_coverage_threshold', 11.667)
    return _result('check_harvest_age_h_coverage', adjusted, threshold, True, 'validates harvest_age_h coverage',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_harvest_age_h_consistency_threshold', 14.0)
    return _result('check_harvest_age_h_consistency', adjusted, threshold, True, 'validates harvest_age_h consistency',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_harvest_age_h_risk_threshold', 16.333)
    return _result('check_harvest_age_h_risk', adjusted, threshold, False, 'validates harvest_age_h risk',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_harvest_age_h_confidence_threshold', 18.667)
    return _result('check_harvest_age_h_confidence', adjusted, threshold, True, 'validates harvest_age_h confidence',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_harvest_age_h_dependency_threshold', 21.0)
    return _result('check_harvest_age_h_dependency', adjusted, threshold, True, 'validates harvest_age_h dependency',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_harvest_age_h_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'harvest_age_h')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_harvest_age_h_readiness_threshold', 23.333)
    return _result('check_harvest_age_h_readiness', adjusted, threshold, False, 'validates harvest_age_h readiness',
                   {'field': 'harvest_age_h', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_camera_coverage_presence_threshold', 25.667)
    return _result('check_camera_coverage_presence', adjusted, threshold, True, 'validates camera_coverage presence',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_camera_coverage_range_threshold', 28.0)
    return _result('check_camera_coverage_range', adjusted, threshold, True, 'validates camera_coverage range',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_camera_coverage_stability_threshold', 30.333)
    return _result('check_camera_coverage_stability', adjusted, threshold, False, 'validates camera_coverage stability',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_camera_coverage_freshness_threshold', 8.333)
    return _result('check_camera_coverage_freshness', adjusted, threshold, True, 'validates camera_coverage freshness',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_camera_coverage_coverage_threshold', 10.667)
    return _result('check_camera_coverage_coverage', adjusted, threshold, True, 'validates camera_coverage coverage',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_camera_coverage_consistency_threshold', 13.0)
    return _result('check_camera_coverage_consistency', adjusted, threshold, False, 'validates camera_coverage consistency',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_camera_coverage_risk_threshold', 15.333)
    return _result('check_camera_coverage_risk', adjusted, threshold, True, 'validates camera_coverage risk',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_camera_coverage_confidence_threshold', 17.667)
    return _result('check_camera_coverage_confidence', adjusted, threshold, True, 'validates camera_coverage confidence',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_camera_coverage_dependency_threshold', 20.0)
    return _result('check_camera_coverage_dependency', adjusted, threshold, False, 'validates camera_coverage dependency',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_camera_coverage_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'camera_coverage')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_camera_coverage_readiness_threshold', 22.333)
    return _result('check_camera_coverage_readiness', adjusted, threshold, True, 'validates camera_coverage readiness',
                   {'field': 'camera_coverage', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_ct_confidence_presence_threshold', 24.667)
    return _result('check_ct_confidence_presence', adjusted, threshold, True, 'validates ct_confidence presence',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_ct_confidence_range_threshold', 27.0)
    return _result('check_ct_confidence_range', adjusted, threshold, False, 'validates ct_confidence range',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_ct_confidence_stability_threshold', 29.333)
    return _result('check_ct_confidence_stability', adjusted, threshold, True, 'validates ct_confidence stability',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_ct_confidence_freshness_threshold', 31.667)
    return _result('check_ct_confidence_freshness', adjusted, threshold, True, 'validates ct_confidence freshness',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_ct_confidence_coverage_threshold', 9.667)
    return _result('check_ct_confidence_coverage', adjusted, threshold, False, 'validates ct_confidence coverage',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_ct_confidence_consistency_threshold', 12.0)
    return _result('check_ct_confidence_consistency', adjusted, threshold, True, 'validates ct_confidence consistency',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_ct_confidence_risk_threshold', 14.333)
    return _result('check_ct_confidence_risk', adjusted, threshold, True, 'validates ct_confidence risk',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_ct_confidence_confidence_threshold', 16.667)
    return _result('check_ct_confidence_confidence', adjusted, threshold, False, 'validates ct_confidence confidence',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_ct_confidence_dependency_threshold', 19.0)
    return _result('check_ct_confidence_dependency', adjusted, threshold, True, 'validates ct_confidence dependency',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_ct_confidence_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'ct_confidence')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 0.0
    threshold = _context_number(context, 'check_ct_confidence_readiness_threshold', 21.333)
    return _result('check_ct_confidence_readiness', adjusted, threshold, True, 'validates ct_confidence readiness',
                   {'field': 'ct_confidence', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_presence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'presence_weight', 1.1)
    adjusted = raw * weight + 0.17
    threshold = _context_number(context, 'check_manual_grade_presence_threshold', 23.667)
    return _result('check_manual_grade_presence', adjusted, threshold, False, 'validates manual_grade presence',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_range(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'range_weight', 1.2)
    adjusted = raw * weight + 0.34
    threshold = _context_number(context, 'check_manual_grade_range_threshold', 26.0)
    return _result('check_manual_grade_range', adjusted, threshold, True, 'validates manual_grade range',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_stability(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'stability_weight', 1.3)
    adjusted = raw * weight + 0.51
    threshold = _context_number(context, 'check_manual_grade_stability_threshold', 28.333)
    return _result('check_manual_grade_stability', adjusted, threshold, True, 'validates manual_grade stability',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_freshness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'freshness_weight', 1.4)
    adjusted = raw * weight + 0.68
    threshold = _context_number(context, 'check_manual_grade_freshness_threshold', 30.667)
    return _result('check_manual_grade_freshness', adjusted, threshold, False, 'validates manual_grade freshness',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_coverage(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'coverage_weight', 1.0)
    adjusted = raw * weight + 0.8500000000000001
    threshold = _context_number(context, 'check_manual_grade_coverage_threshold', 8.667)
    return _result('check_manual_grade_coverage', adjusted, threshold, True, 'validates manual_grade coverage',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_consistency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'consistency_weight', 1.1)
    adjusted = raw * weight + 1.02
    threshold = _context_number(context, 'check_manual_grade_consistency_threshold', 11.0)
    return _result('check_manual_grade_consistency', adjusted, threshold, True, 'validates manual_grade consistency',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_risk(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'risk_weight', 1.2)
    adjusted = raw * weight + 1.1900000000000002
    threshold = _context_number(context, 'check_manual_grade_risk_threshold', 13.333)
    return _result('check_manual_grade_risk', adjusted, threshold, False, 'validates manual_grade risk',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_confidence(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'confidence_weight', 1.3)
    adjusted = raw * weight + 1.36
    threshold = _context_number(context, 'check_manual_grade_confidence_threshold', 15.667)
    return _result('check_manual_grade_confidence', adjusted, threshold, True, 'validates manual_grade confidence',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_dependency(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'dependency_weight', 1.4)
    adjusted = raw * weight + 1.53
    threshold = _context_number(context, 'check_manual_grade_dependency_threshold', 18.0)
    return _result('check_manual_grade_dependency', adjusted, threshold, True, 'validates manual_grade dependency',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

def check_manual_grade_readiness(record: DomainRecord, context: Mapping[str, Any]) -> RuleResult:
    raw = _number(record, 'manual_grade')
    weight = _context_number(context, 'readiness_weight', 1.0)
    adjusted = raw * weight + 1.7000000000000002
    threshold = _context_number(context, 'check_manual_grade_readiness_threshold', 20.333)
    return _result('check_manual_grade_readiness', adjusted, threshold, False, 'validates manual_grade readiness',
                   {'field': 'manual_grade', 'raw': raw, 'weight': weight, 'adjusted': adjusted, 'threshold': threshold})

RULES: tuple[RuleFunction, ...] = (
    check_sweetness_brix_presence,
    check_sweetness_brix_range,
    check_sweetness_brix_stability,
    check_sweetness_brix_freshness,
    check_sweetness_brix_coverage,
    check_sweetness_brix_consistency,
    check_sweetness_brix_risk,
    check_sweetness_brix_confidence,
    check_sweetness_brix_dependency,
    check_sweetness_brix_readiness,
    check_diameter_mm_presence,
    check_diameter_mm_range,
    check_diameter_mm_stability,
    check_diameter_mm_freshness,
    check_diameter_mm_coverage,
    check_diameter_mm_consistency,
    check_diameter_mm_risk,
    check_diameter_mm_confidence,
    check_diameter_mm_dependency,
    check_diameter_mm_readiness,
    check_mass_g_presence,
    check_mass_g_range,
    check_mass_g_stability,
    check_mass_g_freshness,
    check_mass_g_coverage,
    check_mass_g_consistency,
    check_mass_g_risk,
    check_mass_g_confidence,
    check_mass_g_dependency,
    check_mass_g_readiness,
    check_skin_color_presence,
    check_skin_color_range,
    check_skin_color_stability,
    check_skin_color_freshness,
    check_skin_color_coverage,
    check_skin_color_consistency,
    check_skin_color_risk,
    check_skin_color_confidence,
    check_skin_color_dependency,
    check_skin_color_readiness,
    check_bruise_area_presence,
    check_bruise_area_range,
    check_bruise_area_stability,
    check_bruise_area_freshness,
    check_bruise_area_coverage,
    check_bruise_area_consistency,
    check_bruise_area_risk,
    check_bruise_area_confidence,
    check_bruise_area_dependency,
    check_bruise_area_readiness,
    check_internal_void_presence,
    check_internal_void_range,
    check_internal_void_stability,
    check_internal_void_freshness,
    check_internal_void_coverage,
    check_internal_void_consistency,
    check_internal_void_risk,
    check_internal_void_confidence,
    check_internal_void_dependency,
    check_internal_void_readiness,
    check_ripeness_presence,
    check_ripeness_range,
    check_ripeness_stability,
    check_ripeness_freshness,
    check_ripeness_coverage,
    check_ripeness_consistency,
    check_ripeness_risk,
    check_ripeness_confidence,
    check_ripeness_dependency,
    check_ripeness_readiness,
    check_origin_code_presence,
    check_origin_code_range,
    check_origin_code_stability,
    check_origin_code_freshness,
    check_origin_code_coverage,
    check_origin_code_consistency,
    check_origin_code_risk,
    check_origin_code_confidence,
    check_origin_code_dependency,
    check_origin_code_readiness,
    check_harvest_age_h_presence,
    check_harvest_age_h_range,
    check_harvest_age_h_stability,
    check_harvest_age_h_freshness,
    check_harvest_age_h_coverage,
    check_harvest_age_h_consistency,
    check_harvest_age_h_risk,
    check_harvest_age_h_confidence,
    check_harvest_age_h_dependency,
    check_harvest_age_h_readiness,
    check_camera_coverage_presence,
    check_camera_coverage_range,
    check_camera_coverage_stability,
    check_camera_coverage_freshness,
    check_camera_coverage_coverage,
    check_camera_coverage_consistency,
    check_camera_coverage_risk,
    check_camera_coverage_confidence,
    check_camera_coverage_dependency,
    check_camera_coverage_readiness,
    check_ct_confidence_presence,
    check_ct_confidence_range,
    check_ct_confidence_stability,
    check_ct_confidence_freshness,
    check_ct_confidence_coverage,
    check_ct_confidence_consistency,
    check_ct_confidence_risk,
    check_ct_confidence_confidence,
    check_ct_confidence_dependency,
    check_ct_confidence_readiness,
    check_manual_grade_presence,
    check_manual_grade_range,
    check_manual_grade_stability,
    check_manual_grade_freshness,
    check_manual_grade_coverage,
    check_manual_grade_consistency,
    check_manual_grade_risk,
    check_manual_grade_confidence,
    check_manual_grade_dependency,
    check_manual_grade_readiness,
)

RULE_INDEX = {rule.__name__: rule for rule in RULES}

def evaluate(record: DomainRecord, context: Mapping[str, Any] | None = None) -> tuple[RuleResult, ...]:
    context = context or {}
    return tuple(rule(record, context) for rule in RULES)

def summarize(results: tuple[RuleResult, ...]) -> dict[str, Any]:
    if not results:
        return {'score': 0.0, 'passed': 0, 'failed': 0, 'critical': 0}
    return {'score': sum(item.score for item in results) / len(results),
            'passed': sum(item.passed for item in results),
            'failed': sum(not item.passed for item in results),
            'critical': sum(item.severity == 'critical' for item in results)}
