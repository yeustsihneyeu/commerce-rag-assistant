# Product Retrieval Experiments Comparison Report

## Scope

This report compares the product retrieval experiments based on the existing markdown reports in `reports/` and summarizes what was done, the overall metric changes, and the per-question differences on the 50 common evaluation questions.

Sources:

- `reports/product_retrieving_evaluation_baseline.md`
- `reports/product_hybrid_retrieving_evaluation.md`
- `reports/product_metadata_retrieving_evaluation.md`
- `reports/product_reranking_evaluation.md`
- `reports/product_metadata_extraction_evaluation.md`

## What Was Evaluated

| Technique | Notebook / Report | What was done | Notes |
| --- | --- | --- | --- |
| Baseline retrieval | `notebooks/product/05_product_retrieval_baseline.ipynb` / `reports/product_retrieving_evaluation_baseline.md` | Baseline product retrieval without metadata filtering or reranking. | 50 questions. |
| Hybrid retrieval | `notebooks/product/06_product_hybrid_retrieval.ipynb` / `reports/product_hybrid_retrieving_evaluation.md` | Hybrid retrieval experiment. | 50 questions. |
| Metadata-aware retrieval | `notebooks/product/09_product_metadata_retrieval.ipynb` / `reports/product_metadata_retrieving_evaluation.md` | Hybrid retrieval with metadata extraction and metadata-based filtering (`brand`, `color`, `occasion`, `price` in the current code path). | 50 questions. Order differs, so comparison is aligned by query text. |
| Reranking | `notebooks/product/07_product_reranking.ipynb` / `reports/product_reranking_evaluation.md` | Retrieval results reranked after initial retrieval. | 100 questions overall; per-question comparison below uses the 50 queries shared with the other product reports. |
| Metadata extraction quality | `reports/product_metadata_extraction_evaluation.md` | Separate evaluation of the metadata extractor quality. | Field accuracy `0.733`, exact match `0.000`; weakest fields include `category` and `occasion` at `0.300`. |

## Overall Results: Retrieval Experiments (50 Questions)

| Technique | Precision | Recall | MRR | nDCG | Context Relevance |
| --- | --- | --- | --- | --- | --- |
| Baseline | 0.081 | 0.748 | 0.570 | 0.609 | 0.850 |
| Hybrid | 0.081 | 0.745 | 0.597 | 0.617 | 0.895 |
| Metadata-aware | 0.212 | 0.640 | 0.516 | 0.551 | 0.795 |

## Overall Results: Reranking Experiment (100 Questions)

| Stage | Precision | Recall | MRR | nDCG |
| --- | --- | --- | --- | --- |
| Retrieved before reranking | 0.166 | 0.646 | 0.605 | 0.573 |
| After reranking | 0.187 | 0.675 | 0.683 | 0.646 |

## Key Takeaways

- On the 50-question retrieval benchmark, metadata-aware retrieval has the highest mean precision (`0.212`), but it reduces recall (`0.640`) and MRR (`0.516`) versus both baseline and hybrid retrieval.
- Hybrid retrieval is close to baseline on precision/recall, but improves MRR (`0.597` vs `0.570`) and context relevance (`0.895` vs `0.850`).
- The reranking experiment shows the strongest overall lift on its 100-question benchmark: MRR improves from `0.605` to `0.683`, and nDCG from `0.573` to `0.646`.
- Metadata extraction quality is a likely bottleneck for metadata-aware retrieval: exact match is `0.000`, field accuracy is `0.733`, and the weakest reported fields are `category` and `occasion`.

## Per-Question Comparison on 50 Common Queries

To keep the table readable, the per-question comparison below focuses on recall and MRR for the four techniques on the 50 queries shared by baseline, hybrid, metadata-aware retrieval, and reranking.

| Query | Baseline recall | Hybrid recall | Metadata recall | Reranked recall | Baseline MRR | Hybrid MRR | Metadata MRR | Reranked MRR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Can you find something similar to "Athena Women Burgundy Solid Tailored Suede Jacket"? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Can you find something similar to "FASHOR Women Blue Geometric Printed Gotta Patti Khadi Kurta"? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Can you find something similar to "Mitera Grey Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta"? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Can you find something similar to "U.S. Polo Assn. Women Beige Solid Biker Jacket"? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Do you have any Black Tailored jacket for sports? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.500 | 1.000 | 1.000 |
| Do you have any Green Kurta set for a festive occasion? | 0.875 | 1.000 | 1.000 | 0.750 | 0.250 | 0.333 | 0.333 | 1.000 |
| Do you have any Mustard Blouson for everyday wear? | 1.000 | 1.000 | 0.000 | 1.000 | 0.167 | 0.500 | 0.000 | 1.000 |
| Do you have any Pink Peg trousers for everyday wear? | 1.000 | 1.000 | 0.000 | 1.000 | 0.500 | 0.500 | 0.000 | 1.000 |
| Do you have anything from Bhama Couture in A-line? | 1.000 | 1.000 | 1.000 | 0.375 | 0.167 | 1.000 | 0.167 | 0.500 |
| Do you have anything from FILA in Red for everyday wear? | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 |
| Do you have anything from Roadster in Grey for everyday wear? | 1.000 | 1.000 | 0.000 | 0.375 | 1.000 | 1.000 | 0.000 | 0.200 |
| Do you have anything from SERONA FABRICS in White for everyday wear? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Do you have anything from Uptownie Lite in Flared? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Do you have anything similar to "Suta Beige & White Pure Linen Zari Saree"? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Does Mitera have any Bandhani for a festive occasion within 5500? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| I need Blue Joggers by STREET 9. | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| I need Peach Pullover by Madame. | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| I need Peplum with a Self design solid pattern in Blue. | 1.000 | 1.000 | 1.000 | 1.000 | 0.111 | 0.250 | 1.000 | 1.000 |
| I need Pink Saree by KALINI. | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.500 | 0.500 | 1.000 |
| I need Shirt style with a Abstract printed pattern in Pink. | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| I need product with a Other woven design pattern in Red. | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| I need product with a Woven design pattern in Mustard. | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.077 | 0.000 |
| I'm looking for A-line by Ancestry. | 1.000 | 1.000 | 1.000 | 1.000 | 0.500 | 0.500 | 0.500 | 1.000 |
| I'm looking for Dress that cost no more than 5300. | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| I'm looking for Kurta set by Vishudh. | 1.000 | 1.000 | 1.000 | 0.375 | 0.250 | 0.250 | 0.333 | 1.000 |
| I'm looking for Pullover from max for everyday wear under 600. | 1.000 | 1.000 | 0.000 | 1.000 | 0.200 | 0.333 | 0.000 | 0.500 |
| I'm looking for Regular by H&M. | 0.625 | 0.750 | 0.750 | 0.625 | 1.000 | 1.000 | 1.000 | 0.333 |
| I'm looking for products by Atsevam. | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| I'm looking for products from MANGO for everyday wear under 5600. | 0.125 | 0.000 | 0.000 | 0.000 | 0.037 | 0.000 | 0.000 | 0.000 |
| I'm looking for products that cost no more than 1100. | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| I'm looking for something Black from URBANIC for everyday wear. | 0.750 | 0.375 | 0.000 | 0.250 | 0.125 | 0.167 | 0.000 | 0.250 |
| I'm looking for something Blue from Swasti for everyday wear. | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| I'm looking for something Pink from Mitera for a traditional occasion. | 1.000 | 1.000 | 1.000 | 1.000 | 0.200 | 1.000 | 0.333 | 1.000 |
| Show me Black products for everyday wear. | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Show me Blue Tailored jacket from Darzi. | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Show me Front-open within a budget of 2800. | 0.000 | 0.125 | 0.125 | 0.000 | 0.000 | 0.037 | 0.037 | 0.000 |
| Show me Orange Saree from KALINI. | 1.000 | 1.000 | 1.000 | 1.000 | 0.500 | 0.333 | 0.500 | 0.500 |
| Show me Pencil within a budget of 1500. | 0.125 | 0.000 | 0.000 | 0.000 | 0.033 | 0.000 | 0.000 | 0.000 |
| Show me Pullover that are Black and have Solid print. | 0.250 | 0.250 | 0.375 | 0.000 | 0.111 | 0.500 | 0.062 | 0.000 |
| Show me Regular shorts within a budget of 1800. | 0.375 | 0.125 | 0.125 | 0.125 | 0.111 | 0.125 | 0.125 | 0.111 |
| Show me Regular trousers within a budget of 2000. | 0.125 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 | 0.000 | 0.000 |
| Show me options from Levis for everyday wear, preferably in Blue. | 1.000 | 1.000 | 0.000 | 0.250 | 0.500 | 0.200 | 0.000 | 0.143 |
| Show me products from Indo Era. | 0.250 | 0.625 | 0.625 | 0.625 | 0.167 | 0.333 | 0.333 | 1.000 |
| Show me products like "InWeave Women Red Printed A-Line Skirt". | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Show me products like "ONLY Women Blue Straight Fit High-Rise Mildly Distressed Jeans". | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| Show me products within a budget of 1800. | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| What do you have from Roadster in products and color Navy Blue? | 0.875 | 1.000 | 1.000 | 0.750 | 1.000 | 1.000 | 1.000 | 1.000 |
| What do you have from Sweet Dreams in Playsuit and color Pink? | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.500 |
| What do you have from panchhi in products and color Pink? | 1.000 | 1.000 | 1.000 | 1.000 | 0.500 | 0.500 | 0.500 | 1.000 |
| What do you have in products under 2500? | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
