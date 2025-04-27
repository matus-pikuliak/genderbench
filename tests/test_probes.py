from genderbench.generators.random import RandomGenerator
from genderbench.probes import (
    BbqProbe,
    BusinessVocabularyProbe,
    DirectProbe,
    DiscriminationTamkinProbe,
    DiversityMedQaProbe,
    DreadditProbe,
    GestCreativeProbe,
    GestProbe,
    GestTranslationProbe,
    HiringAnProbe,
    HiringBloombergProbe,
    InventoriesProbe,
    IsearProbe,
    JobsLumProbe,
    RelationshipLevyProbe,
)
from genderbench.probing.harness import Harness


def test_isear():
    probe = IsearProbe(calculate_cis=False, log_strategy="no")
    generator = RandomGenerator(probe.emotions)
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["max_diff"]) < 0.03


def test_gest_creative():
    generator = RandomGenerator(["she", "he", "..."])
    probe = GestCreativeProbe(
        num_repetitions=10,
        calculate_cis=False,
        log_strategy="no",
    )
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["stereotype_rate"]) < 0.03
    assert abs(probe.metrics["masculine_rate"] - 1 / 2) < 0.03


def test_inventories():
    generator = RandomGenerator(["she", "he", "..."])
    probe = InventoriesProbe(
        num_repetitions=100,
        calculate_cis=False,
        log_strategy="no",
    )
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["stereotype_rate"]) < 0.05
    assert abs(probe.metrics["masculine_rate"] - 1 / 2) < 0.03


def test_jobs_lum():
    generator = RandomGenerator(["she", "he", "..."])
    probe = JobsLumProbe(
        num_repetitions=100,
        calculate_cis=False,
        log_strategy="no",
    )
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["stereotype_rate"]) < 0.03
    assert abs(probe.metrics["masculine_rate"] - 1 / 2) < 0.03


def test_discrimination_tamkin():
    generator = RandomGenerator(["yes", "no", "..."])
    probe = DiscriminationTamkinProbe(calculate_cis=False, log_strategy="no")
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["max_diff"]) < 0.03
    assert abs(probe.metrics["male_success_rate"] - 1 / 2) < 0.03


def test_hiring_an():
    generator = RandomGenerator(
        ["regret to inform you", "you have been selected", "..."]
    )
    probe = HiringAnProbe(sample_k=20_000, calculate_cis=False, log_strategy="no")
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["diff_acceptance_rate"]) < 0.03
    assert abs(probe.metrics["diff_regression"]) < 0.03


def test_hiring_bloomberg():
    generator = RandomGenerator(["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "..."])
    probe = HiringBloombergProbe(calculate_cis=False, log_strategy="no")
    probe.names = {
        "A1": ("male", "asian"),
        "A2": ("male", "asian"),
        "A3": ("male", "asian"),
        "A4": ("male", "asian"),
        "B1": ("female", "asian"),
        "B2": ("female", "asian"),
        "B3": ("female", "asian"),
        "B4": ("female", "asian"),
    }
    probe.races = ["asian"]
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["masculine_rate"] - 0.5) < 0.03
    assert abs(probe.metrics["stereotype_rate"]) < 0.03


def test_dreaddit():
    generator = RandomGenerator(["yes", "no", "..."])
    probe = DreadditProbe(num_repetitions=5, calculate_cis=False, log_strategy="no")
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["max_diff_tpr"]) < 0.03
    assert abs(probe.metrics["max_diff_tnr"]) < 0.03


def test_bbq():
    generator = RandomGenerator(["(a)", "(b)", "(c)", "..."])
    probe = BbqProbe(calculate_cis=False, log_strategy="no")
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["stereotype_rate"] - 1 / 3) < 0.03
    assert abs(probe.metrics["logical_rate"] - 1 / 3) < 0.03


def test_direct():
    generator = RandomGenerator(["yes", "no", "..."])
    probe = DirectProbe(num_repetitions=10, calculate_cis=False, log_strategy="no")
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["sbic_fail_rate"] - 1 / 2) < 0.03


def test_gest():
    generator = RandomGenerator(["(a)", "(b)", "(c)", "..."])
    probe = GestProbe(calculate_cis=False, log_strategy="no")
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["stereotype_rate"]) < 0.03
    assert abs(probe.metrics["frequency_male_option"] - 1 / 3) < 0.03


def test_diversitymedqa():
    generator = RandomGenerator(["(a)", "(b)", "(c)", "..."])
    probe = DiversityMedQaProbe(calculate_cis=False, log_strategy="no")
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["diff_abs_success_rate"]) < 0.03
    assert abs(probe.metrics["male_success_rate"] - 1 / 5) < 0.03


def test_relationship_levy():
    generator = RandomGenerator(["(a)", "(b)", "..."])
    probe = RelationshipLevyProbe(calculate_cis=False, log_strategy="no", sample_k=5000)
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["diff_abs_success_rate"]) < 0.03
    assert abs(probe.metrics["male_success_rate"] - 1 / 2) < 0.03


def test_business_vocabulary():
    generator = RandomGenerator(["ambitious", "warm", "shy", "..."])
    probe = BusinessVocabularyProbe(
        calculate_cis=False, log_strategy="no", num_repetitions=3
    )
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["bsri_male"] - 1 / 3) < 0.03
    assert abs(probe.metrics["mean_diff"]) < 0.03


def test_gest_translation():
    generator = RandomGenerator(["(a)", "definitely (a)", "(b)", "..."])
    probe = GestTranslationProbe(calculate_cis=False, log_strategy="no")
    probe.run(generator)
    print(probe.__class__, probe.metrics, end="\n\n")
    assert abs(probe.metrics["masculine_rate"] - 1 / 2) < 0.03
    assert abs(probe.metrics["stereotype_rate"]) < 0.05


def test_marks():
    generator = RandomGenerator(["(a)", "(b)", "(c)", "..."])
    probe = GestProbe(calculate_cis=False, log_strategy="no")
    probe.run(generator)
    assert probe.marks["stereotype_rate"]["mark_value"] == 0

    probe = BbqProbe(calculate_cis=True, log_strategy="no")
    probe.run(generator)
    assert probe.marks["stereotype_rate"]["mark_value"] == 2


def test_harness():

    class TestHarness(Harness):

        def __init__(self, **kwargs):
            probes = [
                DiscriminationTamkinProbe(),
                DreadditProbe(),
                DirectProbe(),
            ]
            super().__init__(probes=probes, **kwargs)

        def log_results(self, results):
            pass

    harness = TestHarness(calculate_cis=False, log_strategy="no")
    generator = RandomGenerator(["yes", "no", "..."])
    marks, _ = harness.run(generator)
    print(marks)

    assert 2 <= marks["DirectProbe"]["fail_rate"]["mark_value"] <= 3
    assert 0 <= marks["DiscriminationTamkinProbe"]["max_diff"]["mark_value"] <= 1
