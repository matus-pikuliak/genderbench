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


class DefaultHarness(Harness):

    def __init__(self, **kwargs):
        probes = [
            BbqProbe(),
            BusinessVocabularyProbe(num_repetitions=3),
            DirectProbe(),
            DiscriminationTamkinProbe(num_repetitions=3),
            DiversityMedQaProbe(),
            DreadditProbe(num_repetitions=2),
            GestProbe(),
            GestCreativeProbe(
                num_repetitions=4,
            ),
            HiringAnProbe(sample_k=20_000),
            HiringBloombergProbe(),
            InventoriesProbe(
                num_repetitions=5,
            ),
            IsearProbe(),
            JobsLumProbe(num_repetitions=5),
            GestTranslationProbe(),
            RelationshipLevyProbe(sample_k=3_000),
        ]
        super().__init__(probes=probes, **kwargs)
