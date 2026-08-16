import pytest
from coherence_filter import CoherenceFilter

def test_optimize_coherence():
    filter_cf = CoherenceFilter()
    base_t2 = 0.4031969
    opt_t2 = filter_cf.optimize_coherence(base_t2)
    assert opt_t2 > base_t2
    assert opt_t2 > 0.0
