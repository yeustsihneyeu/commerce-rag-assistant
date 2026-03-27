# Retrieval Evaluation Report

Source notebook: `notebooks/product/09_product_metadata_retrieval.ipynb`

## Overview

- Evaluated questions: 50
- Mean precision: 0.212
- Mean recall: 0.640
- Mean MRR: 0.516
- Mean ndcg: 0.551
- Mean context relevance: 0.795

## Summary Tables

### Final Metrics

| row | precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- | --- |
| mean | 0.212 | 0.640 | 0.516 | 0.551 | 0.795 |

## Detailed Results

### Question 1/50

**Query:** Can you find something similar to "Mitera Grey Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta"?

**Retrieval metadata:** brand == Mitera, color == Grey

**Relevant docs:** `['16950080']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.167 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 16950080 | - | 1.000 | brand=Mitera, color=Grey, price=5999.0 | Product: Mitera Grey Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Grey Dupatta: With dupatta Pattern: Embellished Neck: Roun... |
| 2 | no | 17413544 | - | 0.342 | brand=Mitera, color=Grey, category=Saree, occasion=Party, price=6899.0 | Product: Mitera Women Grey & Black Premium Crushed Georgette Pleated Saree Brand: Mitera Color: Grey Category: Saree Pattern: Embellished Occasion: Party Wash care: Dry clean |
| 3 | no | 19276886 | - | 0.162 | brand=Mitera, color=Grey, category=Saree, occasion=Party, price=4999.0 | Product: Mitera Grey Floral Embroidered Net Fusion Saree Brand: Mitera Color: Grey Category: Saree Pattern: Floral embroidered Occasion: Party Wash care: Dry clean |
| 4 | no | 16615812 | - | 0.133 | brand=Mitera, color=Grey, category=Saree, occasion=Party, price=4899.0 | Product: Mitera Floral Saree With Embroidered Border Brand: Mitera Color: Grey Category: Saree Pattern: Floral embroidered Occasion: Party Wash care: Dry clean |
| 5 | no | 18302978 | - | 0.069 | brand=Mitera, color=Grey, category=Banarasi, occasion=Festive, price=6999.0 | Product: Mitera Grey & Silver-Toned Floral Zari Pure Linen Banarasi Saree Brand: Mitera Color: Grey Category: Banarasi Pattern: Floral woven design Occasion: Festive Wash care: ... |
| 6 | no | 16587914 | - | 0.055 | brand=Mitera, color=Grey, category=Banarasi, occasion=Party, price=5999.0 | Product: Mitera Grey & Gold-Toned Woven Design Zari Silk Cotton Banarasi Saree Brand: Mitera Color: Grey Category: Banarasi Pattern: Woven design Occasion: Party Wash care: Dry ... |

### Question 2/50

**Query:** Show me Regular trousers within a budget of 2000.

**Retrieval metadata:** price <= 2000.0

**Relevant docs:** `['17817750', '18770002', '18769968', '18769944', '18769702', '15026996', '15092120', '16814696']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.750 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 16279046 | - | 0.740 | brand=20Dresses, color=Blue, category=Regular trousers, occasion=Casual, price=2295.0 | Product: 20Dresses Women Blue Trousers Brand: 20Dresses Color: Blue Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Pockets: 2 W... |
| 2 | no | 14220194 | - | 0.621 | brand=DressBerry, color=Burgundy, category=Regular trousers, occasion=Casual, price=1849.0 | Product: DressBerry Women Burgundy Trousers Brand: DressBerry Color: Burgundy Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Po... |
| 3 | no | 13523706 | - | 0.500 | brand=Varanga, color=Black, occasion=Daily, price=1799.0 | Product: Varanga Women Black & White Geometric Printed Bell Sleeves Kurta Brand: Varanga Color: Black Pattern: Geometric printed Shape: Straight Neck: Mandarin collar Sleeves: T... |
| 4 | no | 13647622 | - | 0.486 | brand=Varanga, color=Pink, occasion=Daily, price=3599.0 | Product: Varanga Women Pink & White Leheriya Printed Angrakha Kurta With Embroidery Brand: Varanga Color: Pink Pattern: Leheriya printed Shape: A-line Neck: V-neck Sleeves: Thre... |
| 5 | no | 13769372 | - | 0.485 | brand=Varanga, color=Black, occasion=Daily, price=2299.0 | Product: Varanga Classic Black and White Bandhani Print Cotton Kurta Brand: Varanga Color: Black Pattern: Bandhani printed Shape: Straight Neck: Tie-up neck Sleeves: Three-quart... |
| 6 | no | 11421530 | - | 0.429 | brand=Ginni Arora Label, color=Red, category=Regular trousers, occasion=Casual, price=1199.0 | Product: Ginni Arora Label Women Red Slim Fit Solid Regular Trousers Brand: Ginni Arora Label Color: Red Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Co... |
| 7 | no | 17393956 | - | 0.424 | brand=Fabindia, color=Beige, category=Regular trousers, occasion=Casual, price=1299.0 | Product: Fabindia Women Beige & Red Striped Cotton Regular Trousers Brand: Fabindia Color: Beige Category: Regular trousers Pattern: Striped Length: Regular Top fabric: Cotton O... |
| 8 | no | 16044098 | - | 0.419 | brand=SASSAFRAS, color=Blue, category=Regular trousers, occasion=Casual, price=1899.0 | Product: SASSAFRAS Women Blue Ribbed Trousers Brand: SASSAFRAS Color: Blue Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Wash car... |
| 9 | no | 18770032 | - | 0.398 | brand=Trendyol, color=Black, category=Regular trousers, occasion=Casual, price=1999.0 | Product: Trendyol Women Black High-Rise Trousers Brand: Trendyol Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Wa... |
| 10 | no | 17378344 | - | 0.386 | brand=Saffron Threads, color=Black, category=Regular trousers, occasion=Casual, price=1299.0 | Product: Saffron Threads Women Black Original Trousers Brand: Saffron Threads Color: Black Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion:... |
| 11 | no | 17625016 | - | 0.382 | brand=Fabindia, color=Off White, category=Regular trousers, occasion=Casual, price=1899.0 | Product: Fabindia Women Off White Cotton Trousers Brand: Fabindia Color: Off White Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual ... |
| 12 | no | 17104470 | - | 0.370 | brand=Fabindia, color=Blue, category=Regular trousers, occasion=Casual, price=1499.0 | Product: Fabindia Women Blue Striped Relaxed Trousers Brand: Fabindia Color: Blue Category: Regular trousers Pattern: Striped Length: Regular Top fabric: Cotton Occasion: Casual... |
| 13 | no | 18838354 | - | 0.359 | brand=Styli, color=Multi, category=Regular trousers, occasion=Casual, price=1599.0 | Product: Styli Women Multicoloured Printed High-Rise Trousers Brand: Styli Color: Multi Category: Regular trousers Pattern: Geometric printed Length: Regular Top fabric: Polyest... |
| 14 | no | 19011990 | - | 0.355 | brand=Trendyol, color=Blue, category=Regular trousers, occasion=Casual, price=2599.0 | Product: Trendyol Women Blue Pure Cotton Solid Trousers Brand: Trendyol Color: Blue Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual... |
| 15 | no | 18769616 | - | 0.347 | brand=Trendyol, color=Beige, category=Regular trousers, occasion=Casual, price=2799.0 | Product: Trendyol Women Beige & Brown Pure Cotton Colourblocked High-Rise Trousers Brand: Trendyol Color: Beige Category: Regular trousers Pattern: Colourblocked solid Length: R... |
| 16 | no | 17608014 | - | 0.346 | brand=MANGO, color=Green, category=Regular trousers, occasion=Casual, price=3790.0 | Product: MANGO Women Green Chain Printed Trousers Brand: MANGO Color: Green Category: Regular trousers Pattern: Geometric printed Length: Regular Top fabric: Polyester Occasion:... |
| 17 | no | 10440556 | - | 0.345 | brand=DressBerry, color=Olive, category=Regular trousers, occasion=Casual, price=1699.0 | Product: DressBerry Women Olive Green Regular Fit Solid Regular Mid-Rise Trousers Brand: DressBerry Color: Olive Category: Regular trousers Pattern: Solid Length: Regular Top fa... |
| 18 | no | 14220222 | - | 0.344 | brand=DressBerry, color=Green, category=Regular trousers, occasion=Casual, price=1849.0 | Product: DressBerry Women Green Trousers Brand: DressBerry Color: Green Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Pockets:... |
| 19 | no | 18770054 | - | 0.343 | brand=Trendyol, color=Blue, category=Regular trousers, occasion=Casual, price=2999.0 | Product: Trendyol Women Blue & Yellow Ethnic Motifs Printed High-Rise Trousers Brand: Trendyol Color: Blue Category: Regular trousers Pattern: Ethnic motifs printed Length: Regu... |
| 20 | no | 17046802 | - | 0.343 | brand=Chemistry, color=Black, category=Regular trousers, occasion=Casual, price=1899.0 | Product: Chemistry Women Black Pleated Trousers Brand: Chemistry Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Po... |
| 21 | no | 14514992 | - | 0.342 | brand=RIVI, color=Blue, category=Regular trousers, occasion=Casual, price=2250.0 | Product: RIVI Women Blue Regular Trousers Brand: RIVI Color: Blue Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 2 Wash c... |
| 22 | no | 17197754 | - | 0.338 | brand=Mast & Harbour, color=Blue, category=Regular trousers, occasion=Casual, price=2499.0 | Product: Mast & Harbour Women Blue Pure Cotton Regular Trousers Brand: Mast & Harbour Color: Blue Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Oc... |
| 23 | no | 18867438 | - | 0.338 | brand=URBANIC, color=Black, category=Regular trousers, occasion=Casual, price=2490.0 | Product: URBANIC Women Black Trousers Brand: URBANIC Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Wash care: Mac... |
| 24 | no | 18811270 | - | 0.336 | brand=BoStreet, color=White, category=Regular trousers, occasion=Casual, price=2599.0 | Product: BoStreet Women White Loose Fit Trousers Brand: BoStreet Color: White Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Wa... |
| 25 | no | 18838276 | - | 0.330 | brand=Styli, color=Pink, category=Regular trousers, occasion=Casual, price=1299.0 | Product: Styli Women Pink Skinny Fit High-Rise Trousers Brand: Styli Color: Pink Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual... |
| 26 | no | 18838318 | - | 0.329 | brand=Styli, color=White, category=Regular trousers, occasion=Casual, price=1599.0 | Product: Styli Women White Tapered Fit High-Rise Trousers Brand: Styli Color: White Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Cas... |
| 27 | no | 18838300 | - | 0.328 | brand=Styli, color=Black, category=Regular trousers, occasion=Casual, price=1749.0 | Product: Styli Women Black Straight Fit High-Rise Trousers Brand: Styli Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Ca... |
| 28 | no | 17830914 | - | 0.325 | brand=KALINI, color=Grey, category=Regular trousers, occasion=Casual, price=1699.0 | Product: KALINI Women Grey Pleated Trousers Brand: KALINI Color: Grey Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 2 Wa... |
| 29 | no | 17864146 | - | 0.322 | brand=plusS, color=Olive, category=Regular trousers, occasion=Casual, price=2199.0 | Product: plusS Women Olive Green Trousers Brand: plusS Color: Olive Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Pockets: 2 W... |
| 30 | no | 15693320 | - | 0.319 | brand=Fabindia, color=Beige, category=Regular trousers, occasion=Casual, price=990.0 | Product: Fabindia Women Beige Ethnic Trousers Brand: Fabindia Color: Beige Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets:... |

### Question 3/50

**Query:** Can you find something similar to "Athena Women Burgundy Solid Tailored Suede Jacket"?

**Retrieval metadata:** brand == Athena, color == Burgundy

**Relevant docs:** `['11166548']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 11166548 | - | 1.000 | brand=Athena, color=Burgundy, category=Tailored jacket, occasion=Casual, price=2999.0 | Product: Athena Women Burgundy Solid Tailored Suede Jacket Brand: Athena Color: Burgundy Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: ... |
| 2 | no | 10758214 | - | 0.085 | brand=Athena, color=Burgundy, category=Pullover, occasion=Casual, price=1699.0 | Product: Athena Women Burgundy Solid Pullover Sweatshirt Brand: Athena Color: Burgundy Category: Pullover Pattern: Solid Neck: High neck Sleeves: Long sleeves Length: Regular He... |
| 3 | no | 12086086 | - | 0.016 | brand=Athena, color=Burgundy, category=Pencil, occasion=Casual, price=1299.0 | Product: Athena Women Burgundy Solid Pencil Midi Skirt Brand: Athena Color: Burgundy Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fabric: Polyester Occasio... |
| 4 | no | 11634534 | - | 0.006 | brand=Athena, color=Burgundy, category=Basic jumpsuit, price=2499.0 | Product: Athena Women Burgundy Solid Basic Jumpsuit Brand: Athena Color: Burgundy Category: Basic jumpsuit Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless Top fabric: P... |
| 5 | no | 11634536 | - | 0.004 | brand=Athena, color=Burgundy, category=Basic jumpsuit, price=2499.0 | Product: Athena Women Burgundy Solid Basic Jumpsuit Brand: Athena Color: Burgundy Category: Basic jumpsuit Pattern: Solid Neck: Halter neck Sleeves: Sleeveless Top fabric: Polye... |

### Question 4/50

**Query:** Show me products like "InWeave Women Red Printed A-Line Skirt".

**Retrieval metadata:** brand == InWeave, color == Red

**Relevant docs:** `['18921114']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 18921114 | - | 1.000 | brand=InWeave, color=Red, category=A-line, occasion=Casual, price=2399.0 | Product: InWeave Women Red Printed A-Line Skirt Brand: InWeave Color: Red Category: A-line Pattern: Floral printed Length: Maxi Hemline: Flared Top fabric: Viscose rayon Occasio... |
| 2 | no | 17168254 | - | 0.908 | brand=InWeave, color=Red, category=A-line, occasion=Casual, price=2499.0 | Product: InWeave Women Red Printed Pure Cotton A-Line Maxi Skirt Brand: InWeave Color: Red Category: A-line Pattern: Geometric printed Length: Maxi Hemline: Flared Top fabric: P... |
| 3 | no | 15760840 | - | 0.380 | brand=InWeave, color=Red, category=Regular, occasion=Ethnic, price=1999.0 | Product: InWeave Red & Gold-Toned Regular Crop Top Brand: InWeave Color: Red Category: Regular Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Three-quarter flared slee... |
| 4 | no | 13497800 | - | 0.108 | brand=InWeave, color=Red, category=Regular, occasion=Ethnic, price=1999.0 | Product: InWeave Women Red Striped A-Line Top Brand: InWeave Color: Red Category: Regular Pattern: Vertical stripes self design Neck: Round neck Sleeves: Sleeveless no Length: R... |
| 5 | no | 18922178 | - | 0.076 | brand=InWeave, color=Red, occasion=Western, price=1999.0 | Product: InWeave Women Red Flared Palazzos Brand: InWeave Color: Red Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion: Western Wash care: Hand wash |

### Question 5/50

**Query:** I need product with a Woven design pattern in Mustard.

**Retrieval metadata:** color == Mustard

**Relevant docs:** `['12824928', '18262088']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.067 | 1.000 | 0.077 | 0.289 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 10451734 | - | 0.855 | brand=WEAVERS VILLA, color=Mustard, occasion=Daily, price=1450.0 | Product: WEAVERS VILLA Women Mustard Yellow & Purple Woven Design Shawl Brand: WEAVERS VILLA Color: Mustard Pattern: Floral woven design Top fabric: Wool Occasion: Daily |
| 2 | no | 19218994 | - | 0.696 | brand=Mitera, color=Mustard, category=Kanjeevaram, occasion=Traditional, price=4999.0 | Product: Mitera Mustard & Red Woven Design Zari Art Silk Kanjeevaram Saree Brand: Mitera Color: Mustard Category: Kanjeevaram Pattern: Woven design Occasion: Traditional Wash ca... |
| 3 | no | 18122478 | - | 0.674 | brand=PERFECTBLUE, color=Mustard, category=Saree, occasion=Festive, price=2999.0 | Product: PERFECTBLUE Mustard Yellow & Fuchsia Floral Woven Design Saree Brand: PERFECTBLUE Color: Mustard Category: Saree Pattern: Floral woven design Occasion: Festive Wash car... |
| 4 | no | 17663018 | - | 0.660 | brand=Dupatta Bazaar, color=Mustard, occasion=Party, price=1199.0 | Product: Dupatta Bazaar Mustard Yellow Ethnic Motifs Woven Design Silk Dupatta Brand: Dupatta Bazaar Color: Mustard Pattern: Ethnic motifs woven design Top fabric: Silk blend Oc... |
| 5 | no | 16719554 | - | 0.642 | brand=Banarasi Style, color=Mustard, occasion=Daily, price=3599.0 | Product: Banarasi Style Mustard Woven Design Dupatta with Zari Brand: Banarasi Style Color: Mustard Pattern: Floral woven design Top fabric: Silk blend Occasion: Daily Wash care... |
| 6 | no | 11117288 | - | 0.626 | brand=Mitera, color=Mustard, category=Kanjeevaram, occasion=Traditional, price=4999.0 | Product: Mitera Mustard & Pink Silk Blend Woven Design Kanjeevaram Saree Brand: Mitera Color: Mustard Category: Kanjeevaram Pattern: Embellished woven design Occasion: Tradition... |
| 7 | no | 18135092 | - | 0.567 | brand=Mitera, color=Mustard, category=Banarasi, occasion=Traditional, price=5999.0 | Product: Mitera Mustard Yellow Ethnic Motifs Zari Silk Cotton Banarasi Saree Brand: Mitera Color: Mustard Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Tradit... |
| 8 | no | 16921550 | - | 0.496 | brand=Safaa, color=Mustard, category=Dress, occasion=Daily, price=2699.0 | Product: Safaa Women Mustard Woven Design Wool Unstitched Dress Material Brand: Safaa Color: Mustard Category: Dress Pattern: Floral Bottom fabric: Viscose rayon Dupatta fabric:... |
| 9 | no | 18141434 | - | 0.489 | brand=MANOHARI, color=Mustard, category=Saree, occasion=Festive, price=9699.0 | Product: MANOHARI Mustard & Gold-Toned Woven Design Sequinned Silk Blend Saree Brand: MANOHARI Color: Mustard Category: Saree Pattern: Woven design Occasion: Festive Wash care: ... |
| 10 | no | 14071540 | - | 0.431 | brand=DressBerry, color=Mustard, category=Front-open, occasion=Casual, price=2399.0 | Product: DressBerry Women Stylish Mustard Self-Design Knitted Sweater Brand: DressBerry Color: Mustard Category: Front-open Pattern: Open knit self design Neck: V-neck Sleeves: ... |
| 11 | no | 19240508 | - | 0.408 | brand=max, color=Mustard, occasion=Daily, price=599.0 | Product: max Women Mustard Yellow Yoke Design Thread Work Kurta Brand: max Color: Mustard Pattern: Solid yoke design Shape: Straight Neck: Mandarin collar Sleeves: Three-quarter... |
| 12 | no | 18696924 | - | 0.401 | brand=RANGMANCH BY PANTALOONS, color=Mustard, occasion=Daily, price=799.0 | Product: RANGMANCH BY PANTALOONS Women Mustard Yellow Kurta Brand: RANGMANCH BY PANTALOONS Color: Mustard Pattern: Striped woven design Shape: Straight Neck: Mandarin collar Sle... |
| 13 | yes | 12824928 | - | 0.400 | brand=DIVASTRI, color=Mustard, occasion=Festive, price=5999.0 | Product: DIVASTRI Mustard & Pink Woven Design Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: DIVASTRI Color: Mustard Dupatta: With dupatta Pattern: Woven design N... |
| 14 | no | 15379610 | - | 0.398 | brand=Chhabra 555, color=Mustard, price=7900.0 | Product: Chhabra 555 Mustard Yellow & Red Semi-Stitched Banarasi Brocade Silk Lehenga Set Brand: Chhabra 555 Color: Mustard Dupatta: With dupatta Pattern: Woven design Sleeves: ... |
| 15 | no | 18196770 | - | 0.394 | brand=LOOKNBOOK ART, color=Mustard, price=6800.0 | Product: LOOKNBOOK ART Mustard Yellow & Red Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: LOOKNBOOK ART Color: Mustard Dupatta: With dupatta Pattern: Woven desig... |
| 16 | no | 18509068 | - | 0.391 | brand=SANGAM PRINTS, color=Mustard, category=Saree, occasion=Festive, price=1799.0 | Product: SANGAM PRINTS Mustard & Golden Ethnic Motifs Silk Blend Saree Brand: SANGAM PRINTS Color: Mustard Category: Saree Pattern: Ethnic motifs woven design Occasion: Festive ... |
| 17 | no | 14402632 | - | 0.389 | brand=InWeave, color=Mustard, category=A-line, occasion=Ethnic, price=1999.0 | Product: InWeave Mustard Yellow & Blue A-Line Top Brand: InWeave Color: Mustard Category: A-line Pattern: Graphic printed Neck: Round neck Sleeves: Sleeveless no Length: Regular... |
| 18 | no | 13676084 | - | 0.376 | brand=Vishudh, color=Mustard, occasion=Ethnic, price=999.0 | Product: Vishudh Women Mustard Yellow Solid Hem Design Straight Palazzos Brand: Vishudh Color: Mustard Pattern: Geometric hem design Length: Regular Top fabric: Viscose rayon Oc... |
| 19 | no | 15287502 | - | 0.355 | brand=Mast & Harbour, color=Mustard, category=Regular, occasion=Casual, price=1499.0 | Product: Mast & Harbour Mustard Yellow Dobby Weave Ruffles Detail Top Brand: Mast & Harbour Color: Mustard Category: Regular Pattern: Self design Neck: Round neck Sleeves: Long ... |
| 20 | no | 12130790 | - | 0.355 | brand=Inddus, color=Mustard, category=Kurta set, occasion=Festive, price=2699.0 | Product: Inddus Women Mustard Yellow & Red Woven Design Kurta with Trousers Brand: Inddus Color: Mustard Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Woven... |
| 21 | no | 1319900 | - | 0.346 | brand=Desi Weavess, color=Mustard, price=1890.0 | Product: Desi Weavess Mustard Orange & Red Printed Jodhpuri Jumpsuit Brand: Desi Weavess Color: Mustard Pattern: Printed Neck: Shirt collar Sleeves: Sleeveless Top fabric: Cotto... |
| 22 | no | 5567866 | - | 0.330 | brand=DressBerry, color=Mustard, category=Pullover, occasion=Casual, price=2299.0 | Product: DressBerry Women Mustard Yellow Self Design Pullover Brand: DressBerry Color: Mustard Category: Pullover Pattern: Cable knit self design Neck: Round neck Sleeves: Long ... |
| 23 | no | 19145502 | - | 0.321 | brand=The Chennai Silks, color=Mustard, category=Taant, occasion=Traditional, price=3299.0 | Product: The Chennai Silks Mustard & Brown Pure Cotton Fusion Taant Saree Brand: The Chennai Silks Color: Mustard Category: Taant Pattern: Solid Occasion: Traditional Wash care:... |
| 24 | no | 15019972 | - | 0.319 | brand=Cayman, color=Mustard, category=Pullover, occasion=Casual, price=2795.0 | Product: Cayman Women Mustard Yellow Self Designed Floral Pullover Sweater Brand: Cayman Color: Mustard Category: Pullover Pattern: Floral self design Neck: Round neck Sleeves: ... |
| 25 | no | 14096934 | - | 0.313 | brand=NEUDIS, color=Mustard, category=Pencil, occasion=Casual, price=1099.0 | Product: NEUDIS Women Mustard Yellow Self Design Pencil Knee Length Skirt Brand: NEUDIS Color: Mustard Category: Pencil Pattern: Self design Length: Knee length Hemline: Straigh... |
| 26 | no | 17138148 | - | 0.308 | brand=SHECZZAR, color=Mustard, category=Pullover, occasion=Casual, price=1859.0 | Product: SHECZZAR Women Mustard Yellow & Orange Ribbed Colourblocked Sleeveless Pullover Brand: SHECZZAR Color: Mustard Category: Pullover Pattern: Ribbed self design Neck: Turt... |
| 27 | yes | 18262088 | - | 0.303 | brand=Chhabra 555, color=Mustard, price=7990.0 | Product: Chhabra 555 Mustard & Red Beads and Stones Kalamkari Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Chhabra 555 Color: Mustard Dupatta: With dupatta Patt... |
| 28 | no | 16931650 | - | 0.287 | brand=all about you, color=Mustard, category=Regular, occasion=Casual, price=1699.0 | Product: all about you Mustard Yellow Self-Design Round Neck Top Brand: all about you Color: Mustard Category: Regular Pattern: Self design Neck: Round neck Sleeves: Three-quart... |
| 29 | no | 14087386 | - | 0.266 | brand=SASSAFRAS, color=Mustard, category=A-line, occasion=Casual, price=1499.0 | Product: SASSAFRAS Women Mustard Yellow & Pink Floral Lace Design Midi A-Line Skirt with Side Slit Brand: SASSAFRAS Color: Mustard Category: A-line Pattern: Floral self design L... |
| 30 | no | 18801976 | - | 0.251 | brand=Mitera, color=Mustard, category=Kanjeevaram, occasion=Traditional, price=1599.0 | Product: Mitera Mustard & Purple Striped Zari Kanjeevaram Saree Brand: Mitera Color: Mustard Category: Kanjeevaram Pattern: Striped Occasion: Traditional Wash care: Hand wash |

### Question 6/50

**Query:** I'm looking for products from MANGO for everyday wear under 5600.

**Retrieval metadata:** brand == MANGO, occasion == Daily, price <= 5600.0

**Relevant docs:** `['15315768', '15265896', '15265898', '16892568', '15977044', '18257264', '16708118', '16708114']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |

### Question 7/50

**Query:** What do you have from Sweet Dreams in Playsuit and color Pink?

**Retrieval metadata:** brand == Sweet Dreams, color == Pink

**Relevant docs:** `['11581420', '11581366']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.500 | 1.000 | 1.000 | 0.920 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 11581420 | - | 1.000 | brand=Sweet Dreams, color=Pink, category=Playsuit, price=1399.0 | Product: Sweet Dreams Women Pink & Green Heart Print Playsuit Brand: Sweet Dreams Color: Pink Category: Playsuit Pattern: Printed Neck: Round neck Sleeves: Short sleeves Top fab... |
| 2 | no | 11581448 | - | 0.925 | brand=Sweet Dreams, color=Pink, category=Playsuit, occasion=Casual, price=1549.0 | Product: Sweet Dreams Women Pink & Green Heart Print Playsuit Brand: Sweet Dreams Color: Pink Category: Playsuit Pattern: Printed Neck: Round neck Sleeves: Short sleeves Top fab... |
| 3 | yes | 11581366 | - | 0.924 | brand=Sweet Dreams, color=Pink, category=Playsuit, occasion=Casual, price=1499.0 | Product: Sweet Dreams Women Pink & Green Heart Print Playsuit Brand: Sweet Dreams Color: Pink Category: Playsuit Pattern: Printed Neck: Round neck Sleeves: Short sleeves Top fab... |
| 4 | no | 12882594 | - | 0.000 | brand=Sweet Dreams, color=Pink, category=Pullover, occasion=Casual, price=1674.0 | Product: Sweet Dreams Women Peach-Coloured & Black Kitty Print Sweatshirt Brand: Sweet Dreams Color: Pink Category: Pullover Pattern: Conversational printed Neck: Round neck Sle... |

### Question 8/50

**Query:** I'm looking for Kurta set by Vishudh.

**Retrieval metadata:** brand == Vishudh

**Relevant docs:** `['13536726', '15997054', '18262138', '13119222', '18263032', '15820432', '15639890', '18929144']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.267 | 1.000 | 0.333 | 0.626 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 13799826 | - | 0.976 | brand=Vishudh, color=Grey, category=Kurta set, occasion=Daily, price=2549.0 | Product: Vishudh Women Grey & Gold-Coloured Checked Kurta with Trousers & Dupatta Brand: Vishudh Color: Grey Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: W... |
| 2 | no | 14860664 | - | 0.947 | brand=Vishudh, color=Black, category=Kurta set, occasion=Daily, price=2349.0 | Product: Vishudh Women Black Regular Printed Kurta with Palazzos Brand: Vishudh Color: Black Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Checked yoke desi... |
| 3 | yes | 13536726 | - | 0.940 | brand=Vishudh, color=Yellow, category=Kurta set, occasion=Daily, price=3649.0 | Product: Vishudh Women Yellow & Off-White Printed Kurta with Trousers & Dupatta Brand: Vishudh Color: Yellow Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: W... |
| 4 | no | 7572969 | - | 0.930 | brand=Vishudh, color=Red, category=Kurta set, occasion=Festive, price=6799.0 | Product: Vishudh Women Red & Orange Self Design Kurta with Palazzos Brand: Vishudh Color: Red Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Floral self desi... |
| 5 | yes | 15997054 | - | 0.924 | brand=Vishudh, color=Yellow, category=Kurta set, occasion=Daily, price=3199.0 | Product: Vishudh Women Yellow Floral Embroidered Regular Kurta with Palazzos Brand: Vishudh Color: Yellow Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Flor... |
| 6 | no | 9867983 | - | 0.906 | brand=Vishudh, color=Navy Blue, category=Kurta set, occasion=Daily, price=2149.0 | Product: Vishudh Women Navy Blue Floral Printed Regular Pure Cotton Kurta with Palazzos Brand: Vishudh Color: Navy Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos... |
| 7 | no | 7572958 | - | 0.891 | brand=Vishudh, color=Mauve, category=Kurta set, occasion=Festive, price=4399.0 | Product: Vishudh Women Mauve Regular Kurta with Sharara & With Dupatta Brand: Vishudh Color: Mauve Category: Kurta set Top type: Kurta Bottom type: Sharara Dupatta: With dupatta... |
| 8 | yes | 13119222 | - | 0.891 | brand=Vishudh, color=Black, category=Kurta set, occasion=Daily, price=2149.0 | Product: Vishudh Women Black & Off-White Checked Kurta with Palazzos Brand: Vishudh Color: Black Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Checked self ... |
| 9 | no | 13433674 | - | 0.878 | brand=Vishudh, color=Sea Green, category=Kurta set, occasion=Daily, price=3249.0 | Product: Vishudh Women Sea Green & White Printed Kurta with Palazzos & Dupatta Brand: Vishudh Color: Sea Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta:... |
| 10 | yes | 18929144 | - | 0.832 | brand=Vishudh, color=Purple, category=Kurta set, occasion=Festive, price=2349.0 | Product: Vishudh Women Purple Ethnic Straight Kurta with Trousers & With Dupatta Brand: Vishudh Color: Purple Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: ... |
| 11 | no | 16858486 | - | 0.828 | brand=Vishudh, color=Red, category=Kurta set, occasion=Daily, price=2399.0 | Product: Vishudh Women Red Embroidered Pure Cotton Kurta with Trousers Brand: Vishudh Color: Red Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Solid striped... |
| 12 | no | 17656860 | - | 0.827 | brand=Vishudh, color=Turquoise Blue, category=Kurta set, occasion=Daily, price=2799.0 | Product: Vishudh Women Turquoise Blue Floral Printed Kurta Trouser With Dupatta Brand: Vishudh Color: Turquoise Blue Category: Kurta set Top type: Kurta Bottom type: Trousers Du... |
| 13 | yes | 18262138 | - | 0.822 | brand=Vishudh, color=Yellow, category=Kurta set, occasion=Festive, price=3299.0 | Product: Vishudh Women Yellow & Grey Ethnic Motifs Kurta with Trouser and Jacket Brand: Vishudh Color: Yellow Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: ... |
| 14 | no | 13975624 | - | 0.807 | brand=Vishudh, color=Off White, category=Kurta set, occasion=Daily, price=2549.0 | Product: Vishudh Women Off-White Checked Kurta with Palazzo and Dupatta Brand: Vishudh Color: Off White Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With d... |
| 15 | yes | 15639890 | - | 0.798 | brand=Vishudh, color=Green, category=Kurta set, occasion=Daily, price=2349.0 | Product: Vishudh Women Green & White Floral Printed Regular Kurta With Trousers & Dupatta Brand: Vishudh Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers D... |
| 16 | yes | 15820432 | - | 0.791 | brand=Vishudh, color=Off White, category=Kurta set, occasion=Daily, price=2199.0 | Product: Vishudh Women Off White Embroidered Regular Pure Cotton Kurta with Palazzo Brand: Vishudh Color: Off White Category: Kurta set Top type: Kurta Bottom type: Palazzos Pat... |
| 17 | no | 18929396 | - | 0.784 | brand=Vishudh, color=Pink, category=Kurta set, occasion=Festive, price=3299.0 | Product: Vishudh Women Pink Thread Work Kurta with Trousers & Jacket Brand: Vishudh Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Solid Shape: A... |
| 18 | no | 18261878 | - | 0.779 | brand=Vishudh, color=Blue, category=Kurta set, occasion=Daily, price=2949.0 | Product: Vishudh Women Blue Floral Printed Kurta with Palazzos & With Dupatta Brand: Vishudh Color: Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With ... |
| 19 | no | 16123926 | - | 0.776 | brand=Vishudh, color=Mauve, category=Kurta set, occasion=Festive, price=3949.0 | Product: Vishudh Women Mauve Floral Embroidered Kurta with Skirt & With Dupatta Brand: Vishudh Color: Mauve Category: Kurta set Top type: Kurta Bottom type: Skirt Dupatta: With ... |
| 20 | no | 9673749 | - | 0.776 | brand=Vishudh, color=Turquoise Blue, category=Kurta set, occasion=Daily, price=2649.0 | Product: Vishudh Women Turquoise Blue & Gold-Toned Printed Kurti with Palazzos Brand: Vishudh Color: Turquoise Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos Pat... |
| 21 | yes | 18263032 | - | 0.775 | brand=Vishudh, color=Green, category=Kurta set, occasion=Daily, price=2149.0 | Product: Vishudh Women Checked Pure Cotton Kurta with Trouser Brand: Vishudh Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Checked Shape: A-lin... |
| 22 | no | 17445358 | - | 0.756 | brand=Vishudh, color=Purple, category=Kurta set, occasion=Festive, price=2849.0 | Product: Vishudh Women Purple Printed Kurta with Sharara & With Dupatta Brand: Vishudh Color: Purple Category: Kurta set Top type: Kurta Bottom type: Sharara Dupatta: With dupat... |
| 23 | no | 15335772 | - | 0.751 | brand=Vishudh, color=Yellow, category=Kurta set, occasion=Daily, price=2199.0 | Product: Vishudh Women Yellow Striped Regular Pure Cotton Kurta with Palazzos Brand: Vishudh Color: Yellow Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Sol... |
| 24 | no | 18688392 | - | 0.742 | brand=Vishudh, color=Red, category=Kurta set, occasion=Daily, price=3399.0 | Product: Vishudh Women Printed Kurta with Dupatta Brand: Vishudh Color: Red Category: Kurta set Top type: Kurti Bottom type: Trousers Dupatta: With dupatta Pattern: Striped embr... |
| 25 | no | 17132180 | - | 0.719 | brand=Vishudh, color=Black, category=Kurta set, occasion=Daily, price=2399.0 | Product: Vishudh Women Black & Teal Blue Checked Pure Cotton Kurta with Palazzo & Dupatta Brand: Vishudh Color: Black Category: Kurta set Top type: Kurti Bottom type: Trousers D... |
| 26 | no | 18929148 | - | 0.496 | brand=Vishudh, color=Turquoise Blue, category=Kurti set, occasion=Daily, price=2349.0 | Product: Vishudh Women Turquoise Blue Pleated Kurti with Trouser & With Dupatta Brand: Vishudh Color: Turquoise Blue Category: Kurti set Top type: Kurti Bottom type: Dhoti pants... |
| 27 | no | 836967 | - | 0.466 | brand=Vishudh, color=White, occasion=Casual, price=2349.0 | Product: Vishudh White & Green Shirt with Skirt Brand: Vishudh Color: White Neck: Shirt collar Sleeves: Long sleeves Occasion: Casual |
| 28 | no | 2467322 | - | 0.455 | brand=Vishudh, color=Navy Blue, occasion=Daily, price=1749.0 | Product: Vishudh Women Navy Blue & Mustard Printed Anarkali Kurta Brand: Vishudh Color: Navy Blue Pattern: Ethnic motifs printed Shape: Anarkali Neck: Round neck Sleeves: Three-... |
| 29 | no | 6613532 | - | 0.432 | brand=Vishudh, color=Navy Blue, occasion=Daily, price=1699.0 | Product: Vishudh Women Navy Blue Yoke Design Straight Kurta Brand: Vishudh Color: Navy Blue Pattern: Ethnic motifs yoke design Shape: Straight Neck: Round neck Sleeves: Three-qu... |
| 30 | no | 7334039 | - | 0.422 | brand=Vishudh, color=White, occasion=Daily, price=1799.0 | Product: Vishudh Women White & Pink Printed A-Line Kurta Brand: Vishudh Color: White Pattern: Ethnic motifs printed Shape: A-line Neck: Round neck Sleeves: Three-quarter bell sl... |

### Question 9/50

**Query:** I'm looking for A-line by Ancestry.

**Retrieval metadata:** brand == Ancestry

**Relevant docs:** `['15407228', '19152780', '14873702']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.250 | 1.000 | 0.500 | 0.733 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 14873856 | - | 0.954 | brand=Ancestry, color=Grey, category=A-line, occasion=Ethnic, price=2490.0 | Product: Ancestry Women Grey & White Striped A-Line Top Brand: Ancestry Color: Grey Category: A-line Pattern: Vertical stripes striped Neck: V-neck Sleeves: Three-quarter regula... |
| 2 | yes | 15407228 | - | 0.777 | brand=Ancestry, color=Pink, category=A-line, occasion=Ethnic, price=2490.0 | Product: Ancestry Pink Pure Cotton Self Design A-Line Top Brand: Ancestry Color: Pink Category: A-line Pattern: Self design Neck: Round neck Sleeves: Three-quarter bell sleeves ... |
| 3 | yes | 14873702 | - | 0.731 | brand=Ancestry, color=Pink, category=A-line, occasion=Ethnic, price=3490.0 | Product: Ancestry Women Pink Melange Effect Pure Silk A-Line Longline Top Brand: Ancestry Color: Pink Category: A-line Pattern: Solid Neck: Cowl neck Sleeves: Long cuffed sleeve... |
| 4 | yes | 19152780 | - | 0.505 | brand=Ancestry, color=Pink, category=A-line, occasion=Ethnic, price=1790.0 | Product: Ancestry Women Pink Regular Top Brand: Ancestry Color: Pink Category: A-line Pattern: Self design solid Neck: Round neck Sleeves: Sleeveless no Length: Regular Top fabr... |
| 5 | no | 14873748 | - | 0.414 | brand=Ancestry, color=Beige, occasion=Ethnic, price=3990.0 | Product: Ancestry Women Taupe Embroidered Longline Tie-Up Shrug Brand: Ancestry Color: Beige Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: Straight Top fabric: ... |
| 6 | no | 15407188 | - | 0.225 | brand=Ancestry, color=Navy Blue, occasion=Casual, price=2790.0 | Product: Ancestry Women Navy Blue & White Pure Cotton Checked Longline Tie-Up Shrug Brand: Ancestry Color: Navy Blue Pattern: Checked Sleeves: Short sleeves Length: Longline Hem... |
| 7 | no | 19152792 | - | 0.221 | brand=Ancestry, color=Gold, category=Tailored jacket, occasion=Ethnic, price=4990.0 | Product: Ancestry Women Gold-Toned Longline Tailored Jacket Brand: Ancestry Color: Gold Category: Tailored jacket Pattern: Abstract self design Sleeves: Sleeveless Length: Longl... |
| 8 | no | 16588088 | - | 0.192 | brand=Ancestry, color=Pink, category=Regular, occasion=Ethnic, price=2990.0 | Product: Ancestry Pink & Black Ethnic Motifs Print Bishop Sleeves Modal Regular Top Brand: Ancestry Color: Pink Category: Regular Pattern: Ethnic motifs printed Neck: V-neck Sle... |
| 9 | no | 17149934 | - | 0.175 | brand=Ancestry, color=Maroon, category=Tailored jacket, occasion=Casual, price=2990.0 | Product: Ancestry Women Maroon Crop Tailored Jacket Brand: Ancestry Color: Maroon Category: Tailored jacket Pattern: Striped Sleeves: Long sleeves Length: Crop Hemline: Curved T... |
| 10 | no | 19152772 | - | 0.080 | brand=Ancestry, color=Mustard, occasion=Party, price=3490.0 | Product: Ancestry Mustard Embroidered Organza Dupatta Brand: Ancestry Color: Mustard Pattern: Solid embroidered Top fabric: Organza Occasion: Party Wash care: Dry clean |
| 11 | no | 17326880 | - | 0.047 | brand=Ancestry, color=Pink, category=Parallel trousers, occasion=Casual, price=2990.0 | Product: Ancestry Women Pink Regular Fit Pleated Chanderi Parallel Trousers Brand: Ancestry Color: Pink Category: Parallel trousers Pattern: Solid Length: Cropped Top fabric: Ot... |
| 12 | no | 15407164 | - | 0.014 | brand=Ancestry, color=White, category=Shirt style, occasion=Ethnic, price=2790.0 | Product: Ancestry White & Red Pure Cotton Geometric Printed Shirt Style Top Brand: Ancestry Color: White Category: Shirt style Pattern: Geometric printed Neck: Shirt collar Slee... |

### Question 10/50

**Query:** Can you find something similar to "FASHOR Women Blue Geometric Printed Gotta Patti Khadi Kurta"?

**Retrieval metadata:** brand == FASHOR, color == Blue

**Relevant docs:** `['19140952']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.250 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 19140952 | - | 1.000 | brand=FASHOR, color=Blue, occasion=Daily, price=1899.0 | Product: FASHOR Women Blue Geometric Printed Gotta Patti Khadi Kurta Brand: FASHOR Color: Blue Pattern: Geometric printed Shape: A-line Neck: V-neck Sleeves: Three-quarter regul... |
| 2 | no | 18964098 | - | 0.427 | brand=FASHOR, color=Turquoise Blue, occasion=Daily, price=1799.0 | Product: FASHOR Women Turquoise Blue Geometric Printed Kurta Brand: FASHOR Color: Turquoise Blue Pattern: Geometric printed Shape: Straight Neck: Mandarin collar Sleeves: Short ... |
| 3 | no | 19198414 | - | 0.064 | brand=FASHOR, color=Navy Blue, occasion=Daily, price=2699.0 | Product: FASHOR Women Navy Blue Floral Embroidered Thread Work Kurta Brand: FASHOR Color: Navy Blue Pattern: Floral embroidered Shape: A-line Neck: Round neck Sleeves: Three-qua... |
| 4 | no | 19324632 | - | 0.049 | brand=FASHOR, color=Blue, occasion=Festive, price=2399.0 | Product: FASHOR Women Blue & White Yoke Design Straight Fit Kurta Brand: FASHOR Color: Blue Pattern: Striped yoke design Shape: Straight Neck: Round neck Sleeves: Three-quarter ... |

### Question 11/50

**Query:** Show me Blue Tailored jacket from Darzi.

**Retrieval metadata:** brand == Darzi, color == Blue

**Relevant docs:** `['14460680']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.500 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 14460680 | - | 1.000 | brand=Darzi, color=Blue, category=Tailored jacket, occasion=Casual, price=1999.0 | Product: Darzi Women Blue Tailored Jacket Brand: Darzi Color: Blue Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: P... |
| 2 | no | 17665702 | - | 0.000 | brand=Darzi, color=Navy Blue, category=Bomber, occasion=Casual, price=1499.0 | Product: Darzi Women Navy Blue Colourblocked Fleece Bomber with Embroidered Jacket Brand: Darzi Color: Navy Blue Category: Bomber Pattern: Solid colourblocked Sleeves: Sleeveles... |

### Question 12/50

**Query:** Can you find something similar to "U.S. Polo Assn. Women Beige Solid Biker Jacket"?

**Retrieval metadata:** brand == U.S. Polo Assn., color == Beige

**Relevant docs:** `['13703470']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 1.000 | 1.000 | 1.000 | 1.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 13703470 | - | 1.000 | brand=U.S. Polo Assn., color=Beige, category=Biker jacket, occasion=Casual, price=4999.0 | Product: U.S. Polo Assn. Women Beige Solid Biker Jacket Brand: U.S. Polo Assn. Color: Beige Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: ... |

### Question 13/50

**Query:** Does Mitera have any Bandhani for a festive occasion within 5500?

**Retrieval metadata:** brand == Mitera, occasion == Festive, price <= 5500.0

**Relevant docs:** `['15637468']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.033 | 1.000 | 1.000 | 1.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 15637468 | - | 1.000 | brand=Mitera, color=Yellow, category=Bandhani, occasion=Festive, price=5499.0 | Product: Mitera Yellow & Multicoloured Floral Printed Silk Blend Saree Brand: Mitera Color: Yellow Category: Bandhani Pattern: Floral printed Occasion: Festive Wash care: Dry clean |
| 2 | no | 17325496 | - | 0.488 | brand=Mitera, color=Green, category=Dress, occasion=Festive, price=9999.0 | Product: Mitera Green & Off-White Embroidered Unstitched Dress Material Brand: Mitera Color: Green Category: Dress Pattern: Ethnic motifs Bottom fabric: Poly georgette Dupatta f... |
| 3 | no | 17325492 | - | 0.488 | brand=Mitera, color=Green, category=Dress, occasion=Festive, price=9999.0 | Product: Mitera Green & Golden Embroidered Unstitched Dress Material Brand: Mitera Color: Green Category: Dress Pattern: Ethnic motifs Bottom fabric: Poly georgette Dupatta fabr... |
| 4 | no | 17325498 | - | 0.480 | brand=Mitera, color=Maroon, category=Dress, occasion=Festive, price=9999.0 | Product: Mitera Maroon & Golden Embroidered Unstitched Dress Material Brand: Mitera Color: Maroon Category: Dress Pattern: Floral Bottom fabric: Poly georgette Dupatta fabric: P... |
| 5 | no | 17325490 | - | 0.474 | brand=Mitera, color=Black, category=Dress, occasion=Festive, price=9999.0 | Product: Mitera Black & Golden Embroidered Unstitched Dress Material Brand: Mitera Color: Black Category: Dress Pattern: Floral Bottom fabric: Poly georgette Dupatta fabric: Pol... |
| 6 | no | 17392504 | - | 0.468 | brand=Mitera, color=Blue, category=Kanjeevaram, occasion=Festive, price=6795.0 | Product: Mitera Blue & Gold-Toned Ethnic Motifs Zari Organza Kanjeevaram Saree Brand: Mitera Color: Blue Category: Kanjeevaram Pattern: Ethnic motifs woven design Occasion: Fest... |
| 7 | no | 16595928 | - | 0.454 | brand=Mitera, color=Maroon, category=Saree, occasion=Festive, price=6196.0 | Product: Mitera Maroon & Golden Ethnic Motifs Saree with Zari Work Brand: Mitera Color: Maroon Category: Saree Pattern: Ethnic motifs woven design Occasion: Festive Wash care: D... |
| 8 | no | 11530694 | - | 0.425 | brand=Mitera, color=Peach, occasion=Festive, price=6248.0 | Product: Mitera Peach-Coloured & Gold-Toned Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Peach Dupatta: With dupatta Pattern: Embroide... |
| 9 | no | 16588146 | - | 0.399 | brand=Mitera, color=Blue, category=Saree, occasion=Festive, price=11999.0 | Product: Mitera Blue & Purple Ethnic Motifs Silk Blend Saree Brand: Mitera Color: Blue Category: Saree Pattern: Ethnic motifs woven design Occasion: Festive Wash care: Dry clean |
| 10 | no | 18189984 | - | 0.393 | brand=Mitera, color=Green, category=Saree, occasion=Festive, price=4275.0 | Product: Mitera Leheriya Saree with Woven Design border Brand: Mitera Color: Green Category: Saree Pattern: Leheriya printed Occasion: Festive Wash care: Machine wash |
| 11 | no | 13515386 | - | 0.389 | brand=Mitera, color=Mustard, occasion=Festive, price=12497.0 | Product: Mitera Mustard Yellow & Red Embroidered Semi-Stitched Lehenga Set Brand: Mitera Color: Mustard Dupatta: With dupatta Pattern: Embroidered Neck: Round neck Sleeves: Shor... |
| 12 | no | 16286084 | - | 0.382 | brand=Mitera, color=Black, category=Dress, occasion=Festive, price=4263.0 | Product: Mitera Black & Gold-Toned Unstitched Dress Material Brand: Mitera Color: Black Category: Dress Pattern: Floral Bottom fabric: Silk blend Dupatta fabric: Silk blend Occa... |
| 13 | no | 18647316 | - | 0.367 | brand=Mitera, color=Blue, category=Saree, occasion=Festive, price=3999.0 | Product: Mitera Blue & Black Embellished Sequinned Saree Brand: Mitera Color: Blue Category: Saree Pattern: Embellished Occasion: Festive Wash care: Hand wash |
| 14 | no | 17206828 | - | 0.367 | brand=Mitera, color=Black, category=Dress, occasion=Festive, price=3999.0 | Product: Mitera Black & Beige Embroidered Unstitched Dress Material Brand: Mitera Color: Black Category: Dress Pattern: Ethnic motifs Bottom fabric: Shantoon Dupatta fabric: Pol... |
| 15 | no | 16286120 | - | 0.355 | brand=Mitera, color=Red, category=Dress, occasion=Festive, price=4097.0 | Product: Mitera Red & Green Silk Blend Unstitched Dress Material Brand: Mitera Color: Red Category: Dress Pattern: Floral Bottom fabric: Silk blend Dupatta fabric: Silk blend Oc... |
| 16 | no | 16171474 | - | 0.355 | brand=Mitera, color=Red, category=Dress, occasion=Festive, price=4999.0 | Product: Mitera Red & Gold-Toned Dupion Silk Banarasi Jacquard Unstitched Dress Material Brand: Mitera Color: Red Category: Dress Pattern: Ethnic motifs Bottom fabric: Satin Dup... |
| 17 | no | 12668502 | - | 0.353 | brand=Mitera, color=Pink, occasion=Festive, price=7999.0 | Product: Mitera Pink & Blue Woven Design Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Pink Dupatta: With dupatta Pattern: Woven design Sleeves: Th... |
| 18 | no | 12668552 | - | 0.352 | brand=Mitera, color=Turquoise Blue, occasion=Festive, price=5999.0 | Product: Mitera Turquoise Blue & Red Woven Design Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Turquoise Blue Dupatta: With dupatta Pattern: Woven... |
| 19 | no | 18302882 | - | 0.345 | brand=Mitera, color=Teal, category=Saree, occasion=Festive, price=8299.0 | Product: Mitera Teal & Gold-Toned Woven Design Silk Blend Saree Brand: Mitera Color: Teal Category: Saree Pattern: Woven design Occasion: Festive Wash care: Dry clean |
| 20 | no | 15480316 | - | 0.344 | brand=Mitera, color=Teal, category=Saree, occasion=Festive, price=6995.0 | Product: Mitera Teal Blue Sequinned Ready to Wear Saree Brand: Mitera Color: Teal Category: Saree Pattern: Solid Occasion: Festive Wash care: Dry clean |
| 21 | no | 18107770 | - | 0.336 | brand=Mitera, color=Orange, category=Saree, occasion=Festive, price=3999.0 | Product: Mitera Orange & Gold-Toned Embellished Sequinned Pure Georgette Saree Brand: Mitera Color: Orange Category: Saree Pattern: Embellished embroidered Occasion: Festive Was... |
| 22 | no | 15012204 | - | 0.326 | brand=Mitera, color=Pink, category=Banarasi, occasion=Festive, price=3599.0 | Product: Mitera Pink & Gold-Toned Woven Design Zari Silk Blend Banarasi Saree Brand: Mitera Color: Pink Category: Banarasi Pattern: Woven design Occasion: Festive Wash care: Dry... |
| 23 | no | 14479084 | - | 0.324 | brand=Mitera, color=Red, category=Saree, occasion=Festive, price=10599.0 | Product: Mitera Red & Gold-Toned Zari Silk Blend Saree Brand: Mitera Color: Red Category: Saree Pattern: Solid Occasion: Festive Wash care: Dry clean |
| 24 | no | 16967652 | - | 0.314 | brand=Mitera, color=Gold, category=Saree, occasion=Festive, price=4999.0 | Product: Mitera Gold-Toned & Pink Woven Design Saree Brand: Mitera Color: Gold Category: Saree Pattern: Woven design Occasion: Festive Wash care: Machine wash |
| 25 | no | 18121996 | - | 0.311 | brand=Mitera, color=Red, category=Saree, occasion=Festive, price=5999.0 | Product: Mitera Red Striped Sequinned Organza Saree Brand: Mitera Color: Red Category: Saree Pattern: Striped Occasion: Festive Wash care: Dry clean |
| 26 | no | 18656200 | - | 0.304 | brand=Mitera, color=Yellow, category=Saree, occasion=Festive, price=3999.0 | Product: Mitera Yellow & Brown Embellished Sequinned Saree Brand: Mitera Color: Yellow Category: Saree Pattern: Embellished Occasion: Festive Wash care: Hand wash |
| 27 | no | 16967650 | - | 0.301 | brand=Mitera, color=Beige, category=Saree, occasion=Festive, price=4999.0 | Product: Mitera Beige & Red Ethnic Motifs Zari Silk Cotton Saree Brand: Mitera Color: Beige Category: Saree Pattern: Ethnic motifs woven design Occasion: Festive Wash care: Mach... |
| 28 | no | 16286118 | - | 0.300 | brand=Mitera, color=Navy Blue, category=Dress, occasion=Festive, price=4097.0 | Product: Mitera Navy Blue & Red Unstitched Dress Material Brand: Mitera Color: Navy Blue Category: Dress Pattern: Geometric Bottom fabric: Silk blend Dupatta fabric: Silk blend ... |
| 29 | no | 18585472 | - | 0.287 | brand=Mitera, color=Black, category=Saree, occasion=Festive, price=22300.0 | Product: Mitera Black & Pink Floral Pure Linen Saree Brand: Mitera Color: Black Category: Saree Pattern: Floral woven design Occasion: Festive Wash care: Dry clean |
| 30 | no | 16576216 | - | 0.281 | brand=Mitera, color=Red, category=Banarasi, occasion=Festive, price=5999.0 | Product: Mitera Red & Golden Ethnic Motifs Banarasi Saree with Zari Border Brand: Mitera Color: Red Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Festive Wash... |

### Question 14/50

**Query:** Show me Pencil within a budget of 1500.

**Retrieval metadata:** price <= 1500.0

**Relevant docs:** `['15940138', '9552849', '15301318', '12086086', '18834976', '18454266', '15637548', '6629440']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 14011652 | - | 0.797 | brand=FableStreet, color=Black, category=Pencil, occasion=Formal, price=1995.0 | Product: FableStreet Black Mini Pencil Skirt Brand: FableStreet Color: Black Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Occasion: Formal Pockets: 1 Wash care... |
| 2 | no | 1294879 | - | 0.767 | brand=Purple Feather, color=Black, category=Pencil, occasion=Formal, price=1499.0 | Product: Purple Feather Black Pencil Skirt With Back Slit Brand: Purple Feather Color: Black Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Occasion: Form... |
| 3 | no | 18215398 | - | 0.695 | brand=Popwings, color=Camel Brown, category=Pencil, occasion=Casual, price=1299.0 | Product: Popwings Women Camel Brown Pencil Slit Skirts Brand: Popwings Color: Camel Brown Category: Pencil Pattern: Solid Length: Above knee Hemline: Straight Top fabric: Polyes... |
| 4 | no | 14798956 | - | 0.687 | brand=Trendyol, color=Taupe, category=Pencil, occasion=Casual, price=2299.0 | Product: Trendyol Women Taupe Solid Pencil Midi Skirt Brand: Trendyol Color: Taupe Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fabric: Polyester Occasion:... |
| 5 | no | 17899166 | - | 0.671 | brand=PATRORNA, color=Green, category=Pencil, occasion=Casual, price=2499.0 | Product: PATRORNA Women Green Solid Pencil Above Knee-Length Skirts Brand: PATRORNA Color: Green Category: Pencil Pattern: Solid Length: Above knee Hemline: Curved Top fabric: C... |
| 6 | no | 14372466 | - | 0.664 | brand=Chemistry, color=Black, category=Pencil, occasion=Casual, price=1499.0 | Product: Chemistry Black Pure Cotton Ribbed Midi Pencil Skirt Brand: Chemistry Color: Black Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fabric: Pure cotto... |
| 7 | no | 17739956 | - | 0.635 | brand=Kotty, color=Black, category=Pencil, occasion=Casual, price=2999.0 | Product: Kotty Women Black Solid Faux Leather Pencil Mini Skirts Brand: Kotty Color: Black Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Top fabric: Leather Occ... |
| 8 | no | 13496046 | - | 0.620 | brand=FableStreet, color=Olive, category=Pencil, occasion=Formal, price=1995.0 | Product: FableStreet Olive Green Knitted Pencil Skirt Brand: FableStreet Color: Olive Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Occasion: Formal Wash... |
| 9 | no | 17931744 | - | 0.613 | brand=PATRORNA, color=Green, category=Pencil, occasion=Casual, price=2399.0 | Product: PATRORNA Women Green & Black Solid Knee Length Pencil Skirts Brand: PATRORNA Color: Green Category: Pencil Pattern: Solid Length: Knee length Hemline: Curved Top fabric... |
| 10 | no | 19072638 | - | 0.608 | brand=DRAAX Fashions, color=Maroon, category=Pencil, occasion=Formal, price=1754.0 | Product: DRAAX Fashions Women Maroon Solid Mini Pencil Formal Skirt Brand: DRAAX Fashions Color: Maroon Category: Pencil Pattern: Solid Length: Above knee Hemline: Straight Top ... |
| 11 | no | 17403200 | - | 0.605 | brand=BROADSTAR, color=Black, category=Pencil, occasion=Casual, price=2499.0 | Product: BROADSTAR Women Black Solid Pencil Mini Skirt Brand: BROADSTAR Color: Black Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Top fabric: Viscose rayon Occ... |
| 12 | no | 19181106 | - | 0.593 | brand=Bitterlime, color=Olive, category=Pencil, occasion=Party, price=1999.0 | Product: Bitterlime Women Olive Green & Black Colourblocked Pencil Skirts Brand: Bitterlime Color: Olive Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight To... |
| 13 | no | 18215396 | - | 0.589 | brand=Popwings, color=Black, category=Pencil, occasion=Casual, price=1299.0 | Product: Popwings Women Above Knee-Length Black Pencil Skirts Brand: Popwings Color: Black Category: Pencil Pattern: Solid self design Length: Above knee Hemline: Straight Top f... |
| 14 | no | 17306262 | - | 0.584 | brand=Purple Feather, color=Black, category=Pencil, occasion=Formal, price=1499.0 | Product: Purple Feather Women Black Solid Stretchable Midi Pencil Skirt Brand: Purple Feather Color: Black Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fab... |
| 15 | no | 17927414 | - | 0.571 | brand=PATRORNA, color=Sea Green, category=Pencil, occasion=Casual, price=2499.0 | Product: PATRORNA Women Sea Green Solid Above Knee Length Pencil Skirts Brand: PATRORNA Color: Sea Green Category: Pencil Pattern: Solid Length: Above knee Hemline: Curved Top f... |
| 16 | no | 17899190 | - | 0.564 | brand=PATRORNA, color=Purple, category=Pencil, occasion=Casual, price=2499.0 | Product: PATRORNA Women Purple Solid Pencil Above Knee-Length Skirts Brand: PATRORNA Color: Purple Category: Pencil Pattern: Solid Length: Above knee Hemline: Curved Top fabric:... |
| 17 | no | 17898168 | - | 0.557 | brand=PATRORNA, color=Black, category=Pencil, occasion=Casual, price=1799.0 | Product: PATRORNA Women Black Solid Knee Length Pencil Skirts Brand: PATRORNA Color: Black Category: Pencil Pattern: Solid Length: Knee length Hemline: Curved Top fabric: Cotton... |
| 18 | no | 17365546 | - | 0.544 | brand=BROADSTAR, color=Black, category=Pencil, occasion=Casual, price=2499.0 | Product: BROADSTAR Women Black Solid Pencil Knee Length Skirt Brand: BROADSTAR Color: Black Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Top fabric: Cot... |
| 19 | no | 17795314 | - | 0.539 | brand=Trend Arrest, color=Navy Blue, category=Pencil, occasion=Party, price=1199.0 | Product: Trend Arrest Women Navy Blue Sequence Pencil Mini Skirt Brand: Trend Arrest Color: Navy Blue Category: Pencil Pattern: Embellished Length: Mini Hemline: Straight Top fa... |
| 20 | no | 18034350 | - | 0.538 | brand=Missguided, color=Olive, category=Pencil, occasion=Party, price=2999.0 | Product: Missguided Women Olive Green Solid Mini Pencil Skirt Brand: Missguided Color: Olive Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Top fabric: Polyester... |
| 21 | no | 14024850 | - | 0.529 | brand=OTORVA, color=Blue, category=Pencil, occasion=Casual, price=1599.0 | Product: OTORVA Women Denim Blue Solid Pencil Mini Skirt Brand: OTORVA Color: Blue Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Top fabric: Polyester Occasion:... |
| 22 | no | 18841536 | - | 0.529 | brand=Styli, color=Burgundy, category=Pencil, occasion=Casual, price=1849.0 | Product: Styli Women Burgundy Solid Pencil Skirts Brand: Styli Color: Burgundy Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fabric: Polyester Occasion: Cas... |
| 23 | no | 15315920 | - | 0.522 | brand=MANGO, color=Green, category=Pencil, occasion=Casual, price=1790.0 | Product: MANGO Women Mint Green Solid Pure Cotton Knee Length Pencil Skirt Brand: MANGO Color: Green Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Top fa... |
| 24 | no | 18977850 | - | 0.516 | brand=Popwings, color=Black, category=Pencil, occasion=Casual, price=1299.0 | Product: Popwings Women Black Solid Pencil Skirts Brand: Popwings Color: Black Category: Pencil Pattern: Solid Length: Knee length Hemline: Curved Top fabric: Polyester Occasion... |
| 25 | no | 12086090 | - | 0.514 | brand=Athena, color=Pink, category=Pencil, occasion=Casual, price=1299.0 | Product: Athena Women Pink Solid Midi Pencil Skirt Brand: Athena Color: Pink Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fabric: Polyester Occasion: Casua... |
| 26 | no | 17694094 | - | 0.512 | brand=Antheaa, color=Black, category=Pencil, occasion=Casual, price=2259.0 | Product: Antheaa Women Black Embellished Pencil Skirt Brand: Antheaa Color: Black Category: Pencil Pattern: Embellished Length: Above knee Hemline: Flared Top fabric: Polyester ... |
| 27 | no | 18629568 | - | 0.495 | brand=IX IMPRESSION, color=Gold, category=Pencil, occasion=Casual, price=1399.0 | Product: IX IMPRESSION Women Gold Solid Pencil Above Knee Straight Skirts Brand: IX IMPRESSION Color: Gold Category: Pencil Pattern: Solid Length: Above knee Hemline: Straight T... |
| 28 | no | 18173820 | - | 0.483 | brand=Kotty, color=Brown, category=Pencil, occasion=Casual, price=2999.0 | Product: Kotty Women Brown Solid Faux Leather Mini Skirt Brand: Kotty Color: Brown Category: Pencil Pattern: Solid Length: Above knee Hemline: Straight Top fabric: Leather Occas... |
| 29 | no | 14270952 | - | 0.476 | brand=NEUDIS, color=Black, category=Pencil, occasion=Ethnic, price=2499.0 | Product: NEUDIS Women Pack Of 2 Solid Velvet Pencil Skirts Brand: NEUDIS Color: Black Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Top fabric: Polyester... |
| 30 | no | 16042324 | - | 0.475 | brand=STYL CO., color=Green, category=Pencil, occasion=Casual, price=1499.0 | Product: STYL CO. Women Green & Orange Graphic Printed Above Knee Length Pencil Skirt Brand: STYL CO. Color: Green Category: Pencil Pattern: Graphic printed Length: Above knee H... |

### Question 15/50

**Query:** Do you have any Mustard Blouson for everyday wear?

**Retrieval metadata:** color == Mustard, occasion == Daily

**Relevant docs:** `['13532718']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.750 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 18456682 | - | 0.814 | brand=Fabindia, color=Mustard, occasion=Daily, price=1699.0 | Product: Fabindia Women Mustard Yellow Pure Cotton Straight Knee Length Kurta Brand: Fabindia Color: Mustard Pattern: Solid Shape: Straight Neck: Round neck Sleeves: Three-quart... |
| 2 | no | 10451734 | - | 0.741 | brand=WEAVERS VILLA, color=Mustard, occasion=Daily, price=1450.0 | Product: WEAVERS VILLA Women Mustard Yellow & Purple Woven Design Shawl Brand: WEAVERS VILLA Color: Mustard Pattern: Floral woven design Top fabric: Wool Occasion: Daily |
| 3 | no | 17090522 | - | 0.740 | brand=Anouk, color=Mustard, occasion=Daily, price=2099.0 | Product: Anouk Women Mustard Yellow Pathani Kurta Brand: Anouk Color: Mustard Pattern: Abstract printed Shape: Pathani Neck: Shirt collar Sleeves: Three-quarter roll-up sleeves ... |
| 4 | no | 2076112 | - | 0.737 | brand=Vishudh, color=Mustard, occasion=Daily, price=1749.0 | Product: Vishudh Women Mustard Yellow Floral Print A-Line Kurta Brand: Vishudh Color: Mustard Pattern: Floral printed Shape: A-line Neck: Round neck Sleeves: Three-quarter regul... |
| 5 | no | 18198270 | - | 0.650 | brand=Biba, color=Mustard, occasion=Daily, price=1999.0 | Product: Biba Women Mustard Yellow & Pink Floral Printed Pure Cotton Straight Kurta Brand: Biba Color: Mustard Pattern: Floral printed Shape: Straight Neck: Round neck Sleeves: ... |
| 6 | no | 17044784 | - | 0.649 | brand=Studio Shringaar, color=Mustard, occasion=Daily, price=699.0 | Product: Studio Shringaar Mustard Yellow Embroidered Dupatta Brand: Studio Shringaar Color: Mustard Pattern: Abstract embroidered Top fabric: Net Occasion: Daily Wash care: Hand... |
| 7 | no | 13337668 | - | 0.643 | brand=Kvsfab, color=Mustard, category=Dress, occasion=Daily, price=3989.0 | Product: Kvsfab Mustard Yellow & Off-White Embroidered Unstitched Dress Material Brand: Kvsfab Color: Mustard Category: Dress Pattern: Floral Bottom fabric: Cotton blend Dupatta... |
| 8 | no | 12413214 | - | 0.643 | brand=Varanga, color=Mustard, occasion=Daily, price=1999.0 | Product: Varanga Women Mustard Yellow Floral Yoke Embroidered Straight Kurta Brand: Varanga Color: Mustard Pattern: Floral embroidered Shape: Straight Neck: Round neck Sleeves: ... |
| 9 | no | 17455814 | - | 0.635 | brand=Anouk, color=Mustard, category=Kurta set, occasion=Daily, price=1699.0 | Product: Anouk Women Mustard Yellow Ethnic Motifs Printed Pure Cotton Kurta with Trousers Brand: Anouk Color: Mustard Category: Kurta set Top type: Kurta Bottom type: Trousers P... |
| 10 | no | 17096082 | - | 0.598 | brand=Anouk, color=Mustard, occasion=Daily, price=2299.0 | Product: Anouk Women Mustard Yellow Geometric Printed Pure Cotton Kurta Brand: Anouk Color: Mustard Pattern: Geometric printed Shape: Straight Neck: Shirt collar Sleeves: Short ... |
| 11 | no | 14925332 | - | 0.598 | brand=Anouk, color=Mustard, occasion=Daily, price=1099.0 | Product: Anouk Women Mustard Yellow & Red Geometric Printed Kurta Brand: Anouk Color: Mustard Pattern: Geometric printed Shape: Straight Neck: V-neck Sleeves: Three-quarter regu... |
| 12 | no | 17094636 | - | 0.584 | brand=Anouk, color=Mustard, occasion=Daily, price=1799.0 | Product: Anouk Women Mustard Yellow & White Chevron Printed Kurta Brand: Anouk Color: Mustard Pattern: Chevron printed Shape: Straight Neck: Mandarin collar Sleeves: Short regul... |
| 13 | no | 13861554 | - | 0.557 | brand=mf, color=Mustard, category=Dress, occasion=Daily, price=2499.0 | Product: mf Mustard & Pink Cotton Blend Unstitched Dress Material Brand: mf Color: Mustard Category: Dress Pattern: Floral Bottom fabric: Cotton blend Dupatta fabric: Poly chiff... |
| 14 | no | 10513948 | - | 0.557 | brand=Anubhutee, color=Mustard, occasion=Daily, price=1999.0 | Product: Anubhutee Women Mustard Yellow & Brown Screen Printed Straight Kurta Brand: Anubhutee Color: Mustard Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck Sle... |
| 15 | no | 19240508 | - | 0.549 | brand=max, color=Mustard, occasion=Daily, price=599.0 | Product: max Women Mustard Yellow Yoke Design Thread Work Kurta Brand: max Color: Mustard Pattern: Solid yoke design Shape: Straight Neck: Mandarin collar Sleeves: Three-quarter... |
| 16 | no | 13381632 | - | 0.529 | brand=Yuris, color=Mustard, category=Kurta set, occasion=Daily, price=4299.0 | Product: Yuris Women Mustard Yellow & Pink Pure Cotton Printed Kurta with Trousers & Dupatta Brand: Yuris Color: Mustard Category: Kurta set Top type: Kurta Bottom type: Trouser... |
| 17 | no | 15781530 | - | 0.494 | brand=max, color=Mustard, occasion=Daily, price=299.0 | Product: max Mustard Viscose Rayon Dupatta Brand: max Color: Mustard Pattern: Solid Top fabric: Viscose rayon Occasion: Daily Wash care: Machine wash |
| 18 | no | 18696924 | - | 0.485 | brand=RANGMANCH BY PANTALOONS, color=Mustard, occasion=Daily, price=799.0 | Product: RANGMANCH BY PANTALOONS Women Mustard Yellow Kurta Brand: RANGMANCH BY PANTALOONS Color: Mustard Pattern: Striped woven design Shape: Straight Neck: Mandarin collar Sle... |
| 19 | no | 18874302 | - | 0.483 | brand=SHANVIKA, color=Mustard, category=Block print, occasion=Daily, price=3799.0 | Product: SHANVIKA Mustard Ethnic Motifs Pure Cotton Block Print Saree Brand: SHANVIKA Color: Mustard Category: Block print Pattern: Ethnic motifs printed Occasion: Daily Wash ca... |
| 20 | no | 17480778 | - | 0.450 | brand=SALWAR STUDIO, color=Mustard, category=Dress, occasion=Daily, price=1095.0 | Product: SALWAR STUDIO Mustard & Brown Printed Unstitched Dress Material Brand: SALWAR STUDIO Color: Mustard Category: Dress Pattern: Checked Bottom fabric: Poly crepe Dupatta f... |
| 21 | no | 17104804 | - | 0.443 | brand=Anouk, color=Mustard, category=Kurta set, occasion=Daily, price=1999.0 | Product: Anouk Women Mustard Yellow Printed Pure Cotton Kurta with Trousers Brand: Anouk Color: Mustard Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Stripe... |
| 22 | no | 17090232 | - | 0.436 | brand=Anouk, color=Mustard, category=Kurta set, occasion=Daily, price=3499.0 | Product: Anouk Women Mustard Yellow Solid Kaftan Kurta with Dhoti Pants Brand: Anouk Color: Mustard Category: Kurta set Top type: Kurta Bottom type: Dhoti pants Pattern: Solid S... |
| 23 | no | 13001114 | - | 0.418 | brand=YASH GALLERY, color=Mustard, occasion=Daily, price=3199.0 | Product: YASH GALLERY Women Plus Size Mustard Yellow Ethnic Printed Detail Keyhole Neck Kurta Brand: YASH GALLERY Color: Mustard Pattern: Solid Shape: A-line Neck: Keyhole neck ... |
| 24 | no | 18727242 | - | 0.416 | brand=Clora Creation, color=Mustard, occasion=Daily, price=1399.0 | Product: Clora Creation Mustard & White Ethnic Motifs Embroidered Dupatta with Sequinned Brand: Clora Creation Color: Mustard Pattern: Ethnic motifs embroidered Top fabric: Net ... |
| 25 | no | 16719554 | - | 0.403 | brand=Banarasi Style, color=Mustard, occasion=Daily, price=3599.0 | Product: Banarasi Style Mustard Woven Design Dupatta with Zari Brand: Banarasi Style Color: Mustard Pattern: Floral woven design Top fabric: Silk blend Occasion: Daily Wash care... |
| 26 | no | 14224394 | - | 0.389 | brand=Nayo, color=Mustard, category=Kurta set, occasion=Daily, price=3499.0 | Product: Nayo Women Mustard Printed Straight Kurta With Plazzo & Dupatta Brand: Nayo Color: Mustard Category: Kurta set Top type: Kurti Bottom type: Palazzos Dupatta: With dupat... |
| 27 | no | 19040576 | - | 0.375 | brand=KARAJ JAIPUR, color=Mustard, category=Kurta set, occasion=Daily, price=3595.0 | Product: KARAJ JAIPUR Women Mustard Yellow Yoke Design Pure Cotton Kurta with Palazzos & Dupatta Brand: KARAJ JAIPUR Color: Mustard Category: Kurta set Top type: Kurta Bottom ty... |
| 28 | no | 18431602 | - | 0.364 | brand=SHAVYA, color=Mustard, category=Dress, occasion=Daily, price=3599.0 | Product: SHAVYA Mustard & Blue Printed Unstitched Dress Material Brand: SHAVYA Color: Mustard Category: Dress Pattern: Floral Bottom fabric: Cotton blend Dupatta fabric: Pure co... |
| 29 | no | 10265397 | - | 0.359 | brand=Saadgi, color=Mustard, occasion=Daily, price=1760.0 | Product: Saadgi Mustard Yellow Gotta Patti Dupatta Brand: Saadgi Color: Mustard Pattern: Solid Top fabric: Poly chiffon Occasion: Daily Wash care: Hand wash |
| 30 | no | 15892784 | - | 0.359 | brand=HERE&NOW, color=Mustard, category=Kurta set, occasion=Daily, price=2399.0 | Product: HERE&NOW Women Mustard Yellow & Black Ethnic Motifs Print Kurta with Trousers Brand: HERE&NOW Color: Mustard Category: Kurta set Top type: Kurta Bottom type: Trousers P... |

### Question 16/50

**Query:** I need Blue Joggers by STREET 9.

**Retrieval metadata:** brand == STREET 9, color == Blue

**Relevant docs:** `['13038932', '13071994']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.087 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 13071994 | - | 1.000 | brand=STREET 9, color=Blue, category=Joggers, occasion=Casual, price=2099.0 | Product: STREET 9 Women Blue Regular Fit Solid Joggers Brand: STREET 9 Color: Blue Category: Joggers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets: ... |
| 2 | yes | 13038932 | - | 0.968 | brand=STREET 9, color=Blue, category=Joggers, occasion=Casual, price=1999.0 | Product: STREET 9 Women Blue Regular Fit Solid Joggers Brand: STREET 9 Color: Blue Category: Joggers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: ... |
| 3 | no | 5389019 | - | 0.574 | brand=STREET 9, color=Blue, category=Culotte jumpsuit, price=1799.0 | Product: STREET 9 Women Blue Striped Culotte Jumpsuit Brand: STREET 9 Color: Blue Category: Culotte jumpsuit Pattern: Striped Neck: Round neck Sleeves: Sleeveless Top fabric: Co... |
| 4 | no | 15803276 | - | 0.488 | brand=STREET 9, color=Blue, category=Basic jumpsuit, occasion=Casual, price=2299.0 | Product: STREET 9 Blue Basic Jumpsuit Brand: STREET 9 Color: Blue Category: Basic jumpsuit Pattern: Solid Neck: Shirt collar Sleeves: Long sleeves Top fabric: Cotton Occasion: C... |
| 5 | no | 6608510 | - | 0.451 | brand=STREET 9, color=Navy Blue, category=Basic jumpsuit, price=1899.0 | Product: STREET 9 Navy Blue Solid Basic Jumpsuit Brand: STREET 9 Color: Navy Blue Category: Basic jumpsuit Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless Top fabric: P... |
| 6 | no | 12277584 | - | 0.436 | brand=STREET 9, color=Navy Blue, category=Cargos, occasion=Casual, price=2299.0 | Product: STREET 9 Women Navy Blue Regular Fit Solid Cargos Brand: STREET 9 Color: Navy Blue Category: Cargos Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual P... |
| 7 | no | 12693476 | - | 0.341 | brand=STREET 9, color=Blue, occasion=Casual, price=2199.0 | Product: STREET 9 Women Blue Straight Fit Mid-Rise Clean Look Stretchable Jeans Brand: STREET 9 Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 8 | no | 12693490 | - | 0.336 | brand=STREET 9, color=Blue, occasion=Casual, price=2399.0 | Product: STREET 9 Women Blue Straight Fit Mid-Rise Clean Look Stretchable Jeans Brand: STREET 9 Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 9 | no | 9781829 | - | 0.319 | brand=STREET 9, color=Blue, category=A-line, occasion=Casual, price=1399.0 | Product: STREET 9 Blue Denim Pleated Mini A-Line Pure Cotton Skirt Brand: STREET 9 Color: Blue Category: A-line Pattern: Solid Length: Mini Hemline: Straight Occasion: Casual Wa... |
| 10 | no | 13041492 | - | 0.269 | brand=STREET 9, color=Blue, category=Pullover, occasion=Casual, price=1799.0 | Product: STREET 9 Women Blue Solid Sweatshirt Brand: STREET 9 Color: Blue Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Strai... |
| 11 | no | 13038878 | - | 0.269 | brand=STREET 9, color=Blue, category=Pullover, occasion=Casual, price=1999.0 | Product: STREET 9 Women Blue Solid Sweatshirt Brand: STREET 9 Color: Blue Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Strai... |
| 12 | no | 14136072 | - | 0.268 | brand=STREET 9, color=Blue, category=Parallel trousers, occasion=Casual, price=2299.0 | Product: STREET 9 Women Blue Flared Faded Parallel Trousers Brand: STREET 9 Color: Blue Category: Parallel trousers Pattern: Solid Length: Cropped Top fabric: Denim Occasion: Ca... |
| 13 | no | 12682016 | - | 0.263 | brand=STREET 9, color=Blue, occasion=Casual, price=2199.0 | Product: STREET 9 Women Blue Skinny Fit Mid-Rise Clean Look Stretchable Jeans Brand: STREET 9 Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash car... |
| 14 | no | 12682038 | - | 0.253 | brand=STREET 9, color=Blue, occasion=Casual, price=1999.0 | Product: STREET 9 Women Blue Skinny Fit Mid-Rise Clean Look Stretchable Jeans Brand: STREET 9 Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash car... |
| 15 | no | 17904100 | - | 0.251 | brand=STREET 9, color=Blue, occasion=Casual, price=2699.0 | Product: STREET 9 Women Blue Hottie Relaxed Fit High-Rise Pure Cotton Dual Tone Jeans Brand: STREET 9 Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 4 ... |
| 16 | no | 15884810 | - | 0.249 | brand=STREET 9, color=Navy Blue, category=Dress, occasion=Party, price=2399.0 | Product: STREET 9 Navy Blue Satin Midi Dress Brand: STREET 9 Color: Navy Blue Category: Dress Top type: Top Bottom type: Skirt Pattern: Solid Neck: Shoulder straps Sleeves: Slee... |
| 17 | no | 14136188 | - | 0.238 | brand=STREET 9, color=Blue, occasion=Casual, price=2399.0 | Product: STREET 9 Women Blue Relaxed Fit Mid-Rise Highly Distressed Jeans Brand: STREET 9 Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 4 Wash care: M... |
| 18 | no | 13738560 | - | 0.159 | brand=STREET 9, color=Turquoise Blue, category=Sporty jacket, occasion=Casual, price=1599.0 | Product: STREET 9 Women Turquoise Blue Lightweight Jacket Brand: STREET 9 Color: Turquoise Blue Category: Sporty jacket Sleeves: Three-quarter sleeves Length: Crop Hemline: Curv... |
| 19 | no | 14136152 | - | 0.156 | brand=STREET 9, color=Navy Blue, category=Basic jumpsuit, occasion=Casual, price=2199.0 | Product: STREET 9 Women Navy Blue Solid Cotton Denim Jumpsuit Brand: STREET 9 Color: Navy Blue Category: Basic jumpsuit Pattern: Solid Neck: Square neck Sleeves: Sleeveless Top ... |
| 20 | no | 18497968 | - | 0.115 | brand=STREET 9, color=Blue, category=Top, occasion=Ethnic, price=3699.0 | Product: STREET 9 Women Blue & Red Printed Pure Cotton Ethnic Co-Ords Brand: STREET 9 Color: Blue Category: Top Top type: Top Bottom type: Trousers Pattern: Printed Neck: Round ... |
| 21 | no | 14136180 | - | 0.108 | brand=STREET 9, color=Navy Blue, category=Playsuit, occasion=Casual, price=1899.0 | Product: STREET 9 Women Navy Blue Solid Denim Playsuit Brand: STREET 9 Color: Navy Blue Category: Playsuit Pattern: Solid Neck: Round neck Sleeves: Sleeveless Top fabric: Cotton... |
| 22 | no | 13904884 | - | 0.036 | brand=STREET 9, color=Navy Blue, category=Regular, occasion=Casual, price=1699.0 | Product: Street 9 Navy Blue Embellished Halter Neck Georgette Regular Top Brand: STREET 9 Color: Navy Blue Category: Regular Pattern: Embellished Neck: Halter neck Sleeves: Slee... |
| 23 | no | 17637532 | - | 0.015 | brand=STREET 9, color=Turquoise Blue, category=Regular, occasion=Casual, price=1599.0 | Product: STREET 9 Women Enchanting Turquoise Blue Colourblocked Top Brand: STREET 9 Color: Turquoise Blue Category: Regular Pattern: Colourblocked Neck: Round neck Sleeves: Shor... |

### Question 17/50

**Query:** Show me Front-open within a budget of 2800.

**Retrieval metadata:** price <= 2800.0

**Relevant docs:** `['16382036', '16382150', '5829334', '5829327', '11991214', '15007832', '14328000', '16461758']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.033 | 0.125 | 0.037 | 0.053 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 14382336 | - | 0.551 | brand=DressBerry, color=Pink, category=Front-open, occasion=Casual, price=1899.0 | Product: DressBerry Women Pink Melange Effect Longline Front-Open Brand: DressBerry Color: Pink Category: Front-open Pattern: Solid Neck: V-neck Sleeves: Long sleeves Length: Lo... |
| 2 | no | 16082246 | - | 0.500 | brand=plusS, color=Grey, category=Front-open, occasion=Casual, price=2800.0 | Product: plusS Women Grey Hooded Sweatshirt Brand: plusS Color: Grey Category: Front-open Pattern: Colourblocked solid Neck: Mock collar Sleeves: Long sleeves Length: Regular He... |
| 3 | no | 17685090 | - | 0.500 | brand=BUY NEW TREND, color=Red, category=Open front jacket, occasion=Casual, price=1499.0 | Product: BUY NEW TREND Women Red Black Colourblocked Lightweight Crop Open Front Jacket Brand: BUY NEW TREND Color: Red Category: Open front jacket Pattern: Colourblocked Sleeve... |
| 4 | no | 19087856 | - | 0.490 | brand=ONLY, color=Beige, category=Front-open, occasion=Casual, price=2499.0 | Product: ONLY Women Beige & Navy Blue Colourblocked Front-Open Longline Brand: ONLY Color: Beige Category: Front-open Pattern: Colourblocked Neck: Round neck Sleeves: Long sleev... |
| 5 | no | 2223198 | - | 0.437 | brand=W, color=Red, category=Front-open, occasion=Casual, price=2099.0 | Product: W Women Red Solid Front-Open Longline Sweater Brand: W Color: Red Category: Front-open Pattern: Solid Neck: Round neck Sleeves: Long sleeves Hemline: Straight Top fabri... |
| 6 | no | 11952000 | - | 0.431 | brand=DressBerry, color=Navy Blue, category=Front-open, occasion=Casual, price=1999.0 | Product: DressBerry Women Navy Blue Ribbed Longline Front-Open Sweater Brand: DressBerry Color: Navy Blue Category: Front-open Pattern: Solid ribbed Neck: V-neck Sleeves: Long s... |
| 7 | no | 7736701 | - | 0.428 | brand=W, color=Teal, category=Front-open, occasion=Casual, price=2099.0 | Product: W Women Teal Blue Solid Front-Open Longline Sweater Brand: W Color: Teal Category: Front-open Pattern: Solid Neck: Shawl collar Sleeves: Long sleeves Length: Longline H... |
| 8 | no | 14071540 | - | 0.406 | brand=DressBerry, color=Mustard, category=Front-open, occasion=Casual, price=2399.0 | Product: DressBerry Women Stylish Mustard Self-Design Knitted Sweater Brand: DressBerry Color: Mustard Category: Front-open Pattern: Open knit self design Neck: V-neck Sleeves: ... |
| 9 | no | 15844140 | - | 0.403 | brand=URBANIC, color=Grey, category=Front-open, occasion=Casual, price=1490.0 | Product: URBANIC Women Grey & Black Colourblocked Longline Front-Open Sweater Brand: URBANIC Color: Grey Category: Front-open Pattern: Colourblocked Neck: Shawl collar Sleeves: ... |
| 10 | no | 15137944 | - | 0.387 | brand=AND, color=Black, category=Open front jacket, occasion=Casual, price=1999.0 | Product: AND Women Black & White Geometric Open Front Jacket Brand: AND Color: Black Category: Open front jacket Pattern: Geometric printed Sleeves: Long sleeves Length: Regular... |
| 11 | no | 13523706 | - | 0.323 | brand=Varanga, color=Black, occasion=Daily, price=1799.0 | Product: Varanga Women Black & White Geometric Printed Bell Sleeves Kurta Brand: Varanga Color: Black Pattern: Geometric printed Shape: Straight Neck: Mandarin collar Sleeves: T... |
| 12 | no | 15353040 | - | 0.321 | brand=ether, color=Maroon, category=Front-open, occasion=Casual, price=1999.0 | Product: ether Women Maroon Solid Front Open Sweater Brand: ether Color: Maroon Category: Front-open Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: Rib... |
| 13 | no | 14210706 | - | 0.320 | brand=MANGO, color=Peach, category=Front-open, occasion=Casual, price=3590.0 | Product: MANGO Women Peach-Coloured Solid Open Front Sweater Brand: MANGO Color: Peach Category: Front-open Pattern: Solid Neck: Shawl collar Sleeves: Short sleeves Length: Regu... |
| 14 | no | 15413660 | - | 0.317 | brand=Cayman, color=Black, category=Front-open, occasion=Casual, price=6245.0 | Product: Cayman Women Black & Beige Longline Front-Open Sweater Brand: Cayman Color: Black Category: Front-open Pattern: Geometric self design Neck: V-neck Sleeves: Long sleeves... |
| 15 | no | 12524642 | - | 0.316 | brand=MANGO, color=Olive, category=Front-open, occasion=Casual, price=2590.0 | Product: MANGO Women Olive Green Solid Longline Front-Open Sweater Brand: MANGO Color: Olive Category: Front-open Pattern: Solid Neck: Shawl collar Sleeves: Long sleeves Length:... |
| 16 | no | 11973294 | - | 0.312 | brand=Mast & Harbour, color=Pink, category=Front-open, occasion=Casual, price=2199.0 | Product: Mast & Harbour Women Dusty Pink Shimmer Effect Striped Front-Open Sweater Brand: Mast & Harbour Color: Pink Category: Front-open Pattern: Striped Neck: Round neck Sleev... |
| 17 | no | 13647622 | - | 0.309 | brand=Varanga, color=Pink, occasion=Daily, price=3599.0 | Product: Varanga Women Pink & White Leheriya Printed Angrakha Kurta With Embroidery Brand: Varanga Color: Pink Pattern: Leheriya printed Shape: A-line Neck: V-neck Sleeves: Thre... |
| 18 | no | 13769372 | - | 0.308 | brand=Varanga, color=Black, occasion=Daily, price=2299.0 | Product: Varanga Classic Black and White Bandhani Print Cotton Kurta Brand: Varanga Color: Black Pattern: Bandhani printed Shape: Straight Neck: Tie-up neck Sleeves: Three-quart... |
| 19 | no | 15415146 | - | 0.306 | brand=Flying Machine, color=Charcoal, category=Front-open, occasion=Casual, price=2499.0 | Product: Flying Machine Women Charcoal Typograhy Printed Front-Open Sweatshirt Brand: Flying Machine Color: Charcoal Category: Front-open Pattern: Typography printed Neck: Mock ... |
| 20 | no | 18210214 | - | 0.290 | brand=FABRIC FITOOR, color=Black, category=Kaftan, occasion=Ethnic, price=2199.0 | Product: FABRIC FITOOR Black Pure Cotton Printed Kaftan Top Brand: FABRIC FITOOR Color: Black Category: Kaftan Pattern: Abstract printed Neck: Round neck Sleeves: Short kimono s... |
| 21 | no | 2322431 | - | 0.284 | brand=Hypernation, color=Navy Blue, occasion=Casual, price=985.0 | Product: Hypernation Navy Blue Solid Open Front Shrug Brand: Hypernation Color: Navy Blue Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: Asymmetric Top fabric: C... |
| 22 | no | 7811561 | - | 0.282 | brand=Hypernation, color=Orange, occasion=Casual, price=999.0 | Product: Hypernation Orange Solid Open Front Shrug Brand: Hypernation Color: Orange Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: Asymmetric Top fabric: Cotton ... |
| 23 | no | 15415116 | - | 0.280 | brand=Flying Machine, color=Blue, category=Front-open, occasion=Casual, price=2299.0 | Product: Flying Machine Women Blue Solid Mock-Collar Front-Open Sweatshirt Brand: Flying Machine Color: Blue Category: Front-open Pattern: Solid Neck: Mock collar Sleeves: Long ... |
| 24 | no | 8928317 | - | 0.275 | brand=Hypernation, color=Rust, occasion=Casual, price=999.0 | Product: Hypernation Rust Brown Solid Open Front Longline Shrug Brand: Hypernation Color: Rust Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: Asymmetric Top fabr... |
| 25 | no | 11102094 | - | 0.265 | brand=Alcis, color=Charcoal, category=Front-open, occasion=Outdoor, price=2599.0 | Product: Alcis Women Charcoal Grey Solid Hooded Front-Open Sweatshirt Brand: Alcis Color: Charcoal Category: Front-open Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: R... |
| 26 | no | 16154282 | - | 0.264 | brand=JC Mode, color=Brown, category=Open front jacket, occasion=Casual, price=2899.0 | Product: JC Mode Women Brown Open Front Jacket Brand: JC Mode Color: Brown Category: Open front jacket Pattern: Solid Sleeves: Sleeveless Length: Regular Hemline: Straight Top f... |
| 27 | yes | 16382036 | - | 0.239 | brand=Vero Moda, color=Cream, category=Front-open, occasion=Casual, price=2799.0 | Product: Vero Moda Women Cream-Coloured Longline Brand: Vero Moda Color: Cream Category: Front-open Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Longline Hemline: Cur... |
| 28 | no | 16044812 | - | 0.232 | brand=Forever New, color=Green, occasion=Casual, price=6800.0 | Product: Forever New Women Green Solid Comfort-Fit Open-Front Casual Blazer Brand: Forever New Color: Green Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Poly... |
| 29 | no | 17685350 | - | 0.226 | brand=BUY NEW TREND, color=Maroon, category=Open front jacket, occasion=Casual, price=1499.0 | Product: BUY NEW TREND Women Maroon Lightweight Crop Open Front Jacket Brand: BUY NEW TREND Color: Maroon Category: Open front jacket Pattern: Abstract solid Sleeves: Three-quar... |
| 30 | no | 17226172 | - | 0.225 | brand=SHOWOFF, color=Orange, occasion=Casual, price=3905.0 | Product: SHOWOFF Women Orange Mom Fit High-Rise Clean Look Stretchable Jeans Brand: SHOWOFF Color: Orange Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 2 Wash c... |

### Question 18/50

**Query:** Do you have anything from FILA in Red for everyday wear?

**Retrieval metadata:** brand == FILA, color == Red, occasion == Daily

**Relevant docs:** `['13255768']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |

### Question 19/50

**Query:** I'm looking for products that cost no more than 1100.

**Retrieval metadata:** price <= 1100.0

**Relevant docs:** `['13135238', '15241584', '13181706', '17739302', '15218838', '11579058', '17113756', '13951522']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 17403640 | - | 0.500 | brand=I Saw It First, color=Khaki, occasion=Casual, price=3199.0 | Product: I Saw It First Women Khaki Crinkled Tie-Up Shrug Brand: I Saw It First Color: Khaki Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: P... |
| 2 | no | 2117164 | - | 0.500 | brand=Noi, color=Cream, occasion=Daily, price=1999.0 | Product: Noi Cream-Coloured & Brown Printed Shawl Brand: Noi Color: Cream Pattern: Animal printed Top fabric: Wool Occasion: Daily |
| 3 | no | 17403254 | - | 0.485 | brand=I Saw It First, color=Blue, occasion=Casual, price=4099.0 | Product: I Saw It First Women Blue Skinny Fit Stretchable Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machi... |
| 4 | no | 13452734 | - | 0.483 | brand=I AM FOR YOU, color=Green, occasion=Western, price=2299.0 | Product: I AM FOR YOU Women Green & Grey Printed Flared Palazzos Brand: I AM FOR YOU Color: Green Pattern: Abstract printed Length: Regular Top fabric: Viscose rayon Occasion: W... |
| 5 | no | 17403434 | - | 0.477 | brand=I Saw It First, color=White, category=Playsuit, occasion=Casual, price=3199.0 | Product: I Saw It First Women White & Blue Floral Printed Skort Playsuit Brand: I Saw It First Color: White Category: Playsuit Pattern: Printed Neck: Round neck Sleeves: Short s... |
| 6 | no | 17365722 | - | 0.474 | brand=I Saw It First, color=Beige, category=Regular shorts, occasion=Casual, price=1999.0 | Product: I Saw It First Women Beige Striped High-Rise Shorts Brand: I Saw It First Color: Beige Category: Regular shorts Pattern: Striped Length: Above knee Top fabric: Polyeste... |
| 7 | no | 17403428 | - | 0.472 | brand=I Saw It First, color=Blue, occasion=Casual, price=3799.0 | Product: I Saw It First Women Blue Skinny Fit Highly Distressed Light Fade Stretchable Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casua... |
| 8 | no | 14159320 | - | 0.467 | brand=I AM FOR YOU, color=Yellow, category=A-line, occasion=Casual, price=1699.0 | Product: I AM FOR YOU Women Yellow & White Embroidered Detail A-Line Skirt with Gathers Brand: I AM FOR YOU Color: Yellow Category: A-line Pattern: Solid Length: Mini Hemline: F... |
| 9 | no | 17403380 | - | 0.466 | brand=I Saw It First, color=Blue, occasion=Casual, price=2899.0 | Product: I Saw It First Women Blue Slash Knee Frayed Hem Mom Fit Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care... |
| 10 | no | 17403300 | - | 0.462 | brand=I Saw It First, color=Blue, occasion=Casual, price=4299.0 | Product: I Saw It First Women Blue Light Fade Mid Wash High Rise Skinny Fit Stretchable Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casu... |
| 11 | no | 17365728 | - | 0.459 | brand=I Saw It First, color=Pink, category=Flared, occasion=Casual, price=1499.0 | Product: I Saw It First Women Dusty Pink & White Striped Pleated Mini Skater Skirt Brand: I Saw It First Color: Pink Category: Flared Pattern: Striped Length: Mini Hemline: Flar... |
| 12 | no | 17365720 | - | 0.452 | brand=I Saw It First, color=Green, category=Flared, occasion=Casual, price=1899.0 | Product: I Saw It First Women Green Solid Pleated Mini Side Split Skater Skirt Brand: I Saw It First Color: Green Category: Flared Pattern: Solid Length: Mini Hemline: Flared To... |
| 13 | no | 17570416 | - | 0.362 | brand=SHOWOFF, color=Black, occasion=Casual, price=4220.0 | Product: SHOWOFF Women Black Straight Fit Stretchable Jeans Brand: SHOWOFF Color: Black Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 6 and more Wash care: Dry ... |
| 14 | no | 19097390 | - | 0.353 | brand=I Love She, color=White, category=Regular trousers, occasion=Casual, price=2399.0 | Product: I Love She Women White Relaxed High-Rise Trousers Brand: I Love She Color: White Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: ... |
| 15 | no | 18245104 | - | 0.350 | brand=Miss Chase, color=Blue, occasion=Casual, price=3195.0 | Product: Miss Chase Women Blue Jogger High-Rise Cuffed Hem Stretchable Jeans Brand: Miss Chase Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 6 and mor... |
| 16 | no | 18142614 | - | 0.349 | brand=SHOWOFF, color=Lavender, occasion=Casual, price=4655.0 | Product: SHOWOFF Women Lavender Jogger High-Rise Cuffed Hem Stretchable Jeans Brand: SHOWOFF Color: Lavender Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 6 and... |
| 17 | no | 14925780 | - | 0.348 | brand=Roadster, color=Blue, occasion=Casual, price=2299.0 | Product: Roadster Women Blue Wide Leg Stretchable Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 and more Wash care: Machine wash |
| 18 | no | 12629360 | - | 0.341 | brand=Roadster, color=Rust, occasion=Casual, price=2099.0 | Product: Roadster Women Rust Red Regular Fit Mid-Rise Clean Look Cargo Joggers Jeans Brand: Roadster Color: Rust Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 a... |
| 19 | no | 18245110 | - | 0.341 | brand=Miss Chase, color=Blue, occasion=Casual, price=3195.0 | Product: Miss Chase Women Blue High-Rise Mildly Distressed Stretchable Jeans Brand: Miss Chase Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 and mor... |
| 20 | no | 19097392 | - | 0.336 | brand=I Love She, color=Maroon, category=Regular trousers, occasion=Casual, price=1399.0 | Product: I Love She Women Maroon Relaxed Skinny Fit High-Rise Trousers Brand: I Love She Color: Maroon Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Poly... |
| 21 | no | 14954878 | - | 0.336 | brand=Roadster, color=Charcoal, occasion=Casual, price=2599.0 | Product: Roadster Women Charcoal Mid-Rise Straight Fit Jeans Brand: Roadster Color: Charcoal Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 and more Wash care: M... |
| 22 | no | 11284776 | - | 0.332 | brand=Mast & Harbour, color=Blue, occasion=Casual, price=2299.0 | Product: Mast & Harbour Women Blue Mid-Rise Clean Look Cargo Jogger Jeans Brand: Mast & Harbour Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 and mo... |
| 23 | no | 17570328 | - | 0.331 | brand=SHOWOFF, color=Blue, occasion=Casual, price=4845.0 | Product: SHOWOFF Women Blue Wide Leg High-Rise Low Distress Heavy Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Pockets... |
| 24 | no | 17570364 | - | 0.327 | brand=SHOWOFF, color=Blue, occasion=Casual, price=4655.0 | Product: SHOWOFF Women Blue Straight Fit High-Rise Low Distress Light Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Poc... |
| 25 | no | 16524266 | - | 0.327 | brand=LOOKNBOOK ART, color=Orange, price=4500.0 | Product: LOOKNBOOK ART Orange Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: LOOKNBOOK ART Color: Orange Dupatta: With dupatta Pattern: Woven design Neck: Round n... |
| 26 | no | 13878270 | - | 0.314 | brand=High Star, color=Blue, occasion=Casual, price=1299.0 | Product: High Star Women Blue Straight Fit High-Rise Clean Look Jeans Brand: High Star Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 6 and more Wash c... |
| 27 | no | 15559842 | - | 0.308 | brand=High Star, color=Grey, occasion=Casual, price=2299.0 | Product: High Star Women Grey Jogger High-Rise Jeans Brand: High Star Color: Grey Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 6 and more Wash care: Machine wash |
| 28 | no | 15474590 | - | 0.306 | brand=High Star, color=Rust, occasion=Casual, price=2299.0 | Product: High Star Women Rust Jogger High-Rise Low Distress Jeans Brand: High Star Color: Rust Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 6 and more Wash care:... |
| 29 | no | 15266700 | - | 0.216 | brand=max, color=Beige, occasion=Daily, price=299.0 | Product: max Beige Pure Cotton Dupatta Brand: max Color: Beige Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash |
| 30 | no | 15312982 | - | 0.209 | brand=LOOKNBOOK ART, color=Black, price=3900.0 | Product: LOOKNBOOK ART Black & Beige Embellished Sequinned Semi-Stitched Lehenga Set Brand: LOOKNBOOK ART Color: Black Pattern: Embellished Neck: Round neck Sleeves: Sleeveless ... |

### Question 20/50

**Query:** Do you have anything from Bhama Couture in A-line?

**Retrieval metadata:** brand == Bhama Couture

**Relevant docs:** `['12151804', '10355827', '10356731', '12151824', '10717820', '9430103', '9430109', '10355839']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.267 | 1.000 | 0.167 | 0.574 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 9430121 | - | 0.978 | brand=Bhama Couture, color=Black, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Black Embroidered A-Line Pure Cotton Top Brand: Bhama Couture Color: Black Category: A-line Pattern: Ethnic motifs embellished Neck: V-neck Sleeves: Three... |
| 2 | no | 9430115 | - | 0.965 | brand=Bhama Couture, color=Navy Blue, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Navy Blue Embroidered A-Line Top Brand: Bhama Couture Color: Navy Blue Category: A-line Pattern: Ethnic motifs embellished Neck: Round neck Sleeves:... |
| 3 | no | 13969870 | - | 0.965 | brand=Bhama Couture, color=Navy Blue, category=A-line, occasion=Ethnic, price=2999.0 | Product: Bhama Couture Navy Blue & Red Embroidered Detail A-Line Top Brand: Bhama Couture Color: Navy Blue Category: A-line Pattern: Solid Neck: Round neck Sleeves: Three-quarte... |
| 4 | no | 11672988 | - | 0.962 | brand=Bhama Couture, color=White, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women White & Green Floral Print A-Line Top Brand: Bhama Couture Color: White Category: A-line Pattern: Floral printed Neck: Round neck Sleeves: Sleeveles... |
| 5 | no | 9717189 | - | 0.951 | brand=Bhama Couture, color=Navy Blue, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Navy Blue Embroidered A-Line Pure Cotton Top Brand: Bhama Couture Color: Navy Blue Category: A-line Pattern: Floral embellished Neck: Tie-up neck Sl... |
| 6 | yes | 10355827 | - | 0.947 | brand=Bhama Couture, color=Blue, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Blue Embroidered A-Line Pure Cotton Top Brand: Bhama Couture Color: Blue Category: A-line Pattern: Ethnic motifs embellished Neck: Round neck Sleeve... |
| 7 | yes | 12151824 | - | 0.940 | brand=Bhama Couture, color=Maroon, category=A-line, occasion=Ethnic, price=1499.0 | Product: Bhama Couture Women Maroon Printed A-Line Top Brand: Bhama Couture Color: Maroon Category: A-line Pattern: Ethnic motifs printed Neck: Tie-up neck Sleeves: Three-quarte... |
| 8 | no | 13969820 | - | 0.932 | brand=Bhama Couture, color=Maroon, category=A-line, occasion=Ethnic, price=2999.0 | Product: Bhama Couture Maroon & Black Embroidered Bell Sleeves A-Line Top Brand: Bhama Couture Color: Maroon Category: A-line Pattern: Ethnic motifs embroidered Neck: Round neck... |
| 9 | no | 8339967 | - | 0.920 | brand=Bhama Couture, color=Red, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Red Embroidered Detail A-Line Top Brand: Bhama Couture Color: Red Category: A-line Pattern: Geometric embellished Neck: Tie-up neck Sleeves: Short f... |
| 10 | yes | 12151804 | - | 0.912 | brand=Bhama Couture, color=Blue, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Blue & Pink Floral Print A-Line Pure Cotton Top Brand: Bhama Couture Color: Blue Category: A-line Pattern: Ethnic motifs printed Neck: Keyhole neck ... |
| 11 | yes | 10356731 | - | 0.906 | brand=Bhama Couture, color=Blue, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Blue Embroidered Cotton A-Line Top Brand: Bhama Couture Color: Blue Category: A-line Pattern: Ethnic motifs embellished Neck: Tie-up neck Sleeves: T... |
| 12 | no | 11625546 | - | 0.899 | brand=Bhama Couture, color=Red, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Red & White Striped A-Line Top Brand: Bhama Couture Color: Red Category: A-line Pattern: Vertical stripes striped Neck: Round neck Sleeves: Three-qu... |
| 13 | yes | 10355839 | - | 0.892 | brand=Bhama Couture, color=Red, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Red Solid A-Line Pure Cotton Top Brand: Bhama Couture Color: Red Category: A-line Pattern: Solid Neck: Tie-up neck Sleeves: Three-quarter puff sleev... |
| 14 | yes | 9430103 | - | 0.888 | brand=Bhama Couture, color=Red, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Red Solid A-Line Pure Cotton Top Brand: Bhama Couture Color: Red Category: A-line Pattern: Solid Neck: Round neck Sleeves: Three-quarter regular sle... |
| 15 | yes | 10717820 | - | 0.888 | brand=Bhama Couture, color=Navy Blue, category=A-line, occasion=Ethnic, price=1699.0 | Product: Bhama Couture Women Blue Embroidered Detail Chambray A-Line Pure Cotton Top Brand: Bhama Couture Color: Navy Blue Category: A-line Pattern: Solid Neck: Tie-up neck Slee... |
| 16 | yes | 9430109 | - | 0.866 | brand=Bhama Couture, color=Mustard, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Mustard Yellow A-Line Pure Cotton Top Brand: Bhama Couture Color: Mustard Category: A-line Pattern: Solid Neck: Round neck Sleeves: Three-quarter regular ... |
| 17 | no | 13969880 | - | 0.835 | brand=Bhama Couture, color=Yellow, category=A-line, occasion=Ethnic, price=2549.0 | Product: Bhama Couture Yellow & White Printed Tie-Up Neck Flared Sleeves A-Line Top Brand: Bhama Couture Color: Yellow Category: A-line Pattern: Ethnic motifs printed Neck: Tie-... |
| 18 | no | 12795840 | - | 0.831 | brand=Bhama Couture, color=Black, occasion=Daily, price=1999.0 | Product: Bhama Couture Women Black & Pink Yoke Design Pure Cotton High-Low Kurti Brand: Bhama Couture Color: Black Pattern: Ethnic motifs yoke design Shape: A-line Neck: Mandari... |
| 19 | no | 10745490 | - | 0.769 | brand=Bhama Couture, color=Mustard, category=A-line, occasion=Ethnic, price=1599.0 | Product: Bhama Couture Women Mustard Yellow Solid Mirror Work A-Line Top Brand: Bhama Couture Color: Mustard Category: A-line Pattern: Geometric solid Neck: Tie-up neck Sleeves:... |
| 20 | no | 4380660 | - | 0.702 | brand=Bhama Couture, color=Peach, category=A-line, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Peach-Coloured Printed A-Line Top Brand: Bhama Couture Color: Peach Category: A-line Pattern: Floral printed Neck: Tie-up neck Sleeves: Three-quarte... |
| 21 | no | 4380652 | - | 0.688 | brand=Bhama Couture, color=Off White, category=A-line, occasion=Casual, price=1799.0 | Product: Bhama Couture Women Off-White Printed A-Line Top Brand: Bhama Couture Color: Off White Category: A-line Pattern: Geometric printed Neck: Boat neck Sleeves: Three-quarte... |
| 22 | no | 9816649 | - | 0.586 | brand=Bhama Couture, color=Red, category=Kurta set, occasion=Daily, price=3599.0 | Product: Bhama Couture Women Red Solid Kurta with Palazzos Brand: Bhama Couture Color: Red Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Solid Shape: A-line... |
| 23 | no | 10343559 | - | 0.556 | brand=Bhama Couture, color=Blue, category=Kurta set, occasion=Daily, price=3599.0 | Product: Bhama Couture Women Blue & White Bandhani Printed Kurta with Palazzos Brand: Bhama Couture Color: Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern... |
| 24 | no | 1823751 | - | 0.549 | brand=Bhama Couture, color=Black, occasion=Ethnic, price=1860.0 | Product: Bhama Couture Black Tunic with Embroidered Detail Brand: Bhama Couture Color: Black Pattern: Embroidered Neck: Round neck Sleeves: Three-quarter sleeves Top fabric: Cot... |
| 25 | no | 2129862 | - | 0.541 | brand=Bhama Couture, color=Off White, category=Regular, occasion=Ethnic, price=1899.0 | Product: Bhama Couture Women Off-White Embroidered Top Brand: Bhama Couture Color: Off White Category: Regular Pattern: Floral self design Neck: Mandarin collar Sleeves: Long fl... |
| 26 | no | 18288422 | - | 0.531 | brand=Bhama Couture, color=Off White, occasion=Festive, price=4499.0 | Product: Bhama Couture Women Off White Floral Chanderi Silk Anarkali Kurta & Dupatta Brand: Bhama Couture Color: Off White Pattern: Floral printed Shape: Anarkali Neck: Round ne... |
| 27 | no | 13969840 | - | 0.523 | brand=Bhama Couture, color=White, occasion=Ethnic, price=3249.0 | Product: Bhama Couture Women White & Red Embroidered Tunic Brand: Bhama Couture Color: White Pattern: Embroidered Neck: Round neck Sleeves: Three-quarter sleeves Top fabric: Cot... |
| 28 | no | 9285083 | - | 0.520 | brand=Bhama Couture, color=Mustard, category=Kurta set, occasion=Festive, price=3599.0 | Product: Bhama Couture Women Mustard Yellow Yoke Design Kurta with Palazzos Brand: Bhama Couture Color: Mustard Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern... |
| 29 | no | 15367618 | - | 0.510 | brand=Bhama Couture, color=Purple, occasion=Festive, price=3999.0 | Product: Bhama Couture Women Purple & Gold-Toned Block Print Anarkali Kurta Brand: Bhama Couture Color: Purple Pattern: Woven design Shape: Anarkali Neck: Mandarin collar Sleeve... |
| 30 | no | 2129857 | - | 0.507 | brand=Bhama Couture, color=Off White, category=Regular, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Off-White Solid Pure Cotton Top Brand: Bhama Couture Color: Off White Category: Regular Pattern: Geometric solid Neck: Tie-up neck Sleeves: Three-qu... |

### Question 21/50

**Query:** Do you have any Pink Peg trousers for everyday wear?

**Retrieval metadata:** color == Pink, occasion == Daily

**Relevant docs:** `['15473916']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 15749796 | - | 0.865 | brand=W, color=Pink, category=Kurta set, occasion=Daily, price=2799.0 | Product: W Women Pink Striped Kurta with Trousers Brand: W Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Striped Shape: Straight Neck: Round nec... |
| 2 | no | 16891228 | - | 0.660 | brand=Jaipur Kurti, color=Pink, category=Kurta set, occasion=Daily, price=4649.0 | Product: Jaipur Kurti Women Pink Floral Gotta Patti Pure Cotton Kurta with Trousers & Dupatta Brand: Jaipur Kurti Color: Pink Category: Kurta set Top type: Kurta Bottom type: Tr... |
| 3 | no | 14708328 | - | 0.659 | brand=all about you, color=Pink, occasion=Daily, price=1999.0 | Product: all about you Women Pink & Gold-Toned Embroidered Floral Yoke Design Thread Kurta Brand: all about you Color: Pink Pattern: Floral yoke design Shape: Straight Neck: Rou... |
| 4 | no | 15582360 | - | 0.566 | brand=Anouk, color=Pink, category=Kurta set, occasion=Daily, price=2599.0 | Product: Anouk Women Pink Floral Embroidered Pleated Thread Work Kurta with Trousers Brand: Anouk Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: ... |
| 5 | no | 10317793 | - | 0.557 | brand=Jaipur Kurti, color=Pink, category=Kurta set, occasion=Daily, price=3049.0 | Product: Jaipur Kurti Women Pink & Green Printed Kurta with Trousers Brand: Jaipur Kurti Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Ethnic mo... |
| 6 | no | 16844726 | - | 0.522 | brand=Sangria, color=Pink, category=Kurta set, occasion=Daily, price=3799.0 | Product: Sangria Women Pink & Blue Geometric Printed Pure Cotton Kurta with Trousers Brand: Sangria Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern... |
| 7 | no | 15445194 | - | 0.500 | brand=PIRKO, color=Pink, category=Dress, occasion=Daily, price=2199.0 | Product: PIRKO Pink & Off White Printed Pure Cotton Unstitched Dress Material Brand: PIRKO Color: Pink Category: Dress Pattern: Floral Bottom fabric: Pure cotton Dupatta fabric:... |
| 8 | no | 12307502 | - | 0.492 | brand=Prakhya, color=Pink, category=Kurta set, occasion=Daily, price=3298.0 | Product: Prakhya Women Pink Self Design Kurta with Trousers & Dupatta Brand: Prakhya Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta ... |
| 9 | no | 13078244 | - | 0.473 | brand=W, color=Pink, occasion=Daily, price=1599.0 | Product: W Women Pink Solid Straight Kurta Brand: W Color: Pink Pattern: Solid Shape: Straight Neck: Mandarin collar Sleeves: Three-quarter regular sleeves Length: Calf length H... |
| 10 | no | 17096098 | - | 0.473 | brand=Anouk, color=Pink, category=Kurta set, occasion=Daily, price=2999.0 | Product: Anouk Women Pink Pure Cotton Kurta with Trousers Brand: Anouk Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Solid Shape: Straight Neck:... |
| 11 | no | 17090142 | - | 0.464 | brand=Anouk, color=Pink, category=Kurta set, occasion=Daily, price=3399.0 | Product: Anouk Women Pink Solid Kurta with Trousers Brand: Anouk Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Solid Shape: Straight Neck: V-nec... |
| 12 | no | 16872392 | - | 0.460 | brand=Sangria, color=Pink, category=Kurta set, occasion=Daily, price=1999.0 | Product: Sangria Women Pink Printed Keyhole Neck Kurta with Trousers Brand: Sangria Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Checked printe... |
| 13 | no | 12663796 | - | 0.457 | brand=EXTRA LOVE BY LIBAS, color=Pink, category=Kurta set, occasion=Daily, price=2499.0 | Product: EXTRA LOVE BY LIBAS Plus Size Women Pink Ethnic Motifs Printed Cotton Kurta with Trousers Brand: EXTRA LOVE BY LIBAS Color: Pink Category: Kurta set Top type: Kurta Bot... |
| 14 | no | 14949672 | - | 0.455 | brand=Stylum, color=Pink, category=Kurta set, occasion=Daily, price=3200.0 | Product: Stylum Women Pink Ethnic Motifs Printed Pure Cotton Kurta with Trousers & Dupatta Brand: Stylum Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Du... |
| 15 | no | 16874556 | - | 0.449 | brand=Sangria, color=Pink, category=Kurta set, occasion=Daily, price=1799.0 | Product: Sangria Women Pink Printed Pure Cotton Kurta with Trousers Brand: Sangria Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Geometric print... |
| 16 | no | 12105006 | - | 0.440 | brand=Sangria, color=Pink, category=Kurta set, occasion=Daily, price=1899.0 | Product: Sangria Women Pink & Golden Printed Pure Cotton Kurta with Trousers Brand: Sangria Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Ethnic... |
| 17 | no | 12873874 | - | 0.433 | brand=Anubhutee, color=Pink, category=Kurta set, occasion=Daily, price=3999.0 | Product: Anubhutee Women Pink & White Printed Kurta with Trousers & Dupatta Brand: Anubhutee Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With ... |
| 18 | no | 19040404 | - | 0.423 | brand=KARAJ JAIPUR, color=Pink, category=Kurti set, occasion=Daily, price=4895.0 | Product: KARAJ JAIPUR Women Pink Embroidered Kurti with Trousers & With Dupatta Brand: KARAJ JAIPUR Color: Pink Category: Kurti set Top type: Kurti Bottom type: Trousers Dupatta... |
| 19 | no | 15440308 | - | 0.397 | brand=HERE&NOW, color=Pink, category=Kurta set, occasion=Daily, price=1799.0 | Product: HERE&NOW Women Pink & Grey Ethnic Motifs Print Straight Kurta with Trousers Brand: HERE&NOW Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Patter... |
| 20 | no | 19040436 | - | 0.386 | brand=KARAJ JAIPUR, color=Pink, category=Kurta set, occasion=Daily, price=6995.0 | Product: KARAJ JAIPUR Women Pink Pure Cotton Anarkali Kurta with Trousers & Dupatta Brand: KARAJ JAIPUR Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Dup... |
| 21 | no | 15582352 | - | 0.374 | brand=Anouk, color=Pink, occasion=Daily, price=1699.0 | Product: Anouk Women Pink Pure Cotton Straight Pastel Kurta Brand: Anouk Color: Pink Pattern: Solid Shape: Straight Neck: Round neck Sleeves: Three-quarter regular sleeves Lengt... |
| 22 | no | 13932860 | - | 0.371 | brand=anayna, color=Pink, category=Kurta set, occasion=Daily, price=3190.0 | Product: anayna Women Pink Printed Kurta with Trousers Brand: anayna Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Ethnic motifs printed Shape: ... |
| 23 | no | 19325284 | - | 0.365 | brand=POONAM DESIGNER, color=Pink, occasion=Daily, price=2499.0 | Product: POONAM DESIGNER Women Pink Ethnic Motifs Printed Kurta Brand: POONAM DESIGNER Color: Pink Pattern: Ethnic motifs printed Shape: A-line Neck: Shirt collar Sleeves: Short... |
| 24 | no | 17094694 | - | 0.362 | brand=Anouk, color=Pink, category=Kurta set, occasion=Daily, price=3499.0 | Product: Anouk Women Pink & Orange Bandhani Printed Pure Cotton Kurta with Trousers & Dupatta Brand: Anouk Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers ... |
| 25 | no | 14880040 | - | 0.353 | brand=ADA, color=Pink, category=Dress, occasion=Daily, price=2990.0 | Product: ADA Pink Embroidered Sustainable Unstitched Dress Material Brand: ADA Color: Pink Category: Dress Pattern: Ethnic motifs Bottom fabric: Poly georgette Dupatta fabric: P... |
| 26 | no | 15271046 | - | 0.350 | brand=AHIKA, color=Pink, category=Kurta set, occasion=Daily, price=4247.0 | Product: AHIKA Women Pink & White Bandhani Print Pure Cotton Kurta with Trousers & Dupatta Brand: AHIKA Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Dup... |
| 27 | no | 15816496 | - | 0.321 | brand=Fabindia, color=Pink, occasion=Daily, price=2799.0 | Product: Fabindia Pink Yoke Design V-Neck Kurti Brand: Fabindia Color: Pink Pattern: Striped yoke design Shape: Straight Neck: V-neck Sleeves: Three-quarter regular sleeves Heml... |
| 28 | no | 18509098 | - | 0.320 | brand=SANGAM PRINTS, color=Pink, category=Saree, occasion=Daily, price=1149.0 | Product: SANGAM PRINTS Pink Floral Poly Georgette Saree Brand: SANGAM PRINTS Color: Pink Category: Saree Pattern: Floral printed Occasion: Daily Wash care: Dry clean |
| 29 | no | 19324656 | - | 0.317 | brand=FASHOR, color=Pink, occasion=Daily, price=2799.0 | Product: FASHOR Women Pink Floral Embroidered Straight Fit Kurta Brand: FASHOR Color: Pink Pattern: Floral embroidered Shape: Straight Neck: Round neck Sleeves: Long regular sle... |
| 30 | no | 10356859 | - | 0.308 | brand=Libas, color=Pink, category=Kurta set, occasion=Daily, price=2499.0 | Product: Libas Floral Bliss Side Pocket Cotton Kurta Set Brand: Libas Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Floral printed Shape: A-line... |

### Question 22/50

**Query:** Show me Regular shorts within a budget of 1800.

**Retrieval metadata:** price <= 1800.0

**Relevant docs:** `['15402090', '14170730', '18283554', '18747132', '16164252', '11535910', '14609842', '15083714']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.033 | 0.125 | 0.125 | 0.080 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 13523706 | - | 0.500 | brand=Varanga, color=Black, occasion=Daily, price=1799.0 | Product: Varanga Women Black & White Geometric Printed Bell Sleeves Kurta Brand: Varanga Color: Black Pattern: Geometric printed Shape: Straight Neck: Mandarin collar Sleeves: T... |
| 2 | no | 14272032 | - | 0.500 | brand=Oxolloxo, color=Orange, category=Regular shorts, occasion=Casual, price=1949.0 | Product: Oxolloxo Women Orange Solid Regular Fit Regular Shorts Brand: Oxolloxo Color: Orange Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occas... |
| 3 | no | 13647622 | - | 0.486 | brand=Varanga, color=Pink, occasion=Daily, price=3599.0 | Product: Varanga Women Pink & White Leheriya Printed Angrakha Kurta With Embroidery Brand: Varanga Color: Pink Pattern: Leheriya printed Shape: A-line Neck: V-neck Sleeves: Thre... |
| 4 | no | 13769372 | - | 0.485 | brand=Varanga, color=Black, occasion=Daily, price=2299.0 | Product: Varanga Classic Black and White Bandhani Print Cotton Kurta Brand: Varanga Color: Black Pattern: Bandhani printed Shape: Straight Neck: Tie-up neck Sleeves: Three-quart... |
| 5 | no | 9621439 | - | 0.470 | brand=WISSTLER, color=Blue, category=Regular shorts, occasion=Casual, price=799.0 | Product: WISSTLER Women Blue Printed Regular Fit Regular Shorts Brand: WISSTLER Color: Blue Category: Regular shorts Pattern: Geometric printed Length: Above knee Top fabric: Po... |
| 6 | no | 11101312 | - | 0.468 | brand=WISSTLER, color=Blue, category=Regular shorts, occasion=Casual, price=899.0 | Product: WISSTLER Women Blue Printed Regular Fit Shorts Brand: WISSTLER Color: Blue Category: Regular shorts Pattern: Abstract printed Length: Above knee Top fabric: Polyester O... |
| 7 | no | 17251600 | - | 0.458 | brand=Athena, color=Black, category=Regular shorts, occasion=Casual, price=1499.0 | Product: Athena Women Black Shorts Brand: Athena Color: Black Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Polyester Occasion: Casual Pockets: 2 Wash c... |
| 8 | yes | 15083714 | - | 0.443 | brand=DressBerry, color=Green, category=Regular shorts, occasion=Casual, price=1349.0 | Product: DressBerry Women Green Striped Regular Shorts Brand: DressBerry Color: Green Category: Regular shorts Pattern: Striped Length: Above knee Top fabric: Polyester Occasion... |
| 9 | no | 16836260 | - | 0.407 | brand=Roadster, color=Blue, category=Regular shorts, occasion=Casual, price=1899.0 | Product: Roadster Women Indigo Shaded Mid Rise Casual Shorts Brand: Roadster Color: Blue Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: ... |
| 10 | no | 14027018 | - | 0.382 | brand=Oxolloxo, color=Olive, category=Regular shorts, occasion=Casual, price=1699.0 | Product: Oxolloxo Women Olive Green Solid Regular Fit Regular Shorts Brand: Oxolloxo Color: Olive Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton O... |
| 11 | no | 14272016 | - | 0.378 | brand=Oxolloxo, color=Green, category=Regular shorts, occasion=Casual, price=1899.0 | Product: Oxolloxo Women Green Solid Regular Fit Regular Shorts Brand: Oxolloxo Color: Green Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasio... |
| 12 | no | 14340718 | - | 0.368 | brand=MANGO, color=Peach, category=Regular shorts, occasion=Casual, price=2390.0 | Product: MANGO Women Peach-Coloured Solid Regular Shorts Brand: MANGO Color: Peach Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Viscose rayon Occasion:... |
| 13 | no | 14388576 | - | 0.366 | brand=Oxolloxo, color=Black, category=Regular shorts, occasion=Casual, price=1599.0 | Product: Oxolloxo Women Black & Yellow Polka Dot Print Regular Fit Shorts Brand: Oxolloxo Color: Black Category: Regular shorts Pattern: Geometric printed Length: Above knee Top... |
| 14 | no | 19235420 | - | 0.355 | brand=Oxolloxo, color=Brown, category=Regular shorts, occasion=Casual, price=1899.0 | Product: Oxolloxo Women Brown Shorts Brand: Oxolloxo Color: Brown Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wash ... |
| 15 | no | 13529198 | - | 0.352 | brand=Harvard, color=White, category=Regular shorts, occasion=Casual, price=1399.0 | Product: Harvard Women White & Navy Striped Regular Shorts with Belt Brand: Harvard Color: White Category: Regular shorts Pattern: Striped Length: Above knee Top fabric: Polyest... |
| 16 | no | 12969482 | - | 0.339 | brand=Hypernation, color=Olive, category=Regular shorts, occasion=Casual, price=1199.0 | Product: Hypernation Women Olive Green Solid Slim Fit Regular Shorts Brand: Hypernation Color: Olive Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotto... |
| 17 | no | 13060194 | - | 0.334 | brand=QUARANTINE, color=Off White, category=Regular shorts, occasion=Casual, price=899.0 | Product: QUARANTINE Women Off-White Printed Regular Fit Regular Shorts Brand: QUARANTINE Color: Off White Category: Regular shorts Pattern: Graphic printed Length: Above knee To... |
| 18 | no | 13985432 | - | 0.334 | brand=Belle Fille, color=Blue, category=Regular shorts, occasion=Casual, price=1199.0 | Product: Belle Fille Women Blue Solid Regular Fit Shorts Brand: Belle Fille Color: Blue Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Polyester Occasion... |
| 19 | no | 14672892 | - | 0.333 | brand=Colour Me by Melange, color=Navy Blue, category=Regular shorts, occasion=Casual, price=799.0 | Product: Colour Me by Melange Women Navy Blue Mid-Rise Regular Cotton Shorts Brand: Colour Me by Melange Color: Navy Blue Category: Regular shorts Pattern: Solid Length: Above k... |
| 20 | no | 19047410 | - | 0.332 | brand=Roadster, color=Black, category=Regular shorts, occasion=Casual, price=999.0 | Product: Roadster Women Black Solid Shorts Brand: Roadster Color: Black Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Polyester Occasion: Casual Wash ca... |
| 21 | no | 17256464 | - | 0.317 | brand=Athena, color=Blue, category=Regular shorts, occasion=Casual, price=1499.0 | Product: Athena Women Blue Shorts Brand: Athena Color: Blue Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Polyester Occasion: Casual Pockets: 2 Wash car... |
| 22 | no | 14219670 | - | 0.306 | brand=DressBerry, color=Navy Blue, category=Regular shorts, occasion=Casual, price=1299.0 | Product: DressBerry Women Navy Blue Shorts Brand: DressBerry Color: Navy Blue Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pock... |
| 23 | no | 15103054 | - | 0.297 | brand=MANGO, color=Yellow, category=Regular shorts, occasion=Casual, price=2390.0 | Product: MANGO Women Yellow Floral Printed High-Rise Regular Shorts Brand: MANGO Color: Yellow Category: Regular shorts Pattern: Floral printed Length: Above knee Top fabric: Vi... |
| 24 | no | 15083698 | - | 0.294 | brand=DressBerry, color=Pink, category=Regular shorts, occasion=Casual, price=1349.0 | Product: DressBerry Women Pink Striped Regular Shorts Brand: DressBerry Color: Pink Category: Regular shorts Pattern: Striped Length: Above knee Top fabric: Polyester Occasion: ... |
| 25 | no | 13391802 | - | 0.287 | brand=Mast & Harbour, color=Grey Melange, category=Regular shorts, occasion=Casual, price=1099.0 | Product: Mast & Harbour Women Grey Melange Solid Regular Fit Regular Shorts Brand: Mast & Harbour Color: Grey Melange Category: Regular shorts Pattern: Solid Length: Above knee ... |
| 26 | no | 12929508 | - | 0.286 | brand=Mast & Harbour, color=Navy Blue, category=Regular shorts, occasion=Casual, price=1299.0 | Product: Mast & Harbour Women Navy Blue Solid Regular Shorts Brand: Mast & Harbour Color: Navy Blue Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Polyes... |
| 27 | no | 11012420 | - | 0.268 | brand=HRX by Hrithik Roshan, color=Black, category=Regular shorts, occasion=Sports, price=1499.0 | Product: HRX by Hrithik Roshan Women Black & Orange Colourblocked Regular Fit Lifestyle Shorts Brand: HRX by Hrithik Roshan Color: Black Category: Regular shorts Pattern: Colour... |
| 28 | no | 18611674 | - | 0.267 | brand=Honey by Pantaloons, color=Khaki, category=Regular shorts, occasion=Casual, price=1099.0 | Product: Honey by Pantaloons Women Khaki Striped High-Rise Linen Shorts Brand: Honey by Pantaloons Color: Khaki Category: Regular shorts Pattern: Striped Length: Above knee Top ... |
| 29 | no | 14954482 | - | 0.265 | brand=Roadster, color=Olive, category=Regular shorts, occasion=Casual, price=1899.0 | Product: Roadster Women Olive Green Loose Fit High-Rise Shorts Brand: Roadster Color: Olive Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasio... |
| 30 | no | 16885654 | - | 0.260 | brand=Alsace Lorraine Paris, color=Pink, category=Regular shorts, occasion=Casual, price=1499.0 | Product: Alsace Lorraine Paris Women Pink Shorts Brand: Alsace Lorraine Paris Color: Pink Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Viscose rayon Oc... |

### Question 23/50

**Query:** I'm looking for Regular by H&M.

**Retrieval metadata:** brand == H&M

**Relevant docs:** `['17964932', '17883620', '18652012', '14258606', '18084562', '18170658', '19074168', '17674588']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.200 | 0.750 | 1.000 | 0.601 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 17674588 | - | 1.000 | brand=H&M, color=Brown, category=Regular, occasion=Casual, price=699.0 | Product: H&M Women Brown Mesh Top Brand: H&M Color: Brown Category: Regular Pattern: Solid Neck: Round neck Sleeves: Long regular sleeves Length: Regular Top fabric: Polyester O... |
| 2 | no | 17965024 | - | 0.861 | brand=H&M, color=Orange, category=Regular trousers, occasion=Casual, price=1999.0 | Product: H&M Orange Ankle-Length Trousers Brand: H&M Color: Orange Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Pockets: 2 Wa... |
| 3 | no | 12383500 | - | 0.783 | brand=H&M, color=Black, category=Regular, occasion=Casual, price=799.0 | Product: H&M Women Black Solid Long-Sleeved Jersey Top Brand: H&M Color: Black Category: Regular Pattern: Solid Neck: Round neck Sleeves: Long regular sleeves Length: Regular To... |
| 4 | no | 17883650 | - | 0.735 | brand=H&M, color=Beige, category=Regular trousers, occasion=Casual, price=1299.0 | Product: H&M Beige Pattern-Knit Trousers Brand: H&M Color: Beige Category: Regular trousers Pattern: Solid self design Length: Regular Top fabric: Polyester Occasion: Casual Was... |
| 5 | no | 17842774 | - | 0.721 | brand=H&M, color=Beige, category=Regular trousers, occasion=Casual, price=2299.0 | Product: H&M Beige Wide Linen-Blend Trousers Brand: H&M Color: Beige Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion: Casual Pockets... |
| 6 | no | 18131688 | - | 0.710 | brand=H&M, color=Black, category=Regular trousers, occasion=Casual, price=1499.0 | Product: H&M Women Black Wide Linen-blend Trousers Brand: H&M Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion: Casual W... |
| 7 | yes | 14258606 | - | 0.701 | brand=H&M, color=White, category=Regular, occasion=Casual, price=399.0 | Product: H&M Girls White Solid Jersey Top Brand: H&M Color: White Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short cap sleeves Length: Regular Top fabric: Polyco... |
| 8 | yes | 17964932 | - | 0.681 | brand=H&M, color=Yellow, category=Regular, occasion=Casual, price=1299.0 | Product: H&M Women Yellow Rapid-Dry Sports Top Brand: H&M Color: Yellow Category: Regular Pattern: Horizontal stripes striped Neck: Round neck Sleeves: Short regular sleeves Len... |
| 9 | no | 17842776 | - | 0.666 | brand=H&M, color=Beige, category=Regular trousers, occasion=Casual, price=2299.0 | Product: H&M Women Beige Striped Wide Linen-Blend Trousers Brand: H&M Color: Beige Category: Regular trousers Pattern: Striped Length: Regular Top fabric: Polyester Occasion: Ca... |
| 10 | no | 17883622 | - | 0.660 | brand=H&M, color=Beige, category=Regular, occasion=Casual, price=499.0 | Product: H&M Girls Beige Cotton Jersey Cropped Top Brand: H&M Color: Beige Category: Regular Pattern: Floral printed Neck: Round neck Sleeves: Short regular sleeves Length: Regu... |
| 11 | yes | 19074168 | - | 0.625 | brand=H&M, color=Green, category=Regular, occasion=Casual, price=699.0 | Product: H&M Women Green Ribbed Cropped Top Brand: H&M Color: Green Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short regular sleeves Length: Crop Top fabric: Cot... |
| 12 | no | 16396394 | - | 0.624 | brand=H&M, color=Green, category=Joggers, occasion=Casual, price=1999.0 | Product: H&M Women Green Fine-Knit Joggers Brand: H&M Color: Green Category: Joggers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Wash care: Hand wash |
| 13 | no | 18747130 | - | 0.611 | brand=H&M, color=Beige, category=Regular shorts, occasion=Casual, price=999.0 | Product: H&M Women Beige Sweatshirt Shorts Brand: H&M Color: Beige Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wash... |
| 14 | no | 17855308 | - | 0.609 | brand=H&M, color=Orange, category=Regular shorts, occasion=Casual, price=1499.0 | Product: H&M Women Orange Pointelle-Knit Cotton Shorts Brand: H&M Color: Orange Category: Regular shorts Pattern: Self design solid Length: Above knee Top fabric: Cotton Occasio... |
| 15 | no | 19074138 | - | 0.608 | brand=H&M, color=Pink, category=Regular, occasion=Casual, price=1499.0 | Product: H&M Women Pink Ribbed Cut-Out Top Brand: H&M Color: Pink Category: Regular Pattern: Solid Neck: Round neck Sleeves: Long regular sleeves Length: Regular Top fabric: Cot... |
| 16 | no | 18747106 | - | 0.607 | brand=H&M, color=Orange, category=Regular shorts, occasion=Casual, price=1299.0 | Product: H&M Women Orange Sweatshirt Shorts Brand: H&M Color: Orange Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wa... |
| 17 | no | 17185856 | - | 0.606 | brand=H&M, color=Blue, occasion=Casual, price=2299.0 | Product: H&M Women Blue Straight High Jeans Brand: H&M Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 18 | yes | 17883620 | - | 0.602 | brand=H&M, color=Yellow, category=Regular, occasion=Casual, price=399.0 | Product: H&M Yellow Puff-Sleeved Jersey Top Brand: H&M Color: Yellow Category: Regular Pattern: Floral printed Neck: Round neck Sleeves: Short regular sleeves Length: Regular To... |
| 19 | no | 17575906 | - | 0.598 | brand=H&M, color=Blue, occasion=Casual, price=1499.0 | Product: H&M Women Blue Solid Skinny Regular Jeans Brand: H&M Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Hand wash |
| 20 | no | 16175534 | - | 0.593 | brand=H&M, color=Red, category=Joggers, occasion=Casual, price=1299.0 | Product: H&M Women Red Cotton Blend Sweatpants Brand: H&M Color: Red Category: Joggers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 2 Wash care: M... |
| 21 | no | 17185466 | - | 0.593 | brand=H&M, color=Beige, category=Regular shorts, occasion=Casual, price=1299.0 | Product: H&M Women Beige & Grey Solid Sweatshirt Shorts Brand: H&M Color: Beige Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Po... |
| 22 | no | 19071830 | - | 0.590 | brand=H&M, color=Blue, occasion=Casual, price=2299.0 | Product: H&M Women Blue Wide High Jeans Brand: H&M Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 23 | no | 19175092 | - | 0.586 | brand=H&M, color=Beige, category=Regular trousers, occasion=Casual, price=1499.0 | Product: H&M Women Beige Solid Pull-On Lyocell-Blend Trousers Brand: H&M Color: Beige Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: C... |
| 24 | no | 18747132 | - | 0.576 | brand=H&M, color=Green, category=Regular shorts, occasion=Casual, price=999.0 | Product: H&M Women Green Terry Shorts Brand: H&M Color: Green Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wash care... |
| 25 | yes | 18170658 | - | 0.547 | brand=H&M, color=White, category=Regular, occasion=Casual, price=599.0 | Product: H&M White Cotton Vest Top Brand: H&M Color: White Category: Regular Pattern: Solid Neck: Scoop neck Sleeves: Sleeveless no Length: Regular Top fabric: Cotton blend Occa... |
| 26 | no | 18834764 | - | 0.534 | brand=H&M, color=Black, category=Parallel trousers, occasion=Casual, price=2299.0 | Product: H&M Women Black Corduroy trousers Brand: H&M Color: Black Category: Parallel trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash... |
| 27 | no | 19174870 | - | 0.527 | brand=H&M, color=Black, category=Regular shorts, occasion=Casual, price=1499.0 | Product: H&M Women Black Low-Waisted Bermuda Shorts Brand: H&M Color: Black Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Polyester Occasion: Casual Was... |
| 28 | no | 18747182 | - | 0.511 | brand=H&M, color=Yellow, category=Regular shorts, occasion=Casual, price=999.0 | Product: H&M Women Yellow Sweatshirt Shorts Brand: H&M Color: Yellow Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wa... |
| 29 | no | 19266944 | - | 0.511 | brand=H&M, color=Blue, category=Regular, occasion=Casual, price=1299.0 | Product: H&M Women Blue Stand-up Collar Satin Blouse Brand: H&M Color: Blue Category: Regular Pattern: Floral printed Neck: High neck Sleeves: Long cuffed sleeves Length: Regula... |
| 30 | no | 19176992 | - | 0.509 | brand=H&M, color=Green, category=Regular, occasion=Casual, price=799.0 | Product: H&M Women Green Ribbed Cut-out Top Brand: H&M Color: Green Category: Regular Pattern: Self design Neck: Round neck Sleeves: Short regular sleeves Length: Crop Top fabri... |

### Question 24/50

**Query:** I need Pink Saree by KALINI.

**Retrieval metadata:** brand == KALINI, color == Pink

**Relevant docs:** `['15858094', '17852902', '15102290', '14678908', '16421936']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.385 | 1.000 | 0.500 | 0.782 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 16914910 | - | 0.906 | brand=KALINI, color=Pink, category=Saree, occasion=Daily, price=1299.0 | Product: KALINI Pink Poly Georgette Casual Saree Brand: KALINI Color: Pink Category: Saree Pattern: Geometric printed Occasion: Daily Wash care: Hand wash |
| 2 | yes | 16421936 | - | 0.836 | brand=KALINI, color=Pink, category=Saree, occasion=Festive, price=2699.0 | Product: KALINI Pink & Gold-Toned Paisley Saree Brand: KALINI Color: Pink Category: Saree Pattern: Paisley printed Occasion: Festive Wash care: Dry clean |
| 3 | yes | 15102290 | - | 0.758 | brand=KALINI, color=Pink, category=Saree, occasion=Traditional, price=1949.0 | Product: KALINI Pink & Gold-Toned Woven Design Zari Art Silk Saree Brand: KALINI Color: Pink Category: Saree Pattern: Woven design Occasion: Traditional Wash care: Hand wash |
| 4 | yes | 17852902 | - | 0.726 | brand=KALINI, color=Pink, category=Saree, occasion=Festive, price=999.0 | Product: KALINI Pink & Gold-Toned Zari Saree Brand: KALINI Color: Pink Category: Saree Pattern: Solid Occasion: Festive Wash care: Hand wash |
| 5 | yes | 14678908 | - | 0.723 | brand=KALINI, color=Pink, category=Saree, occasion=Festive, price=2199.0 | Product: KALINI Pink & Yellow Floral Pure Chiffon Saree Brand: KALINI Color: Pink Category: Saree Pattern: Floral printed Occasion: Festive Wash care: Hand wash |
| 6 | yes | 15858094 | - | 0.636 | brand=KALINI, color=Pink, category=Saree, occasion=Daily, price=2999.0 | Product: KALINI Pack of 2 Pink & Blue Floral Sarees Brand: KALINI Color: Pink Category: Saree Pattern: Floral printed Occasion: Daily Wash care: Machine wash |
| 7 | no | 16948530 | - | 0.602 | brand=KALINI, color=Pink, category=Bandhani, occasion=Work, price=2699.0 | Product: KALINI Pink & Grey Paisley Printed Chiffon Bandhani Saree Brand: KALINI Color: Pink Category: Bandhani Pattern: Paisley printed Occasion: Work Wash care: Hand wash |
| 8 | no | 14798392 | - | 0.548 | brand=KALINI, color=Pink, category=Kota, occasion=Traditional, price=2099.0 | Product: KALINI Pink & Green Ethnic Motifs Kota Saree Brand: KALINI Color: Pink Category: Kota Pattern: Ethnic motifs printed Occasion: Traditional Wash care: Hand wash |
| 9 | no | 12961094 | - | 0.534 | brand=KALINI, color=Pink, category=Kanjeevaram, occasion=Traditional, price=1299.0 | Product: KALINI Pink & Navy Blue Half & Half Printed Kanjeevaram Saree Brand: KALINI Color: Pink Category: Kanjeevaram Pattern: Kalamkari printed Occasion: Traditional Wash care... |
| 10 | no | 17414120 | - | 0.527 | brand=KALINI, color=Pink, category=Block print, occasion=Traditional, price=2699.0 | Product: KALINI Pink & White Batik Zari Block Print Cotton Saree Brand: KALINI Color: Pink Category: Block print Pattern: Batik printed Occasion: Traditional Wash care: Hand wash |
| 11 | no | 16505402 | - | 0.116 | brand=KALINI, color=Pink, occasion=Daily, price=1999.0 | Product: KALINI Women Pink Bandhani Printed Anarkali Kurta Brand: KALINI Color: Pink Pattern: Bandhani printed Shape: Anarkali Neck: Round neck Sleeves: Sleeveless regular Lengt... |
| 12 | no | 18952254 | - | 0.038 | brand=KALINI, color=Pink, occasion=Daily, price=1150.0 | Product: KALINI Women Pink Ethnic Motifs Embroidered Keyhole Neck Georgette Kurta Brand: KALINI Color: Pink Pattern: Ethnic motifs embroidered Shape: Straight Neck: Keyhole neck... |
| 13 | no | 18503778 | - | 0.016 | brand=KALINI, color=Pink, category=Kurti set, occasion=Daily, price=2999.0 | Product: KALINI Women Pink Floral Embroidered Layered Gotta Patti Kurti with Sharara & With Dupatta Brand: KALINI Color: Pink Category: Kurti set Top type: Kurti Bottom type: Sh... |

### Question 25/50

**Query:** Show me products within a budget of 1800.

**Retrieval metadata:** price <= 1800.0

**Relevant docs:** `['17094636', '13905652', '13905672', '13905666', '2322905', '17423996', '14925534', '14925544']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 13523706 | - | 0.500 | brand=Varanga, color=Black, occasion=Daily, price=1799.0 | Product: Varanga Women Black & White Geometric Printed Bell Sleeves Kurta Brand: Varanga Color: Black Pattern: Geometric printed Shape: Straight Neck: Mandarin collar Sleeves: T... |
| 2 | no | 17226172 | - | 0.500 | brand=SHOWOFF, color=Orange, occasion=Casual, price=3905.0 | Product: SHOWOFF Women Orange Mom Fit High-Rise Clean Look Stretchable Jeans Brand: SHOWOFF Color: Orange Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 2 Wash c... |
| 3 | no | 13647622 | - | 0.486 | brand=Varanga, color=Pink, occasion=Daily, price=3599.0 | Product: Varanga Women Pink & White Leheriya Printed Angrakha Kurta With Embroidery Brand: Varanga Color: Pink Pattern: Leheriya printed Shape: A-line Neck: V-neck Sleeves: Thre... |
| 4 | no | 13769372 | - | 0.485 | brand=Varanga, color=Black, occasion=Daily, price=2299.0 | Product: Varanga Classic Black and White Bandhani Print Cotton Kurta Brand: Varanga Color: Black Pattern: Bandhani printed Shape: Straight Neck: Tie-up neck Sleeves: Three-quart... |
| 5 | no | 17570458 | - | 0.472 | brand=SHOWOFF, color=Brown, occasion=Casual, price=4655.0 | Product: SHOWOFF Women Brown Jogger High-Rise Stretchable Jogger Brand: SHOWOFF Color: Brown Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 4 Wash care: Dry clean |
| 6 | no | 18142596 | - | 0.430 | brand=SHOWOFF, color=Blue, occasion=Casual, price=4500.0 | Product: SHOWOFF Women Blue Jogger High-Rise Low Distress Heavy Fade Cuffed Hem Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casua... |
| 7 | no | 17790642 | - | 0.400 | brand=SHOWOFF, color=Orange, category=Culotte jumpsuit, occasion=Casual, price=3720.0 | Product: SHOWOFF Orange & White Printed Culotte Jumpsuit Brand: SHOWOFF Color: Orange Category: Culotte jumpsuit Pattern: Printed Neck: Round neck Sleeves: Three-quarter sleeves... |
| 8 | no | 17685090 | - | 0.399 | brand=BUY NEW TREND, color=Red, category=Open front jacket, occasion=Casual, price=1499.0 | Product: BUY NEW TREND Women Red Black Colourblocked Lightweight Crop Open Front Jacket Brand: BUY NEW TREND Color: Red Category: Open front jacket Pattern: Colourblocked Sleeve... |
| 9 | no | 17250550 | - | 0.390 | brand=SHOWOFF, color=Black, category=Top, occasion=Ethnic, price=5190.0 | Product: SHOWOFF Women Black Embellished Top with Trousers Brand: SHOWOFF Color: Black Category: Top Top type: Top Bottom type: Trousers Pattern: Embellished Neck: Round neck Sl... |
| 10 | no | 18388758 | - | 0.390 | brand=SHOWOFF, color=Burgundy, category=Culotte jumpsuit, occasion=Casual, price=4845.0 | Product: SHOWOFF Burgundy Solid Culotte Jumpsuit Brand: SHOWOFF Color: Burgundy Category: Culotte jumpsuit Pattern: Solid Neck: Round neck Sleeves: Short sleeves Top fabric: Pol... |
| 11 | no | 17801950 | - | 0.390 | brand=SHOWOFF, color=Peach, occasion=Daily, price=1750.0 | Product: SHOWOFF Peach-Coloured & White Ethnic Motifs Printed Kurti Brand: SHOWOFF Color: Peach Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck Sleeves: Three-qu... |
| 12 | no | 18189378 | - | 0.344 | brand=SHOWOFF, color=Blue, category=Capri jumpsuit, occasion=Casual, price=3190.0 | Product: SHOWOFF Blue Strapless Capri Jumpsuit Brand: SHOWOFF Color: Blue Category: Capri jumpsuit Pattern: Solid Neck: Strapless Sleeves: Sleeveless Top fabric: Polyester Occas... |
| 13 | no | 17672184 | - | 0.323 | brand=SHOWOFF, color=Blue, occasion=Casual, price=4565.0 | Product: SHOWOFF Women Blue High-Rise Heavy Fade Stretchable Jogger Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 5 Wash care: Dry clean |
| 14 | no | 18210214 | - | 0.290 | brand=FABRIC FITOOR, color=Black, category=Kaftan, occasion=Ethnic, price=2199.0 | Product: FABRIC FITOOR Black Pure Cotton Printed Kaftan Top Brand: FABRIC FITOOR Color: Black Category: Kaftan Pattern: Abstract printed Neck: Round neck Sleeves: Short kimono s... |
| 15 | no | 19276886 | - | 0.288 | brand=Mitera, color=Grey, category=Saree, occasion=Party, price=4999.0 | Product: Mitera Grey Floral Embroidered Net Fusion Saree Brand: Mitera Color: Grey Category: Saree Pattern: Floral embroidered Occasion: Party Wash care: Dry clean |
| 16 | no | 18468196 | - | 0.281 | brand=KAMI KUBI, color=Blue, category=Regular, occasion=Casual, price=999.0 | Product: KAMI KUBI Women Blue schiffli-Embroidered Crop Top Brand: KAMI KUBI Color: Blue Category: Regular Pattern: Solid Neck: Round neck Sleeves: Sleeveless no Length: Regular... |
| 17 | no | 18338282 | - | 0.273 | brand=SHOWOFF, color=Blue, occasion=Casual, price=4190.0 | Product: SHOWOFF Women Blue Slim Fit High-Rise Mildly Distressed Light Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Po... |
| 18 | no | 14006764 | - | 0.269 | brand=Saree mall, color=Green, category=Banarasi, occasion=Traditional, price=7299.0 | Product: Saree mall Floral Silk Blend Saree with Woven Design border Brand: Saree mall Color: Green Category: Banarasi Pattern: Floral woven design Occasion: Traditional Wash ca... |
| 19 | no | 18056594 | - | 0.269 | brand=Martini, color=Black, category=Flared, occasion=Party, price=1800.0 | Product: Martini Women Black Pleated Flared Mini Skirt Brand: Martini Color: Black Category: Flared Pattern: Solid Length: Mini Hemline: Curved Top fabric: Polyester Occasion: P... |
| 20 | no | 17570450 | - | 0.268 | brand=SHOWOFF, color=Black, occasion=Casual, price=3720.0 | Product: SHOWOFF Women Black Slim Fit Stretchable Cropped Jeans Brand: SHOWOFF Color: Black Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 5 Wash care: Dry clean |
| 21 | no | 18425088 | - | 0.267 | brand=SHOWOFF, color=Navy Blue, category=Pullover, occasion=Casual, price=1800.0 | Product: SHOWOFF Women Navy Blue Striped Hooded Sweatshirt Brand: SHOWOFF Color: Navy Blue Category: Pullover Pattern: Striped Neck: Round neck Sleeves: Long sleeves Length: Reg... |
| 22 | no | 17872080 | - | 0.265 | brand=Taavi, color=Blue, category=Peplum, occasion=Casual, price=2299.0 | Product: Taavi Women Indigo & White Indigo Print Pure Cotton Casual Peplum Top Brand: Taavi Color: Blue Category: Peplum Pattern: Ethnic motifs printed Neck: Round neck Sleeves:... |
| 23 | no | 18263720 | - | 0.264 | brand=SHOWOFF, color=Grey, category=Top, occasion=Casual, price=4720.0 | Product: SHOWOFF Women Grey & Maroon Floral Print Co-Ords Brand: SHOWOFF Color: Grey Category: Top Top type: Top Bottom type: Palazzos Pattern: Printed Neck: V-neck Sleeves: Thr... |
| 24 | no | 18067038 | - | 0.260 | brand=BUY NEW TREND, color=Blue, occasion=Western, price=1399.0 | Product: BUY NEW TREND Blue Flared Knitted Palazzos Brand: BUY NEW TREND Color: Blue Pattern: Solid Length: Regular Top fabric: Modal Occasion: Western Wash care: Machine wash |
| 25 | no | 16309970 | - | 0.257 | brand=aarke Ritu Kumar, color=Olive, category=Regular trousers, occasion=Casual, price=1800.0 | Product: aarke Ritu Kumar Women Olive Green Solid Pleated Tulip Hem Trousers Brand: aarke Ritu Kumar Color: Olive Category: Regular trousers Pattern: Solid Length: Regular Top f... |
| 26 | no | 17570446 | - | 0.251 | brand=SHOWOFF, color=Blue, occasion=Casual, price=3720.0 | Product: SHOWOFF Women Blue Boyfriend Fit High-Rise Low Distress Light Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Po... |
| 27 | no | 18142614 | - | 0.241 | brand=SHOWOFF, color=Lavender, occasion=Casual, price=4655.0 | Product: SHOWOFF Women Lavender Jogger High-Rise Cuffed Hem Stretchable Jeans Brand: SHOWOFF Color: Lavender Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 6 and... |
| 28 | no | 17093664 | - | 0.240 | brand=Roadster, color=Black, category=Denim shorts, occasion=Casual, price=1699.0 | Product: The Roadster Lifestyle Co Women Black Denim Shorts Brand: Roadster Color: Black Category: Denim shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Ca... |
| 29 | no | 17570328 | - | 0.239 | brand=SHOWOFF, color=Blue, occasion=Casual, price=4845.0 | Product: SHOWOFF Women Blue Wide Leg High-Rise Low Distress Heavy Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Pockets... |
| 30 | no | 17093660 | - | 0.238 | brand=Roadster, color=Charcoal, category=Denim shorts, occasion=Casual, price=1699.0 | Product: The Roadster Lifestyle Co Women Charcoal High-Rise Denim Shorts Brand: Roadster Color: Charcoal Category: Denim shorts Pattern: Solid Length: Above knee Top fabric: Cot... |

### Question 26/50

**Query:** I need product with a Other woven design pattern in Red.

**Retrieval metadata:** color == Red

**Relevant docs:** `['16379852', '16379914', '15768366']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 16379914 | - | 1.000 | brand=Safaa, color=Red, occasion=Daily, price=999.0 | Product: Safaa Women Red Woven Design Acrylic Blend Shawl Brand: Safaa Color: Red Pattern: Other woven design Top fabric: Acrylic Occasion: Daily |
| 2 | yes | 15768366 | - | 0.993 | brand=VERO AMORE, color=Red, occasion=Daily, price=2250.0 | Product: VERO AMORE Women Red & Beige Woven-Design Jacquard Shawl Brand: VERO AMORE Color: Red Pattern: Other woven design Top fabric: Wool Occasion: Daily |
| 3 | yes | 16379852 | - | 0.936 | brand=Safaa, color=Red, occasion=Daily, price=999.0 | Product: Safaa Women Red & Black Woven Design Shawl Brand: Safaa Color: Red Pattern: Other woven design Top fabric: Acrylic Occasion: Daily |
| 4 | no | 11379820 | - | 0.768 | brand=SHINGORA, color=Red, occasion=Daily, price=3295.0 | Product: SHINGORA Women Red & Blue Woven Design Pure Woolen Jacquard Weave Shawl Brand: SHINGORA Color: Red Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily |
| 5 | no | 13104106 | - | 0.666 | brand=Pashmoda, color=Red, occasion=Daily, price=1495.0 | Product: Pashmoda Women Red Woven Design Shawl Brand: Pashmoda Color: Red Pattern: Paisley woven design Top fabric: Wool Occasion: Daily |
| 6 | no | 13616810 | - | 0.650 | brand=Dupatta Bazaar, color=Red, occasion=Daily, price=899.0 | Product: Dupatta Bazaar Red & Orange Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Striped woven design Top fabric: Cotton blend Occasion: Daily Wash care: Hand... |
| 7 | no | 15121622 | - | 0.642 | brand=Cayman, color=Red, occasion=Daily, price=3795.0 | Product: Cayman Women Red & Beige Woollen Woven Design Shawl Brand: Cayman Color: Red Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily |
| 8 | no | 15874790 | - | 0.634 | brand=Pashmoda, color=Red, occasion=Daily, price=1495.0 | Product: Pashmoda Women Red Woven Design Jamawar Shawl Brand: Pashmoda Color: Red Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily |
| 9 | no | 19366710 | - | 0.633 | brand=RIVAMA, color=Red, occasion=Daily, price=1999.0 | Product: RIVAMA Red & Green Ethnic Motifs Woven Design Cotton Silk Foil Print Dupatta Brand: RIVAMA Color: Red Pattern: Ethnic motifs woven design Top fabric: Cotton silk Occasi... |
| 10 | no | 17662882 | - | 0.614 | brand=Dupatta Bazaar, color=Red, occasion=Party, price=999.0 | Product: Dupatta Bazaar Red Woven Design Dupatta with Sequinned Detail Brand: Dupatta Bazaar Color: Red Pattern: Geometric woven design Top fabric: Net Occasion: Party Wash care... |
| 11 | no | 4444074 | - | 0.590 | brand=Dupatta Bazaar, color=Red, occasion=Party, price=1699.0 | Product: Dupatta Bazaar Red & Orange Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Paisley woven design Top fabric: Silk blend Occasion: Party Wash care: Dry clean |
| 12 | no | 16874574 | - | 0.569 | brand=Mitera, color=Red, category=Paithani, occasion=Traditional, price=5999.0 | Product: Mitera Red Woven Design Zari Silk Blend Paithani Saree Brand: Mitera Color: Red Category: Paithani Pattern: Woven design Occasion: Traditional Wash care: Dry clean |
| 13 | no | 18205188 | - | 0.532 | brand=Inddus, color=Red, category=Patola, occasion=Traditional, price=4399.0 | Product: Inddus Red & Gold-Toned Woven Design Silk Blend Patola Saree Brand: Inddus Color: Red Category: Patola Pattern: Ethnic motifs woven design Occasion: Traditional Wash ca... |
| 14 | no | 11149776 | - | 0.516 | brand=Style Quotient, color=Red, occasion=Daily, price=1599.0 | Product: Style Quotient Women Red & Black Checked Shawl Brand: Style Quotient Color: Red Pattern: Checked woven design Top fabric: Acrylic Occasion: Daily |
| 15 | no | 18806012 | - | 0.500 | brand=awesome, color=Red, category=Banarasi, occasion=Traditional, price=5999.0 | Product: awesome Red & Gold-Toned Woven Design Zari Pure Silk Banarasi Saree Brand: awesome Color: Red Category: Banarasi Pattern: Woven design Occasion: Traditional Wash care: ... |
| 16 | no | 13497800 | - | 0.472 | brand=InWeave, color=Red, category=Regular, occasion=Ethnic, price=1999.0 | Product: InWeave Women Red Striped A-Line Top Brand: InWeave Color: Red Category: Regular Pattern: Vertical stripes self design Neck: Round neck Sleeves: Sleeveless no Length: R... |
| 17 | no | 8278529 | - | 0.470 | brand=Faserz, color=Red, occasion=Party, price=1665.0 | Product: Faserz Red Woven Design Banarasi Dupatta Brand: Faserz Color: Red Pattern: Ethnic motifs woven design Top fabric: Silk blend Occasion: Party Wash care: Dry clean |
| 18 | no | 16197692 | - | 0.438 | brand=Pashmoda, color=Red, occasion=Daily, price=3695.0 | Product: Pashmoda Womens Red Kaani Woven Design Shawl Brand: Pashmoda Color: Red Pattern: Floral woven design Top fabric: Wool Occasion: Daily |
| 19 | no | 17764814 | - | 0.432 | brand=Silk Land, color=Red, occasion=Party, price=3520.0 | Product: Silk Land Red & Gold-Toned Ethnic Motifs Woven Design Dupatta with Zari Brand: Silk Land Color: Red Pattern: Ethnic motifs woven design Top fabric: Silk blend Occasion:... |
| 20 | no | 17929928 | - | 0.429 | brand=Silk Land, color=Red, occasion=Party, price=1996.0 | Product: Silk Land Red & Gold-Toned Ethnic Motifs Woven Design Pure Banarasi Silk Dupatta Brand: Silk Land Color: Red Pattern: Ethnic motifs woven design Top fabric: Pure silk O... |
| 21 | no | 10358133 | - | 0.426 | brand=Dupatta Bazaar, color=Red, occasion=Daily, price=699.0 | Product: Dupatta Bazaar Red & Gold-Coloured Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Polka dots woven design Top fabric: Poly chiffon Occasion: Daily Wash ... |
| 22 | no | 13552260 | - | 0.426 | brand=Dupatta Bazaar, color=Red, occasion=Party, price=1999.0 | Product: Dupatta Bazaar Red & Yellow Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Bandhani woven design Top fabric: Pure silk Occasion: Party Wash care: Dry clean |
| 23 | no | 19029736 | - | 0.422 | brand=Mitera, color=Red, category=Patola, occasion=Traditional, price=6599.0 | Product: Mitera Red & Gold-Toned Woven Design Zari Silk Blend Patola Saree Brand: Mitera Color: Red Category: Patola Pattern: Woven design Occasion: Traditional Wash care: Dry c... |
| 24 | no | 17693086 | - | 0.407 | brand=Silk Land, color=Red, category=Banarasi, occasion=Traditional, price=1567.0 | Product: Silk Land Red & Gold-Toned Woven Design Zari Pure Silk Banarasi Saree Brand: Silk Land Color: Red Category: Banarasi Pattern: Woven design Occasion: Traditional Wash ca... |
| 25 | no | 6581979 | - | 0.404 | brand=Dupatta Bazaar, color=Red, occasion=Party, price=1499.0 | Product: Dupatta Bazaar Red & Gold-Toned Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Floral woven design Top fabric: Pure silk Occasion: Party Wash care: Dry ... |
| 26 | no | 7079364 | - | 0.364 | brand=Blissta, color=Red, occasion=Party, price=2497.0 | Product: Blissta Red & Gold-Toned Woven Design Dupatta Brand: Blissta Color: Red Pattern: Ethnic motifs woven design Top fabric: Pure silk Occasion: Party Wash care: Dry clean |
| 27 | no | 17764826 | - | 0.360 | brand=Silk Land, color=Red, occasion=Party, price=3520.0 | Product: Silk Land Women Red Jacquared Banarasi Dupatta Brand: Silk Land Color: Red Pattern: Ethnic motifs woven design Top fabric: Silk blend Occasion: Party Wash care: Dry clean |
| 28 | no | 17735542 | - | 0.354 | brand=Iris, color=Red, category=Saree, occasion=Party, price=3499.0 | Product: Iris Red Floral Net Saree Brand: Iris Color: Red Category: Saree Pattern: Floral woven design Occasion: Party Wash care: Hand wash |
| 29 | no | 6849866 | - | 0.351 | brand=Sugathari, color=Red, occasion=Party, price=2399.0 | Product: Sugathari Red & Gold-Toned Woven Design Banarasi Dupatta Brand: Sugathari Color: Red Pattern: Ethnic motifs woven design Top fabric: Silk blend Occasion: Party Wash car... |
| 30 | no | 17764856 | - | 0.320 | brand=Silk Land, color=Red, occasion=Party, price=3520.0 | Product: Silk Land Red & Gold-Toned Ethnic Motifs Jacquared Banarasi Dupatta Brand: Silk Land Color: Red Pattern: Ethnic motifs woven design Top fabric: Silk blend Occasion: Par... |

### Question 27/50

**Query:** Do you have anything from SERONA FABRICS in White for everyday wear?

**Retrieval metadata:** brand == SERONA FABRICS, color == White, occasion == Daily

**Relevant docs:** `['15917640']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 15917640 | - | 1.000 | brand=SERONA FABRICS, color=White, occasion=Daily, price=3999.0 | Product: SERONA FABRICS White & Pink Floral Embroidered Anarkali Kurti Brand: SERONA FABRICS Color: White Pattern: Floral embroidered Shape: Anarkali Neck: Round neck Sleeves: T... |

### Question 28/50

**Query:** Do you have any Green Kurta set for a festive occasion?

**Retrieval metadata:** color == Green, occasion == Festive

**Relevant docs:** `['17140156', '16505434', '14121912', '16825614', '16707970', '15677426', '17232410', '14920000']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.267 | 1.000 | 0.333 | 0.647 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 15258422 | - | 0.836 | brand=Indo Era, color=Green, category=Kurta set, occasion=Festive, price=4599.0 | Product: Indo Era Floral Cotton Blend Calf Length Kurta Set Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta Pattern:... |
| 2 | no | 17447636 | - | 0.805 | brand=Khushal K, color=Green, category=Kurta set, occasion=Festive, price=5699.0 | Product: Khushal K Women Green Ethnic Motifs Printed Gotta Patti Kurta with Trousers & Dupatta Brand: Khushal K Color: Green Category: Kurta set Top type: Kurta Bottom type: Tro... |
| 3 | yes | 17232410 | - | 0.796 | brand=InWeave, color=Green, category=Kurta set, occasion=Festive, price=4299.0 | Product: InWeave Green Pure Cotton Print Parade Kurta Set Brand: InWeave Color: Green Category: Kurta set Top type: Kurta Bottom type: Sharara Pattern: Ethnic motifs printed Sha... |
| 4 | yes | 16707970 | - | 0.795 | brand=mokshi, color=Green, category=Kurta set, occasion=Festive, price=3899.0 | Product: mokshi Ethnic Motifs Viscose Rayon Kurta Set Brand: mokshi Color: Green Category: Kurta set Top type: Kurta Bottom type: Skirt Pattern: Ethnic motifs printed Shape: Ana... |
| 5 | no | 12989804 | - | 0.791 | brand=mokshi, color=Green, category=Kurta set, occasion=Festive, price=2499.0 | Product: mokshi Women Green & Maroon Foil Print Front Slit Kurta with Palazzos Brand: mokshi Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Ethn... |
| 6 | no | 15654150 | - | 0.787 | brand=Indo Era, color=Green, category=Kurta set, occasion=Festive, price=5399.0 | Product: Indo Era Women Green Ethnic Motifs Yoke Design Regular Kurta with Trousers & With Dupatta Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: ... |
| 7 | no | 15508896 | - | 0.764 | brand=Indo Era, color=Green, category=Kurta set, occasion=Festive, price=6599.0 | Product: Indo Era Women Green Ethnic Motifs Yoke Design Kurta with Palazzos & With Dupatta Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos... |
| 8 | no | 15054430 | - | 0.738 | brand=Biba, color=Green, category=Kurta set, occasion=Festive, price=4995.0 | Product: Biba Women Green Ethnic Motifs Printed Regular Pure Cotton Kurta with Palazzos & With Dupatta Brand: Biba Color: Green Category: Kurta set Top type: Kurta Bottom type: ... |
| 9 | yes | 15677426 | - | 0.715 | brand=SWAGG INDIA, color=Green, category=Kurta set, occasion=Festive, price=3999.0 | Product: SWAGG INDIA Women Green Floral Embroidered Regular Kurta with Trousers & With Dupatta Brand: SWAGG INDIA Color: Green Category: Kurta set Top type: Kurta Bottom type: T... |
| 10 | yes | 17140156 | - | 0.707 | brand=Myshka, color=Green, category=Kurta set, occasion=Festive, price=5499.0 | Product: Myshka Women Green Kurta with Palazzos & With Dupatta Brand: Myshka Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With dupatta Pattern... |
| 11 | no | 15258010 | - | 0.692 | brand=Libas, color=Green, category=Kurta set, occasion=Festive, price=6499.0 | Product: Libas Women Green & White Floral Embroidered Kurta with Palazzos & Dupatta Brand: Libas Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: ... |
| 12 | yes | 16825614 | - | 0.662 | brand=Stylum, color=Green, category=Kurta set, occasion=Festive, price=3599.0 | Product: Stylum Women Green Embroidered Pure Cotton Kurta with Sharara & With Dupatta Brand: Stylum Color: Green Category: Kurta set Top type: Kurta Bottom type: Sharara Dupatta... |
| 13 | yes | 14920000 | - | 0.645 | brand=Indo Era, color=Green, category=Kurta set, occasion=Festive, price=4799.0 | Product: Indo Era Women Green Floral Embroidered Gotta Patti Liva Kurta with Trousers & Dupatta Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: Tro... |
| 14 | yes | 16505434 | - | 0.639 | brand=KALINI, color=Green, category=Kurta set, occasion=Festive, price=2999.0 | Product: KALINI Women Green Floral Printed Pure Cotton Straight Kurta with Trousers Brand: KALINI Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern:... |
| 15 | yes | 14121912 | - | 0.636 | brand=Anouk, color=Green, category=Kurta set, occasion=Festive, price=3199.0 | Product: Anouk Women Dark Green Embroidered Pleated Mirror Work Kurta with Sharara Brand: Anouk Color: Green Category: Kurta set Top type: Kurta Bottom type: Sharara Pattern: Et... |
| 16 | no | 13392426 | - | 0.631 | brand=Khushal K, color=Lime Green, category=Kurta set, occasion=Festive, price=4499.0 | Product: Khushal K Women Lime Green Printed Kurta with Churidar & Dupatta Brand: Khushal K Color: Lime Green Category: Kurta set Top type: Kurta Bottom type: Churidar Dupatta: W... |
| 17 | no | 18002690 | - | 0.619 | brand=SINGNI, color=Green, category=Kurta set, occasion=Festive, price=2999.0 | Product: SINGNI Women Green Embroidered Printed Kurta with Trousers & dupatta Brand: SINGNI Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With ... |
| 18 | no | 18551726 | - | 0.594 | brand=POONAM DESIGNER, color=Lime Green, category=Kurta set, occasion=Festive, price=2198.0 | Product: POONAM DESIGNER Women Lime Green Gotta Patti Pure Cotton Kurta with Trousers & With Dupatta Brand: POONAM DESIGNER Color: Lime Green Category: Kurta set Top type: Kurta... |
| 19 | no | 18765612 | - | 0.558 | brand=mirari, color=Green, category=Kurta set, occasion=Festive, price=1499.0 | Product: mirari Women Green Floral Printed Pure Cotton Kurta with Palazzos Brand: mirari Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Floral p... |
| 20 | no | 16773346 | - | 0.535 | brand=KALINI, color=Sea Green, category=Kurta set, occasion=Festive, price=3499.0 | Product: KALINI Women Sea Green Printed Gotta Patti Kurta with Palazzos & Dupatta Brand: KALINI Color: Sea Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatt... |
| 21 | no | 15224706 | - | 0.468 | brand=Stylee LIFESTYLE, color=Green, category=Dress, occasion=Festive, price=13249.0 | Product: Stylee LIFESTYLE Green Embellished Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Green Category: Dress Pattern: Ethnic motifs Bottom fabric: Satin Dupatta... |
| 22 | no | 17889600 | - | 0.449 | brand=EXTRA LOVE BY LIBAS, color=Sea Green, category=Kurta set, occasion=Festive, price=4999.0 | Product: EXTRA LOVE BY LIBAS Women Plus Size Sea Green Kurta with Trousers & With Dupatta Brand: EXTRA LOVE BY LIBAS Color: Sea Green Category: Kurta set Top type: Kurta Bottom ... |
| 23 | no | 15508612 | - | 0.410 | brand=Saree mall, color=Green, category=Dress, occasion=Festive, price=3299.0 | Product: Saree mall Green Embroidered Unstitched Dress Material Brand: Saree mall Color: Green Category: Dress Pattern: Abstract Bottom fabric: Cotton blend Dupatta fabric: Poly... |
| 24 | no | 15098762 | - | 0.392 | brand=Rajnandini, color=Green, category=Dress, occasion=Festive, price=1663.0 | Product: Rajnandini Green & Black Printed Unstitched Dress Material Brand: Rajnandini Color: Green Category: Dress Pattern: Floral Bottom fabric: Cotton blend Dupatta fabric: Co... |
| 25 | no | 18748558 | - | 0.390 | brand=JATRIQQ, color=Green, category=Dress, occasion=Festive, price=8999.0 | Product: JATRIQQ Green Art Silk Semi-Stitched Dress Material Brand: JATRIQQ Color: Green Category: Dress Pattern: Geometric Bottom fabric: Art silk Dupatta fabric: Jute silk Occ... |
| 26 | no | 17634760 | - | 0.390 | brand=JATRIQQ, color=Green, category=Dress, occasion=Festive, price=5999.0 | Product: JATRIQQ Green Embroidered Silk Georgette Semi-Stitched Dress Material Brand: JATRIQQ Color: Green Category: Dress Pattern: Striped Bottom fabric: Silk georgette Dupatta... |
| 27 | no | 17747744 | - | 0.384 | brand=JATRIQQ, color=Green, category=Dress, occasion=Festive, price=5999.0 | Product: JATRIQQ Women Green Embroidered Silk Georgette Semi-Stitched Dress Material Brand: JATRIQQ Color: Green Category: Dress Pattern: Striped Bottom fabric: Silk georgette D... |
| 28 | no | 16017444 | - | 0.382 | brand=Readiprint Fashions, color=Green, category=Dress, occasion=Festive, price=4650.0 | Product: Readiprint Fashions Green Embroidered Unstitched Dress Material Brand: Readiprint Fashions Color: Green Category: Dress Pattern: Paisley Bottom fabric: Shantoon Dupatta... |
| 29 | no | 18533460 | - | 0.359 | brand=KALINI, color=Green, category=Dress, occasion=Festive, price=2999.0 | Product: KALINI Green Embroidered Unstitched Dress Material Brand: KALINI Color: Green Category: Dress Pattern: Other Bottom fabric: Silk blend Dupatta fabric: Poly georgette Oc... |
| 30 | no | 16017486 | - | 0.353 | brand=Readiprint Fashions, color=Green, category=Dress, occasion=Festive, price=5300.0 | Product: Readiprint Fashions Green Embroidered Unstitched Dress Material Brand: Readiprint Fashions Color: Green Category: Dress Pattern: Floral Bottom fabric: Shantoon Dupatta ... |

### Question 29/50

**Query:** I'm looking for something Black from URBANIC for everyday wear.

**Retrieval metadata:** brand == URBANIC, color == Black, occasion == Daily

**Relevant docs:** `['15849954', '15634138', '18929182', '15086606', '15633414', '18866648', '18605954', '18907592']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |

### Question 30/50

**Query:** Show me Black products for everyday wear.

**Retrieval metadata:** color == Black, occasion == Daily

**Relevant docs:** `['9440729', '18207452', '18992236', '16612058', '9073715', '16728358', '7437296', '16728350']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 16379842 | - | 0.651 | brand=Safaa, color=Black, occasion=Daily, price=999.0 | Product: Safaa Women Black & Beige Woven Design Shawl Brand: Safaa Color: Black Pattern: Other woven design Top fabric: Acrylic Occasion: Daily |
| 2 | no | 16379878 | - | 0.577 | brand=Safaa, color=Black, occasion=Daily, price=1155.0 | Product: Safaa Women Black & Blue Woven Design Shawl Brand: Safaa Color: Black Pattern: Other woven design Top fabric: Acrylic Occasion: Daily |
| 3 | no | 2380261 | - | 0.564 | brand=Janasya, color=Black, category=Saree, occasion=Daily, price=899.0 | Product: Janasya Black Solid Saree Blouse Brand: Janasya Color: Black Category: Saree Pattern: Solid Neck: Round neck Sleeves: Long sleeves Top fabric: Cotton Occasion: Daily |
| 4 | no | 19296144 | - | 0.561 | brand=La Vastraa, color=Black, occasion=Daily, price=8290.0 | Product: La Vastraa Women Black & Brown Woven Design Shawl Brand: La Vastraa Color: Black Pattern: Floral woven design Top fabric: Wool Occasion: Daily |
| 5 | no | 10451770 | - | 0.544 | brand=WEAVERS VILLA, color=Black, occasion=Daily, price=2450.0 | Product: WEAVERS VILLA Women Black & Beige Woven Design Shawl Brand: WEAVERS VILLA Color: Black Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily |
| 6 | no | 16379928 | - | 0.544 | brand=Safaa, color=Black, occasion=Daily, price=999.0 | Product: Safaa Women Black & Beige Woven Design Acrylic Blend Shawl Brand: Safaa Color: Black Pattern: Other woven design Top fabric: Acrylic Occasion: Daily |
| 7 | no | 16736530 | - | 0.514 | brand=SHINGORA, color=Black, occasion=Daily, price=3495.0 | Product: SHINGORA Women Black & Brown Woven-Design Shawl Brand: SHINGORA Color: Black Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily |
| 8 | no | 2380278 | - | 0.508 | brand=Janasya, color=Black, category=Saree, occasion=Daily, price=969.0 | Product: Janasya Black Cotton Lycra Saree Blouse Brand: Janasya Color: Black Category: Saree Pattern: Solid Neck: Round neck Sleeves: Short sleeves Top fabric: Other Occasion: D... |
| 9 | no | 13552234 | - | 0.503 | brand=Dupatta Bazaar, color=Black, occasion=Daily, price=599.0 | Product: Dupatta Bazaar Black Solid Dupatta Brand: Dupatta Bazaar Color: Black Pattern: Solid Top fabric: Poly chiffon Occasion: Daily Wash care: Machine wash |
| 10 | no | 17351596 | - | 0.500 | brand=anayna, color=Black, occasion=Daily, price=1599.0 | Product: anayna Women Black & White Ethnic Motifs Printed Kantha Work Kurta Brand: anayna Color: Black Pattern: Ethnic motifs printed Shape: Straight Neck: Boat neck Sleeves: Sl... |
| 11 | no | 11387498 | - | 0.497 | brand=Inddus, color=Black, category=Saree, occasion=Daily, price=1199.0 | Product: Inddus Black Cotton Stretchable Solid Saree Blouse Brand: Inddus Color: Black Category: Saree Pattern: Solid Neck: Round neck Sleeves: Short sleeves Top fabric: Cotton ... |
| 12 | no | 18207362 | - | 0.485 | brand=Dupatta Bazaar, color=Black, occasion=Daily, price=899.0 | Product: Dupatta Bazaar Black Linen Dupatta Brand: Dupatta Bazaar Color: Black Pattern: Solid Top fabric: Linen Occasion: Daily Wash care: Hand wash |
| 13 | no | 2082103 | - | 0.467 | brand=Saree mall, color=Black, category=Dress, occasion=Daily, price=3199.0 | Product: Saree mall Black Unstitched Dress Material Brand: Saree mall Color: Black Category: Dress Pattern: Ethnic motifs Bottom fabric: Cotton blend Dupatta fabric: Poly chiffo... |
| 14 | no | 15952994 | - | 0.435 | brand=Prakrti, color=Black, occasion=Daily, price=1899.0 | Product: Prakrti Black Printed Kurti Brand: Prakrti Color: Black Pattern: Abstract printed Shape: Straight Neck: Round neck Sleeves: Three-quarter regular sleeves Hemline: Strai... |
| 15 | no | 15768382 | - | 0.420 | brand=VERO AMORE, color=Black, occasion=Daily, price=2150.0 | Product: VERO AMORE Women Black & Orange Woven-Design Jacquard Kullu Shawl Brand: VERO AMORE Color: Black Pattern: Geometric woven design Top fabric: Wool Occasion: Daily |
| 16 | no | 9369411 | - | 0.418 | brand=Myshka, color=Black, occasion=Daily, price=1699.0 | Product: Myshka Women Black & White Striped Straight Kurta Brand: Myshka Color: Black Pattern: Striped Shape: Straight Neck: Mandarin collar Sleeves: Three-quarter regular sleev... |
| 17 | no | 16608222 | - | 0.412 | brand=VERO AMORE, color=Black, occasion=Daily, price=2250.0 | Product: VERO AMORE Women Black & Red Woven Design Shawl Brand: VERO AMORE Color: Black Pattern: Other woven design Top fabric: Wool Occasion: Daily |
| 18 | no | 18272052 | - | 0.407 | brand=HERE&NOW, color=Black, category=Saree, occasion=Daily, price=4599.0 | Product: HERE&NOW Striped Saree with Embroidered Border Brand: HERE&NOW Color: Black Category: Saree Pattern: Striped Occasion: Daily Wash care: Machine wash |
| 19 | no | 2528692 | - | 0.400 | brand=Moda Rapido, color=Black, occasion=Daily, price=1799.0 | Product: Moda Rapido Women Black Solid Straight Kurta Brand: Moda Rapido Color: Black Pattern: Solid Shape: Straight Neck: Round neck Sleeves: Short regular sleeves Length: Calf... |
| 20 | no | 15953036 | - | 0.396 | brand=Prakrti, color=Black, occasion=Daily, price=1599.0 | Product: Prakrti Black Solid Kurti Brand: Prakrti Color: Black Pattern: Solid Shape: Straight Neck: Round neck Sleeves: Three-quarter regular sleeves Hemline: Straight Top fabri... |
| 21 | no | 12159600 | - | 0.387 | brand=WEAVERS VILLA, color=Black, occasion=Daily, price=1999.0 | Product: WEAVERS VILLA Women Black & Orange Embroidered Shawl Brand: WEAVERS VILLA Color: Black Pattern: Ethnic motifs embroidered Top fabric: Wool Occasion: Daily |
| 22 | no | 18636196 | - | 0.386 | brand=Tweedle, color=Black, occasion=Daily, price=1999.0 | Product: Tweedle Women Black & Red Striped Woven Wool Shawl Brand: Tweedle Color: Black Pattern: Striped woven design Top fabric: Wool Occasion: Daily |
| 23 | no | 15768348 | - | 0.374 | brand=VERO AMORE, color=Black, occasion=Daily, price=2250.0 | Product: VERO AMORE Women Black & Red Woven-Design Jacquard Shawl Brand: VERO AMORE Color: Black Pattern: Paisley woven design Top fabric: Wool Occasion: Daily |
| 24 | no | 12967812 | - | 0.367 | brand=Dupatta Bazaar, color=Black, occasion=Daily, price=1099.0 | Product: Dupatta Bazaar Black Printed Kalamkari Dupatta Brand: Dupatta Bazaar Color: Black Pattern: Ethnic motifs printed Top fabric: Silk blend Occasion: Daily Wash care: Hand ... |
| 25 | no | 15768400 | - | 0.349 | brand=VERO AMORE, color=Black, occasion=Daily, price=2150.0 | Product: VERO AMORE Women Black & Red Woven-Design Jacquard Kullu Shawl Brand: VERO AMORE Color: Black Pattern: Geometric woven design Top fabric: Wool Occasion: Daily |
| 26 | no | 16197678 | - | 0.331 | brand=Pashmoda, color=Black, occasion=Daily, price=3065.0 | Product: Pashmoda Women Black Kaani Woven Shawl Brand: Pashmoda Color: Black Pattern: Floral woven design Top fabric: Wool Occasion: Daily |
| 27 | no | 13833448 | - | 0.329 | brand=Sangria, color=Black, category=Saree, occasion=Daily, price=3299.0 | Product: Sangria Black & White Dyed Celebrity Saree Brand: Sangria Color: Black Category: Saree Pattern: Tie and dye dyed Occasion: Daily Wash care: Machine wash |
| 28 | no | 15768324 | - | 0.323 | brand=VERO AMORE, color=Black, occasion=Daily, price=2150.0 | Product: VERO AMORE Women Black & Red Woven Kullu Design Jacquard Shawl Brand: VERO AMORE Color: Black Pattern: Other woven design Top fabric: Wool Occasion: Daily |
| 29 | no | 17077530 | - | 0.322 | brand=SATYAM WEAVES, color=Black, category=Dress, occasion=Daily, price=3499.0 | Product: SATYAM WEAVES Women Black & Red Unstitched Printed Dress Material Brand: SATYAM WEAVES Color: Black Category: Dress Pattern: Ethnic motifs Bottom fabric: Cotton blend D... |
| 30 | no | 17093788 | - | 0.318 | brand=Anouk, color=Black, occasion=Daily, price=1699.0 | Product: Anouk Women Black Solid Pleated Round Neck Pure Cotton Kurta Brand: Anouk Color: Black Pattern: Solid Shape: Straight Neck: Round neck Sleeves: Short regular sleeves Le... |

### Question 31/50

**Query:** I'm looking for something Blue from Swasti for everyday wear.

**Retrieval metadata:** brand == Swasti, color == Blue, occasion == Daily

**Relevant docs:** `['18819296']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 18819296 | - | 1.000 | brand=Swasti, color=Blue, occasion=Daily, price=2070.0 | Product: Swasti Women Blue Ethnic Motifs Printed Mirror Work Floral Kurta Brand: Swasti Color: Blue Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck Sleeves: Long... |

### Question 32/50

**Query:** I need Shirt style with a Abstract printed pattern in Pink.

**Retrieval metadata:** color == Pink

**Relevant docs:** `['13244594']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.033 | 1.000 | 1.000 | 1.000 | 0.750 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 13244594 | - | 1.000 | brand=Mayra, color=Pink, category=Shirt style, occasion=Casual, price=1195.0 | Product: Mayra Women Pink Printed Shirt Style Top Brand: Mayra Color: Pink Category: Shirt style Pattern: Abstract printed Neck: Mandarin collar Sleeves: Three-quarter roll-up s... |
| 2 | no | 15841446 | - | 0.810 | brand=URBANIC, color=Pink, category=Shirt style, occasion=Casual, price=1490.0 | Product: URBANIC Pink & Beige Floral Print Shirt Style Top Brand: URBANIC Color: Pink Category: Shirt style Pattern: Floral printed Neck: V-neck Sleeves: Long regular sleeves Le... |
| 3 | no | 19195222 | - | 0.744 | brand=PRASTHAN, color=Pink, category=Shirt style, occasion=Casual, price=2999.0 | Product: PRASTHAN Women Pink Floral Print Crepe Shirt Style Top Brand: PRASTHAN Color: Pink Category: Shirt style Pattern: Floral printed Neck: Shirt collar Sleeves: Long bishop... |
| 4 | no | 19201936 | - | 0.671 | brand=H&M, color=Pink, category=Shirt style, occasion=Casual, price=1499.0 | Product: H&M Women Pink Pure Cotton Frill-Collared Blouse Brand: H&M Color: Pink Category: Shirt style Pattern: Solid Neck: Mandarin collar Sleeves: Short regular sleeves Length... |
| 5 | no | 18605378 | - | 0.595 | brand=Vishal Prints, color=Pink, category=Saree, occasion=Daily, price=2739.0 | Product: Vishal Prints Pink & Grey Abstract Print Saree Brand: Vishal Prints Color: Pink Category: Saree Pattern: Abstract printed Occasion: Daily Wash care: Machine wash |
| 6 | no | 19325284 | - | 0.460 | brand=POONAM DESIGNER, color=Pink, occasion=Daily, price=2499.0 | Product: POONAM DESIGNER Women Pink Ethnic Motifs Printed Kurta Brand: POONAM DESIGNER Color: Pink Pattern: Ethnic motifs printed Shape: A-line Neck: Shirt collar Sleeves: Short... |
| 7 | no | 17820020 | - | 0.452 | brand=Mast & Harbour, color=Pink, category=Shirt style, occasion=Casual, price=1499.0 | Product: Mast & Harbour Pink Floral Print Mandarin Collar Shirt Style Top Brand: Mast & Harbour Color: Pink Category: Shirt style Pattern: Floral printed Neck: Mandarin collar S... |
| 8 | no | 19188354 | - | 0.432 | brand=Colour Me by Melange, color=Pink, category=Shirt style, occasion=Casual, price=899.0 | Product: Colour Me by Melange Women Pink Mandarin Collar Pleated Top Brand: Colour Me by Melange Color: Pink Category: Shirt style Pattern: Embellished Neck: Mandarin collar Sle... |
| 9 | no | 11762378 | - | 0.432 | brand=AKKRITI BY PANTALOONS, color=Pink, category=Regular, occasion=Ethnic, price=799.0 | Product: AKKRITI BY PANTALOONS Women Pink Printed Top Brand: AKKRITI BY PANTALOONS Color: Pink Category: Regular Pattern: Abstract printed Neck: Mandarin collar Sleeves: Three-q... |
| 10 | no | 17348862 | - | 0.412 | brand=JC Collection, color=Pink, category=Shirt, occasion=Casual, price=5999.0 | Product: JC Collection Women Pink & Green Printed Shirt with Trousers Brand: JC Collection Color: Pink Category: Shirt Top type: Shirt Bottom type: Trousers Pattern: Printed Nec... |
| 11 | no | 15632410 | - | 0.395 | brand=URBANIC, color=Pink, category=T-shirt, occasion=Casual, price=1290.0 | Product: URBANIC Women Pink Solid T-shirt with Shorts Brand: URBANIC Color: Pink Category: T-shirt Top type: T-shirt Bottom type: Shorts Pattern: Solid Neck: Round neck Sleeves:... |
| 12 | no | 18076132 | - | 0.383 | brand=Saree mall, color=Pink, category=Saree, occasion=Daily, price=2399.0 | Product: Saree mall Pink & Black Printed Saree Brand: Saree mall Color: Pink Category: Saree Pattern: Abstract printed Occasion: Daily Wash care: Dry clean |
| 13 | no | 17000316 | - | 0.343 | brand=Marks & Spencer, color=Pink, category=Shirt style, occasion=Casual, price=2999.0 | Product: Marks & Spencer Pink Shirt Style Top Brand: Marks & Spencer Color: Pink Category: Shirt style Pattern: Solid Neck: Shirt collar Sleeves: Long cuffed sleeves Length: Reg... |
| 14 | no | 15791350 | - | 0.339 | brand=iki chic, color=Pink, category=T-shirt, occasion=Casual, price=1999.0 | Product: iki chic Women Pink & Black Printed T-shirt with Capris Brand: iki chic Color: Pink Category: T-shirt Top type: T-shirt Bottom type: Capris Pattern: Printed Neck: Round... |
| 15 | no | 18529956 | - | 0.317 | brand=JC Collection, color=Pink, category=Shirt, occasion=Party, price=6099.0 | Product: JC Collection Women Pink & White Printed Shirt & Skirt Co-Ords Brand: JC Collection Color: Pink Category: Shirt Top type: Shirt Bottom type: Skirt Pattern: Printed Neck... |
| 16 | no | 10720170 | - | 0.300 | brand=Style Quotient, color=Pink, occasion=Casual, price=1399.0 | Product: Style Quotient Women Pink Self Design Crop Shrug Brand: Style Quotient Color: Pink Pattern: Self design Sleeves: Three-quarter sleeves Length: Crop Hemline: Straight To... |
| 17 | no | 15851572 | - | 0.299 | brand=URBANIC, color=Pink, category=T-shirt, occasion=Casual, price=2090.0 | Product: URBANIC Women Pink Solid T-shirt with Joggers Brand: URBANIC Color: Pink Category: T-shirt Top type: T-shirt Bottom type: Trousers Pattern: Solid Neck: Hood Sleeves: Lo... |
| 18 | no | 15720246 | - | 0.296 | brand=HIGHLIGHT FASHION EXPORT, color=Pink, category=Regular, occasion=Ethnic, price=1999.0 | Product: HIGHLIGHT FASHION EXPORT Pink Embroidered Regular Top Brand: HIGHLIGHT FASHION EXPORT Color: Pink Category: Regular Pattern: Abstract embroidered Neck: Round neck Sleev... |
| 19 | no | 16955084 | - | 0.292 | brand=Kook N Keech Disney, color=Pink, category=T-shirt, occasion=Casual, price=2199.0 | Product: Kook N Keech Disney Women Charming Pink Printed T-Shirt with Solid Trousers Brand: Kook N Keech Disney Color: Pink Category: T-shirt Top type: T-shirt Bottom type: Trou... |
| 20 | no | 18667672 | - | 0.291 | brand=Stylee LIFESTYLE, color=Pink, category=Dress, occasion=Festive, price=5449.0 | Product: Stylee LIFESTYLE Pink & Red Satin Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Pink Category: Dress Pattern: Abstract Bottom fabric: Shantoon Dupatta fabric... |
| 21 | no | 19032532 | - | 0.257 | brand=BUY NEW TREND, color=Pink, occasion=Casual, price=1399.0 | Product: BUY NEW TREND Women Pink & Yellow Printed Tie-Up Shrug Brand: BUY NEW TREND Color: Pink Pattern: Printed Sleeves: Long sleeves Length: Regular Hemline: Straight Top fab... |
| 22 | no | 18087234 | - | 0.252 | brand=Tikhi Imli, color=Pink, category=Saree, occasion=Party, price=1598.0 | Product: Tikhi Imli Pink & Blue Butterfly Printed Poly Georgette Saree Brand: Tikhi Imli Color: Pink Category: Saree Pattern: Abstract printed Occasion: Party Wash care: Dry clean |
| 23 | no | 9301311 | - | 0.243 | brand=Tissu, color=Pink, occasion=Daily, price=1499.0 | Product: Tissu Women Pink & Off-White Floral Print Anarkali Kurta Brand: Tissu Color: Pink Pattern: Floral printed Shape: Anarkali Neck: Round neck Sleeves: Three-quarter regula... |
| 24 | no | 19280832 | - | 0.238 | brand=VividArtsy, color=Pink, category=Sweatshirt, occasion=Casual, price=2499.0 | Product: VividArtsy Women Pink Tie & Dye Printed Co-Ords Brand: VividArtsy Color: Pink Category: Sweatshirt Top type: Sweatshirt Bottom type: Trousers Pattern: Dyed Neck: Hood S... |
| 25 | no | 15228856 | - | 0.236 | brand=Blissta, color=Pink, category=Dress, occasion=Festive, price=6149.0 | Product: Blissta Pink Unstitched Dress Material Brand: Blissta Color: Pink Category: Dress Pattern: Abstract Bottom fabric: Shantoon Dupatta fabric: Silk blend Occasion: Festive... |
| 26 | no | 17365728 | - | 0.234 | brand=I Saw It First, color=Pink, category=Flared, occasion=Casual, price=1499.0 | Product: I Saw It First Women Dusty Pink & White Striped Pleated Mini Skater Skirt Brand: I Saw It First Color: Pink Category: Flared Pattern: Striped Length: Mini Hemline: Flar... |
| 27 | no | 17973842 | - | 0.231 | brand=MANGO, color=Pink, category=Regular trousers, occasion=Casual, price=4590.0 | Product: MANGO Women Pink & Black Printed Straight Fit High-Rise Trousers Brand: MANGO Color: Pink Category: Regular trousers Pattern: Abstract printed Length: Regular Top fabri... |
| 28 | no | 14955108 | - | 0.225 | brand=Roadster, color=Pink, category=T-shirt, occasion=Casual, price=2399.0 | Product: Roadster Women Pink & Grey Camouflage Printed T-shirt with Joggers Brand: Roadster Color: Pink Category: T-shirt Top type: T-shirt Bottom type: Trousers Pattern: Printe... |
| 29 | no | 16887876 | - | 0.213 | brand=TANKHI, color=Pink, occasion=Ethnic, price=1899.0 | Product: TANKHI Women Pink Floral Printed Tunic Brand: TANKHI Color: Pink Pattern: Printed Neck: Round neck Sleeves: Three-quarter sleeves Top fabric: Silk Occasion: Ethnic Wash... |
| 30 | no | 15496398 | - | 0.210 | brand=JC Collection, color=Pink, category=Top, occasion=Casual, price=6599.0 | Product: JC Collection Women Pink & Brown Printed Shirt with Trousers Brand: JC Collection Color: Pink Category: Top Top type: Top Bottom type: Trousers Pattern: Printed Neck: S... |

### Question 33/50

**Query:** I'm looking for products by Atsevam.

**Retrieval metadata:** brand == Atsevam

**Relevant docs:** `['17754230', '17754250', '17754248', '19217168', '19217170', '17584576', '19217176']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.700 | 1.000 | 1.000 | 0.964 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 17754230 | - | 0.872 | brand=Atsevam, color=Cream, price=5001.0 | Product: Atsevam Cream-Coloured & Red Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Cream Dupatta: With dupatta Pattern: Woven design Neck: V-neck... |
| 2 | yes | 17754248 | - | 0.809 | brand=Atsevam, color=Red, price=5001.0 | Product: Atsevam Red Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Red Dupatta: With dupatta Pattern: Embroidered Neck: Ro... |
| 3 | yes | 19217168 | - | 0.433 | brand=Atsevam, color=Green, price=5599.0 | Product: Atsevam Green & Gold-Toned Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Green Dupatta: With dupatta Pattern: Emb... |
| 4 | yes | 17754250 | - | 0.420 | brand=Atsevam, color=Pink, price=5001.0 | Product: Atsevam Women Pink Embroidered Semi-Stitched Lehenga Unstitched Choli & Dupatta Brand: Atsevam Color: Pink Dupatta: With dupatta Pattern: Embroidered Neck: Round neck S... |
| 5 | no | 19217196 | - | 0.411 | brand=Atsevam, color=Pink, price=7349.0 | Product: Atsevam Pink Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Pink Dupatta: With dupatta Pattern: Embroidered Neck: ... |
| 6 | yes | 19217170 | - | 0.394 | brand=Atsevam, color=Red, price=6699.0 | Product: Atsevam Red & Gold-Toned Embroidered Thread Work Tie and Dye Semi-Stitched Lehenga & Unstitched Blouse With Brand: Atsevam Color: Red Dupatta: With dupatta Pattern: Emb... |
| 7 | no | 17834516 | - | 0.387 | brand=Atsevam, color=Blue, price=5000.0 | Product: Atsevam Blue & Pink Ready to Wear Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Blue Dupatta: With dupatta Pattern: Woven design Neck: Round neck Sleev... |
| 8 | no | 19217186 | - | 0.384 | brand=Atsevam, color=Green, price=5349.0 | Product: Atsevam Women Green & Pink Printed Tie and Dye Semi-Stitched Lehenga Choli Brand: Atsevam Color: Green Dupatta: With dupatta Pattern: Printed Neck: Round neck Sleeves: ... |
| 9 | yes | 17584576 | - | 0.383 | brand=Atsevam, color=Orange, price=6999.0 | Product: Atsevam Orange & Red Printed Tie and Dye Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Orange Dupatta: With dupatta Pattern: Printed Neck... |
| 10 | yes | 19217176 | - | 0.274 | brand=Atsevam, color=White, price=7999.0 | Product: Atsevam White & Pink Tie and Dye Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: White Dupatta: With dupatta Pattern: Woven design Neck: V-... |

### Question 34/50

**Query:** What do you have from panchhi in products and color Pink?

**Retrieval metadata:** brand == panchhi, color == Pink

**Relevant docs:** `['19046346', '12003682']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.500 | 1.000 | 0.500 | 0.651 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 18070000 | - | 1.000 | brand=panchhi, color=Pink, price=12999.0 | Product: panchhi Pink Embroidered Sequinned Unstitched Lehenga & Blouse With Dupatta Brand: panchhi Color: Pink Dupatta: With dupatta Pattern: Embroidered Neck: V-neck Sleeves: ... |
| 2 | yes | 19046346 | - | 0.382 | brand=panchhi, color=Pink, price=12999.0 | Product: panchhi Pink & Sea Green Embellished Sequinned Semi-Stitched Lehenga & Ready to Wear Blouse With Dupatta Brand: panchhi Color: Pink Dupatta: With dupatta Pattern: Embel... |
| 3 | no | 18175384 | - | 0.136 | brand=panchhi, color=Pink, price=12999.0 | Product: panchhi Pink Net Embroidered Sequinned Semi-Stitched Lehenga & Blouse With Dupatta Brand: panchhi Color: Pink Dupatta: With dupatta Pattern: Embroidered Neck: Round nec... |
| 4 | yes | 12003682 | - | 0.095 | brand=panchhi, color=Pink, occasion=Festive, price=3999.0 | Product: panchhi Pink & Beige Embellished Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Pink Dupatta: With dupatta Pattern: Embellished Neck: V-ne... |

### Question 35/50

**Query:** What do you have in products under 2500?

**Retrieval metadata:** price <= 2500.0

**Relevant docs:** `['11765970', '17662818', '15514544', '18068482', '16989998', '16563320', '15011850', '15266776']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 16858560 | - | 0.500 | brand=NEUDIS, color=Black, category=Regular trousers, occasion=Casual, price=1799.0 | Product: NEUDIS Women Black Comfort Flared Trousers Brand: NEUDIS Color: Black Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Polyester Occasion: Casual P... |
| 2 | no | 19177952 | - | 0.500 | brand=250 DESIGNS, color=Black, occasion=Casual, price=1999.0 | Product: 250 DESIGNS Women Black & Brown Printed Sheer Shrug Brand: 250 DESIGNS Color: Black Pattern: Printed Sleeves: Short sleeves Length: Regular Hemline: Straight Top fabric... |
| 3 | no | 17612960 | - | 0.462 | brand=250 DESIGNS, color=Navy Blue, category=Top, occasion=Casual, price=4999.0 | Product: 250 DESIGNS Women Navy Blue Floral Co-Ord Set Brand: 250 DESIGNS Color: Navy Blue Category: Top Top type: Top Bottom type: Palazzos Pattern: Printed Neck: V-neck Sleeve... |
| 4 | no | 16172382 | - | 0.346 | brand=NEUDIS, color=Red, category=Regular, occasion=Casual, price=1499.0 | Product: NEUDIS Red Cowl Neck Satin Regular Top Brand: NEUDIS Color: Red Category: Regular Pattern: Solid Neck: Cowl neck Sleeves: Sleeveless no Length: Regular Top fabric: Sati... |
| 5 | no | 18489222 | - | 0.342 | brand=NEUDIS, color=Red, category=Regular, occasion=Casual, price=1499.0 | Product: NEUDIS Red Cowl Neck Satin Top Brand: NEUDIS Color: Red Category: Regular Pattern: Solid Neck: Cowl neck Sleeves: Sleeveless no Length: Regular Top fabric: Satin Occasi... |
| 6 | no | 17255464 | - | 0.338 | brand=NEUDIS, color=Red, category=Styled back, occasion=Casual, price=1499.0 | Product: NEUDIS Women Satin Red Embillished Solid A-Line Top Brand: NEUDIS Color: Red Category: Styled back Pattern: Solid Neck: Jewel neck Sleeves: Sleeveless no Length: Regula... |
| 7 | no | 18057660 | - | 0.300 | brand=NEUDIS, color=White, category=A-line, occasion=Casual, price=1599.0 | Product: NEUDIS Women White Self-Design A-Line Skirt Brand: NEUDIS Color: White Category: A-line Pattern: Self design solid Length: Knee length Hemline: Flared Top fabric: Polye... |
| 8 | no | 17336142 | - | 0.284 | brand=UNDER ARMOUR, color=Pink, category=Sports shorts, occasion=Sports, price=1999.0 | Product: UNDER ARMOUR Women Pink Loose Fit Training Play Up Shorts 3.0 Brand: UNDER ARMOUR Color: Pink Category: Sports shorts Pattern: Solid Length: Above knee Top fabric: Poly... |
| 9 | no | 2507000 | - | 0.261 | brand=Roadster, color=Pink, category=Regular, occasion=Casual, price=899.0 | Product: Roadster Pink Knitted Lace Top Brand: Roadster Color: Pink Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short regular sleeves Length: Regular Occasion: Ca... |
| 10 | no | 18806012 | - | 0.237 | brand=awesome, color=Red, category=Banarasi, occasion=Traditional, price=5999.0 | Product: awesome Red & Gold-Toned Woven Design Zari Pure Silk Banarasi Saree Brand: awesome Color: Red Category: Banarasi Pattern: Woven design Occasion: Traditional Wash care: ... |
| 11 | no | 16034502 | - | 0.236 | brand=Berrylush, color=Yellow, category=Playsuit, occasion=Casual, price=2199.0 | Product: Berrylush Women Bright Yellow Printed Cinched Waist Jumpsuit Brand: Berrylush Color: Yellow Category: Playsuit Pattern: Printed Neck: Halter neck Sleeves: Sleeveless To... |
| 12 | no | 18290992 | - | 0.230 | brand=Superminis, color=Brown, price=2499.0 | Product: Superminis Girls Brown & Embroidered Ready to Wear Lehenga & Blouse With Dupatta Brand: Superminis Color: Brown Dupatta: With dupatta Pattern: Embroidered Neck: Round n... |
| 13 | no | 18284594 | - | 0.228 | brand=HERSHEINBOX, color=Purple, category=Basic jumpsuit, occasion=Casual, price=1939.0 | Product: HERSHEINBOX Women Purple Printed Noughties Spaghetti Jumpsuit Brand: HERSHEINBOX Color: Purple Category: Basic jumpsuit Pattern: Printed Neck: Scoop neck Sleeves: Sleev... |
| 14 | no | 17238348 | - | 0.226 | brand=NEUDIS, color=Beige, category=Regular, occasion=Casual, price=1499.0 | Product: NEUDIS Beige Cowl Neck Sheen Satin Finish Top Brand: NEUDIS Color: Beige Category: Regular Pattern: Solid Neck: Cowl neck Sleeves: Sleeveless no Length: Regular Top fab... |
| 15 | no | 15381904 | - | 0.219 | brand=Berrylush, color=Pink, category=Basic jumpsuit, occasion=Casual, price=1899.0 | Product: Berrylush Women Pink Solid Ruffled Jumpsuit Brand: Berrylush Color: Pink Category: Basic jumpsuit Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless Top fabric: P... |
| 16 | no | 17209256 | - | 0.207 | brand=Unnati Silks, color=Cream, category=Banarasi, occasion=Traditional, price=7198.0 | Product: Unnati Silks Cream-Coloured & Black Ethnic Motifs Embroidered Tissue Banarasi Saree Brand: Unnati Silks Color: Cream Category: Banarasi Pattern: Ethnic motifs embroider... |
| 17 | no | 16758920 | - | 0.207 | brand=ZIYAA, color=White, category=Basic jumpsuit, occasion=Ethnic, price=3747.0 | Product: ZIYAA Women Classic White Printed Cinched Waist Jumpsuit Brand: ZIYAA Color: White Category: Basic jumpsuit Pattern: Printed Neck: Round neck Sleeves: Long sleeves Top ... |
| 18 | no | 16372904 | - | 0.205 | brand=Netram, color=Beige, price=13206.0 | Product: Netram Beige Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Net Dupatta Brand: Netram Color: Beige Dupatta: With dupatta Pattern: Embroidered Sleeves: Short... |
| 19 | no | 18512872 | - | 0.200 | brand=Amrutam Fab, color=Cream, price=11999.0 | Product: Amrutam Fab Cream-Coloured & Navy Blue Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Brand: Amrutam Fab Color: Cream Dupatta: With dupatta Patter... |
| 20 | no | 15508760 | - | 0.193 | brand=SASSAFRAS, color=Navy Blue, category=Basic jumpsuit, occasion=Casual, price=2199.0 | Product: SASSAFRAS Women Deep Navy Blue Solid Boiler Jumpsuit Brand: SASSAFRAS Color: Navy Blue Category: Basic jumpsuit Pattern: Solid Neck: Shirt collar Sleeves: Short sleeves... |
| 21 | no | 18290988 | - | 0.192 | brand=Superminis, color=Lime Green, price=2499.0 | Product: Superminis Girls Lime Green & Beige Embroidered Ready to Wear Lehenga & Blouse With Dupatta Brand: Superminis Color: Lime Green Dupatta: With dupatta Pattern: Embroider... |
| 22 | no | 15589086 | - | 0.181 | brand=Netram, color=Lavender, price=11409.0 | Product: Netram Lavender & Silver-Toned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Netram Color: Lavender Dupatta: With dupatta Pattern: Embroidered Sleeves: ... |
| 23 | no | 17725246 | - | 0.180 | brand=DIVASTRI, color=Red, price=5999.0 | Product: DIVASTRI Red & Mustard Banarasi Silk Semi-Stitched Lehenga & Unstitched Blouse & Dupatta Brand: DIVASTRI Color: Red Dupatta: With dupatta Pattern: Woven design Neck: Bo... |
| 24 | no | 15071832 | - | 0.177 | brand=all about you, color=Blue, category=Saree, occasion=Daily, price=3599.0 | Product: all about you Blue & Violet Floral Organza Saree Brand: all about you Color: Blue Category: Saree Pattern: Floral printed Occasion: Daily Wash care: Dry clean |
| 25 | no | 18258322 | - | 0.175 | brand=Netram, color=Red, price=10340.0 | Product: Netram Red & Gold-Toned Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Netram Color: Red Dupatta: With dupatta Pattern: Embroidered Neck: Rou... |
| 26 | no | 16311568 | - | 0.174 | brand=all about you, color=Grey, category=Saree, occasion=Festive, price=3999.0 | Product: all about you Grey Leheriya Organza Saree Brand: all about you Color: Grey Category: Saree Pattern: Leheriya embroidered Occasion: Festive Wash care: Dry clean |
| 27 | no | 16311702 | - | 0.174 | brand=all about you, color=Pink, category=Kanjeevaram, occasion=Traditional, price=2999.0 | Product: all about you Pink Woven Design Silk Blend Kanjeevaram Saree Brand: all about you Color: Pink Category: Kanjeevaram Pattern: Woven design Occasion: Traditional Wash car... |
| 28 | no | 16311684 | - | 0.173 | brand=all about you, color=Blue, category=Saree, occasion=Festive, price=3999.0 | Product: all about you Blue Leheriya Organza Saree Brand: all about you Color: Blue Category: Saree Pattern: Leheriya embroidered Occasion: Festive Wash care: Dry clean |
| 29 | no | 16311576 | - | 0.173 | brand=all about you, color=Pink, category=Saree, occasion=Festive, price=3499.0 | Product: all about you Pink Embroidered with Bead Work Net Saree Brand: all about you Color: Pink Category: Saree Pattern: Floral embroidered Occasion: Festive Wash care: Dry clean |
| 30 | no | 16828018 | - | 0.173 | brand=all about you, color=Pink, category=Saree, occasion=Party, price=3699.0 | Product: all about you Women Pink & Silver Floral Embroidered Fusion Net Saree Brand: all about you Color: Pink Category: Saree Pattern: Floral embroidered Occasion: Party Wash ... |

### Question 36/50

**Query:** Show me products from Indo Era.

**Retrieval metadata:** brand == Indo Era

**Relevant docs:** `['14239788', '11459668', '12040868', '15520698', '12040878', '12122360', '13250074', '17553564']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.167 | 0.625 | 0.333 | 0.439 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 14869156 | - | 0.961 | brand=Indo Era, color=Black, price=5999.0 | Product: Indo Era Deep Black Solid Lehenga with Embroidered Choli Brand: Indo Era Color: Black Pattern: Embroidered Neck: V-neck Sleeves: Three-quarter regular sleeves Hemline: ... |
| 2 | no | 16188740 | - | 0.881 | brand=Indo Era, color=Green, occasion=Western, price=2499.0 | Product: Indo Era Women Green Solid Cotton Palazzos Brand: Indo Era Color: Green Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Western Pockets: 2 Wash care: Hand wash |
| 3 | yes | 12122360 | - | 0.881 | brand=Indo Era, color=Brown, occasion=Daily, price=1299.0 | Product: Indo Era Brown & Golden Woven Design Dupatta Brand: Indo Era Color: Brown Pattern: Geometric woven design Top fabric: Art silk Occasion: Daily Wash care: Hand wash |
| 4 | no | 16950290 | - | 0.796 | brand=Indo Era, color=Sea Green, category=Regular, occasion=Ethnic, price=2799.0 | Product: Indo Era Sea Green Floral Print Tie-Up Neck Top Brand: Indo Era Color: Sea Green Category: Regular Pattern: Floral printed Neck: Tie-up neck Sleeves: Three-quarter regu... |
| 5 | yes | 12040878 | - | 0.775 | brand=Indo Era, color=Orange, occasion=Daily, price=999.0 | Product: Indo Era Orange & Pink Striped Dupatta Brand: Indo Era Color: Orange Pattern: Striped Top fabric: Art silk Occasion: Daily Wash care: Hand wash |
| 6 | no | 16950218 | - | 0.771 | brand=Indo Era, color=Blue, category=Peplum, occasion=Ethnic, price=3399.0 | Product: Indo Era Blue Ethnic Motif Printed Peplum Top Brand: Indo Era Color: Blue Category: Peplum Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Three-quarter regula... |
| 7 | yes | 11459668 | - | 0.765 | brand=Indo Era, color=Navy Blue, occasion=Party, price=999.0 | Product: Indo Era Navy Blue & Gold-Toned Striped Dupatta Brand: Indo Era Color: Navy Blue Pattern: Striped Top fabric: Art silk Occasion: Party Wash care: Hand wash |
| 8 | yes | 12040868 | - | 0.739 | brand=Indo Era, color=Navy Blue, occasion=Party, price=999.0 | Product: Indo Era Navy Blue & Golden Striped Dupatta Brand: Indo Era Color: Navy Blue Pattern: Striped Top fabric: Art silk Occasion: Party Wash care: Hand wash |
| 9 | no | 17577466 | - | 0.734 | brand=Indo Era, color=Orange, category=A-line, occasion=Ethnic, price=2799.0 | Product: Indo Era Women Bright Orange Ethnic Fusion Top Brand: Indo Era Color: Orange Category: A-line Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Short regular sle... |
| 10 | no | 17577464 | - | 0.729 | brand=Indo Era, color=Blue, category=A-line, occasion=Ethnic, price=2999.0 | Product: Indo Era Women Stunning Blue Floral Ethnic Fusion Top Brand: Indo Era Color: Blue Category: A-line Pattern: Floral printed Neck: Shoulder straps Sleeves: Sleeveless sho... |
| 11 | no | 13810898 | - | 0.729 | brand=Indo Era, color=Blue, category=Kurta set, occasion=Festive, price=4599.0 | Product: Indo Era Women Blue & Green Printed Kurta with Palazzos & Dupatta Brand: Indo Era Color: Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With du... |
| 12 | no | 17577456 | - | 0.725 | brand=Indo Era, color=Off White, category=A-line, occasion=Ethnic, price=2799.0 | Product: Indo Era Women Classic Off-White Ethnic Motifs Nuovo Sleeves Top Brand: Indo Era Color: Off White Category: A-line Pattern: Ethnic motifs solid Neck: Round neck Sleeves... |
| 13 | no | 16713198 | - | 0.703 | brand=Indo Era, color=Grey, category=Kurta set, occasion=Festive, price=7999.0 | Product: Indo Era Grey Silk Blend Scalloped Edge Kurta Set Brand: Indo Era Color: Grey Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta Pattern: E... |
| 14 | no | 15098594 | - | 0.694 | brand=Indo Era, color=Teal, occasion=Daily, price=1999.0 | Product: Indo Era Women Teal Green & Golden Ethnic Motifs Yoke Design Kurta Brand: Indo Era Color: Teal Pattern: Ethnic motifs yoke design Shape: Straight Neck: Round neck Sleev... |
| 15 | no | 12122358 | - | 0.690 | brand=Indo Era, color=Black, category=Kurta set, occasion=Festive, price=2799.0 | Product: Indo Era Women Black & Teal Blue Yoke Design Kurta with Palazzos & Dupatta Brand: Indo Era Color: Black Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatt... |
| 16 | no | 15258422 | - | 0.685 | brand=Indo Era, color=Green, category=Kurta set, occasion=Festive, price=4599.0 | Product: Indo Era Floral Cotton Blend Calf Length Kurta Set Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta Pattern:... |
| 17 | no | 17069054 | - | 0.680 | brand=Indo Era, color=Black, category=Kurta set, occasion=Festive, price=5799.0 | Product: Indo Era Women Black Ethnic Motifs Yoke Design Thread Work Kurta with Trousers & With Dupatta Brand: Indo Era Color: Black Category: Kurta set Top type: Kurta Bottom ty... |
| 18 | no | 17553556 | - | 0.656 | brand=Indo Era, color=Green, occasion=Daily, price=2099.0 | Product: Indo Era Green & Gold-Toned Woven Design Dupatta Brand: Indo Era Color: Green Pattern: Solid woven design Top fabric: Silk blend Occasion: Daily Wash care: Hand wash |
| 19 | no | 15098616 | - | 0.655 | brand=Indo Era, color=Burgundy, occasion=Festive, price=2699.0 | Product: Indo Era Women Burgundy & Golden Ethnic Motifs Yoke Design Kurta Brand: Indo Era Color: Burgundy Pattern: Ethnic motifs yoke design Shape: Straight Neck: Round neck Sle... |
| 20 | no | 14235030 | - | 0.653 | brand=Indo Era, color=Black, category=Kurta set, occasion=Festive, price=3499.0 | Product: Indo Era Women Black Floral Printed Pure Cotton Kurta with Trousers & With Dupatta Brand: Indo Era Color: Black Category: Kurta set Top type: Kurta Bottom type: Trouser... |
| 21 | no | 12418804 | - | 0.651 | brand=Indo Era, color=Maroon, category=Kurta set, occasion=Festive, price=2999.0 | Product: Indo Era Women Maroon & Orange Yoke Design Kurta with Palazzos & Dupatta Brand: Indo Era Color: Maroon Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta... |
| 22 | no | 17911130 | - | 0.650 | brand=Indo Era, color=Burgundy, category=Kurta set, occasion=Festive, price=3499.0 | Product: Indo Era Women Burgundy Sequined Kurta with Palazzos & Dupatta Brand: Indo Era Color: Burgundy Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With d... |
| 23 | no | 15654150 | - | 0.644 | brand=Indo Era, color=Green, category=Kurta set, occasion=Festive, price=5399.0 | Product: Indo Era Women Green Ethnic Motifs Yoke Design Regular Kurta with Trousers & With Dupatta Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: ... |
| 24 | no | 11459658 | - | 0.644 | brand=Indo Era, color=Burgundy, category=Kurta set, occasion=Daily, price=4999.0 | Product: Indo Era Folksy Floral Screen Print Cotton Kurta Set Brand: Indo Era Color: Burgundy Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta Pat... |
| 25 | no | 15794640 | - | 0.639 | brand=Indo Era, color=Maroon, category=Kurta set, occasion=Festive, price=6999.0 | Product: Indo Era Woven Design Velvet Kurta Set Brand: Indo Era Color: Maroon Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With dupatta Pattern: Woven desi... |
| 26 | no | 14967448 | - | 0.637 | brand=Indo Era, color=Green, category=Kurta set, occasion=Daily, price=4399.0 | Product: Indo Era Women Green Ethnic Motifs Printed Panelled Gotta Patti Pure Cotton Kurta with Trousers & With Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta ... |
| 27 | no | 16713256 | - | 0.631 | brand=Indo Era, color=Mustard, category=Kurta set, occasion=Festive, price=7999.0 | Product: Indo Era Mustard Liva Calf Length Kurta Set Brand: Indo Era Color: Mustard Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With dupatta Pattern: Flor... |
| 28 | no | 15794634 | - | 0.623 | brand=Indo Era, color=Red, category=Kurta set, occasion=Festive, price=6999.0 | Product: Indo Era Embroidered Velvet Kurta Set Brand: Indo Era Color: Red Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With dupatta Pattern: Ethnic motifs ... |
| 29 | no | 13962300 | - | 0.620 | brand=Indo Era, color=Off White, category=Kurta set, occasion=Festive, price=6999.0 | Product: Indo Era Classy Off White And Yellow Printed Kurta Set Brand: Indo Era Color: Off White Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With dupatta ... |
| 30 | yes | 15520698 | - | 0.600 | brand=Indo Era, color=Navy Blue, occasion=Festive, price=2599.0 | Product: Indo Era Women Navy Blue Floral Yoke Design Kurta Brand: Indo Era Color: Navy Blue Pattern: Floral yoke design Shape: Straight Neck: Round neck Sleeves: Three-quarter r... |

### Question 37/50

**Query:** Show me products like "ONLY Women Blue Straight Fit High-Rise Mildly Distressed Jeans".

**Retrieval metadata:** brand == ONLY, color == Blue

**Relevant docs:** `['18626222']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.033 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 18626222 | - | 1.000 | brand=ONLY, color=Blue, occasion=Casual, price=3699.0 | Product: ONLY Women Blue Straight Fit High-Rise Mildly Distressed Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine... |
| 2 | no | 18620390 | - | 0.946 | brand=ONLY, color=Blue, occasion=Casual, price=2999.0 | Product: ONLY Women Blue Skinny Fit High-Rise Mildly Distressed Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care... |
| 3 | no | 16372376 | - | 0.946 | brand=ONLY, color=Blue, occasion=Casual, price=3699.0 | Product: ONLY Women Blue Slim Fit High-Rise Mildly Distressed Heavy Fade Stretchable Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5... |
| 4 | no | 18626210 | - | 0.945 | brand=ONLY, color=Blue, occasion=Casual, price=3699.0 | Product: ONLY Women Blue Skinny Fit High-Rise Mildly Distressed Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 5 | no | 19089706 | - | 0.933 | brand=ONLY, color=Blue, occasion=Casual, price=4299.0 | Product: ONLY Women Blue Slim Fit High-Rise Mildly Distressed Heavy Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: ... |
| 6 | no | 16699772 | - | 0.913 | brand=ONLY, color=Blue, occasion=Casual, price=4299.0 | Product: ONLY Women Blue High-Rise Mildly Distressed Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 7 | no | 19089710 | - | 0.779 | brand=ONLY, color=Blue, occasion=Casual, price=4999.0 | Product: ONLY Women Blue Flared Mildly Distressed Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 8 | no | 19089694 | - | 0.755 | brand=ONLY, color=Blue, occasion=Casual, price=3699.0 | Product: ONLY Women Blue Straight Fit High-Rise Low Distress Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 9 | no | 19089668 | - | 0.753 | brand=ONLY, color=Blue, occasion=Casual, price=4299.0 | Product: ONLY Women Blue Straight Fit High-Rise Low Distress Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: M... |
| 10 | no | 17914728 | - | 0.748 | brand=ONLY, color=Blue, occasion=Casual, price=3499.0 | Product: ONLY Women Blue Straight Fit High-Rise Low Distress Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: M... |
| 11 | no | 19143972 | - | 0.746 | brand=ONLY, color=Blue, occasion=Casual, price=3999.0 | Product: ONLY Women Blue Straight Fit High-Rise Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 12 | no | 18620400 | - | 0.736 | brand=ONLY, color=Blue, occasion=Casual, price=2999.0 | Product: ONLY Women Blue Skinny Fit High-Rise Low Distress Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 13 | no | 19089666 | - | 0.716 | brand=ONLY, color=Blue, occasion=Casual, price=3999.0 | Product: ONLY Women Blue Slim Fit High-Rise Low Distress Heavy Fade Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machi... |
| 14 | no | 18626226 | - | 0.702 | brand=ONLY, color=Blue, occasion=Casual, price=3699.0 | Product: ONLY Women Blue Straight Fit High-Rise Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 15 | no | 16916588 | - | 0.664 | brand=ONLY, color=Blue, occasion=Casual, price=3699.0 | Product: ONLY Women Blue Mom-Fit High-Rise Light Fade Printed Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 16 | no | 18626254 | - | 0.663 | brand=ONLY, color=Blue, occasion=Casual, price=3499.0 | Product: ONLY Women Blue Bootcut High-Rise Low Distress Light Fade Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machin... |
| 17 | no | 18626232 | - | 0.658 | brand=ONLY, color=Blue, occasion=Casual, price=3699.0 | Product: ONLY Women Blue Skinny Fit High-Rise Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 18 | no | 18620404 | - | 0.654 | brand=ONLY, color=Blue, occasion=Casual, price=2499.0 | Product: ONLY Women Blue Skinny Fit High-Rise Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 19 | no | 18626248 | - | 0.654 | brand=ONLY, color=Blue, occasion=Casual, price=3699.0 | Product: ONLY Women Blue Skinny Fit High-Rise Slash Knee Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 20 | no | 17914732 | - | 0.648 | brand=ONLY, color=Blue, occasion=Casual, price=3999.0 | Product: ONLY Women Blue Skinny Fit High-Rise Slash Knee Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machi... |
| 21 | no | 19089662 | - | 0.625 | brand=ONLY, color=Blue, occasion=Casual, price=3499.0 | Product: ONLY Women Blue Skinny Fit High-Rise Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 22 | no | 18809318 | - | 0.517 | brand=ONLY, color=Blue, occasion=Casual, price=2999.0 | Product: ONLY Women Blue Skinny Fit Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 23 | no | 18809310 | - | 0.517 | brand=ONLY, color=Blue, occasion=Casual, price=2999.0 | Product: ONLY Women Blue Skinny Fit Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 24 | no | 19175980 | - | 0.439 | brand=ONLY, color=Blue, category=Regular trousers, occasion=Casual, price=3299.0 | Product: ONLY Women Blue High-Rise Trousers Brand: ONLY Color: Blue Category: Regular trousers Pattern: Solid self design Length: Regular Top fabric: Nylon Occasion: Casual Wash... |
| 25 | no | 19175662 | - | 0.359 | brand=ONLY, color=Blue, category=Denim jacket, occasion=Casual, price=4499.0 | Product: ONLY Women Blue Washed Crop Denim Jacket Brand: ONLY Color: Blue Category: Denim jacket Pattern: Washed solid Sleeves: Long sleeves Length: Crop Hemline: Straight Top f... |
| 26 | no | 19175664 | - | 0.356 | brand=ONLY, color=Blue, category=Denim jacket, occasion=Casual, price=4499.0 | Product: ONLY Women Blue Washed Colourblocked Crop Denim Jacket Brand: ONLY Color: Blue Category: Denim jacket Pattern: Washed colourblocked Sleeves: Long sleeves Length: Crop H... |
| 27 | no | 18624784 | - | 0.345 | brand=ONLY, color=Blue, category=Denim jacket, occasion=Casual, price=3699.0 | Product: ONLY Women Blue Crop Denim Jacket with Embroidered Brand: ONLY Color: Blue Category: Denim jacket Pattern: Graphic solid Sleeves: Long sleeves Length: Crop Hemline: Str... |
| 28 | no | 19175660 | - | 0.342 | brand=ONLY, color=Blue, category=Denim jacket, occasion=Casual, price=5499.0 | Product: ONLY Women Blue Colourblocked Crop Denim Jacket Brand: ONLY Color: Blue Category: Denim jacket Pattern: Colourblocked Sleeves: Long sleeves Length: Crop Hemline: Straig... |
| 29 | no | 19175872 | - | 0.328 | brand=ONLY, color=Blue, category=A-line, occasion=Casual, price=3499.0 | Product: ONLY Women Blue Solid Denim Mini Skirts Brand: ONLY Color: Blue Category: A-line Pattern: Colourblocked Length: Mini Hemline: Straight Top fabric: Pure cotton Occasion:... |
| 30 | no | 19175668 | - | 0.313 | brand=ONLY, color=Blue, category=Denim jacket, occasion=Casual, price=4499.0 | Product: ONLY Women Blue Washed Denim Jacket Brand: ONLY Color: Blue Category: Denim jacket Pattern: Washed solid Sleeves: Long sleeves Length: Regular Hemline: Curved Top fabri... |

### Question 38/50

**Query:** Do you have anything from Uptownie Lite in Flared?

**Retrieval metadata:** brand == Uptownie Lite

**Relevant docs:** `['17944738', '16608122', '11511460', '11425704', '13467524']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.333 | 1.000 | 1.000 | 0.943 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 17944738 | - | 0.922 | brand=Uptownie Lite, color=Grey, category=Flared, occasion=Casual, price=1999.0 | Product: Uptownie Lite Grey Solid Pleated Form Skirt Brand: Uptownie Lite Color: Grey Category: Flared Pattern: Solid Length: Midi Hemline: Flared Top fabric: Silk blend Occasio... |
| 2 | yes | 11425704 | - | 0.759 | brand=Uptownie Lite, color=Brown, category=Flared, occasion=Party, price=1999.0 | Product: Uptownie Lite Brown Satin Pleated Flared Midi Skirt Brand: Uptownie Lite Color: Brown Category: Flared Pattern: Solid Length: Midi Hemline: Flared Occasion: Party Wash ... |
| 3 | no | 11425706 | - | 0.744 | brand=Uptownie Lite, color=Black, category=Flared, occasion=Party, price=1999.0 | Product: Uptownie Lite Black Satin Pleated Flared Midi Skirt Brand: Uptownie Lite Color: Black Category: Flared Pattern: Solid Length: Midi Hemline: Flared Occasion: Party Wash ... |
| 4 | yes | 13467524 | - | 0.676 | brand=Uptownie Lite, color=Red, category=Flared, occasion=Casual, price=1999.0 | Product: Uptownie Lite Women Red Solid Pleated Midi Flare Skirt Brand: Uptownie Lite Color: Red Category: Flared Pattern: Solid Length: Midi Hemline: Flared Top fabric: Polyeste... |
| 5 | yes | 11511460 | - | 0.640 | brand=Uptownie Lite, color=Maroon, category=Flared, occasion=Party, price=1999.0 | Product: Uptownie Lite Women Maroon Solid Pleated Flared Midi Crepe Skirt Brand: Uptownie Lite Color: Maroon Category: Flared Pattern: Solid Length: Midi Hemline: Flared Top fab... |
| 6 | no | 15355338 | - | 0.578 | brand=Uptownie Lite, color=Black, category=Flared, occasion=Party, price=1699.0 | Product: Uptownie Lite Girls Black Crepe Printed Pleated Skirt Brand: Uptownie Lite Color: Black Category: Flared Pattern: Floral printed Length: Midi Hemline: Flared Top fabric... |
| 7 | yes | 16608122 | - | 0.564 | brand=Uptownie Lite, color=Black, category=Flared, occasion=Party, price=1699.0 | Product: Uptownie Lite Girls Black & Pink Printed Accordian Pleated Flared Knee-Length Skirt Brand: Uptownie Lite Color: Black Category: Flared Pattern: Floral printed Length: K... |
| 8 | no | 11335786 | - | 0.550 | brand=Uptownie Lite, color=Gold, category=Flared, occasion=Party, price=1999.0 | Product: Uptownie Lite Women Gold-Coloured Solid Accordion Pleated Flared Midi Skirt Brand: Uptownie Lite Color: Gold Category: Flared Pattern: Solid Length: Midi Hemline: Flare... |
| 9 | no | 11234642 | - | 0.346 | brand=Uptownie Lite, color=Black, category=Basic jumpsuit, price=2499.0 | Product: Uptownie Lite Women Black Solid Basic Jumpsuit with Belt Brand: Uptownie Lite Color: Black Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves: Sleeveless ... |
| 10 | no | 10418102 | - | 0.329 | brand=Uptownie Lite, color=Maroon, category=Basic jumpsuit, price=2299.0 | Product: Uptownie Lite Women Maroon Solid Ruffled Relaxed Fit Basic Jumpsuit Brand: Uptownie Lite Color: Maroon Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves:... |
| 11 | no | 11234652 | - | 0.269 | brand=Uptownie Lite, color=Burgundy, category=Basic jumpsuit, price=2499.0 | Product: Uptownie Lite Women Burgundy Solid Basic Jumpsuit with Belt Brand: Uptownie Lite Color: Burgundy Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves: Sleev... |
| 12 | no | 19169942 | - | 0.173 | brand=Uptownie Lite, color=Yellow, category=Basic jumpsuit, occasion=Casual, price=2499.0 | Product: Uptownie Lite Women Yellow Crepe Smocked Strapless Basic Jumpsuit Brand: Uptownie Lite Color: Yellow Category: Basic jumpsuit Pattern: Solid Neck: Strapless Sleeves: Sl... |
| 13 | no | 17267836 | - | 0.163 | brand=Uptownie Lite, color=Red, category=Basic jumpsuit, occasion=Casual, price=2199.0 | Product: Uptownie Lite Red & Yellow Striped Basic Jumpsuit Brand: Uptownie Lite Color: Red Category: Basic jumpsuit Pattern: Striped Neck: Round neck Sleeves: Sleeveless Top fab... |
| 14 | no | 11322090 | - | 0.156 | brand=Uptownie Lite, color=Black, category=Basic jumpsuit, price=2299.0 | Product: Uptownie Lite Women Black Solid Basic Ruffle Jumpsuit Brand: Uptownie Lite Color: Black Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves: Short sleeves ... |
| 15 | no | 13501842 | - | 0.088 | brand=Uptownie Lite, color=Black, category=Basic jumpsuit, occasion=Casual, price=2399.0 | Product: Uptownie Lite Women Black Solid Dhoti Jumpsuit Brand: Uptownie Lite Color: Black Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves: Sleeveless Top fabric... |

### Question 39/50

**Query:** Do you have anything similar to "Suta Beige & White Pure Linen Zari Saree"?

**Retrieval metadata:** brand == Suta, (color == Beige, color == White) [FILTERCONDITION.OR]

**Relevant docs:** `['15243956']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.111 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 15243956 | - | 1.000 | brand=Suta, color=Beige, category=Saree, occasion=Festive, price=3300.0 | Product: Suta Beige & White Pure Linen Zari Saree Brand: Suta Color: Beige Category: Saree Pattern: Solid Occasion: Festive Wash care: Dry clean |
| 2 | no | 14988280 | - | 0.361 | brand=Suta, color=Beige, category=Saree, occasion=Party, price=5731.0 | Product: Suta Beige & Black Pure Cotton solid Ruffle Saree Brand: Suta Color: Beige Category: Saree Pattern: Solid Occasion: Party Wash care: Hand wash |
| 3 | no | 16909300 | - | 0.302 | brand=Suta, color=Off White, category=Maheshwari, occasion=Traditional, price=6770.0 | Product: Suta Off White & Black Zari Silk Cotton Maheshwari Saree Brand: Suta Color: Off White Category: Maheshwari Pattern: Solid Occasion: Traditional Wash care: Dry clean |
| 4 | no | 15244224 | - | 0.288 | brand=Suta, color=Beige, category=Saree, occasion=Festive, price=3250.0 | Product: Suta Beige & White Floral Embroidered Saree Brand: Suta Color: Beige Category: Saree Pattern: Floral embroidered Occasion: Festive Wash care: Dry clean |
| 5 | no | 15244106 | - | 0.220 | brand=Suta, color=White, category=Saree, occasion=Daily, price=2700.0 | Product: Suta White & Pink Polka Dot Printed Pure Cotton Saree Brand: Suta Color: White Category: Saree Pattern: Polka dots printed Occasion: Daily Wash care: Hand wash |
| 6 | no | 15244024 | - | 0.204 | brand=Suta, color=Beige, category=Saree, occasion=Daily, price=4400.0 | Product: Suta Beige Pink Floral Motifs PolyCotton Saree Brand: Suta Color: Beige Category: Saree Pattern: Floral embroidered Occasion: Daily Wash care: Dry clean |
| 7 | no | 15244118 | - | 0.131 | brand=Suta, color=White, category=Saree, occasion=Work, price=6770.0 | Product: Suta White & Black Ethnic Motifs Jamdani Polycotton Saree Brand: Suta Color: White Category: Saree Pattern: Ethnic motifs printed Occasion: Work Wash care: Dry clean |
| 8 | no | 18390702 | - | 0.083 | brand=Suta, color=Off White, category=Saree, occasion=Festive, price=3540.0 | Product: Suta Off White & Golden Striped Saree Brand: Suta Color: Off White Category: Saree Pattern: Striped Occasion: Festive Wash care: Dry clean |
| 9 | no | 18166926 | - | 0.000 | brand=Suta, color=White, category=Saree, occasion=Daily, price=2900.0 | Product: Suta Women White Embroidered Cotton Saree Blouse Brand: Suta Color: White Category: Saree Pattern: Embroidered Neck: Boat neck Sleeves: Short sleeves Top fabric: Cotton... |

### Question 40/50

**Query:** Show me options from Levis for everyday wear, preferably in Blue.

**Retrieval metadata:** brand == Levis, color == Blue, occasion == Daily

**Relevant docs:** `['18069226', '16532142', '18069298', '18069260', '16653678', '16653750', '16653608', '16653786']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |

### Question 41/50

**Query:** Show me Pullover that are Black and have Solid print.

**Retrieval metadata:** color == Black

**Relevant docs:** `['16707678', '16124454', '13534776', '15964092', '15274016', '15963804', '15198584', '15243336']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.100 | 0.375 | 0.062 | 0.171 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 19266888 | - | 0.783 | brand=H&M, color=Black, category=Pullover, occasion=Casual, price=1999.0 | Product: H&M Women Black Solid Collared Sweatshirt Brand: H&M Color: Black Category: Pullover Pattern: Solid Neck: Mock collar Sleeves: Long sleeves Length: Regular Hemline: Rib... |
| 2 | no | 15845464 | - | 0.749 | brand=URBANIC, color=Black, category=Pullover, occasion=Casual, price=1890.0 | Product: URBANIC Women Black Solid Cotton Sweatshirt Brand: URBANIC Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Crop Hemline: S... |
| 3 | no | 17038044 | - | 0.740 | brand=Levis, color=Black, category=Pullover, occasion=Casual, price=2999.0 | Product: Levis Women Black Pullover Sweater Brand: Levis Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Ribbed To... |
| 4 | no | 9478497 | - | 0.735 | brand=Roadster, color=Black, category=Pullover, occasion=Casual, price=1299.0 | Product: The Roadster Lifestyle Co Women Black Solid Sweater Brand: Roadster Color: Black Category: Pullover Pattern: Solid Neck: V-neck Sleeves: Long sleeves Hemline: Ribbed To... |
| 5 | no | 14080898 | - | 0.725 | brand=DressBerry, color=Black, category=Pullover, occasion=Casual, price=1799.0 | Product: DressBerry Women Black Print Detail Sweatshirt Brand: DressBerry Color: Black Category: Pullover Pattern: Typography solid Neck: Round neck Sleeves: Long sleeves Length... |
| 6 | no | 10575458 | - | 0.717 | brand=Roadster, color=Black, category=Pullover, occasion=Casual, price=1699.0 | Product: The Roadster Lifestyle Co Women Black Solid Sweater Brand: Roadster Color: Black Category: Pullover Pattern: Solid Neck: Turtle neck Sleeves: Long sleeves Hemline: Curv... |
| 7 | no | 15642616 | - | 0.711 | brand=Aesthetic Bodies, color=Black, category=Pullover, occasion=Casual, price=1299.0 | Product: Aesthetic Bodies Women Black Cotton Sweatshirt Brand: Aesthetic Bodies Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Cro... |
| 8 | no | 15630060 | - | 0.697 | brand=H&M, color=Black, category=Pullover, occasion=Casual, price=1499.0 | Product: H&M Women Black Solid Hoodie Brand: H&M Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Longline Hemline: Straight Top fabric: C... |
| 9 | no | 6726577 | - | 0.693 | brand=Mast & Harbour, color=Black, category=Pullover, occasion=Casual, price=1299.0 | Product: Mast & Harbour Women Black Solid Pullover Brand: Mast & Harbour Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Hemline: Ribbed To... |
| 10 | no | 12048466 | - | 0.689 | brand=INVICTUS, color=Black, category=Pullover, occasion=Casual, price=1499.0 | Product: INVICTUS Women Black Solid Pullover Brand: INVICTUS Color: Black Category: Pullover Pattern: Solid Neck: V-neck Sleeves: Long sleeves Length: Regular Hemline: Ribbed To... |
| 11 | no | 14331596 | - | 0.680 | brand=Roadster, color=Black, category=Pullover, occasion=Casual, price=1299.0 | Product: Roadster Women Black Solid Turtle Neck Pullover Brand: Roadster Color: Black Category: Pullover Pattern: Solid Neck: Turtle neck Sleeves: Long sleeves Length: Regular H... |
| 12 | no | 10714640 | - | 0.680 | brand=Taanz, color=Black, category=Pullover, occasion=Casual, price=1499.0 | Product: Taanz Women Black Solid Sweatshirt Brand: Taanz Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Straight ... |
| 13 | no | 14512956 | - | 0.676 | brand=Powerpuff Girls by Kook N Keech, color=Black, category=Pullover, occasion=Casual, price=1899.0 | Product: Powerpuff Girls by Kook N Keech Women Black Solid Sweatshirt Brand: Powerpuff Girls by Kook N Keech Color: Black Category: Pullover Pattern: Solid Neck: Round neck Slee... |
| 14 | no | 15870014 | - | 0.667 | brand=New Balance, color=Black, category=Pullover, occasion=Casual, price=3999.0 | Product: New Balance Women Black Sweatshirt Brand: New Balance Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Str... |
| 15 | no | 14080668 | - | 0.663 | brand=DressBerry, color=Black, category=Pullover, occasion=Casual, price=1849.0 | Product: DressBerry Women Black Solid Sweatshirt Brand: DressBerry Color: Black Category: Pullover Pattern: Solid Neck: Mock collar Sleeves: Long sleeves Length: Regular Hemline... |
| 16 | yes | 15198584 | - | 0.663 | brand=H&M, color=Black, category=Pullover, occasion=Casual, price=799.0 | Product: H&M Women Black Sweatshirt Brand: H&M Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Ribbed Top fabric: ... |
| 17 | no | 10611428 | - | 0.660 | brand=Alsace Lorraine Paris, color=Black, category=Pullover, occasion=Casual, price=1499.0 | Product: Alsace Lorraine Paris Women Black Solid Hooded Sweatshirt Brand: Alsace Lorraine Paris Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves L... |
| 18 | no | 19269372 | - | 0.653 | brand=BoStreet, color=Black, category=Pullover, occasion=Casual, price=2599.0 | Product: BoStreet Women Black Colourblocked Long Sleeves Sweatshirts Brand: BoStreet Color: Black Category: Pullover Pattern: Solid colourblocked Neck: Hood Sleeves: Long sleeve... |
| 19 | no | 10683730 | - | 0.648 | brand=STREET 9, color=Black, category=Pullover, occasion=Casual, price=2399.0 | Product: STREET 9 Women Black Solid Sweater Brand: STREET 9 Color: Black Category: Pullover Pattern: Solid Neck: Turtle neck Sleeves: Long sleeves Hemline: Straight Top fabric: ... |
| 20 | no | 13615048 | - | 0.638 | brand=Flying Machine, color=Black, category=Pullover, occasion=Casual, price=2099.0 | Product: Flying Machine Women Black Solid Sweatshirt Brand: Flying Machine Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemlin... |
| 21 | no | 10791506 | - | 0.612 | brand=The Vanca, color=Black, category=Pullover, occasion=Casual, price=1499.0 | Product: The Vanca Women Black & Navy Blue Solid Longline Pullover Sweatshirt Brand: The Vanca Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Three-qua... |
| 22 | yes | 15964092 | - | 0.594 | brand=MANGO, color=Black, category=Pullover, occasion=Casual, price=2990.0 | Product: MANGO Women Black Solid Pullover Brand: MANGO Color: Black Category: Pullover Pattern: Solid Neck: Boat neck Sleeves: Long sleeves Length: Regular Hemline: Ribbed Top f... |
| 23 | no | 16533910 | - | 0.587 | brand=RAREISM, color=Black, category=Pullover, occasion=Casual, price=3299.0 | Product: RAREISM Women Black Hooded Sweatshirt Brand: RAREISM Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: Straight T... |
| 24 | no | 18004440 | - | 0.584 | brand=Aeropostale, color=Black, category=Pullover, occasion=Casual, price=2499.0 | Product: Aeropostale Women Black Printed Hooded Sweatshirt Brand: Aeropostale Color: Black Category: Pullover Pattern: Typography printed Neck: Hood Sleeves: Long sleeves Length... |
| 25 | no | 11109236 | - | 0.584 | brand=DOLCE CRUDO, color=Black, category=Pullover, occasion=Casual, price=2299.0 | Product: DOLCE CRUDO Women Black Solid Hooded Sweatshirt Brand: DOLCE CRUDO Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemli... |
| 26 | yes | 15963804 | - | 0.582 | brand=MANGO, color=Black, category=Pullover, occasion=Casual, price=2990.0 | Product: MANGO Women Black Solid Pullover Sweater Brand: MANGO Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Rib... |
| 27 | no | 13593756 | - | 0.572 | brand=BEVERLY BLUES, color=Black, category=Pullover, occasion=Casual, price=1599.0 | Product: BEVERLY BLUES Women Black Solid Sweatshirt Brand: BEVERLY BLUES Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Crop Hemli... |
| 28 | no | 16583226 | - | 0.558 | brand=20Dresses, color=Black, category=Pullover, occasion=Casual, price=1795.0 | Product: 20Dresses Women Black Plus Size Cotton Sweatshirt Brand: 20Dresses Color: Black Category: Pullover Pattern: Solid Neck: High neck Sleeves: Long sleeves Length: Regular ... |
| 29 | no | 10747958 | - | 0.555 | brand=Alsace Lorraine Paris, color=Black, category=Pullover, occasion=Casual, price=1899.0 | Product: Alsace Lorraine Paris Women Black & Yellow Solid Cropped Hooded Sweatshirt Brand: Alsace Lorraine Paris Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeve... |
| 30 | no | 18144562 | - | 0.553 | brand=Marks & Spencer, color=Black, category=Pullover, occasion=Outdoor, price=4999.0 | Product: Marks & Spencer Women Black Sherpa Sweatshirt Brand: Marks & Spencer Color: Black Category: Pullover Pattern: Solid Neck: Shirt collar Sleeves: Long sleeves Length: Reg... |

### Question 42/50

**Query:** I'm looking for Dress that cost no more than 5300.

**Retrieval metadata:** price <= 5300.0

**Relevant docs:** `['13878542', '17705690', '18365368', '16921564', '16921510', '16921508', '16921524', '16921550']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 17403640 | - | 0.500 | brand=I Saw It First, color=Khaki, occasion=Casual, price=3199.0 | Product: I Saw It First Women Khaki Crinkled Tie-Up Shrug Brand: I Saw It First Color: Khaki Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: P... |
| 2 | no | 13843640 | - | 0.500 | brand=Stylee LIFESTYLE, color=Navy Blue, category=Dress, occasion=Festive, price=23849.0 | Product: Stylee LIFESTYLE Navy Blue & Gold-Toned Velvet Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Navy Blue Category: Dress Pattern: Ethnic motifs Bottom fabri... |
| 3 | no | 17403254 | - | 0.486 | brand=I Saw It First, color=Blue, occasion=Casual, price=4099.0 | Product: I Saw It First Women Blue Skinny Fit Stretchable Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machi... |
| 4 | no | 13452734 | - | 0.484 | brand=I AM FOR YOU, color=Green, occasion=Western, price=2299.0 | Product: I AM FOR YOU Women Green & Grey Printed Flared Palazzos Brand: I AM FOR YOU Color: Green Pattern: Abstract printed Length: Regular Top fabric: Viscose rayon Occasion: W... |
| 5 | no | 17403434 | - | 0.478 | brand=I Saw It First, color=White, category=Playsuit, occasion=Casual, price=3199.0 | Product: I Saw It First Women White & Blue Floral Printed Skort Playsuit Brand: I Saw It First Color: White Category: Playsuit Pattern: Printed Neck: Round neck Sleeves: Short s... |
| 6 | no | 17365722 | - | 0.475 | brand=I Saw It First, color=Beige, category=Regular shorts, occasion=Casual, price=1999.0 | Product: I Saw It First Women Beige Striped High-Rise Shorts Brand: I Saw It First Color: Beige Category: Regular shorts Pattern: Striped Length: Above knee Top fabric: Polyeste... |
| 7 | no | 17403428 | - | 0.473 | brand=I Saw It First, color=Blue, occasion=Casual, price=3799.0 | Product: I Saw It First Women Blue Skinny Fit Highly Distressed Light Fade Stretchable Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casua... |
| 8 | no | 14159320 | - | 0.468 | brand=I AM FOR YOU, color=Yellow, category=A-line, occasion=Casual, price=1699.0 | Product: I AM FOR YOU Women Yellow & White Embroidered Detail A-Line Skirt with Gathers Brand: I AM FOR YOU Color: Yellow Category: A-line Pattern: Solid Length: Mini Hemline: F... |
| 9 | no | 17403380 | - | 0.467 | brand=I Saw It First, color=Blue, occasion=Casual, price=2899.0 | Product: I Saw It First Women Blue Slash Knee Frayed Hem Mom Fit Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care... |
| 10 | no | 17403300 | - | 0.464 | brand=I Saw It First, color=Blue, occasion=Casual, price=4299.0 | Product: I Saw It First Women Blue Light Fade Mid Wash High Rise Skinny Fit Stretchable Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casu... |
| 11 | no | 17365728 | - | 0.461 | brand=I Saw It First, color=Pink, category=Flared, occasion=Casual, price=1499.0 | Product: I Saw It First Women Dusty Pink & White Striped Pleated Mini Skater Skirt Brand: I Saw It First Color: Pink Category: Flared Pattern: Striped Length: Mini Hemline: Flar... |
| 12 | no | 17365720 | - | 0.454 | brand=I Saw It First, color=Green, category=Flared, occasion=Casual, price=1899.0 | Product: I Saw It First Women Green Solid Pleated Mini Side Split Skater Skirt Brand: I Saw It First Color: Green Category: Flared Pattern: Solid Length: Mini Hemline: Flared To... |
| 13 | no | 17136852 | - | 0.432 | brand=Readiprint Fashions, color=Blue, occasion=Festive, price=5300.0 | Product: Readiprint Fashions Blue & Silver Embroidered Unstitched Kurta Set Material Brand: Readiprint Fashions Color: Blue Pattern: Floral Bottom fabric: Shantoon Dupatta fabri... |
| 14 | no | 18750730 | - | 0.413 | brand=Stylee LIFESTYLE, color=Olive, category=Dress, occasion=Festive, price=6899.0 | Product: Stylee LIFESTYLE Olive Green & Red Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Olive Category: Dress Pattern: Other Bottom fabric: Silk blend Dupatta fabri... |
| 15 | no | 19392350 | - | 0.400 | brand=Ethnic Yard, color=Green, category=Dress, occasion=Festive, price=3699.0 | Product: Ethnic Yard Green & Grey Embroidered Semi-Stitched Dress Material Brand: Ethnic Yard Color: Green Category: Dress Pattern: Ethnic motifs Occasion: Festive Wash care: Dr... |
| 16 | no | 17287376 | - | 0.392 | brand=Stylee LIFESTYLE, color=Yellow, category=Dress, occasion=Festive, price=15099.0 | Product: Stylee LIFESTYLE Yellow & Gold-Toned Embellished Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Yellow Category: Dress Pattern: Ethnic motifs Bottom fabric: P... |
| 17 | no | 18766164 | - | 0.370 | brand=Stylee LIFESTYLE, color=Black, category=Dress, occasion=Festive, price=10149.0 | Product: Stylee LIFESTYLE Black & Gold-Toned Pure Silk Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Black Category: Dress Pattern: Floral Bottom fabric: Pure silk Du... |
| 18 | no | 17570416 | - | 0.368 | brand=SHOWOFF, color=Black, occasion=Casual, price=4220.0 | Product: SHOWOFF Women Black Straight Fit Stretchable Jeans Brand: SHOWOFF Color: Black Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 6 and more Wash care: Dry ... |
| 19 | no | 19097390 | - | 0.359 | brand=I Love She, color=White, category=Regular trousers, occasion=Casual, price=2399.0 | Product: I Love She Women White Relaxed High-Rise Trousers Brand: I Love She Color: White Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: ... |
| 20 | no | 18245104 | - | 0.356 | brand=Miss Chase, color=Blue, occasion=Casual, price=3195.0 | Product: Miss Chase Women Blue Jogger High-Rise Cuffed Hem Stretchable Jeans Brand: Miss Chase Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 6 and mor... |
| 21 | no | 18142614 | - | 0.356 | brand=SHOWOFF, color=Lavender, occasion=Casual, price=4655.0 | Product: SHOWOFF Women Lavender Jogger High-Rise Cuffed Hem Stretchable Jeans Brand: SHOWOFF Color: Lavender Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 6 and... |
| 22 | no | 14925780 | - | 0.354 | brand=Roadster, color=Blue, occasion=Casual, price=2299.0 | Product: Roadster Women Blue Wide Leg Stretchable Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 and more Wash care: Machine wash |
| 23 | no | 19396408 | - | 0.348 | brand=Stylee LIFESTYLE, color=Beige, category=Dress, occasion=Festive, price=12949.0 | Product: Stylee LIFESTYLE Womens Beige Embroidered Pure Silk Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Beige Category: Dress Pattern: Striped Bottom fabric: Pure ... |
| 24 | no | 12629360 | - | 0.348 | brand=Roadster, color=Rust, occasion=Casual, price=2099.0 | Product: Roadster Women Rust Red Regular Fit Mid-Rise Clean Look Cargo Joggers Jeans Brand: Roadster Color: Rust Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 a... |
| 25 | no | 18245110 | - | 0.348 | brand=Miss Chase, color=Blue, occasion=Casual, price=3195.0 | Product: Miss Chase Women Blue High-Rise Mildly Distressed Stretchable Jeans Brand: Miss Chase Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 and mor... |
| 26 | no | 19097392 | - | 0.343 | brand=I Love She, color=Maroon, category=Regular trousers, occasion=Casual, price=1399.0 | Product: I Love She Women Maroon Relaxed Skinny Fit High-Rise Trousers Brand: I Love She Color: Maroon Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Poly... |
| 27 | no | 14954878 | - | 0.343 | brand=Roadster, color=Charcoal, occasion=Casual, price=2599.0 | Product: Roadster Women Charcoal Mid-Rise Straight Fit Jeans Brand: Roadster Color: Charcoal Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 and more Wash care: M... |
| 28 | no | 11284776 | - | 0.339 | brand=Mast & Harbour, color=Blue, occasion=Casual, price=2299.0 | Product: Mast & Harbour Women Blue Mid-Rise Clean Look Cargo Jogger Jeans Brand: Mast & Harbour Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 and mo... |
| 29 | no | 17570328 | - | 0.338 | brand=SHOWOFF, color=Blue, occasion=Casual, price=4845.0 | Product: SHOWOFF Women Blue Wide Leg High-Rise Low Distress Heavy Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Pockets... |
| 30 | no | 16533888 | - | 0.335 | brand=Ethnic Junction, color=Navy Blue, category=Dress, occasion=Festive, price=3596.0 | Product: Ethnic Junction Navy Blue & Gold-Toned Embroidered Unstitched Dress Material Brand: Ethnic Junction Color: Navy Blue Category: Dress Pattern: Floral Bottom fabric: Shan... |

### Question 43/50

**Query:** I'm looking for something Pink from Mitera for a traditional occasion.

**Retrieval metadata:** brand == Mitera, color == Pink, occasion == Traditional

**Relevant docs:** `['15012182', '11454958', '11244988', '18302880']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.571 | 1.000 | 0.333 | 0.653 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 13886174 | - | 1.000 | brand=Mitera, color=Pink, category=Taant, occasion=Traditional, price=4999.0 | Product: Mitera Pink & White Pure Cotton Woven Design Taant Saree Brand: Mitera Color: Pink Category: Taant Pattern: Woven design Occasion: Traditional Wash care: Dry clean |
| 2 | no | 11218670 | - | 0.787 | brand=Mitera, color=Pink, category=Kanjeevaram, occasion=Traditional, price=4999.0 | Product: Mitera Pink & Gold-Toned Silk Blend Woven Design Kanjeevaram Saree Brand: Mitera Color: Pink Category: Kanjeevaram Pattern: Woven design Occasion: Traditional Wash care... |
| 3 | yes | 11244988 | - | 0.528 | brand=Mitera, color=Pink, category=Kanjeevaram, occasion=Traditional, price=3999.0 | Product: Mitera Pink & Gold-Toned Silk Blend Woven Design Kanjeevaram Saree Brand: Mitera Color: Pink Category: Kanjeevaram Pattern: Ethnic motifs woven design Occasion: Traditi... |
| 4 | yes | 18302880 | - | 0.457 | brand=Mitera, color=Pink, category=Kanjeevaram, occasion=Traditional, price=8699.0 | Product: Mitera Pink & Gold-Toned Woven Design Zari Silk Blend Kanjeevaram Saree Brand: Mitera Color: Pink Category: Kanjeevaram Pattern: Woven design Occasion: Traditional Wash... |
| 5 | yes | 11454958 | - | 0.368 | brand=Mitera, color=Pink, category=Banarasi, occasion=Traditional, price=3299.0 | Product: Mitera Pink & Golden Woven Design Banarasi Saree Brand: Mitera Color: Pink Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Traditional Wash care: Dry c... |
| 6 | yes | 15012182 | - | 0.301 | brand=Mitera, color=Pink, category=Banarasi, occasion=Traditional, price=5199.0 | Product: Mitera Pink & Silver-Toned Paisley Zari Silk Blend Banarasi Saree Brand: Mitera Color: Pink Category: Banarasi Pattern: Paisley woven design Occasion: Traditional Wash ... |
| 7 | no | 14850332 | - | 0.108 | brand=Mitera, color=Pink, category=Banarasi, occasion=Traditional, price=5199.0 | Product: Mitera Pink & Gold-Toned Woven Design Silk Blend Banarasi Saree Brand: Mitera Color: Pink Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Traditional W... |

### Question 44/50

**Query:** I'm looking for Pullover from max for everyday wear under 600.

**Retrieval metadata:** brand == max, occasion == Daily, price <= 600.0

**Relevant docs:** `['19204850', '15878996', '16156132']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 18782340 | - | 0.905 | brand=max, color=Brown, occasion=Daily, price=599.0 | Product: max Women Brown Kurta Brand: max Color: Brown Pattern: Striped solid Shape: Straight Neck: Shirt collar Sleeves: Three-quarter regular sleeves Length: Ankle length Heml... |
| 2 | no | 19240558 | - | 0.888 | brand=max, color=Rust, occasion=Daily, price=599.0 | Product: max Women Rust Kurta Brand: max Color: Rust Pattern: Striped woven design Shape: Straight Neck: Mandarin collar Sleeves: Long regular sleeves Length: Calf length Hemlin... |
| 3 | no | 17748850 | - | 0.707 | brand=max, color=Black, occasion=Daily, price=399.0 | Product: max Black Pure Cotton Dupatta Brand: max Color: Black Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash |
| 4 | no | 18782346 | - | 0.657 | brand=max, color=Blue, occasion=Daily, price=499.0 | Product: max Women Blue Paisley Kurta Brand: max Color: Blue Pattern: Paisley solid Shape: Straight Neck: V-neck Sleeves: Three-quarter regular sleeves Length: Above knee Hemlin... |
| 5 | no | 16464196 | - | 0.632 | brand=max, color=Black, occasion=Daily, price=399.0 | Product: max Black Solid Dupatta Brand: max Color: Black Pattern: Solid Top fabric: Viscose rayon Occasion: Daily Wash care: Hand wash |
| 6 | no | 19240492 | - | 0.617 | brand=max, color=Blue, occasion=Daily, price=599.0 | Product: max Women Blue Yoke Design Kurta Brand: max Color: Blue Pattern: Solid yoke design Shape: A-line Neck: Round neck Sleeves: Three-quarter regular sleeves Length: Calf le... |
| 7 | no | 15266700 | - | 0.609 | brand=max, color=Beige, occasion=Daily, price=299.0 | Product: max Beige Pure Cotton Dupatta Brand: max Color: Beige Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash |
| 8 | no | 19240508 | - | 0.590 | brand=max, color=Mustard, occasion=Daily, price=599.0 | Product: max Women Mustard Yellow Yoke Design Thread Work Kurta Brand: max Color: Mustard Pattern: Solid yoke design Shape: Straight Neck: Mandarin collar Sleeves: Three-quarter... |
| 9 | no | 15119222 | - | 0.590 | brand=max, color=Red, occasion=Daily, price=499.0 | Product: max Women Red Ethnic Motifs Printed Kurta Brand: max Color: Red Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck Sleeves: Three-quarter regular sleeves L... |
| 10 | no | 19068142 | - | 0.580 | brand=max, color=Blue, occasion=Daily, price=1199.0 | Product: max Women Blue Floral Printed Flared Sleeves Kurta Brand: max Color: Blue Pattern: Floral printed Shape: A-line Neck: Keyhole neck Sleeves: Three-quarter flared sleeves... |
| 11 | no | 15119204 | - | 0.560 | brand=max, color=Black, occasion=Daily, price=599.0 | Product: max Women Black Ethnic Motifs Yoke Design Mirror Work Kurta Brand: max Color: Black Pattern: Ethnic motifs yoke design Shape: A-line Neck: Boat neck Sleeves: Three-quar... |
| 12 | no | 19069132 | - | 0.558 | brand=max, color=Yellow, occasion=Daily, price=699.0 | Product: max Yellow & Silver-Toned Embroidered Dupatta Brand: max Color: Yellow Pattern: Floral embroidered Top fabric: Poly crepe Occasion: Daily Wash care: Machine wash |
| 13 | no | 15266776 | - | 0.540 | brand=max, color=Navy Blue, occasion=Daily, price=299.0 | Product: max Navy Blue Pure Cotton Dupatta with Tasselled Border Brand: max Color: Navy Blue Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash |
| 14 | no | 19240582 | - | 0.527 | brand=max, color=Green, occasion=Daily, price=599.0 | Product: max Women Green Flared Sleeves Kurta Brand: max Color: Green Pattern: Striped woven design Shape: A-line Neck: Boat neck Sleeves: Three-quarter flared sleeves Length: C... |
| 15 | no | 17469612 | - | 0.526 | brand=max, color=Maroon, occasion=Daily, price=599.0 | Product: max Women Maroon Floral Embroidered Kurta Brand: max Color: Maroon Pattern: Floral embroidered Shape: Straight Neck: Boat neck Sleeves: Three-quarter regular sleeves Le... |
| 16 | no | 15781530 | - | 0.520 | brand=max, color=Mustard, occasion=Daily, price=299.0 | Product: max Mustard Viscose Rayon Dupatta Brand: max Color: Mustard Pattern: Solid Top fabric: Viscose rayon Occasion: Daily Wash care: Machine wash |
| 17 | no | 19240524 | - | 0.513 | brand=max, color=Olive, occasion=Daily, price=599.0 | Product: max Women Olive Green Geometric Printed Kurta Brand: max Color: Olive Pattern: Geometric printed Shape: Straight Neck: Round neck Sleeves: Three-quarter regular sleeves... |
| 18 | no | 15266714 | - | 0.503 | brand=max, color=Coral, occasion=Daily, price=299.0 | Product: max Coral Pure Cotton Dupatta Brand: max Color: Coral Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash |
| 19 | no | 18782350 | - | 0.499 | brand=max, color=Fuchsia, occasion=Daily, price=499.0 | Product: max Women Fuchsia Kurta Brand: max Color: Fuchsia Pattern: Ethnic motifs woven design Shape: Straight Neck: Boat neck Sleeves: Three-quarter regular sleeves Length: Cal... |
| 20 | no | 19068162 | - | 0.467 | brand=max, color=Rust, occasion=Daily, price=599.0 | Product: max Women Rust Ethnic Motifs Printed Kurta Brand: max Color: Rust Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck Sleeves: Three-quarter regular sleeves... |
| 21 | no | 15781516 | - | 0.462 | brand=max, color=Green, occasion=Daily, price=299.0 | Product: max Green Viscose Rayon Solid Dupatta Brand: max Color: Green Pattern: Solid Top fabric: Viscose rayon Occasion: Daily Wash care: Machine wash |
| 22 | no | 15266736 | - | 0.456 | brand=max, color=Blue, occasion=Daily, price=299.0 | Product: max Blue Pure Cotton Dupatta with Tasselled Border Brand: max Color: Blue Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash |
| 23 | no | 19240544 | - | 0.438 | brand=max, color=Green, occasion=Daily, price=1499.0 | Product: max Women Green Geometric Embroidered Flared Sleeves Thread Work Anarkali Kurta Brand: max Color: Green Pattern: Geometric embroidered Shape: Anarkali Neck: Mandarin co... |
| 24 | no | 19240516 | - | 0.395 | brand=max, color=Fuchsia, occasion=Daily, price=599.0 | Product: max Women Fuchsia Ethnic Motifs Kurta Brand: max Color: Fuchsia Pattern: Ethnic motifs solid Shape: A-line Neck: Round neck Sleeves: Three-quarter regular sleeves Lengt... |
| 25 | no | 19068150 | - | 0.388 | brand=max, color=Green, occasion=Daily, price=599.0 | Product: max Women Green Keyhole Neck Thread Work Kurta Brand: max Color: Green Pattern: Solid Shape: A-line Neck: Keyhole neck Sleeves: Three-quarter regular sleeves Length: Kn... |
| 26 | no | 15266716 | - | 0.384 | brand=max, color=Red, occasion=Daily, price=399.0 | Product: max Red Dupatta with Tasseled Border Brand: max Color: Red Pattern: Solid Top fabric: Viscose rayon Occasion: Daily Wash care: Machine wash |
| 27 | no | 14443728 | - | 0.346 | brand=max, color=Orange, occasion=Daily, price=399.0 | Product: max Orange Dupatta with Beads and Stones Brand: max Color: Orange Pattern: Solid Top fabric: Poly chiffon Occasion: Daily Wash care: Hand wash |
| 28 | no | 19241696 | - | 0.333 | brand=max, color=Blue, category=Kurti, occasion=Daily, price=999.0 | Product: max Women Blue Printed Kurti with Palazzos Brand: max Color: Blue Category: Kurti Top type: Kurti Bottom type: Palazzos Pattern: Geometric printed Shape: A-line Neck: V... |
| 29 | no | 16228478 | - | 0.077 | brand=max, color=Green, occasion=Daily, price=499.0 | Product: max Green Geometric Embroidered Thread Work Thread Work Empire Kurti Brand: max Color: Green Pattern: Geometric embroidered Shape: A-line Neck: Round neck Sleeves: Thre... |

### Question 45/50

**Query:** What do you have from Roadster in products and color Navy Blue?

**Retrieval metadata:** brand == Roadster, color == Navy Blue

**Relevant docs:** `['12278640', '11987092', '8803831', '8963467', '12278652', '14094106', '16187090', '15897498']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.333 | 1.000 | 1.000 | 0.778 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 14094106 | - | 0.966 | brand=Roadster, color=Navy Blue, occasion=Casual, price=2499.0 | Product: Roadster Women Deep Navy Blue High-Rise Regular Fit Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 4 Wa... |
| 2 | no | 5447351 | - | 0.890 | brand=Roadster, color=Navy Blue, category=Cardigan, occasion=Casual, price=1499.0 | Product: Roadster Women Navy Blue Striped Cardigan Brand: Roadster Color: Navy Blue Category: Cardigan Pattern: Striped Neck: Round neck Sleeves: Long sleeves Hemline: Ribbed To... |
| 3 | yes | 12278640 | - | 0.831 | brand=Roadster, color=Navy Blue, occasion=Casual, price=2499.0 | Product: Roadster Women Navy Blue Flared Fit High-Rise Clean Look Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets:... |
| 4 | no | 11296068 | - | 0.826 | brand=Roadster, color=Navy Blue, category=Regular, occasion=Casual, price=899.0 | Product: Roadster Women Navy Blue Solid Bell Sleeves Top Brand: Roadster Color: Navy Blue Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short bell sleeves Length: R... |
| 5 | no | 13700180 | - | 0.762 | brand=Roadster, color=Navy Blue, category=Straight, occasion=Casual, price=2599.0 | Product: Roadster Women Navy Blue Solid Straight Fit Skirt Brand: Roadster Color: Navy Blue Category: Straight Pattern: Solid Length: Knee length Hemline: Straight Top fabric: P... |
| 6 | no | 14331672 | - | 0.685 | brand=Roadster, color=Navy Blue, category=Pullover, occasion=Casual, price=1299.0 | Product: Roadster Women Navy Blue & Pink Striped Pullover Brand: Roadster Color: Navy Blue Category: Pullover Pattern: Striped Neck: Turtle neck Sleeves: Long sleeves Length: Re... |
| 7 | no | 14094050 | - | 0.682 | brand=Roadster, color=Navy Blue, occasion=Casual, price=2099.0 | Product: Roadster Women Deep Navy Blue High-Rise Straight Cropped Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets:... |
| 8 | yes | 12278652 | - | 0.635 | brand=Roadster, color=Navy Blue, occasion=Casual, price=2099.0 | Product: Roadster Women Navy Blue Bootcut Mid-Rise Clean Look Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 W... |
| 9 | no | 14535816 | - | 0.628 | brand=Roadster, color=Navy Blue, category=Denim jacket, occasion=Casual, price=2799.0 | Product: Roadster Women Pure Cotton Navy Blue Denim Jacket Brand: Roadster Color: Navy Blue Category: Denim jacket Pattern: Geometric self design Sleeves: Long sleeves Length: R... |
| 10 | yes | 16187090 | - | 0.619 | brand=Roadster, color=Navy Blue, occasion=Casual, price=2499.0 | Product: The Roadster Lifestyle Co Women Navy Blue Straight Fit High-Rise Light Fade Cotton Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: C... |
| 11 | no | 17074032 | - | 0.598 | brand=Roadster, color=Navy Blue, category=Regular, occasion=Casual, price=1499.0 | Product: Roadster Women Navy Blue & White Striped High Neck Regular Top Brand: Roadster Color: Navy Blue Category: Regular Pattern: Horizontal stripes striped Neck: High neck Sl... |
| 12 | no | 14356168 | - | 0.571 | brand=Roadster, color=Navy Blue, category=Padded jacket, occasion=Casual, price=2999.0 | Product: Roadster Women Navy Blue & Maroon Colourblocked Padded Jacket Brand: Roadster Color: Navy Blue Category: Padded jacket Pattern: Colourblocked Sleeves: Long sleeves Leng... |
| 13 | yes | 15897498 | - | 0.550 | brand=Roadster, color=Navy Blue, occasion=Casual, price=2599.0 | Product: The Roadster Lifestyle Co Women Navy Blue Cotton Wide Leg High-Rise Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: ... |
| 14 | no | 14356146 | - | 0.548 | brand=Roadster, color=Navy Blue, category=Tailored jacket, occasion=Casual, price=4999.0 | Product: Roadster Women Navy Blue Convertible Tailored Jacket Brand: Roadster Color: Navy Blue Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hem... |
| 15 | yes | 8963467 | - | 0.545 | brand=Roadster, color=Navy Blue, occasion=Casual, price=1999.0 | Product: The Roadster Lifestyle Co Women Navy Blue Skinny Fit Mid-Rise Mildly Distressed Stretchable Cropped Jeans Brand: Roadster Color: Navy Blue Length: Cropped Top fabric: C... |
| 16 | no | 14925764 | - | 0.532 | brand=Roadster, color=Navy Blue, occasion=Casual, price=1499.0 | Product: Roadster Women Navy Blue Pure Cotton Jogger Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 2 Wash care:... |
| 17 | yes | 11987092 | - | 0.532 | brand=Roadster, color=Navy Blue, occasion=Casual, price=1299.0 | Product: Roadster Women Navy Blue & Green Checked Open Front Shrug Brand: Roadster Color: Navy Blue Pattern: Checked Sleeves: Three-quarter sleeves Length: Regular Hemline: Stra... |
| 18 | no | 15088232 | - | 0.496 | brand=Roadster, color=Navy Blue, category=Sweatshirt, occasion=Casual, price=3199.0 | Product: Roadster Women Navy Blue Solid Half-Zipper Sweatshirt with Joggers Brand: Roadster Color: Navy Blue Category: Sweatshirt Top type: Sweatshirt Bottom type: Joggers Patte... |
| 19 | no | 11688510 | - | 0.491 | brand=Roadster, color=Navy Blue, category=Denim shorts, occasion=Casual, price=1399.0 | Product: Roadster Women Navy Blue Washed Regular Fit Denim Shorts Brand: Roadster Color: Navy Blue Category: Denim shorts Pattern: Washed Length: Above knee Top fabric: Cotton O... |
| 20 | no | 14356150 | - | 0.459 | brand=Roadster, color=Navy Blue, category=Bomber, occasion=Casual, price=3999.0 | Product: Roadster Women Navy Blue Grey Striped Bomber Jacket Brand: Roadster Color: Navy Blue Category: Bomber Pattern: Striped Sleeves: Long sleeves Length: Regular Hemline: St... |
| 21 | no | 14535784 | - | 0.324 | brand=Roadster, color=Navy Blue, category=Denim jacket, occasion=Casual, price=3699.0 | Product: Roadster Women Deep Navy Blue Solid Denim Trucker Jacket Brand: Roadster Color: Navy Blue Category: Denim jacket Pattern: Solid Sleeves: Long sleeves Length: Regular He... |
| 22 | no | 16833828 | - | 0.296 | brand=Roadster, color=Navy Blue, category=Top, occasion=Casual, price=1799.0 | Product: The Roadster Lifestyle Co Women Navy Blue Self Design Co-Ord Set Brand: Roadster Color: Navy Blue Category: Top Top type: Top Bottom type: Shorts Pattern: Self design N... |
| 23 | yes | 8803831 | - | 0.241 | brand=Roadster, color=Navy Blue, occasion=Casual, price=1699.0 | Product: Roadster Women Navy Blue Skinny Fit Mid-Rise Clean Look Stretchable Cropped Jeans Brand: Roadster Color: Navy Blue Length: Cropped Top fabric: Cotton Occasion: Casual P... |
| 24 | no | 13756790 | - | 0.235 | brand=Roadster, color=Navy Blue, category=Denim shorts, occasion=Casual, price=2499.0 | Product: Roadster X DISCOVERY ADVENTURES Women Navy Blue Denim Shorts Brand: Roadster Color: Navy Blue Category: Denim shorts Pattern: Solid Length: Above knee Top fabric: Cotto... |

### Question 46/50

**Query:** Show me Orange Saree from KALINI.

**Retrieval metadata:** brand == KALINI, color == Orange

**Relevant docs:** `['14490860']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.333 | 1.000 | 0.500 | 0.631 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | no | 14541316 | - | 0.966 | brand=KALINI, color=Orange, category=Saree, occasion=Festive, price=3999.0 | Product: KALINI Orange & Gold-Toned Ethnic Motifs Art Silk Saree Brand: KALINI Color: Orange Category: Saree Pattern: Ethnic motifs woven design Occasion: Festive Wash care: Han... |
| 2 | yes | 14490860 | - | 0.827 | brand=KALINI, color=Orange, category=Saree, occasion=Daily, price=1659.0 | Product: KALINI Orange & Gold-Toned Pure Chiffon Saree Brand: KALINI Color: Orange Category: Saree Pattern: Solid Occasion: Daily Wash care: Hand wash |
| 3 | no | 18390376 | - | 0.000 | brand=KALINI, color=Orange, category=Kurta set, occasion=Daily, price=3000.0 | Product: KALINI Women Orange Printed Pure Cotton Kurta with Trouser & With Dupatta Brand: KALINI Color: Orange Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta:... |

### Question 47/50

**Query:** Do you have any Black Tailored jacket for sports?

**Retrieval metadata:** color == Black, occasion == Sports

**Relevant docs:** `['14646546']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.033 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 14646546 | - | 1.000 | brand=HRX by Hrithik Roshan, color=Black, category=Tailored jacket, occasion=Sports, price=3999.0 | Product: HRX By Hrithik Roshan Outdoor Women Winter Moss Rapid-Dry Colourblock Jackets Brand: HRX by Hrithik Roshan Color: Black Category: Tailored jacket Pattern: Colourblocked... |
| 2 | no | 11383846 | - | 0.800 | brand=Alcis, color=Black, category=Sporty jacket, occasion=Sports, price=3999.0 | Product: Alcis Nari Women Black Solid Lightweight Sporty Jacket Brand: Alcis Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: S... |
| 3 | no | 15789142 | - | 0.735 | brand=Slazenger, color=Black, category=Sporty jacket, occasion=Sports, price=2499.0 | Product: Slazenger Women Black Running Sporty Rapid-Dry Jacket Brand: Slazenger Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline... |
| 4 | no | 15953824 | - | 0.707 | brand=Columbia, color=Black, category=Padded jacket, occasion=Sports, price=13999.0 | Product: Columbia Women Black Joy Peak Mid Hooded Reflective Stripe Padded Jacket Brand: Columbia Color: Black Category: Padded jacket Pattern: Solid Sleeves: Long sleeves Lengt... |
| 5 | no | 15743742 | - | 0.682 | brand=ADIDAS, color=Black, category=Sporty jacket, occasion=Sports, price=3999.0 | Product: ADIDAS Women Black Solid Essential Insulated Vest Sporty Jacket Brand: ADIDAS Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Sleeveless Length: Regular He... |
| 6 | no | 18144568 | - | 0.676 | brand=Marks & Spencer, color=Black, category=Padded jacket, occasion=Sports, price=3999.0 | Product: Marks & Spencer Women Black Padded Jacket Brand: Marks & Spencer Color: Black Category: Padded jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Stra... |
| 7 | no | 13609880 | - | 0.668 | brand=HRX by Hrithik Roshan, color=Black, category=Sporty jacket, occasion=Sports, price=3199.0 | Product: HRX by Hrithik Roshan Men Jet Black Solid Packable Rapid-Dry Hooded Running Jacket Brand: HRX by Hrithik Roshan Color: Black Category: Sporty jacket Pattern: Solid Slee... |
| 8 | no | 15389978 | - | 0.663 | brand=PERFKT-U, color=Black, category=Sporty jacket, occasion=Sports, price=2399.0 | Product: PERFKT-U Women Black & Mustard Yellow Colourblocked Lightweight Sporty Jacket Brand: PERFKT-U Color: Black Category: Sporty jacket Pattern: Colourblocked Sleeves: Long ... |
| 9 | no | 15963194 | - | 0.634 | brand=Columbia, color=Black, category=Sporty jacket, occasion=Sports, price=5999.0 | Product: Columbia Women Black Kruser Ridge II Softshell Sporty Jacket Brand: Columbia Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular H... |
| 10 | no | 15953844 | - | 0.628 | brand=Columbia, color=Black, category=Quilted jacket, occasion=Sports, price=7999.0 | Product: Columbia Women Black Delta Ridge Down Vest Reflective Stripe Quilted Jacket Brand: Columbia Color: Black Category: Quilted jacket Pattern: Solid Sleeves: Sleeveless Len... |
| 11 | no | 15953812 | - | 0.622 | brand=Columbia, color=Black, category=Quilted jacket, occasion=Sports, price=10999.0 | Product: Columbia Women Black Delta Ridge Down Hooded Insulator Quilted Jacket Brand: Columbia Color: Black Category: Quilted jacket Pattern: Solid Sleeves: Long sleeves Length:... |
| 12 | no | 14562576 | - | 0.595 | brand=HRX by Hrithik Roshan, color=Black, category=Sporty jacket, occasion=Sports, price=4599.0 | Product: HRX by Hrithik Roshan Women Black & White Printed Hooded Sporty Jacket Brand: HRX by Hrithik Roshan Color: Black Category: Sporty jacket Pattern: Graphic printed Sleeve... |
| 13 | no | 14968448 | - | 0.578 | brand=Chkokko, color=Black, category=Sporty jacket, occasion=Sports, price=2765.0 | Product: Chkokko Women Black & Red Gym Sporty Zipper Jacket Brand: Chkokko Color: Black Category: Sporty jacket Pattern: Colourblocked Sleeves: Long sleeves Length: Regular Heml... |
| 14 | no | 1753301 | - | 0.561 | brand=Amante, color=Black, category=Sports shorts, occasion=Sports, price=1495.0 | Product: Amante Women Black Sports Shorts Brand: Amante Color: Black Category: Sports shorts Pattern: Solid Length: Above knee Top fabric: Polyester Occasion: Sports Wash care: ... |
| 15 | no | 8386077 | - | 0.559 | brand=The Pink Moon, color=Black, category=Sporty jacket, occasion=Sports, price=2499.0 | Product: The Pink Moon Plus Size Women Black Solid Sporty Jacket Brand: The Pink Moon Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular H... |
| 16 | no | 16182100 | - | 0.423 | brand=Ajile by Pantaloons, color=Black, category=Sports shorts, occasion=Sports, price=699.0 | Product: Ajile by Pantaloons Women Black Pure Cotton Sports Shorts Brand: Ajile by Pantaloons Color: Black Category: Sports shorts Pattern: Solid Length: Above knee Top fabric: ... |
| 17 | no | 14704920 | - | 0.419 | brand=HRX by Hrithik Roshan, color=Black, category=Sports shorts, occasion=Sports, price=1299.0 | Product: HRX By Hrithik Roshan Lifestyle Women Jet Black Bio-Wash Solid Shorts Brand: HRX by Hrithik Roshan Color: Black Category: Sports shorts Pattern: Solid Length: Above kne... |
| 18 | no | 17750194 | - | 0.408 | brand=Jinfo, color=Black, category=Sports shorts, occasion=Sports, price=1198.0 | Product: Jinfo Women Black Cycling Sports Shorts Brand: Jinfo Color: Black Category: Sports shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Sports Wash car... |
| 19 | no | 17199012 | - | 0.398 | brand=JUMP USA, color=Black, category=Sports shorts, occasion=Sports, price=1299.0 | Product: JUMP USA Women Black Outdoor Sports Shorts with e-Dry Technology Brand: JUMP USA Color: Black Category: Sports shorts Pattern: Solid Length: Above knee Top fabric: Poly... |
| 20 | no | 17378518 | - | 0.360 | brand=HRX by Hrithik Roshan, color=Black, category=Sports shorts, occasion=Sports, price=1699.0 | Product: HRX By Hrithik Roshan Lifestyle Women Jet Black Bio-Wash Solid Shorts Brand: HRX by Hrithik Roshan Color: Black Category: Sports shorts Pattern: Striped Length: Above k... |
| 21 | no | 17760320 | - | 0.355 | brand=Jinfo, color=Black, category=Sports shorts, occasion=Sports, price=1797.0 | Product: Jinfo Women Black & White Set of 3 Solid Cycling Sports Shorts Brand: Jinfo Color: Black Category: Sports shorts Pattern: Solid Length: Above knee Top fabric: Cotton Oc... |
| 22 | no | 12940070 | - | 0.333 | brand=Revolution, color=Black, category=Sports shorts, occasion=Sports, price=1600.0 | Product: Revolution Women Plus Size Black Solid Pure Cotton Regular Fit Football Shorts Brand: Revolution Color: Black Category: Sports shorts Pattern: Solid Length: Above knee ... |
| 23 | no | 12865416 | - | 0.264 | brand=Chkokko, color=Black, category=Sports shorts, occasion=Sports, price=2665.0 | Product: Chkokko Women Black Side Panelled Regular Fit Double Layered Running Shorts Brand: Chkokko Color: Black Category: Sports shorts Pattern: Solid Length: Above knee Top fa... |
| 24 | no | 11687104 | - | 0.146 | brand=Besiva, color=Black, category=Top, occasion=Sports, price=3899.0 | Product: Besiva Women Black & Off-White Printed Top with Tights Brand: Besiva Color: Black Category: Top Top type: Top Bottom type: Leggings Pattern: Printed Neck: Round neck Sl... |
| 25 | no | 18750114 | - | 0.144 | brand=DeFacto, color=Black, category=Biker shorts, occasion=Sports, price=1299.0 | Product: DeFacto Women Black Skinny Fit Biker Shorts Brand: DeFacto Color: Black Category: Biker shorts Pattern: Solid Length: Above knee Top fabric: Polyester Occasion: Sports ... |
| 26 | no | 16960714 | - | 0.141 | brand=EVERDION, color=Black, category=Top, occasion=Sports, price=2399.0 | Product: EVERDION Women Black Top With Shorts Yoga Set Brand: EVERDION Color: Black Category: Top Top type: Top Bottom type: Shorts Pattern: Solid Neck: Scoop neck Sleeves: Shor... |
| 27 | no | 13695224 | - | 0.133 | brand=HRX by Hrithik Roshan, color=Black, category=Regular shorts, occasion=Sports, price=1899.0 | Product: HRX By Hrithik Roshan Women Jet Black AOP Regular Fit Bio-Wash Lifestyle Shorts Brand: HRX by Hrithik Roshan Color: Black Category: Regular shorts Pattern: Abstract pri... |
| 28 | no | 17760310 | - | 0.128 | brand=Jinfo, color=Black, category=Biker shorts, occasion=Sports, price=1797.0 | Product: Jinfo Women Black Solid Cycling Shorts Pack Of 3 Brand: Jinfo Color: Black Category: Biker shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Sports ... |
| 29 | no | 17760268 | - | 0.123 | brand=Jinfo, color=Black, category=Biker shorts, occasion=Sports, price=1797.0 | Product: Jinfo Women Black Solid Cycling Shorts Pack Of 3 Brand: Jinfo Color: Black Category: Biker shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Sports ... |
| 30 | no | 16995282 | - | 0.120 | brand=ADIDAS, color=Black, category=Regular shorts, occasion=Sports, price=2999.0 | Product: ADIDAS Women Black & Yellow Run Fast Flower Print Shorts Brand: ADIDAS Color: Black Category: Regular shorts Pattern: Floral printed Length: Above knee Top fabric: Poly... |

### Question 48/50

**Query:** Do you have anything from Roadster in Grey for everyday wear?

**Retrieval metadata:** brand == Roadster, color == Grey, occasion == Daily

**Relevant docs:** `['13756948', '8319213', '13339544', '14954872', '10388213', '16835166', '16835204', '16835178']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |

### Question 49/50

**Query:** I need Peplum with a Self design solid pattern in Blue.

**Retrieval metadata:** color == Blue

**Relevant docs:** `['16504028']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.033 | 1.000 | 1.000 | 1.000 | 0.500 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 16504028 | - | 0.848 | brand=ANVI Be Yourself, color=Blue, category=Peplum, occasion=Party, price=1998.0 | Product: ANVI Be Yourself Women Stunning Blue Self-Design Ruffled Skirt Brand: ANVI Be Yourself Color: Blue Category: Peplum Pattern: Self design solid Length: Mini Hemline: Asy... |
| 2 | no | 14641744 | - | 0.746 | brand=FabAlley, color=Blue, category=Peplum, occasion=Casual, price=1300.0 | Product: FabAlley Blue Puff Sleeve Chambray Peplum Top Brand: FabAlley Color: Blue Category: Peplum Pattern: Solid Neck: Round neck Sleeves: Short puff sleeves Length: Regular T... |
| 3 | no | 18514120 | - | 0.745 | brand=Paralians, color=Turquoise Blue, category=Peplum, occasion=Ethnic, price=999.0 | Product: Paralians Turquoise Blue Peplum Top Brand: Paralians Color: Turquoise Blue Category: Peplum Pattern: Ethnic motifs solid Neck: Round neck Sleeves: Three-quarter regular... |
| 4 | no | 11607414 | - | 0.665 | brand=Bhama Couture, color=Blue, category=Peplum, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Blue Printed Peplum Top Brand: Bhama Couture Color: Blue Category: Peplum Pattern: Abstract printed Neck: Round neck Sleeves: Short no sleeves Lengt... |
| 5 | no | 11607374 | - | 0.636 | brand=Bhama Couture, color=Blue, category=Peplum, occasion=Ethnic, price=1799.0 | Product: Bhama Couture Women Blue Printed Peplum Top Brand: Bhama Couture Color: Blue Category: Peplum Pattern: Floral printed Neck: V-neck Sleeves: Three-quarter regular sleeve... |
| 6 | no | 18805426 | - | 0.569 | brand=BoStreet, color=Blue, category=Peplum, occasion=Casual, price=1949.0 | Product: BoStreet Blue Checked Peplum Top Brand: BoStreet Color: Blue Category: Peplum Pattern: Checked Neck: Round neck Sleeves: Short regular sleeves Length: Regular Top fabri... |
| 7 | no | 17445656 | - | 0.516 | brand=Vishudh, color=Blue, category=Peplum, occasion=Ethnic, price=1299.0 | Product: Vishudh Blue Floral Print Peplum Top Brand: Vishudh Color: Blue Category: Peplum Pattern: Floral printed Neck: Round neck Sleeves: Three-quarter regular sleeves Length:... |
| 8 | no | 17872080 | - | 0.515 | brand=Taavi, color=Blue, category=Peplum, occasion=Casual, price=2299.0 | Product: Taavi Women Indigo & White Indigo Print Pure Cotton Casual Peplum Top Brand: Taavi Color: Blue Category: Peplum Pattern: Ethnic motifs printed Neck: Round neck Sleeves:... |
| 9 | no | 8715089 | - | 0.503 | brand=plusS, color=Blue, category=Peplum, occasion=Casual, price=1799.0 | Product: plusS Women Blue Printed Peplum Top Brand: plusS Color: Blue Category: Peplum Pattern: Floral printed Neck: V-neck Sleeves: Three-quarter regular sleeves Length: Regula... |
| 10 | no | 10783322 | - | 0.501 | brand=Sera, color=Navy Blue, category=Peplum, occasion=Ethnic, price=1294.0 | Product: Sera Women Navy Blue Printed Peplum Pure Cotton Top Brand: Sera Color: Navy Blue Category: Peplum Pattern: Floral printed Neck: Round neck Sleeves: Sleeveless no Length... |
| 11 | no | 14231406 | - | 0.444 | brand=all about you, color=Blue, category=Pullover, occasion=Casual, price=1899.0 | Product: all about you Women Blue Self-Design Pullover Brand: all about you Color: Blue Category: Pullover Pattern: Geometric self design Neck: Turtle neck Sleeves: Long sleeves... |
| 12 | no | 14867398 | - | 0.426 | brand=Janasya, color=Blue, category=Peplum, occasion=Ethnic, price=1599.0 | Product: Janasya Women Blue & White Floral Ruffles Peplum Top Brand: Janasya Color: Blue Category: Peplum Pattern: Floral printed Neck: Round neck Sleeves: Sleeveless no Length:... |
| 13 | no | 18604646 | - | 0.409 | brand=Zink London, color=Blue, category=A-line, occasion=Casual, price=1999.0 | Product: Zink London Women Blue Floral Lace Design Skirts Brand: Zink London Color: Blue Category: A-line Pattern: Self design solid Length: Knee length Hemline: Straight Top fa... |
| 14 | no | 14424654 | - | 0.398 | brand=ROOTED, color=Navy Blue, category=Peplum, occasion=Ethnic, price=2999.0 | Product: ROOTED Navy Blue Printed Peplum Top Brand: ROOTED Color: Navy Blue Category: Peplum Pattern: Abstract printed Neck: Round neck Sleeves: Long regular sleeves Length: Reg... |
| 15 | no | 17566228 | - | 0.395 | brand=Inddus, color=Blue, category=Top, occasion=Party, price=6799.0 | Product: Inddus Women Blue Woven Design Top & Solid Palazzos with Jacket Brand: Inddus Color: Blue Category: Top Top type: Top Bottom type: Palazzos Pattern: Self design Neck: V... |
| 16 | no | 16950218 | - | 0.359 | brand=Indo Era, color=Blue, category=Peplum, occasion=Ethnic, price=3399.0 | Product: Indo Era Blue Ethnic Motif Printed Peplum Top Brand: Indo Era Color: Blue Category: Peplum Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Three-quarter regula... |
| 17 | no | 17627582 | - | 0.356 | brand=kipek, color=Navy Blue, category=Top, occasion=Casual, price=5379.0 | Product: kipek Women Deep Navy Blue Solid Top with Palazzos Brand: kipek Color: Navy Blue Category: Top Top type: Top Bottom type: Palazzos Pattern: Solid Neck: Shoulder straps ... |
| 18 | no | 15766290 | - | 0.350 | brand=Pepe Jeans, color=Blue, category=Regular trousers, occasion=Casual, price=2799.0 | Product: Pepe Jeans Women Blue Pure Cotton Trousers Brand: Pepe Jeans Color: Blue Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual P... |
| 19 | no | 18998716 | - | 0.347 | brand=KALINI, color=Blue, category=Peplum, occasion=Casual, price=1999.0 | Product: KALINI Blue Print Indigo Pure Cotton Peplum Top Brand: KALINI Color: Blue Category: Peplum Pattern: Ethnic motifs printed Neck: Shoulder straps Sleeves: Sleeveless no L... |
| 20 | no | 13385158 | - | 0.336 | brand=Gipsy, color=Blue, category=Pullover, occasion=Casual, price=1795.0 | Product: Gipsy Women Blue Self Design Sweatshirt Brand: Gipsy Color: Blue Category: Pullover Pattern: Self design solid Neck: Round neck Sleeves: Long sleeves Length: Regular He... |
| 21 | no | 2137522 | - | 0.333 | brand=Tokyo Talkies, color=Blue, category=Regular, occasion=Casual, price=1199.0 | Product: Tokyo Talkies Women Blue Self Design Pure Cotton Top Brand: Tokyo Talkies Color: Blue Category: Regular Pattern: Self design Neck: Round neck Sleeves: Short regular sle... |
| 22 | no | 18454274 | - | 0.321 | brand=Albion, color=Blue, category=A-line, occasion=Casual, price=760.0 | Product: Albion Girls Blue Solid Denim A-Line Skirts Brand: Albion Color: Blue Category: A-line Pattern: Self design solid Length: Knee length Hemline: Curved Top fabric: Cotton... |
| 23 | no | 17132226 | - | 0.314 | brand=Athena, color=Blue, category=Regular, occasion=Casual, price=1699.0 | Product: Athena Women Stunning Blue Self-Design Bustier Top Brand: Athena Color: Blue Category: Regular Pattern: Self design Neck: Sweetheart neck Sleeves: Short puff sleeves Le... |
| 24 | no | 13495564 | - | 0.296 | brand=GRACIT, color=Navy Blue, occasion=Ethnic, price=1449.0 | Product: GRACIT Women Navy Blue Self Design Cotton Wide Leg Palazzos Brand: GRACIT Color: Navy Blue Pattern: Geometric self design Length: Regular Top fabric: Cotton Occasion: E... |
| 25 | no | 19087886 | - | 0.290 | brand=ONLY, color=Blue, category=Pullover, occasion=Casual, price=1999.0 | Product: ONLY Women Blue Acrylic Pullover Brand: ONLY Color: Blue Category: Pullover Pattern: Solid self design Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: C... |
| 26 | no | 13499958 | - | 0.285 | brand=Oxolloxo, color=Navy Blue, occasion=Casual, price=2299.0 | Product: Oxolloxo Women Navy Blue Self-Design Open-Front Casual Blazer Brand: Oxolloxo Color: Navy Blue Pattern: Self design Sleeves: Long sleeves Length: Regular Top fabric: Po... |
| 27 | no | 16935640 | - | 0.266 | brand=flaher, color=Blue, occasion=Festive, price=2169.0 | Product: flaher Women Blue Solid Art Silk Padded Blouse Brand: flaher Color: Blue Pattern: Solid Neck: Halter neck Sleeves: Sleeveless Top fabric: Dupion Occasion: Festive |
| 28 | no | 14658916 | - | 0.255 | brand=Pepe Jeans, color=Blue, category=Regular shorts, occasion=Casual, price=1699.0 | Product: Pepe Jeans Women Blue Washed Mid-Rise Regular Shorts Brand: Pepe Jeans Color: Blue Category: Regular shorts Pattern: Solid washed Length: Above knee Top fabric: Cotton ... |
| 29 | no | 17403254 | - | 0.243 | brand=I Saw It First, color=Blue, occasion=Casual, price=4099.0 | Product: I Saw It First Women Blue Skinny Fit Stretchable Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machi... |
| 30 | no | 17403428 | - | 0.236 | brand=I Saw It First, color=Blue, occasion=Casual, price=3799.0 | Product: I Saw It First Women Blue Skinny Fit Highly Distressed Light Fade Stretchable Jeans Brand: I Saw It First Color: Blue Length: Regular Top fabric: Cotton Occasion: Casua... |

### Question 50/50

**Query:** I need Peach Pullover by Madame.

**Retrieval metadata:** brand == Madame, color == Peach

**Relevant docs:** `['16533076']`

Metrics:

| precision | recall | mrr | ndcg | context_relevance |
| --- | --- | --- | --- | --- |
| 0.500 | 1.000 | 1.000 | 1.000 | 1.000 |

Retrieved documents:

| rank | hit | section_id | title | score | metadata | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | yes | 16533076 | - | 1.000 | brand=Madame, color=Peach, category=Pullover, occasion=Casual, price=2999.0 | Product: Madame Women Peach-Coloured Self Designed Wool Pullover Brand: Madame Color: Peach Category: Pullover Pattern: Open knit self design Neck: Round neck Sleeves: Long slee... |
| 2 | no | 18948340 | - | 0.000 | brand=Madame, color=Peach, category=Styled back, occasion=Casual, price=1699.0 | Product: Madame Peach-Coloured Cuffed Sleeves Styled Back Crop Top Brand: Madame Color: Peach Category: Styled back Pattern: Solid Neck: High neck Sleeves: Long cuffed sleeves L... |
