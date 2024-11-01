import unittest

import anndata as ad
import pandas as pd
from pydeseq2.dds import DeseqDataSet, DefaultInference
from pydeseq2.ds import DeseqStats


class TestDESeq2Container(unittest.TestCase):
    def test_consistency(self):

        # Set up variables
        data_path = "./tests/test_data"
        tcells_path = f"{data_path}/tcells.h5ad"
        expected_output_path = f"{data_path}/expected_results_df.parquet"

        tcells = ad.read_h5ad(tcells_path)

        # Build DESeq2 object
        inference = DefaultInference(n_cpus=8)
        dds = DeseqDataSet(
            adata=tcells,
            design_factors="disease",
            ref_level=["disease", "normal"],
            refit_cooks=True,
            inference=inference,
        )

        # Compute LFCs
        dds.deseq2()

        # Extract contrast between COVID-19 vs normal
        stat_res = DeseqStats(
            dds,
            contrast=["disease", "COVID-19", "normal"],
            inference=inference,
        )

        # Compute Wald test
        stat_res.summary()

        results_df = stat_res.results_df
        expected_results_df = pd.read_parquet(expected_output_path)

        pd.testing.assert_frame_equal(results_df, expected_results_df)


if __name__ == "__main__":
    unittest.main()
