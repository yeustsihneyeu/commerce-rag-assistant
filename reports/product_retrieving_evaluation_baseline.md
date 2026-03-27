# Product Retrieval Evaluation Report

Source notebook: `notebooks/product/05_product_retrieval_baseline.ipynb`

## Overview

- Evaluated questions: 50
- Mean precision: 0.081
- Mean recall: 0.748
- Mean MRR: 0.570
- Mean ndcg: 0.609
- Mean context relevance: 0.850

## Summary Tables

### Final Metrics

| row  | precision | recall | mrr   | ndcg  | context_relevance |
| ---- | --------- | ------ | ----- | ----- | ----------------- |
| mean | 0.081     | 0.748  | 0.570 | 0.609 | 0.850             |

## Detailed Results

### Question 1/50

**Query:** Show me Regular trousers within a budget of 2000.

**Relevant docs:** `['17817750', '18770002', '18769968', '18769944', '18769702', '15026996', '15092120', '16814696']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 0.125  | 0.050 | 0.058 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 16279046   | -     | 1.000 | Product: 20Dresses Women Blue Trousers Brand: 20Dresses Color: Blue Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Pockets: 2 W... |
| 2    | no  | 11421530   | -     | 0.858 | Product: Ginni Arora Label Women Red Slim Fit Solid Regular Trousers Brand: Ginni Arora Label Color: Red Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Co... |
| 3    | no  | 17393956   | -     | 0.849 | Product: Fabindia Women Beige & Red Striped Cotton Regular Trousers Brand: Fabindia Color: Beige Category: Regular trousers Pattern: Striped Length: Regular Top fabric: Cotton O... |
| 4    | no  | 17378344   | -     | 0.772 | Product: Saffron Threads Women Black Original Trousers Brand: Saffron Threads Color: Black Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion:... |
| 5    | no  | 17625016   | -     | 0.765 | Product: Fabindia Women Off White Cotton Trousers Brand: Fabindia Color: Off White Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual ... |
| 6    | no  | 17104470   | -     | 0.741 | Product: Fabindia Women Blue Striped Relaxed Trousers Brand: Fabindia Color: Blue Category: Regular trousers Pattern: Striped Length: Regular Top fabric: Cotton Occasion: Casual... |
| 7    | no  | 14220222   | -     | 0.688 | Product: DressBerry Women Green Trousers Brand: DressBerry Color: Green Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Pockets:... |
| 8    | no  | 18770054   | -     | 0.686 | Product: Trendyol Women Blue & Yellow Ethnic Motifs Printed High-Rise Trousers Brand: Trendyol Color: Blue Category: Regular trousers Pattern: Ethnic motifs printed Length: Regu... |
| 9    | no  | 10440556   | -     | 0.665 | Product: DressBerry Women Olive Green Regular Fit Solid Regular Mid-Rise Trousers Brand: DressBerry Color: Olive Category: Regular trousers Pattern: Solid Length: Regular Top fa... |
| 10   | no  | 15693320   | -     | 0.639 | Product: Fabindia Women Beige Ethnic Trousers Brand: Fabindia Color: Beige Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets:... |
| 11   | no  | 13921450   | -     | 0.638 | Product: Saffron Threads Women Black & Gold Set of 2 Solid Regular Trousers Brand: Saffron Threads Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fab... |
| 12   | no  | 18033910   | -     | 0.612 | Product: Fabindia Women Blue Cotton Trousers Brand: Fabindia Color: Blue Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 2... |
| 13   | no  | 17371040   | -     | 0.589 | Product: Saffron Threads Women Pack of 2 Black & White Trousers Brand: Saffron Threads Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton ... |
| 14   | no  | 16220618   | -     | 0.580 | Product: 20Dresses Women Olive Green Trousers Brand: 20Dresses Color: Olive Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Other Occasion: Casual Pockets:... |
| 15   | no  | 17511712   | -     | 0.573 | Product: SASSAFRAS Women Stylish Black Solid Y2K Cargo Trousers Brand: SASSAFRAS Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occ... |
| 16   | no  | 19327268   | -     | 0.533 | Product: Lakshita Women Navy Blue Women Blue Regular Fit Solid Chambray Trousers Brand: Lakshita Color: Navy Blue Category: Regular trousers Pattern: Solid Length: Regular Top f... |
| 17   | no  | 14099268   | -     | 0.517 | Product: Jaipur Kurti Women Beige Regular Fit Solid Regular Trousers Brand: Jaipur Kurti Color: Beige Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotto... |
| 18   | no  | 18769616   | -     | 0.517 | Product: Trendyol Women Beige & Brown Pure Cotton Colourblocked High-Rise Trousers Brand: Trendyol Color: Beige Category: Regular trousers Pattern: Colourblocked solid Length: R... |
| 19   | no  | 17378342   | -     | 0.512 | Product: Saffron Threads Women Off White Solid Trousers Brand: Saffron Threads Color: Off White Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occa... |
| 20   | yes | 17817750   | -     | 0.507 | Product: Trendyol Women Green Solid High Rise Tie-Up Trousers Brand: Trendyol Color: Green Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Viscose rayon Oc... |
| 21   | no  | 19011990   | -     | 0.503 | Product: Trendyol Women Blue Pure Cotton Solid Trousers Brand: Trendyol Color: Blue Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual... |
| 22   | no  | 13499940   | -     | 0.496 | Product: Oxolloxo Women Black & Black Regular Fit Solid Regular Trousers Brand: Oxolloxo Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polye... |
| 23   | no  | 19239034   | -     | 0.495 | Product: BROADSTAR Women Navy Blue Relaxed Straight Leg Loose Fit High-Rise Non Iron Trousers Brand: BROADSTAR Color: Navy Blue Category: Formal trousers Pattern: Solid Length: ... |
| 24   | no  | 19327338   | -     | 0.468 | Product: Lakshita Women Beige Relaxed Loose Fit Chambray Trousers Brand: Lakshita Color: Beige Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Viscose rayo... |
| 25   | no  | 14099278   | -     | 0.459 | Product: Jaipur Kurti Women Mustard Regular Fit Solid Regular Trousers Brand: Jaipur Kurti Color: Mustard Category: Regular trousers Pattern: Solid Length: Regular Top fabric: C... |
| 26   | no  | 17945078   | -     | 0.455 | Product: Ginni Arora Label Women White Slim Fit Trousers Brand: Ginni Arora Label Color: White Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occas... |
| 27   | no  | 14220194   | -     | 0.414 | Product: DressBerry Women Burgundy Trousers Brand: DressBerry Color: Burgundy Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Po... |
| 28   | no  | 17188132   | -     | 0.407 | Product: Rangriti Women Olive Green Solid Slim Fit Trousers Brand: Rangriti Color: Olive Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion: C... |
| 29   | no  | 14027022   | -     | 0.407 | Product: Oxolloxo Women Multicoloured Regular Fit Abstract Printed Regular Trousers Brand: Oxolloxo Color: Multi Category: Regular trousers Pattern: Abstract printed Length: Reg... |
| 30   | no  | 9436011    | -     | 0.361 | Product: Jaipur Kurti Women Green Regular Fit Solid Trousers Brand: Jaipur Kurti Color: Green Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasi... |

### Question 2/50

**Query:** Can you find something similar to "Athena Women Burgundy Solid Tailored Suede Jacket"?

**Relevant docs:** `['11166548']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 11166548   | -     | 1.000 | Product: Athena Women Burgundy Solid Tailored Suede Jacket Brand: Athena Color: Burgundy Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: ... |
| 2    | no  | 10758214   | -     | 0.480 | Product: Athena Women Burgundy Solid Pullover Sweatshirt Brand: Athena Color: Burgundy Category: Pullover Pattern: Solid Neck: High neck Sleeves: Long sleeves Length: Regular He... |
| 3    | no  | 12086086   | -     | 0.392 | Product: Athena Women Burgundy Solid Pencil Midi Skirt Brand: Athena Color: Burgundy Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fabric: Polyester Occasio... |
| 4    | no  | 11634534   | -     | 0.376 | Product: Athena Women Burgundy Solid Basic Jumpsuit Brand: Athena Color: Burgundy Category: Basic jumpsuit Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless Top fabric: P... |
| 5    | no  | 11634536   | -     | 0.374 | Product: Athena Women Burgundy Solid Basic Jumpsuit Brand: Athena Color: Burgundy Category: Basic jumpsuit Pattern: Solid Neck: Halter neck Sleeves: Sleeveless Top fabric: Polye... |
| 6    | no  | 10856152   | -     | 0.365 | Product: SASSAFRAS Women Burgundy Solid Tailored Jacket Brand: SASSAFRAS Color: Burgundy Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: ... |
| 7    | no  | 11151684   | -     | 0.311 | Product: Athena Women Grey Solid Single Breasted Blazer Brand: Athena Color: Grey Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Wool blend Occasion: Casual Wa... |
| 8    | no  | 12402376   | -     | 0.293 | Product: Belle Fille Women Burgundy Solid Asymmetric Closure Tailored Jacket Brand: Belle Fille Color: Burgundy Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Le... |
| 9    | no  | 7779375    | -     | 0.293 | Product: Athena Women White Solid Cropped Denim Jacket Brand: Athena Color: White Category: Denim jacket Pattern: Solid Sleeves: Long sleeves Length: Crop Hemline: Straight Top ... |
| 10   | no  | 13023122   | -     | 0.261 | Product: Athena Women Mustard Yellow Solid Blazer with Trousers Brand: Athena Color: Mustard Category: Coat Top type: Coat Bottom type: Trousers Pattern: Solid Neck: Shirt colla... |
| 11   | no  | 14320508   | -     | 0.224 | Product: Sztori Plus Size Women Burgundy Hooded Longline Packable Windcheater Jacket Brand: Sztori Color: Burgundy Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves... |
| 12   | no  | 15300920   | -     | 0.219 | Product: Athena Women Striking Coral Sleek Coat with Skirt Brand: Athena Color: Coral Category: Coat Top type: Coat Bottom type: Skirt Pattern: Solid Neck: Shawl neck Sleeves: L... |
| 13   | no  | 16752820   | -     | 0.194 | Product: armure Women Brown & White Checked Suede Lightweight Tailored Jacket Brand: armure Color: Brown Category: Tailored jacket Pattern: Checked Sleeves: Long sleeves Length:... |
| 14   | no  | 7784761    | -     | 0.192 | Product: Athena Women Red Embellished Sweatshirt Brand: Athena Color: Red Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Strai... |
| 15   | no  | 16565622   | -     | 0.182 | Product: Latin Quarters Women Maroon Suede Tailored Jacket Brand: Latin Quarters Color: Maroon Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hem... |
| 16   | no  | 16552340   | -     | 0.171 | Product: armure Women Maroon Lightweight Tailored Jacket Brand: armure Color: Maroon Category: Tailored jacket Pattern: Solid Sleeves: Three-quarter sleeves Length: Regular Heml... |
| 17   | no  | 16429486   | -     | 0.164 | Product: ATHLISIS Women Maroon Lightweight e-Dry Technology Training or Gym Sporty Jacket Brand: ATHLISIS Color: Maroon Category: Sporty jacket Pattern: Solid Sleeves: Long slee... |
| 18   | no  | 18121946   | -     | 0.162 | Product: Athena Women Elegant Lavender Solid Noughties Spaghetti Jumpsuit Brand: Athena Color: Lavender Category: Basic jumpsuit Pattern: Solid Neck: Shoulder straps Sleeves: Sl... |
| 19   | no  | 18121932   | -     | 0.151 | Product: Athena Women Elegant Lavender Solid Feminine Frills Jumpsuit Brand: Athena Color: Lavender Category: Basic jumpsuit Pattern: Solid Neck: Off-shoulder Sleeves: Sleeveles... |
| 20   | no  | 11151706   | -     | 0.151 | Product: Athena Women Fuchsia Pink Solid Sweatshirt Brand: Athena Color: Fuchsia Category: Front-open Pattern: Striped solid Neck: Mandarin collar Sleeves: Long sleeves Length: ... |
| 21   | no  | 10758220   | -     | 0.149 | Product: Athena Women Green Solid Sweatshirt Brand: Athena Color: Green Category: Pullover Pattern: Solid Neck: High neck Sleeves: Long sleeves Length: Regular Hemline: Straight... |
| 22   | no  | 16491516   | -     | 0.146 | Product: Woods Women Burgundy Camouflage Water Resistant Longline Tailored Jacket with Embroidered Brand: Woods Color: Burgundy Category: Tailored jacket Pattern: Camouflage pri... |
| 23   | no  | 16002984   | -     | 0.141 | Product: Athena Women Blue Crop Jacket With Flared Trousers Brand: Athena Color: Blue Category: T-shirt Top type: T-shirt Bottom type: Trousers Pattern: Self design Neck: Shirt ... |
| 24   | no  | 15995804   | -     | 0.130 | Product: FableStreet Women Burgundy Crop Denim Jacket Brand: FableStreet Color: Burgundy Category: Denim jacket Pattern: Solid Sleeves: Three-quarter sleeves Length: Crop Hemlin... |
| 25   | no  | 14356158   | -     | 0.130 | Product: Roadster Women Burgundy Convertible Jacket with Detachable Sleeves Brand: Roadster Color: Burgundy Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length... |
| 26   | no  | 18121952   | -     | 0.124 | Product: Athena Women Black Solid Cut-Out Detail Basic Jumpsuit Brand: Athena Color: Black Category: Basic jumpsuit Pattern: Solid Neck: One shoulder Sleeves: Sleeveless Top fab... |
| 27   | no  | 6968708    | -     | 0.124 | Product: Alcis Women Burgundy Printed Lightweight Sporty Jacket Brand: Alcis Color: Burgundy Category: Sporty jacket Pattern: Self design printed Sleeves: Long sleeves Length: R... |
| 28   | no  | 16706804   | -     | 0.120 | Product: AMERICAN EAGLE OUTFITTERS Women Brown Black Tailored Jacket Brand: AMERICAN EAGLE OUTFITTERS Color: Brown Category: Tailored jacket Pattern: Abstract printed Sleeves: L... |
| 29   | no  | 15851900   | -     | 0.117 | Product: URBANIC Women Blue Solid Hooded Faux Fur Jacket Brand: URBANIC Color: Blue Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Strai... |
| 30   | no  | 15849954   | -     | 0.116 | Product: URBANIC Women Black & White Houndstooth Pattern Tailored Jacket Brand: URBANIC Color: Black Category: Tailored jacket Pattern: Houndstooth checked Sleeves: Long sleeves... |

### Question 3/50

**Query:** Show me products like "InWeave Women Red Printed A-Line Skirt".

**Relevant docs:** `['18921114']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 18921114   | -     | 1.000 | Product: InWeave Women Red Printed A-Line Skirt Brand: InWeave Color: Red Category: A-line Pattern: Floral printed Length: Maxi Hemline: Flared Top fabric: Viscose rayon Occasio... |
| 2    | no  | 17168254   | -     | 0.913 | Product: InWeave Women Red Printed Pure Cotton A-Line Maxi Skirt Brand: InWeave Color: Red Category: A-line Pattern: Geometric printed Length: Maxi Hemline: Flared Top fabric: P... |
| 3    | no  | 15322490   | -     | 0.695 | Product: InWeave Women Black & Yellow Lahariya Printed A-Line Maxi Skirt Brand: InWeave Color: Black Category: A-line Pattern: Abstract printed Length: Maxi Hemline: Flared Top ... |
| 4    | no  | 17168250   | -     | 0.659 | Product: InWeave Women Blue Printed Pure Cotton A-Line Flared Maxi Skirt Brand: InWeave Color: Blue Category: A-line Pattern: Floral printed Length: Maxi Hemline: Flared Top fab... |
| 5    | no  | 15542594   | -     | 0.647 | Product: InWeave Women Mustard Yellow & White Ikkat Printed A-Line Maxi Skirt Brand: InWeave Color: Mustard Category: A-line Pattern: Abstract printed Length: Maxi Hemline: Flar... |
| 6    | no  | 17168268   | -     | 0.579 | Product: InWeave Women Pink & White Printed Pure Cotton Flared Maxi Skirt Brand: InWeave Color: Pink Category: Flared Pattern: Geometric printed Length: Maxi Hemline: Flared Top... |
| 7    | no  | 13497800   | -     | 0.531 | Product: InWeave Women Red Striped A-Line Top Brand: InWeave Color: Red Category: Regular Pattern: Vertical stripes self design Neck: Round neck Sleeves: Sleeveless no Length: R... |
| 8    | no  | 16524822   | -     | 0.510 | Product: InWeave Women Striking Pink Solid Asymmetric Skirt Brand: InWeave Color: Pink Category: Tulip Pattern: Solid Length: Maxi Hemline: Asymmetric Top fabric: Polyester Occa... |
| 9    | no  | 15447990   | -     | 0.465 | Product: InWeave Women Bright Orange Printed Top with Skirt Brand: InWeave Color: Orange Category: Top Top type: Top Bottom type: Skirt Pattern: Printed Neck: V-neck Sleeves: Lo... |
| 10   | no  | 15760840   | -     | 0.412 | Product: InWeave Red & Gold-Toned Regular Crop Top Brand: InWeave Color: Red Category: Regular Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Three-quarter flared slee... |
| 11   | no  | 18922178   | -     | 0.401 | Product: InWeave Women Red Flared Palazzos Brand: InWeave Color: Red Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion: Western Wash care: Hand wash                 |
| 12   | no  | 16524698   | -     | 0.392 | Product: InWeave Women Green Printed Co-Ords Brand: InWeave Color: Green Category: Top Top type: Top Bottom type: Skirt Pattern: Printed Neck: Shoulder straps Sleeves: Sleeveles... |
| 13   | no  | 17355370   | -     | 0.383 | Product: InWeave Women Elegant Charcoal Solid Shirt with Printed Skirt Brand: InWeave Color: Charcoal Category: Shirt Top type: Shirt Bottom type: Skirt Pattern: Solid Neck: V-n... |
| 14   | no  | 14402632   | -     | 0.336 | Product: InWeave Mustard Yellow & Blue A-Line Top Brand: InWeave Color: Mustard Category: A-line Pattern: Graphic printed Neck: Round neck Sleeves: Sleeveless no Length: Regular... |
| 15   | no  | 13610084   | -     | 0.327 | Product: ANVI Be Yourself Women Red & White Printed Pleated A-Line Midi Skirt Brand: ANVI Be Yourself Color: Red Category: A-line Pattern: Geometric printed Length: Midi Hemline... |
| 16   | no  | 13020628   | -     | 0.288 | Product: InWeave Women Blue & Red Ikkat Printed Reversible Open Front Shrug Brand: InWeave Color: Blue Pattern: Printed Sleeves: Sleeveless Length: Regular Hemline: Asymmetric T... |
| 17   | no  | 15485484   | -     | 0.267 | Product: InWeave Women Maroon & Blue Printed Longline Bohemian Shrug Brand: InWeave Color: Maroon Pattern: Printed Sleeves: Sleeveless Length: Longline Hemline: Straight Top fab... |
| 18   | no  | 18922836   | -     | 0.245 | Product: InWeave Navy Blue Empire Solid Kurti Brand: InWeave Color: Navy Blue Pattern: Solid Shape: A-line Neck: Round neck Sleeves: Short regular sleeves Hemline: Flared Top fa... |
| 19   | no  | 18052092   | -     | 0.245 | Product: InWeave Women Green & White Printed Dupatta Brand: InWeave Color: Green Pattern: Geometric printed Top fabric: Silk blend Occasion: Daily Wash care: Hand wash              |
| 20   | no  | 18769480   | -     | 0.234 | Product: Trendyol Women Red & White Floral Print Tiered A-Line Skirt Brand: Trendyol Color: Red Category: A-line Pattern: Floral printed Length: Mini Hemline: Flared Top fabric:... |
| 21   | no  | 18922128   | -     | 0.232 | Product: InWeave Women Black Flared Palazzos Brand: InWeave Color: Black Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion: Western Wash care: Hand wash             |
| 22   | no  | 12379640   | -     | 0.222 | Product: InWeave Women Maroon & Navy Blue Flared Printed Kalamkari Culottes Brand: InWeave Color: Maroon Category: Culottes Pattern: Ethnic motifs printed Length: Cropped Top fa... |
| 23   | no  | 17241002   | -     | 0.214 | Product: InWeave Women Pretty Pink Floral Scarf Top Brand: InWeave Color: Pink Category: Styled back Pattern: Floral printed Neck: Shoulder straps Sleeves: Sleeveless no Length:... |
| 24   | no  | 13857708   | -     | 0.211 | Product: RARE Women White & Red Printed A-Line Midi Skirt Brand: RARE Color: White Category: A-line Pattern: Geometric printed Length: Midi Hemline: Straight Top fabric: Polyest... |
| 25   | no  | 18262776   | -     | 0.204 | Product: InWeave Women Black & Blue Solid Crop Top with Printed Harem Pants Brand: InWeave Color: Black Category: Top Top type: Top Bottom type: Palazzos Pattern: Solid Neck: Hi... |
| 26   | no  | 18052104   | -     | 0.202 | Product: InWeave Maroon & Yellow Printed Organza Dupatta Brand: InWeave Color: Maroon Pattern: Floral printed Top fabric: Organza Occasion: Daily Wash care: Hand wash               |
| 27   | no  | 13718888   | -     | 0.185 | Product: InWeave Off White Floral Printed Top Brand: InWeave Color: Off White Category: Regular Pattern: Floral printed Neck: Round neck Sleeves: Three-quarter regular sleeves L... |
| 28   | no  | 18376990   | -     | 0.173 | Product: kriatma Women Red Printed Midi Skirts Brand: kriatma Color: Red Category: A-line Pattern: Geometric printed Length: Midi Hemline: Flared Top fabric: Polyester Occasion:... |
| 29   | no  | 13676002   | -     | 0.171 | Product: InWeave Maroon Printed Dupatta Brand: InWeave Color: Maroon Pattern: Ethnic motifs printed Top fabric: Cotton silk Occasion: Daily Wash care: Hand wash                     |
| 30   | no  | 13020642   | -     | 0.167 | Product: InWeave Women Mustard Yellow & Green Printed Open Front Reversible Shrug Brand: InWeave Color: Mustard Pattern: Printed Sleeves: Sleeveless Length: Regular Hemline: Asy... |

### Question 4/50

**Query:** I need product with a Woven design pattern in Mustard.

**Relevant docs:** `['12824928', '18262088']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.000     | 0.000  | 0.000 | 0.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 10451734   | -     | 1.000 | Product: WEAVERS VILLA Women Mustard Yellow & Purple Woven Design Shawl Brand: WEAVERS VILLA Color: Mustard Pattern: Floral woven design Top fabric: Wool Occasion: Daily            |
| 2    | no  | 14402632   | -     | 0.774 | Product: InWeave Mustard Yellow & Blue A-Line Top Brand: InWeave Color: Mustard Category: A-line Pattern: Graphic printed Neck: Round neck Sleeves: Sleeveless no Length: Regular... |
| 3    | no  | 19218994   | -     | 0.654 | Product: Mitera Mustard & Red Woven Design Zari Art Silk Kanjeevaram Saree Brand: Mitera Color: Mustard Category: Kanjeevaram Pattern: Woven design Occasion: Traditional Wash ca... |
| 4    | no  | 16719554   | -     | 0.645 | Product: Banarasi Style Mustard Woven Design Dupatta with Zari Brand: Banarasi Style Color: Mustard Pattern: Floral woven design Top fabric: Silk blend Occasion: Daily Wash care... |
| 5    | no  | 17663018   | -     | 0.641 | Product: Dupatta Bazaar Mustard Yellow Ethnic Motifs Woven Design Silk Dupatta Brand: Dupatta Bazaar Color: Mustard Pattern: Ethnic motifs woven design Top fabric: Silk blend Oc... |
| 6    | no  | 1319900    | -     | 0.585 | Product: Desi Weavess Mustard Orange & Red Printed Jodhpuri Jumpsuit Brand: Desi Weavess Color: Mustard Pattern: Printed Neck: Shirt collar Sleeves: Sleeveless Top fabric: Cotto... |
| 7    | no  | 11117288   | -     | 0.555 | Product: Mitera Mustard & Pink Silk Blend Woven Design Kanjeevaram Saree Brand: Mitera Color: Mustard Category: Kanjeevaram Pattern: Embellished woven design Occasion: Tradition... |
| 8    | no  | 15781530   | -     | 0.473 | Product: max Mustard Viscose Rayon Dupatta Brand: max Color: Mustard Pattern: Solid Top fabric: Viscose rayon Occasion: Daily Wash care: Machine wash                                |
| 9    | no  | 14088428   | -     | 0.473 | Product: SheWill Mustard Brown & Green Cotton Blend Unstitched Dress Material Brand: SheWill Color: Mustard Category: Dress Pattern: Ethnic motifs Bottom fabric: Cotton blend Du... |
| 10   | no  | 16921550   | -     | 0.466 | Product: Safaa Women Mustard Woven Design Wool Unstitched Dress Material Brand: Safaa Color: Mustard Category: Dress Pattern: Floral Bottom fabric: Viscose rayon Dupatta fabric:... |
| 11   | no  | 15542594   | -     | 0.451 | Product: InWeave Women Mustard Yellow & White Ikkat Printed A-Line Maxi Skirt Brand: InWeave Color: Mustard Category: A-line Pattern: Abstract printed Length: Maxi Hemline: Flar... |
| 12   | no  | 18135092   | -     | 0.420 | Product: Mitera Mustard Yellow Ethnic Motifs Zari Silk Cotton Banarasi Saree Brand: Mitera Color: Mustard Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Tradit... |
| 13   | no  | 17415222   | -     | 0.415 | Product: The Magic Wand Girls Mustard Yellow & Silver-Toned Solid Straight Palazzos Brand: The Magic Wand Color: Mustard Pattern: Solid Length: Regular Top fabric: Viscose rayon... |
| 14   | no  | 14367932   | -     | 0.384 | Product: Safaa Mustard Yellow & White Pure Cotton Woven Design Unstitched Dress Material For Summer Brand: Safaa Color: Mustard Category: Dress Pattern: Ethnic motifs Bottom fab... |
| 15   | no  | 13020634   | -     | 0.382 | Product: InWeave Women Mustard Yellow Printed Reversible Open Front Shrug Brand: InWeave Color: Mustard Pattern: Printed Sleeves: Sleeveless Length: Regular Hemline: Asymmetric ... |
| 16   | no  | 13020642   | -     | 0.369 | Product: InWeave Women Mustard Yellow & Green Printed Open Front Reversible Shrug Brand: InWeave Color: Mustard Pattern: Printed Sleeves: Sleeveless Length: Regular Hemline: Asy... |
| 17   | no  | 11524932   | -     | 0.350 | Product: Vishudh Women's Mustard & Pink Striped Tunic Brand: Vishudh Color: Mustard Pattern: Striped Neck: Mandarin collar Sleeves: Three-quarter sleeves Top fabric: Viscose ray... |
| 18   | no  | 19240508   | -     | 0.345 | Product: max Women Mustard Yellow Yoke Design Thread Work Kurta Brand: max Color: Mustard Pattern: Solid yoke design Shape: Straight Neck: Mandarin collar Sleeves: Three-quarter... |
| 19   | no  | 19145502   | -     | 0.344 | Product: The Chennai Silks Mustard & Brown Pure Cotton Fusion Taant Saree Brand: The Chennai Silks Color: Mustard Category: Taant Pattern: Solid Occasion: Traditional Wash care:... |
| 20   | no  | 18122478   | -     | 0.339 | Product: PERFECTBLUE Mustard Yellow & Fuchsia Floral Woven Design Saree Brand: PERFECTBLUE Color: Mustard Category: Saree Pattern: Floral woven design Occasion: Festive Wash car... |
| 21   | no  | 16291090   | -     | 0.325 | Product: BROOWL Women Mustard & Orange Floral Embroidered Pullover Brand: BROOWL Color: Mustard Category: Pullover Pattern: Embroidered Neck: Round neck Sleeves: Long sleeves Le... |
| 22   | no  | 17480778   | -     | 0.294 | Product: SALWAR STUDIO Mustard & Brown Printed Unstitched Dress Material Brand: SALWAR STUDIO Color: Mustard Category: Dress Pattern: Checked Bottom fabric: Poly crepe Dupatta f... |
| 23   | no  | 10265397   | -     | 0.292 | Product: Saadgi Mustard Yellow Gotta Patti Dupatta Brand: Saadgi Color: Mustard Pattern: Solid Top fabric: Poly chiffon Occasion: Daily Wash care: Hand wash                         |
| 24   | no  | 18549594   | -     | 0.282 | Product: Amrutam Fab Mustard & Green Printed Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Amrutam Fab Color: Mustard Dupatta: With dupatta Pattern: Printed Neck... |
| 25   | no  | 17044784   | -     | 0.279 | Product: Studio Shringaar Mustard Yellow Embroidered Dupatta Brand: Studio Shringaar Color: Mustard Pattern: Abstract embroidered Top fabric: Net Occasion: Daily Wash care: Hand... |
| 26   | no  | 14987382   | -     | 0.275 | Product: Fabindia Mustard Yellow Pure Cotton Regular Top Brand: Fabindia Color: Mustard Category: Regular Pattern: Solid Neck: Round neck Sleeves: Sleeveless no Length: Regular ... |
| 27   | no  | 13861554   | -     | 0.272 | Product: mf Mustard & Pink Cotton Blend Unstitched Dress Material Brand: mf Color: Mustard Category: Dress Pattern: Floral Bottom fabric: Cotton blend Dupatta fabric: Poly chiff... |
| 28   | no  | 15709312   | -     | 0.267 | Product: Fabindia Mustard Pure Silk Block Print Saree Brand: Fabindia Color: Mustard Category: Block print Pattern: Geometric printed Occasion: Festive Wash care: Dry clean         |
| 29   | no  | 18456682   | -     | 0.252 | Product: Fabindia Women Mustard Yellow Pure Cotton Straight Knee Length Kurta Brand: Fabindia Color: Mustard Pattern: Solid Shape: Straight Neck: Round neck Sleeves: Three-quart... |
| 30   | no  | 18141434   | -     | 0.249 | Product: MANOHARI Mustard & Gold-Toned Woven Design Sequinned Silk Blend Saree Brand: MANOHARI Color: Mustard Category: Saree Pattern: Woven design Occasion: Festive Wash care: ... |

### Question 5/50

**Query:** I'm looking for products from MANGO for everyday wear under 5600.

**Relevant docs:** `['15315768', '15265896', '15265898', '16892568', '15977044', '18257264', '16708118', '16708114']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 0.125  | 0.037 | 0.053 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 16124612   | -     | 1.000 | Product: MANGO Black Self Design Regular Top Brand: MANGO Color: Black Category: Regular Pattern: Self design Neck: Shoulder straps Sleeves: Sleeveless shoulder straps Length: R... |
| 2    | no  | 17607938   | -     | 0.870 | Product: MANGO Women Coral Red Solid Double-Breasted Blazer Brand: MANGO Color: Coral Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Polyviscose Occasion: Casu... |
| 3    | no  | 15274016   | -     | 0.783 | Product: MANGO Women Black Pullover Brand: MANGO Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabr... |
| 4    | no  | 17808618   | -     | 0.767 | Product: MANGO Off White Satin Finish Extended Sleeves Top Brand: MANGO Color: Off White Category: Regular Pattern: Solid Neck: High neck Sleeves: Short extended sleeves Length:... |
| 5    | no  | 18319598   | -     | 0.753 | Product: MANGO Women Beige Solid Oversize Fit Blazer Brand: MANGO Color: Beige Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Polyviscose Occasion: Casual Wash... |
| 6    | no  | 17270200   | -     | 0.695 | Product: MANGO Coral Pink Solid A-line Midi Skirt Brand: MANGO Color: Coral Category: A-line Pattern: Solid Length: Midi Hemline: Straight Top fabric: Viscose rayon Occasion: Ca... |
| 7    | no  | 14340718   | -     | 0.660 | Product: MANGO Women Peach-Coloured Solid Regular Shorts Brand: MANGO Color: Peach Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Viscose rayon Occasion:... |
| 8    | no  | 16124404   | -     | 0.634 | Product: MANGO Women Cream-Coloured Solid Pullover Sweater Brand: MANGO Color: Cream Category: Pullover Pattern: Solid Neck: Mock collar Sleeves: Long sleeves Length: Regular He... |
| 9    | no  | 15102906   | -     | 0.603 | Product: MANGO Off White Linen Regular Top Brand: MANGO Color: Off White Category: Regular Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless shoulder straps Length: Regul... |
| 10   | no  | 15102850   | -     | 0.600 | Product: MANGO Blue Regular Top Brand: MANGO Color: Blue Category: Regular Pattern: Solid Neck: V-neck Sleeves: Short flutter sleeves Length: Regular Top fabric: Polyester Occas... |
| 11   | no  | 15315374   | -     | 0.597 | Product: MANGO Women White Solid Tailored Jacket Brand: MANGO Color: White Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Hem with toggl... |
| 12   | no  | 11844262   | -     | 0.594 | Product: MANGO Women Yellow Solid Single-Breasted Blazer Brand: MANGO Color: Yellow Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Linen Occasion: Casual Wash ... |
| 13   | no  | 18319360   | -     | 0.583 | Product: MANGO Women Green Solid Double-Breasted Blazer Brand: MANGO Color: Green Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Linen Occasion: Casual Wash ca... |
| 14   | no  | 17608074   | -     | 0.572 | Product: MANGO Women Green Solid Double Breasted Blazer Brand: MANGO Color: Green Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Polyviscose Occasion: Casual W... |
| 15   | no  | 18259392   | -     | 0.558 | Product: MANGO Off White Pure Cotton Solid Ruched Top Brand: MANGO Color: Off White Category: Regular Pattern: Solid Neck: V-neck Sleeves: Short puff sleeves Length: Regular Top... |
| 16   | no  | 15963428   | -     | 0.521 | Product: MANGO Women Cream-Coloured Solid Round Neck Pullover Sweater Brand: MANGO Color: Cream Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: ... |
| 17   | no  | 17269008   | -     | 0.519 | Product: MANGO Women Black Solid Oversized Design Blazer Brand: MANGO Color: Black Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Polyester Occasion: Casual Wa... |
| 18   | no  | 18783754   | -     | 0.501 | Product: MANGO Women White and Blue Striped Regular Fit Casual Oversized Blazer Brand: MANGO Color: White Pattern: Striped Sleeves: Long sleeves Length: Regular Top fabric: Cott... |
| 19   | no  | 18783498   | -     | 0.497 | Product: MANGO Cream-Coloured Crochet Knit Smocked Top Brand: MANGO Color: Cream Category: Regular Pattern: Ethnic motifs self design Neck: Shoulder straps Sleeves: Sleeveless s... |
| 20   | no  | 15274330   | -     | 0.497 | Product: MANGO Women Off White & Red Striped Pullover Brand: MANGO Color: Off White Category: Pullover Pattern: Striped Neck: Mock collar Sleeves: Long sleeves Length: Regular H... |
| 21   | no  | 18783796   | -     | 0.494 | Product: MANGO Women Black Shorts Brand: MANGO Color: Black Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Viscose rayon Occasion: Casual Wash care: Mach... |
| 22   | no  | 19101076   | -     | 0.493 | Product: MANGO Women Black Solid Blazer Brand: MANGO Color: Black Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Polyester Occasion: Casual Wash care: Dry clean   |
| 23   | no  | 16957104   | -     | 0.492 | Product: MANGO Women Blue Oversized Pure Cotton Denim Jacket Brand: MANGO Color: Blue Category: Denim jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straig... |
| 24   | no  | 18784288   | -     | 0.492 | Product: MANGO Blue Solid Extended Sleeves Top Brand: MANGO Color: Blue Category: Regular Pattern: Solid Neck: V-neck Sleeves: Short extended sleeves Length: Regular Top fabric:... |
| 25   | no  | 17607846   | -     | 0.479 | Product: MANGO Women Dusty Pink Solid Double Breasted Blazer Brand: MANGO Color: Rose Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Polyviscose Occasion: Casu... |
| 26   | no  | 15962092   | -     | 0.477 | Product: MANGO Women Olive Green Solid Tailored Jacket Brand: MANGO Color: Olive Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight... |
| 27   | yes | 15265896   | -     | 0.462 | Product: MANGO Women Blue Noa Skinny Fit Mid-Rise Clean Look Stretchable Jeans Brand: MANGO Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care:... |
| 28   | no  | 15035500   | -     | 0.456 | Product: MANGO Cream-Coloured Solid Basic Jumpsuit with Belt Brand: MANGO Color: Cream Category: Basic jumpsuit Pattern: Solid Neck: V-neck Sleeves: Sleeveless Top fabric: Visco... |
| 29   | no  | 18259304   | -     | 0.455 | Product: MANGO Women Olive Green Regular Trousers Brand: MANGO Color: Olive Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion: Casual ... |
| 30   | no  | 18319628   | -     | 0.441 | Product: MANGO Women Mint Green Solid Single-Breasted Blazer Brand: MANGO Color: Green Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Linen Occasion: Casual Wa... |

### Question 6/50

**Query:** What do you have from Sweet Dreams in Playsuit and color Pink?

**Relevant docs:** `['11581420', '11581366']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.067     | 1.000  | 1.000 | 0.920 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 11581420   | -     | 1.000 | Product: Sweet Dreams Women Pink & Green Heart Print Playsuit Brand: Sweet Dreams Color: Pink Category: Playsuit Pattern: Printed Neck: Round neck Sleeves: Short sleeves Top fab... |
| 2    | no  | 11581448   | -     | 0.995 | Product: Sweet Dreams Women Pink & Green Heart Print Playsuit Brand: Sweet Dreams Color: Pink Category: Playsuit Pattern: Printed Neck: Round neck Sleeves: Short sleeves Top fab... |
| 3    | yes | 11581366   | -     | 0.994 | Product: Sweet Dreams Women Pink & Green Heart Print Playsuit Brand: Sweet Dreams Color: Pink Category: Playsuit Pattern: Printed Neck: Round neck Sleeves: Short sleeves Top fab... |
| 4    | no  | 12882594   | -     | 0.563 | Product: Sweet Dreams Women Peach-Coloured & Black Kitty Print Sweatshirt Brand: Sweet Dreams Color: Pink Category: Pullover Pattern: Conversational printed Neck: Round neck Sle... |
| 5    | no  | 12882732   | -     | 0.452 | Product: Sweet Dreams Women Coral Pink & Black Kitty Embossed Print Sweatshirt Brand: Sweet Dreams Color: Coral Category: Pullover Pattern: Conversational printed Neck: Round ne... |
| 6    | no  | 12459498   | -     | 0.358 | Product: Sweet Dreams Women Black Solid Regular Fit Sports Shorts Brand: Sweet Dreams Color: Black Category: Sports shorts Pattern: Solid Length: Above knee Top fabric: Cotton O... |
| 7    | no  | 16533336   | -     | 0.351 | Product: Sweet Dreams Women Beige Embroidered Fleece Sweatshirt Brand: Sweet Dreams Color: Beige Category: Pullover Pattern: Floral embroidered Neck: Round neck Sleeves: Long sl... |
| 8    | no  | 16990014   | -     | 0.316 | Product: SASSAFRAS Women Pretty Pink Solid Playsuit Brand: SASSAFRAS Color: Pink Category: Playsuit Pattern: Solid Neck: Strapless Sleeves: Sleeveless Top fabric: Polyester Occa... |
| 9    | no  | 16450186   | -     | 0.298 | Product: Berrylush Women Pretty Pink Printed Romantic Florals Playsuit Brand: Berrylush Color: Pink Category: Playsuit Pattern: Printed Neck: V-neck Sleeves: Sleeveless Top fabr... |
| 10   | no  | 14568680   | -     | 0.288 | Product: Sweet Dreams Women Burgundy Hooded Sweatshirt Brand: Sweet Dreams Color: Burgundy Category: Front-open Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular H... |
| 11   | no  | 15955210   | -     | 0.288 | Product: Missguided Pink Solid Playsuit Brand: Missguided Color: Pink Category: Playsuit Pattern: Solid Neck: Scoop neck Sleeves: Sleeveless Top fabric: Polyester Occasion: Casu... |
| 12   | no  | 16006846   | -     | 0.282 | Product: THE SILHOUETTE STORE Women Pink Solid Jumpsuit Brand: THE SILHOUETTE STORE Color: Pink Category: Playsuit Pattern: Solid Neck: Shirt collar Sleeves: Three-quarter sleev... |
| 13   | no  | 10053735   | -     | 0.256 | Product: Cottinfab Women Pink & Black Printed Layered Playsuit Brand: Cottinfab Color: Pink Category: Playsuit Pattern: Printed Neck: Round neck Sleeves: Short sleeves Top fabri... |
| 14   | no  | 13270464   | -     | 0.243 | Product: Sweet Dreams Women Charcoal Grey Solid Regular Fit Workout Shorts Brand: Sweet Dreams Color: Charcoal Category: Sports shorts Pattern: Solid Length: Above knee Top fabr... |
| 15   | no  | 17919758   | -     | 0.238 | Product: ONLY Women Pink Self Design Round Neck Cotton Jumpsuit Brand: ONLY Color: Pink Category: Playsuit Pattern: Self design Neck: Round neck Sleeves: Short sleeves Top fabri... |
| 16   | no  | 14166398   | -     | 0.230 | Product: Sweet Dreams Women Charcoal Grey Skinny Fit High-Rise Tight Fit Sports Shorts Brand: Sweet Dreams Color: Charcoal Category: Sports shorts Pattern: Solid Length: Above k... |
| 17   | no  | 19231232   | -     | 0.215 | Product: Sweet Dreams Women Grey Humor & Comic Printed Sweatshirt Brand: Sweet Dreams Color: Grey Category: Pullover Pattern: Humour and comic printed Neck: Round neck Sleeves: ... |
| 18   | no  | 17171608   | -     | 0.181 | Product: QUIERO Women Pretty Pink Self-Design Playsuit Brand: QUIERO Color: Pink Category: Playsuit Pattern: Self design Neck: V-neck Sleeves: Long sleeves Top fabric: Polyester... |
| 19   | no  | 15301014   | -     | 0.178 | Product: Athena Women Pretty Pink Sleek Jumpsuit Brand: Athena Color: Pink Category: Playsuit Pattern: Solid Neck: Round neck Sleeves: Long sleeves Top fabric: Polyester Occasio... |
| 20   | no  | 13611470   | -     | 0.175 | Product: 20Dresses Women Pretty Pink Printed Playsuit Brand: 20Dresses Color: Peach Category: Playsuit Pattern: Printed Neck: V-neck Sleeves: Long sleeves Top fabric: Polyester ... |
| 21   | no  | 16466494   | -     | 0.139 | Product: People Pink Basic Jumpsuit Brand: People Color: Pink Category: Basic jumpsuit Pattern: Solid Neck: Shirt collar Sleeves: Short sleeves Top fabric: Viscose rayon Occasio... |
| 22   | no  | 18368472   | -     | 0.136 | Product: 20Dresses Pink Basic Jumpsuit Brand: 20Dresses Color: Pink Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves: Sleeveless Top fabric: Cotton Occasion: Cas... |
| 23   | no  | 11364296   | -     | 0.130 | Product: SASSAFRAS Women Dusty Pink Solid Basic Jumpsuit Brand: SASSAFRAS Color: Pink Category: Basic jumpsuit Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless Top fabri... |
| 24   | no  | 15381904   | -     | 0.128 | Product: Berrylush Women Pink Solid Ruffled Jumpsuit Brand: Berrylush Color: Pink Category: Basic jumpsuit Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless Top fabric: P... |
| 25   | no  | 17605228   | -     | 0.128 | Product: Berrylush Women Red & White Halter Neck Floral Print Playsuit Brand: Berrylush Color: Red Category: Playsuit Pattern: Printed Neck: Halter neck Sleeves: Sleeveless Top ... |
| 26   | no  | 16642084   | -     | 0.125 | Product: 20Dresses Pink Dancing Through The Night Jumpsuit Brand: 20Dresses Color: Pink Category: Basic jumpsuit Pattern: Solid Neck: Square neck Sleeves: Short sleeves Top fabr... |
| 27   | no  | 17813700   | -     | 0.116 | Product: Trendyol Women Peach-Coloured & Grey Tropical Print Playsuit Brand: Trendyol Color: Peach Category: Playsuit Pattern: Printed Neck: Shirt collar Sleeves: Sleeveless Top... |
| 28   | no  | 14708574   | -     | 0.113 | Product: IX IMPRESSION Orange & Navy Blue Printed Tie-Up Jumpsuit Brand: IX IMPRESSION Color: Orange Category: Playsuit Pattern: Printed Neck: Shoulder straps Sleeves: Sleeveles... |
| 29   | no  | 16560336   | -     | 0.099 | Product: AND Women Blue & Pink Off-Shoulder Printed Jumpsuit Brand: AND Color: Blue Category: Playsuit Pattern: Printed Neck: Off-shoulder Sleeves: Three-quarter sleeves Top fab... |
| 30   | no  | 13558724   | -     | 0.099 | Product: People Women Pink Solid Culotte Jumpsuit Brand: People Color: Pink Category: Culotte jumpsuit Pattern: Solid Neck: Round neck Sleeves: Sleeveless Top fabric: Viscose ra... |

### Question 7/50

**Query:** I'm looking for Kurta set by Vishudh.

**Relevant docs:** `['13536726', '15997054', '18262138', '13119222', '18263032', '15820432', '15639890', '18929144']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.267     | 1.000  | 0.250 | 0.598 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 13799826   | -     | 1.000 | Product: Vishudh Women Grey & Gold-Coloured Checked Kurta with Trousers & Dupatta Brand: Vishudh Color: Grey Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: W... |
| 2    | no  | 18688392   | -     | 0.991 | Product: Vishudh Women Printed Kurta with Dupatta Brand: Vishudh Color: Red Category: Kurta set Top type: Kurti Bottom type: Trousers Dupatta: With dupatta Pattern: Striped embr... |
| 3    | no  | 17656860   | -     | 0.954 | Product: Vishudh Women Turquoise Blue Floral Printed Kurta Trouser With Dupatta Brand: Vishudh Color: Turquoise Blue Category: Kurta set Top type: Kurta Bottom type: Trousers Du... |
| 4    | yes | 18929144   | -     | 0.949 | Product: Vishudh Women Purple Ethnic Straight Kurta with Trousers & With Dupatta Brand: Vishudh Color: Purple Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: ... |
| 5    | no  | 17132180   | -     | 0.940 | Product: Vishudh Women Black & Teal Blue Checked Pure Cotton Kurta with Palazzo & Dupatta Brand: Vishudh Color: Black Category: Kurta set Top type: Kurti Bottom type: Trousers D... |
| 6    | yes | 18262138   | -     | 0.933 | Product: Vishudh Women Yellow & Grey Ethnic Motifs Kurta with Trouser and Jacket Brand: Vishudh Color: Yellow Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: ... |
| 7    | yes | 13536726   | -     | 0.929 | Product: Vishudh Women Yellow & Off-White Printed Kurta with Trousers & Dupatta Brand: Vishudh Color: Yellow Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: W... |
| 8    | no  | 16858486   | -     | 0.921 | Product: Vishudh Women Red Embroidered Pure Cotton Kurta with Trousers Brand: Vishudh Color: Red Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Solid striped... |
| 9    | no  | 13975624   | -     | 0.907 | Product: Vishudh Women Off-White Checked Kurta with Palazzo and Dupatta Brand: Vishudh Color: Off White Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With d... |
| 10   | no  | 14860664   | -     | 0.906 | Product: Vishudh Women Black Regular Printed Kurta with Palazzos Brand: Vishudh Color: Black Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Checked yoke desi... |
| 11   | yes | 15639890   | -     | 0.895 | Product: Vishudh Women Green & White Floral Printed Regular Kurta With Trousers & Dupatta Brand: Vishudh Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers D... |
| 12   | no  | 18261878   | -     | 0.873 | Product: Vishudh Women Blue Floral Printed Kurta with Palazzos & With Dupatta Brand: Vishudh Color: Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With ... |
| 13   | yes | 15997054   | -     | 0.852 | Product: Vishudh Women Yellow Floral Embroidered Regular Kurta with Palazzos Brand: Vishudh Color: Yellow Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Flor... |
| 14   | yes | 15820432   | -     | 0.851 | Product: Vishudh Women Off White Embroidered Regular Pure Cotton Kurta with Palazzo Brand: Vishudh Color: Off White Category: Kurta set Top type: Kurta Bottom type: Palazzos Pat... |
| 15   | no  | 7572969    | -     | 0.851 | Product: Vishudh Women Red & Orange Self Design Kurta with Palazzos Brand: Vishudh Color: Red Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Floral self desi... |
| 16   | no  | 16123926   | -     | 0.846 | Product: Vishudh Women Mauve Floral Embroidered Kurta with Skirt & With Dupatta Brand: Vishudh Color: Mauve Category: Kurta set Top type: Kurta Bottom type: Skirt Dupatta: With ... |
| 17   | no  | 9673749    | -     | 0.837 | Product: Vishudh Women Turquoise Blue & Gold-Toned Printed Kurti with Palazzos Brand: Vishudh Color: Turquoise Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos Pat... |
| 18   | no  | 9867983    | -     | 0.831 | Product: Vishudh Women Navy Blue Floral Printed Regular Pure Cotton Kurta with Palazzos Brand: Vishudh Color: Navy Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos... |
| 19   | yes | 18263032   | -     | 0.829 | Product: Vishudh Women Checked Pure Cotton Kurta with Trouser Brand: Vishudh Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Checked Shape: A-lin... |
| 20   | no  | 18929396   | -     | 0.826 | Product: Vishudh Women Pink Thread Work Kurta with Trousers & Jacket Brand: Vishudh Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Solid Shape: A... |
| 21   | no  | 17445358   | -     | 0.807 | Product: Vishudh Women Purple Printed Kurta with Sharara & With Dupatta Brand: Vishudh Color: Purple Category: Kurta set Top type: Kurta Bottom type: Sharara Dupatta: With dupat... |
| 22   | no  | 13433674   | -     | 0.803 | Product: Vishudh Women Sea Green & White Printed Kurta with Palazzos & Dupatta Brand: Vishudh Color: Sea Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta:... |
| 23   | no  | 7572958    | -     | 0.799 | Product: Vishudh Women Mauve Regular Kurta with Sharara & With Dupatta Brand: Vishudh Color: Mauve Category: Kurta set Top type: Kurta Bottom type: Sharara Dupatta: With dupatta... |
| 24   | yes | 13119222   | -     | 0.796 | Product: Vishudh Women Black & Off-White Checked Kurta with Palazzos Brand: Vishudh Color: Black Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Checked self ... |
| 25   | no  | 15335772   | -     | 0.759 | Product: Vishudh Women Yellow Striped Regular Pure Cotton Kurta with Palazzos Brand: Vishudh Color: Yellow Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Sol... |
| 26   | no  | 18929148   | -     | 0.703 | Product: Vishudh Women Turquoise Blue Pleated Kurti with Trouser & With Dupatta Brand: Vishudh Color: Turquoise Blue Category: Kurti set Top type: Kurti Bottom type: Dhoti pants... |
| 27   | no  | 14482494   | -     | 0.487 | Product: Vishudh Women Brown Ethnic Motifs Kurta Brand: Vishudh Color: Brown Pattern: Ethnic motifs woven design Shape: Straight Neck: Round neck Sleeves: Three-quarter regular ... |
| 28   | no  | 6613532    | -     | 0.465 | Product: Vishudh Women Navy Blue Yoke Design Straight Kurta Brand: Vishudh Color: Navy Blue Pattern: Ethnic motifs yoke design Shape: Straight Neck: Round neck Sleeves: Three-qu... |
| 29   | no  | 17445574   | -     | 0.463 | Product: Vishudh Women Blue Floral Embroidered Thread Work Cotton Kurta Brand: Vishudh Color: Blue Pattern: Floral embroidered Shape: Straight Neck: V-neck Sleeves: Three-quarte... |
| 30   | no  | 14194636   | -     | 0.456 | Product: Vishudh Women Grey & Red Floral Printed Kurta Brand: Vishudh Color: Grey Pattern: Floral printed Shape: Straight Neck: Round neck Sleeves: Three-quarter regular sleeves... |

### Question 8/50

**Query:** I'm looking for A-line by Ancestry.

**Relevant docs:** `['15407228', '19152780', '14873702']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.100     | 1.000  | 0.500 | 0.733 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 14873856   | -     | 1.000 | Product: Ancestry Women Grey & White Striped A-Line Top Brand: Ancestry Color: Grey Category: A-line Pattern: Vertical stripes striped Neck: V-neck Sleeves: Three-quarter regula... |
| 2    | yes | 15407228   | -     | 0.849 | Product: Ancestry Pink Pure Cotton Self Design A-Line Top Brand: Ancestry Color: Pink Category: A-line Pattern: Self design Neck: Round neck Sleeves: Three-quarter bell sleeves ... |
| 3    | yes | 14873702   | -     | 0.839 | Product: Ancestry Women Pink Melange Effect Pure Silk A-Line Longline Top Brand: Ancestry Color: Pink Category: A-line Pattern: Solid Neck: Cowl neck Sleeves: Long cuffed sleeve... |
| 4    | yes | 19152780   | -     | 0.821 | Product: Ancestry Women Pink Regular Top Brand: Ancestry Color: Pink Category: A-line Pattern: Self design solid Neck: Round neck Sleeves: Sleeveless no Length: Regular Top fabr... |
| 5    | no  | 19152792   | -     | 0.805 | Product: Ancestry Women Gold-Toned Longline Tailored Jacket Brand: Ancestry Color: Gold Category: Tailored jacket Pattern: Abstract self design Sleeves: Sleeveless Length: Longl... |
| 6    | no  | 15407188   | -     | 0.799 | Product: Ancestry Women Navy Blue & White Pure Cotton Checked Longline Tie-Up Shrug Brand: Ancestry Color: Navy Blue Pattern: Checked Sleeves: Short sleeves Length: Longline Hem... |
| 7    | no  | 14873748   | -     | 0.793 | Product: Ancestry Women Taupe Embroidered Longline Tie-Up Shrug Brand: Ancestry Color: Beige Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: Straight Top fabric: ... |
| 8    | no  | 17149934   | -     | 0.770 | Product: Ancestry Women Maroon Crop Tailored Jacket Brand: Ancestry Color: Maroon Category: Tailored jacket Pattern: Striped Sleeves: Long sleeves Length: Crop Hemline: Curved T... |
| 9    | no  | 17326880   | -     | 0.681 | Product: Ancestry Women Pink Regular Fit Pleated Chanderi Parallel Trousers Brand: Ancestry Color: Pink Category: Parallel trousers Pattern: Solid Length: Cropped Top fabric: Ot... |
| 10   | no  | 19152772   | -     | 0.679 | Product: Ancestry Mustard Embroidered Organza Dupatta Brand: Ancestry Color: Mustard Pattern: Solid embroidered Top fabric: Organza Occasion: Party Wash care: Dry clean             |
| 11   | no  | 15407164   | -     | 0.671 | Product: Ancestry White & Red Pure Cotton Geometric Printed Shirt Style Top Brand: Ancestry Color: White Category: Shirt style Pattern: Geometric printed Neck: Shirt collar Slee... |
| 12   | no  | 16588088   | -     | 0.662 | Product: Ancestry Pink & Black Ethnic Motifs Print Bishop Sleeves Modal Regular Top Brand: Ancestry Color: Pink Category: Regular Pattern: Ethnic motifs printed Neck: V-neck Sle... |
| 13   | no  | 17049154   | -     | 0.276 | Product: Anouk Navy Blue Checked Checked Pure Cotton A-line Top Brand: Anouk Color: Navy Blue Category: A-line Pattern: Checked Neck: Boat neck Sleeves: Short puff sleeves Lengt... |
| 14   | no  | 12135352   | -     | 0.268 | Product: Anouk Women Black Printed A-Line Top Brand: Anouk Color: Black Category: A-line Pattern: Floral printed Neck: Round neck Sleeves: Three-quarter cuffed sleeves Length: R... |
| 15   | no  | 17694118   | -     | 0.245 | Product: Antheaa Women Navy Blue & Black Abstract Printed Ruched Frilled A-Line Skirt Brand: Antheaa Color: Navy Blue Category: A-line Pattern: Abstract printed Length: Mini Hem... |
| 16   | no  | 17049100   | -     | 0.240 | Product: Anouk Mustard Yellow & White Checked Pure Cotton A-line Top Brand: Anouk Color: Mustard Category: A-line Pattern: Checked Neck: Boat neck Sleeves: Short puff sleeves Le... |
| 17   | no  | 13424892   | -     | 0.238 | Product: Antheaa Sea Green & Pink Yoke Embroidered Dobby Weave A-Line Top Brand: Antheaa Color: Sea Green Category: A-line Pattern: Ethnic motifs embroidered Neck: V-neck Sleeve... |
| 18   | no  | 9815193    | -     | 0.229 | Product: anayna Women White & Blue Printed A-Line Kurta Brand: anayna Color: White Pattern: Ethnic motifs printed Shape: A-line Neck: Round neck Sleeves: Sleeveless no Length: C... |
| 19   | no  | 18331422   | -     | 0.217 | Product: Anouk Pink & White Ethnic Motifs Print Pure Cotton Casual A-Line Top Brand: Anouk Color: Pink Category: A-line Pattern: Ethnic motifs printed Neck: Round neck Sleeves: ... |
| 20   | no  | 11197978   | -     | 0.205 | Product: Anouk Women Lime Green & Blue Printed A-Line Kurta Brand: Anouk Color: Lime Green Pattern: Floral printed Shape: A-line Neck: Round neck Sleeves: Three-quarter regular ... |
| 21   | no  | 13424874   | -     | 0.187 | Product: Antheaa Women Rust Brown & Black Embroidered Dobby Weave A-Line Top Brand: Antheaa Color: Rust Category: A-line Pattern: Ethnic motifs embroidered Neck: Round neck Slee... |
| 22   | no  | 17694106   | -     | 0.162 | Product: Antheaa Women Pink & Blue Floral Printed Accordian Pleated A-Line Skirt Brand: Antheaa Color: Pink Category: A-line Pattern: Floral printed Length: Knee length Hemline:... |
| 23   | no  | 13610084   | -     | 0.155 | Product: ANVI Be Yourself Women Red & White Printed Pleated A-Line Midi Skirt Brand: ANVI Be Yourself Color: Red Category: A-line Pattern: Geometric printed Length: Midi Hemline... |
| 24   | no  | 16272186   | -     | 0.154 | Product: Anouk X Earthful Women White & Pink Floral Printed A-Line Kurta Brand: Anouk Color: White Pattern: Floral printed Shape: A-line Neck: V-neck Sleeves: Long puff sleeves ... |
| 25   | no  | 13238592   | -     | 0.149 | Product: Anouk Women Coral Orange & White Cotton Floral Print Panelled A-Line Kurta with Gathers Brand: Anouk Color: Coral Pattern: Floral printed Shape: A-line Neck: Square nec... |
| 26   | no  | 17417200   | -     | 0.148 | Product: Anouk Women Red & White Bandhani Printed Angrakha Gotta Patti A-Line Kurta Brand: Anouk Color: Red Pattern: Bandhani printed Shape: A-line Neck: V-neck Sleeves: Three-q... |
| 27   | no  | 13248456   | -     | 0.143 | Product: anayna Women Red & Golden Printed Feeding Maternity A-Line Kurta Brand: anayna Color: Red Pattern: Ethnic motifs printed Shape: A-line Neck: Keyhole neck Sleeves: Three... |
| 28   | no  | 13238030   | -     | 0.139 | Product: Anouk Women Mustard Kurta Brand: Anouk Color: Mustard Pattern: Solid Shape: A-line Neck: V-neck Sleeves: Three-quarter puff sleeves Length: Calf length Hemline: High-lo... |
| 29   | no  | 7763575    | -     | 0.139 | Product: Anouk Women Red Floral Print A-Line Kurta Brand: Anouk Color: Red Pattern: Floral printed Shape: A-line Neck: Round neck Sleeves: Short cap sleeves Length: Calf length ... |
| 30   | no  | 18331124   | -     | 0.133 | Product: Anouk Yellow & White Floral Print Pure Cotton Regular Top Brand: Anouk Color: Yellow Category: A-line Pattern: Floral printed Neck: Round neck Sleeves: Sleeveless shoul... |

### Question 9/50

**Query:** Can you find something similar to "FASHOR Women Blue Geometric Printed Gotta Patti Khadi Kurta"?

**Relevant docs:** `['19140952']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 19140952   | -     | 1.000 | Product: FASHOR Women Blue Geometric Printed Gotta Patti Khadi Kurta Brand: FASHOR Color: Blue Pattern: Geometric printed Shape: A-line Neck: V-neck Sleeves: Three-quarter regul... |
| 2    | no  | 18964098   | -     | 0.540 | Product: FASHOR Women Turquoise Blue Geometric Printed Kurta Brand: FASHOR Color: Turquoise Blue Pattern: Geometric printed Shape: Straight Neck: Mandarin collar Sleeves: Short ... |
| 3    | no  | 18116634   | -     | 0.313 | Product: FASHOR Women Pink Ethnic Motifs Embroidered Empire Gotta Patti Pure Cotton Kurta with Trousers With Dupatta Brand: FASHOR Color: Pink Category: Kurta set Top type: Kurt... |
| 4    | no  | 19324632   | -     | 0.300 | Product: FASHOR Women Blue & White Yoke Design Straight Fit Kurta Brand: FASHOR Color: Blue Pattern: Striped yoke design Shape: Straight Neck: Round neck Sleeves: Three-quarter ... |
| 5    | no  | 18964110   | -     | 0.300 | Product: FASHOR Women Pink Printed Thread Work Pure Cotton Kurta with Trousers & With Dupatta Brand: FASHOR Color: Pink Category: Kurta set Top type: Kurta Bottom type: Trousers... |
| 6    | no  | 15047458   | -     | 0.262 | Product: FASHOR Women Multicoloured Ethnic Motifs Printed Mirror Work Kurta Brand: FASHOR Color: Multi Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck Sleeves: T... |
| 7    | no  | 16362760   | -     | 0.233 | Product: House of Pataudi Women Navy Blue Floral Printed Jashn Kurta with Palazzos & With Dupatta Brand: House of Pataudi Color: Navy Blue Category: Kurta set Top type: Kurta Bo... |
| 8    | no  | 19198414   | -     | 0.224 | Product: FASHOR Women Navy Blue Floral Embroidered Thread Work Kurta Brand: FASHOR Color: Navy Blue Pattern: Floral embroidered Shape: A-line Neck: Round neck Sleeves: Three-qua... |
| 9    | no  | 16486578   | -     | 0.210 | Product: FASHOR Women Maroon Geometric Printed Flared Sleeves Anarkali Kurta Brand: FASHOR Color: Maroon Pattern: Geometric printed Shape: Anarkali Neck: Round neck Sleeves: Thr... |
| 10   | no  | 19300542   | -     | 0.209 | Product: PARCHHAI Women Blue Geometric Printed Top Brand: PARCHHAI Color: Blue Category: Regular Pattern: Geometric printed Neck: Round neck Sleeves: Three-quarter regular sleev... |
| 11   | no  | 17624890   | -     | 0.194 | Product: KAAJH Women Blue Ethnic Motifs Printed Mirror Work Pure Cotton Kurta with Trousers & With Dupatta Brand: KAAJH Color: Blue Category: Kurta set Top type: Kurta Bottom ty... |
| 12   | no  | 16362738   | -     | 0.193 | Product: House of Pataudi Women Blue & White Floral Embroidered Jashn Kurta Brand: House of Pataudi Color: Blue Pattern: Floral embroidered Shape: Straight Neck: Round neck Slee... |
| 13   | no  | 18787430   | -     | 0.190 | Product: ADEESHA Women Turquoise Blue Printed Empire Gotta Patti Kurti with Palazzos Brand: ADEESHA Color: Turquoise Blue Category: Kurti Top type: Kurti Bottom type: Palazzos P... |
| 14   | no  | 16884160   | -     | 0.167 | Product: Rajnandini Women Blue Abstract Kurta with Patiala & Dupatta Brand: Rajnandini Color: Blue Category: Kurta set Top type: Kurta Bottom type: Patiala Dupatta: With dupatta... |
| 15   | no  | 16931502   | -     | 0.166 | Product: all about you Women Blue & Yellow Ethnic Motifs Printed Kurta Brand: all about you Color: Blue Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck Sleeves: ... |
| 16   | no  | 18720202   | -     | 0.164 | Product: FASHOR Women Purple Ethnic Motifs Printed Mirror Work Kurta Brand: FASHOR Color: Purple Pattern: Ethnic motifs printed Shape: Straight Neck: Mandarin collar Sleeves: Th... |
| 17   | no  | 18778410   | -     | 0.158 | Product: FASHOR Women Multicoloured & nirvana Chevron Printed Thread Work Kurta Brand: FASHOR Color: Multi Pattern: Chevron printed Shape: A-line Neck: Round neck Sleeves: Short... |
| 18   | no  | 17447640   | -     | 0.152 | Product: Khushal K Women White Ethnic Motifs Printed Gotta Patti Kurta with Palazzos & With Dupatta Brand: Khushal K Color: White Category: Kurta set Top type: Kurta Bottom type... |
| 19   | no  | 16362862   | -     | 0.150 | Product: House of Pataudi Women Sea Green & Pink Ethnic Motifs Printed Straight Kurta Brand: House of Pataudi Color: Sea Green Pattern: Ethnic motifs printed Shape: Straight Nec... |
| 20   | no  | 19357994   | -     | 0.150 | Product: FASHOR Women Pink Ethnic Motifs Kurta Brand: FASHOR Color: Pink Pattern: Ethnic motifs woven design Shape: Straight Neck: Round neck Sleeves: Three-quarter regular slee... |
| 21   | no  | 13369436   | -     | 0.144 | Product: YASH GALLERY Women Navy Blue & White Cotton Printed A-Line Kurta Brand: YASH GALLERY Color: Navy Blue Pattern: Geometric printed Shape: A-line Neck: Mandarin collar Sle... |
| 22   | no  | 11369616   | -     | 0.130 | Product: W Women Blue & Silver Printed Straight Kurta Brand: W Color: Blue Pattern: Ethnic motifs printed Shape: Straight Neck: Keyhole neck Sleeves: Three-quarter regular sleev... |
| 23   | no  | 11636314   | -     | 0.122 | Product: Shae by SASSAFRAS Women Blue & Off-White Printed Anarkali Kurta Brand: Shae by SASSAFRAS Color: Blue Pattern: Ethnic motifs printed Shape: Anarkali Neck: Keyhole neck S... |
| 24   | no  | 16266664   | -     | 0.120 | Product: House of Pataudi Women Black & White Ethnic Motifs Printed Pure Cotton A-Line Kurta Brand: House of Pataudi Color: Black Pattern: Ethnic motifs printed Shape: A-line Ne... |
| 25   | no  | 11369528   | -     | 0.118 | Product: W Women Blue & Black Printed Straight Kurta Brand: W Color: Blue Pattern: Geometric printed Shape: Straight Neck: Round neck Sleeves: Three-quarter regular sleeves Leng... |
| 26   | no  | 15889778   | -     | 0.114 | Product: HERE&NOW Women Blue & White Ethnic Motifs Printed Kurta Brand: HERE&NOW Color: Blue Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck Sleeves: Three-quart... |
| 27   | no  | 19168608   | -     | 0.110 | Product: RANGMANCH BY PANTALOONS Women Blue Ethnic Motifs Kurta Brand: RANGMANCH BY PANTALOONS Color: Blue Pattern: Ethnic motifs woven design Shape: Straight Neck: Mandarin col... |
| 28   | no  | 11531500   | -     | 0.107 | Product: Anubhutee Women Navy Blue & Off-White Bandhani Print Kurta with Palazzos Brand: Anubhutee Color: Navy Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos Pat... |
| 29   | no  | 16984006   | -     | 0.103 | Product: FASHOR Women Pink Ethnic Motifs Yoke Design Chanderi Silk Chanderi Silk Kurta Brand: FASHOR Color: Pink Pattern: Ethnic motifs yoke design Shape: Straight Neck: Round n... |
| 30   | no  | 17514330   | -     | 0.100 | Product: Vishudh Women Blue Printed Anarkali Kurta Brand: Vishudh Color: Turquoise Blue Pattern: Abstract printed Shape: Anarkali Neck: Mandarin collar Sleeves: Short roll-up sl... |

### Question 10/50

**Query:** Show me Blue Tailored jacket from Darzi.

**Relevant docs:** `['14460680']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 0.750             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 14460680   | -     | 1.000 | Product: Darzi Women Blue Tailored Jacket Brand: Darzi Color: Blue Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: P... |
| 2    | no  | 14460654   | -     | 0.790 | Product: Darzi Women Red Tailored Jacket Brand: Darzi Color: Red Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Pol... |
| 3    | no  | 14460662   | -     | 0.730 | Product: Darzi Women Maroon Solid Longline Tailored Jacket Brand: Darzi Color: Maroon Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: St... |
| 4    | no  | 17666226   | -     | 0.726 | Product: Darzi Women Maroon Tailored Jacket Brand: Darzi Color: Maroon Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabri... |
| 5    | no  | 17666218   | -     | 0.709 | Product: Darzi Women Yellow Tailored Jacket Brand: Darzi Color: Yellow Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabri... |
| 6    | no  | 17665710   | -     | 0.708 | Product: Darzi Women Yellow Striped Fleece Tailored Jacket Brand: Darzi Color: Yellow Category: Tailored jacket Pattern: Colourblocked striped Sleeves: Three-quarter sleeves Len... |
| 7    | no  | 17513236   | -     | 0.675 | Product: Darzi Women Multicoloured Crop Tailored Jacket Brand: Darzi Color: Multi Category: Tailored jacket Pattern: Graphic printed Sleeves: Long sleeves Length: Crop Hemline: ... |
| 8    | no  | 14460688   | -     | 0.568 | Product: Darzi Women Brown Solid Longline Duster Jacket Brand: Darzi Color: Brown Category: Duster jacket Pattern: Solid colourblocked Sleeves: Long sleeves Length: Longline Hem... |
| 9    | no  | 17665702   | -     | 0.557 | Product: Darzi Women Navy Blue Colourblocked Fleece Bomber with Embroidered Jacket Brand: Darzi Color: Navy Blue Category: Bomber Pattern: Solid colourblocked Sleeves: Sleeveles... |
| 10   | no  | 15784540   | -     | 0.399 | Product: Yaadleen Women Turquoise Blue Floral Tailored Jacket Brand: Yaadleen Color: Turquoise Blue Category: Tailored jacket Pattern: Floral printed Sleeves: Three-quarter slee... |
| 11   | no  | 15859778   | -     | 0.279 | Product: Zink London Women Blue Solid Tailored Jacket Brand: Zink London Color: Blue Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Stra... |
| 12   | no  | 13163000   | -     | 0.257 | Product: FableStreet Women Blue Self Design Tailored Jacket Brand: FableStreet Color: Blue Category: Tailored jacket Pattern: Self design Sleeves: Long sleeves Length: Longline ... |
| 13   | no  | 11445774   | -     | 0.222 | Product: Darzi Women Charcoal Grey Solid Hooded Sweatshirt Brand: Darzi Color: Charcoal Category: Front-open Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Heml... |
| 14   | no  | 11446072   | -     | 0.210 | Product: Darzi Women Charcoal Grey Solid Hooded Sweatshirt Brand: Darzi Color: Charcoal Category: Front-open Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Heml... |
| 15   | no  | 11789162   | -     | 0.200 | Product: Darzi Women Black & White Sheer Floral Print Open Front Shrug Brand: Darzi Color: Black Pattern: Printed Sleeves: Three-quarter sleeves Length: Longline Hemline: Straig... |
| 16   | no  | 14364140   | -     | 0.194 | Product: Mast & Harbour Women Blue Colourblocked Tailored Jacket Brand: Mast & Harbour Color: Blue Category: Tailored jacket Pattern: Colourblocked Sleeves: Long sleeves Length:... |
| 17   | no  | 13449644   | -     | 0.180 | Product: DODO & MOA Women Navy Blue Checked Asymmetric Closure Pure Cotton Tailored Jacket Brand: DODO & MOA Color: Navy Blue Category: Tailored jacket Pattern: Checked Sleeves:... |
| 18   | no  | 16005808   | -     | 0.176 | Product: Juelle Women Blue Tailored Jacket Brand: Juelle Color: Blue Category: Tailored jacket Pattern: Abstract printed Sleeves: Three-quarter sleeves Length: Regular Hemline: ... |
| 19   | no  | 13645548   | -     | 0.163 | Product: Diwaah Women Multicoloured Embellished Tailored Jacket Brand: Diwaah Color: Multi Category: Tailored jacket Pattern: Self design Sleeves: Long sleeves Length: Crop Heml... |
| 20   | no  | 13698728   | -     | 0.163 | Product: Diwaah Women Black Embellished Tailored Jacket Brand: Diwaah Color: Black Category: Tailored jacket Pattern: Self design Sleeves: Long sleeves Length: Crop Hemline: Str... |
| 21   | no  | 12299686   | -     | 0.157 | Product: Darzi Women Maroon Solid Asymmetric Flared Skirt Brand: Darzi Color: Maroon Category: Flared Pattern: Solid Length: Midi Hemline: Asymmetric Top fabric: Polyester Occas... |
| 22   | no  | 15956494   | -     | 0.157 | Product: Missguided Women Blue Striped Pure Cotton Tailored Jacket Brand: Missguided Color: Blue Category: Tailored jacket Pattern: Striped Sleeves: Long sleeves Length: Regular... |
| 23   | no  | 15851444   | -     | 0.156 | Product: URBANIC Women Blue & White Dyed Extra Relaxed Fit Longline Sherpa Tailored Jacket Brand: URBANIC Color: Blue Category: Tailored jacket Pattern: Tie and dye printed Slee... |
| 24   | no  | 15811466   | -     | 0.155 | Product: DECHEN Women Navy Blue Textured Tailored Jacket Brand: DECHEN Color: Navy Blue Category: Tailored jacket Pattern: Self design Sleeves: Long sleeves Length: Regular Heml... |
| 25   | no  | 14500422   | -     | 0.151 | Product: Darzi Women Black Solid A-Line Maxi Skirt Brand: Darzi Color: Black Category: A-line Pattern: Solid Length: Maxi Hemline: Flared Top fabric: Polyester Occasion: Casual ... |
| 26   | no  | 18787832   | -     | 0.148 | Product: Tokyo Talkies Women Blue Washed Denim Jacket Brand: Tokyo Talkies Color: Blue Category: Tailored jacket Pattern: Washed printed Sleeves: Sleeveless Length: Regular Heml... |
| 27   | no  | 11445992   | -     | 0.147 | Product: Darzi Women Maroon Solid Hooded Sweatshirt Brand: Darzi Color: Maroon Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: Straig... |
| 28   | no  | 15851900   | -     | 0.146 | Product: URBANIC Women Blue Solid Hooded Faux Fur Jacket Brand: URBANIC Color: Blue Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Strai... |
| 29   | no  | 16019732   | -     | 0.133 | Product: RANGMANCH BY PANTALOONS Women Navy Blue Geometric Acrylic Longline Tailored Jacket Brand: RANGMANCH BY PANTALOONS Color: Navy Blue Category: Tailored jacket Pattern: Ge... |
| 30   | no  | 15962326   | -     | 0.133 | Product: MANGO Women Blue Solid Denim Shacket Brand: MANGO Color: Blue Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabri... |

### Question 11/50

**Query:** Can you find something similar to "U.S. Polo Assn. Women Beige Solid Biker Jacket"?

**Relevant docs:** `['13703470']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 13703470   | -     | 1.000 | Product: U.S. Polo Assn. Women Beige Solid Biker Jacket Brand: U.S. Polo Assn. Color: Beige Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: ... |
| 2    | no  | 13690162   | -     | 0.502 | Product: U.S. Polo Assn. Women Black Solid Quilted Jacket Brand: U.S. Polo Assn. Color: Black Category: Quilted jacket Pattern: Solid Sleeves: Sleeveless Length: Crop Hemline: S... |
| 3    | no  | 15555424   | -     | 0.365 | Product: BEAVER Women Black Solid Biker Jacket Brand: BEAVER Color: Black Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabri... |
| 4    | no  | 16220536   | -     | 0.324 | Product: 20Dresses Women Beige Biker Jacket Brand: 20Dresses Color: Beige Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabri... |
| 5    | no  | 15555432   | -     | 0.301 | Product: BEAVER Women Black Solid Crop Biker Jacket Brand: BEAVER Color: Black Category: Biker jacket Pattern: Solid Sleeves: Short sleeves Length: Crop Hemline: Curved Top fabr... |
| 6    | no  | 2185647    | -     | 0.289 | Product: U.S.Polo Assn. Women Grey Longline Shrug Brand: U.S. Polo Assn. Women Color: Grey Pattern: Solid Sleeves: Sleeveless Length: Longline Hemline: Asymmetric Top fabric: Vi... |
| 7    | no  | 15555446   | -     | 0.277 | Product: BEAVER Women Black Crop Biker Jacket Brand: BEAVER Color: Black Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Crop Hemline: Straight Top fabric: S... |
| 8    | no  | 14355398   | -     | 0.255 | Product: Roadster Women Chic Brown Solid Biker Jacket Brand: Roadster Color: Brown Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight ... |
| 9    | no  | 14355452   | -     | 0.244 | Product: Roadster Women Chic Brown Solid Biker Jacket Brand: Roadster Color: Brown Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight ... |
| 10   | no  | 14017334   | -     | 0.231 | Product: Leather Retail Women Brown Solid Lightweight Biker Jacket Brand: Leather Retail Color: Brown Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular... |
| 11   | no  | 17983210   | -     | 0.227 | Product: U S Polo Assn Women White Striped Hood Sweatshirt Brand: U.S. Polo Assn. Color: White Category: Front-open Pattern: Striped Neck: Hood Sleeves: Long sleeves Length: Reg... |
| 12   | no  | 15564338   | -     | 0.219 | Product: Puma Women Beige Bomber Jacket Brand: Puma Color: Beige Category: Bomber Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Polyester Oc... |
| 13   | no  | 17855178   | -     | 0.170 | Product: H&M Women Beige Detachable Sleeve Windcheater Jacket Brand: H&M Color: Beige Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Strai... |
| 14   | no  | 15800520   | -     | 0.168 | Product: FabAlley Women Grey Solid Crop Biker Jacket Brand: FabAlley Color: Grey Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Crop Hemline: Curved Top fab... |
| 15   | no  | 14263292   | -     | 0.165 | Product: AMERICAN EAGLE OUTFITTERS Women Black Solid Denim Jacket Brand: AMERICAN EAGLE OUTFITTERS Color: Black Category: Denim jacket Pattern: Washed solid Sleeves: Long sleeve... |
| 16   | no  | 14829462   | -     | 0.154 | Product: Campus Sutra Women Tan Suede Windcheater Biker Jacket Brand: Campus Sutra Color: Tan Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline... |
| 17   | no  | 14355346   | -     | 0.151 | Product: Roadster Women Stylish Black Solid Biker Jacket Brand: Roadster Color: Black Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straig... |
| 18   | no  | 15380284   | -     | 0.140 | Product: Fort Collins Women Beige Solid Padded Jacket Brand: Fort Collins Color: Beige Category: Padded jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Stra... |
| 19   | no  | 15038638   | -     | 0.130 | Product: Campus Sutra Women Brown Suede Windcheater Crop Biker Jacket Brand: Campus Sutra Color: Brown Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Crop H... |
| 20   | no  | 15027768   | -     | 0.130 | Product: Campus Sutra Women Grey Solid Biker Jacket Brand: Campus Sutra Color: Grey Category: Biker jacket Pattern: Solid Sleeves: Sleeveless Length: Regular Hemline: Straight T... |
| 21   | no  | 15673462   | -     | 0.127 | Product: Missguided Women Beige Solid Longline Hooded Puffer Jacket Brand: Missguided Color: Beige Category: Puffer jacket Pattern: Solid Sleeves: Long sleeves Length: Longline ... |
| 22   | no  | 14355478   | -     | 0.123 | Product: Roadster Women Black Solid Coated Biker Jacket with Patchwork Brand: Roadster Color: Black Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular H... |
| 23   | no  | 15673166   | -     | 0.121 | Product: Missguided Women Black Solid Biker Jacket Brand: Missguided Color: Black Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight T... |
| 24   | no  | 14356188   | -     | 0.119 | Product: Roadster Women Beige Solid Longline Sherpa Jacket Brand: Roadster Color: Beige Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: ... |
| 25   | no  | 10829334   | -     | 0.119 | Product: Tokyo Talkies Women Beige Solid Puffer Jacket Brand: Tokyo Talkies Color: Beige Category: Puffer jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Cu... |
| 26   | no  | 15846080   | -     | 0.114 | Product: H&M Women Beige Quilted Faux Shearling Gilet Brand: H&M Color: Beige Category: Quilted jacket Pattern: Solid Sleeves: Sleeveless Length: Regular Hemline: Straight Top f... |
| 27   | no  | 17069364   | -     | 0.111 | Product: Jockey Women Black Solid Hooded Sporty Jacket Brand: Jockey Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight ... |
| 28   | no  | 16103252   | -     | 0.110 | Product: URBANIC Women Beige Buttoned Tailored Jacket Brand: URBANIC Color: Beige Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straigh... |
| 29   | no  | 16103226   | -     | 0.110 | Product: URBANIC Women Beige Red Colourblocked Bomber Jacket Brand: URBANIC Color: Beige Category: Bomber Pattern: Colourblocked Sleeves: Long sleeves Length: Regular Hemline: H... |
| 30   | no  | 15673400   | -     | 0.101 | Product: Missguided Women Black Solid Longline Biker Jacket Brand: Missguided Color: Black Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: ... |

### Question 12/50

**Query:** Does Mitera have any Bandhani for a festive occasion within 5500?

**Relevant docs:** `['15637468']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 15637468   | -     | 1.000 | Product: Mitera Yellow & Multicoloured Floral Printed Silk Blend Saree Brand: Mitera Color: Yellow Category: Bandhani Pattern: Floral printed Occasion: Festive Wash care: Dry clean |
| 2    | no  | 15442988   | -     | 0.987 | Product: Mitera Blue Embellished Embroidered Ready to Wear Bandhani Saree Brand: Mitera Color: Blue Category: Bandhani Pattern: Embellished embroidered Occasion: Party Wash care... |
| 3    | no  | 15519332   | -     | 0.759 | Product: Mitera Purple & Pink Bandhani Saree Brand: Mitera Color: Purple Category: Bandhani Pattern: Bandhani printed Occasion: Traditional Wash care: Dry clean                     |
| 4    | no  | 16331704   | -     | 0.743 | Product: Mitera Yellow & Red Bandhani Saree Brand: Mitera Color: Yellow Category: Bandhani Pattern: Solid Occasion: Traditional Wash care: Dry clean                                 |
| 5    | no  | 17141480   | -     | 0.672 | Product: Mitera Women Olive Green Embroidered Pure Georgette Bandhani Saree Brand: Mitera Color: Olive Category: Bandhani Pattern: Bandhani printed Occasion: Traditional Wash ca... |
| 6    | no  | 17325496   | -     | 0.638 | Product: Mitera Green & Off-White Embroidered Unstitched Dress Material Brand: Mitera Color: Green Category: Dress Pattern: Ethnic motifs Bottom fabric: Poly georgette Dupatta f... |
| 7    | no  | 16286084   | -     | 0.633 | Product: Mitera Black & Gold-Toned Unstitched Dress Material Brand: Mitera Color: Black Category: Dress Pattern: Floral Bottom fabric: Silk blend Dupatta fabric: Silk blend Occa... |
| 8    | no  | 15519378   | -     | 0.632 | Product: Mitera Navy Blue Bandhani Printed Saree Brand: Mitera Color: Navy Blue Category: Bandhani Pattern: Bandhani printed Occasion: Traditional Wash care: Dry clean              |
| 9    | no  | 17325492   | -     | 0.629 | Product: Mitera Green & Golden Embroidered Unstitched Dress Material Brand: Mitera Color: Green Category: Dress Pattern: Ethnic motifs Bottom fabric: Poly georgette Dupatta fabr... |
| 10   | no  | 17325498   | -     | 0.603 | Product: Mitera Maroon & Golden Embroidered Unstitched Dress Material Brand: Mitera Color: Maroon Category: Dress Pattern: Floral Bottom fabric: Poly georgette Dupatta fabric: P... |
| 11   | no  | 12668552   | -     | 0.599 | Product: Mitera Turquoise Blue & Red Woven Design Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Turquoise Blue Dupatta: With dupatta Pattern: Woven... |
| 12   | no  | 12668502   | -     | 0.594 | Product: Mitera Pink & Blue Woven Design Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Pink Dupatta: With dupatta Pattern: Woven design Sleeves: Th... |
| 13   | no  | 17325490   | -     | 0.584 | Product: Mitera Black & Golden Embroidered Unstitched Dress Material Brand: Mitera Color: Black Category: Dress Pattern: Floral Bottom fabric: Poly georgette Dupatta fabric: Pol... |
| 14   | no  | 17206828   | -     | 0.577 | Product: Mitera Black & Beige Embroidered Unstitched Dress Material Brand: Mitera Color: Black Category: Dress Pattern: Ethnic motifs Bottom fabric: Shantoon Dupatta fabric: Pol... |
| 15   | no  | 16171474   | -     | 0.571 | Product: Mitera Red & Gold-Toned Dupion Silk Banarasi Jacquard Unstitched Dress Material Brand: Mitera Color: Red Category: Dress Pattern: Ethnic motifs Bottom fabric: Satin Dup... |
| 16   | no  | 16286120   | -     | 0.567 | Product: Mitera Red & Green Silk Blend Unstitched Dress Material Brand: Mitera Color: Red Category: Dress Pattern: Floral Bottom fabric: Silk blend Dupatta fabric: Silk blend Oc... |
| 17   | no  | 17141474   | -     | 0.554 | Product: Mitera Women Yellow Embroidered Pure Georgette Bandhani Saree Brand: Mitera Color: Yellow Category: Bandhani Pattern: Bandhani printed Occasion: Traditional Wash care: ... |
| 18   | no  | 17392504   | -     | 0.552 | Product: Mitera Blue & Gold-Toned Ethnic Motifs Zari Organza Kanjeevaram Saree Brand: Mitera Color: Blue Category: Kanjeevaram Pattern: Ethnic motifs woven design Occasion: Fest... |
| 19   | no  | 11530694   | -     | 0.503 | Product: Mitera Peach-Coloured & Gold-Toned Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Peach Dupatta: With dupatta Pattern: Embroide... |
| 20   | no  | 16595928   | -     | 0.471 | Product: Mitera Maroon & Golden Ethnic Motifs Saree with Zari Work Brand: Mitera Color: Maroon Category: Saree Pattern: Ethnic motifs woven design Occasion: Festive Wash care: D... |
| 21   | no  | 18302882   | -     | 0.451 | Product: Mitera Teal & Gold-Toned Woven Design Silk Blend Saree Brand: Mitera Color: Teal Category: Saree Pattern: Woven design Occasion: Festive Wash care: Dry clean               |
| 22   | no  | 16311070   | -     | 0.448 | Product: Mitera Maroon & White Bandhani Printed Pure Georgette Saree Brand: Mitera Color: Maroon Category: Saree Pattern: Bandhani printed Occasion: Daily Wash care: Hand wash      |
| 23   | no  | 15012204   | -     | 0.424 | Product: Mitera Pink & Gold-Toned Woven Design Zari Silk Blend Banarasi Saree Brand: Mitera Color: Pink Category: Banarasi Pattern: Woven design Occasion: Festive Wash care: Dry... |
| 24   | no  | 16286118   | -     | 0.415 | Product: Mitera Navy Blue & Red Unstitched Dress Material Brand: Mitera Color: Navy Blue Category: Dress Pattern: Geometric Bottom fabric: Silk blend Dupatta fabric: Silk blend ... |
| 25   | no  | 18647316   | -     | 0.414 | Product: Mitera Blue & Black Embellished Sequinned Saree Brand: Mitera Color: Blue Category: Saree Pattern: Embellished Occasion: Festive Wash care: Hand wash                       |
| 26   | no  | 13515386   | -     | 0.403 | Product: Mitera Mustard Yellow & Red Embroidered Semi-Stitched Lehenga Set Brand: Mitera Color: Mustard Dupatta: With dupatta Pattern: Embroidered Neck: Round neck Sleeves: Shor... |
| 27   | no  | 14479084   | -     | 0.398 | Product: Mitera Red & Gold-Toned Zari Silk Blend Saree Brand: Mitera Color: Red Category: Saree Pattern: Solid Occasion: Festive Wash care: Dry clean                                |
| 28   | no  | 16967650   | -     | 0.361 | Product: Mitera Beige & Red Ethnic Motifs Zari Silk Cotton Saree Brand: Mitera Color: Beige Category: Saree Pattern: Ethnic motifs woven design Occasion: Festive Wash care: Mach... |
| 29   | no  | 16967652   | -     | 0.361 | Product: Mitera Gold-Toned & Pink Woven Design Saree Brand: Mitera Color: Gold Category: Saree Pattern: Woven design Occasion: Festive Wash care: Machine wash                       |
| 30   | no  | 18107770   | -     | 0.355 | Product: Mitera Orange & Gold-Toned Embellished Sequinned Pure Georgette Saree Brand: Mitera Color: Orange Category: Saree Pattern: Embellished embroidered Occasion: Festive Was... |

### Question 13/50

**Query:** Show me Pencil within a budget of 1500.

**Relevant docs:** `['15940138', '9552849', '15301318', '12086086', '18834976', '18454266', '15637548', '6629440']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 0.125  | 0.033 | 0.051 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 14011652   | -     | 1.000 | Product: FableStreet Black Mini Pencil Skirt Brand: FableStreet Color: Black Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Occasion: Formal Pockets: 1 Wash care... |
| 2    | no  | 17739956   | -     | 0.684 | Product: Kotty Women Black Solid Faux Leather Pencil Mini Skirts Brand: Kotty Color: Black Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Top fabric: Leather Occ... |
| 3    | no  | 18215398   | -     | 0.673 | Product: Popwings Women Camel Brown Pencil Slit Skirts Brand: Popwings Color: Camel Brown Category: Pencil Pattern: Solid Length: Above knee Hemline: Straight Top fabric: Polyes... |
| 4    | no  | 19072638   | -     | 0.658 | Product: DRAAX Fashions Women Maroon Solid Mini Pencil Formal Skirt Brand: DRAAX Fashions Color: Maroon Category: Pencil Pattern: Solid Length: Above knee Hemline: Straight Top ... |
| 5    | no  | 17403200   | -     | 0.635 | Product: BROADSTAR Women Black Solid Pencil Mini Skirt Brand: BROADSTAR Color: Black Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Top fabric: Viscose rayon Occ... |
| 6    | no  | 13496046   | -     | 0.632 | Product: FableStreet Olive Green Knitted Pencil Skirt Brand: FableStreet Color: Olive Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Occasion: Formal Wash... |
| 7    | no  | 19181106   | -     | 0.607 | Product: Bitterlime Women Olive Green & Black Colourblocked Pencil Skirts Brand: Bitterlime Color: Olive Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight To... |
| 8    | no  | 17306262   | -     | 0.598 | Product: Purple Feather Women Black Solid Stretchable Midi Pencil Skirt Brand: Purple Feather Color: Black Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fab... |
| 9    | no  | 17899166   | -     | 0.592 | Product: PATRORNA Women Green Solid Pencil Above Knee-Length Skirts Brand: PATRORNA Color: Green Category: Pencil Pattern: Solid Length: Above knee Hemline: Curved Top fabric: C... |
| 10   | no  | 1294879    | -     | 0.545 | Product: Purple Feather Black Pencil Skirt With Back Slit Brand: Purple Feather Color: Black Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Occasion: Form... |
| 11   | no  | 17365546   | -     | 0.528 | Product: BROADSTAR Women Black Solid Pencil Knee Length Skirt Brand: BROADSTAR Color: Black Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Top fabric: Cot... |
| 12   | no  | 18173820   | -     | 0.525 | Product: Kotty Women Brown Solid Faux Leather Mini Skirt Brand: Kotty Color: Brown Category: Pencil Pattern: Solid Length: Above knee Hemline: Straight Top fabric: Leather Occas... |
| 13   | no  | 15315920   | -     | 0.519 | Product: MANGO Women Mint Green Solid Pure Cotton Knee Length Pencil Skirt Brand: MANGO Color: Green Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Top fa... |
| 14   | no  | 17795314   | -     | 0.505 | Product: Trend Arrest Women Navy Blue Sequence Pencil Mini Skirt Brand: Trend Arrest Color: Navy Blue Category: Pencil Pattern: Embellished Length: Mini Hemline: Straight Top fa... |
| 15   | no  | 18034350   | -     | 0.500 | Product: Missguided Women Olive Green Solid Mini Pencil Skirt Brand: Missguided Color: Olive Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Top fabric: Polyester... |
| 16   | no  | 18841536   | -     | 0.486 | Product: Styli Women Burgundy Solid Pencil Skirts Brand: Styli Color: Burgundy Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fabric: Polyester Occasion: Cas... |
| 17   | no  | 17694094   | -     | 0.480 | Product: Antheaa Women Black Embellished Pencil Skirt Brand: Antheaa Color: Black Category: Pencil Pattern: Embellished Length: Above knee Hemline: Flared Top fabric: Polyester ... |
| 18   | no  | 18215396   | -     | 0.479 | Product: Popwings Women Above Knee-Length Black Pencil Skirts Brand: Popwings Color: Black Category: Pencil Pattern: Solid self design Length: Above knee Hemline: Straight Top f... |
| 19   | no  | 14024850   | -     | 0.468 | Product: OTORVA Women Denim Blue Solid Pencil Mini Skirt Brand: OTORVA Color: Blue Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Top fabric: Polyester Occasion:... |
| 20   | no  | 17931744   | -     | 0.463 | Product: PATRORNA Women Green & Black Solid Knee Length Pencil Skirts Brand: PATRORNA Color: Green Category: Pencil Pattern: Solid Length: Knee length Hemline: Curved Top fabric... |
| 21   | no  | 12086090   | -     | 0.459 | Product: Athena Women Pink Solid Midi Pencil Skirt Brand: Athena Color: Pink Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fabric: Polyester Occasion: Casua... |
| 22   | no  | 14798956   | -     | 0.440 | Product: Trendyol Women Taupe Solid Pencil Midi Skirt Brand: Trendyol Color: Taupe Category: Pencil Pattern: Solid Length: Midi Hemline: Straight Top fabric: Polyester Occasion:... |
| 23   | no  | 18676062   | -     | 0.437 | Product: Disrupt Women Mustard-Yellow Solid Slim-Fit Pencil Mini Skirt Brand: Disrupt Color: Mustard Category: Pencil Pattern: Solid Length: Mini Hemline: Straight Top fabric: C... |
| 24   | no  | 14270952   | -     | 0.436 | Product: NEUDIS Women Pack Of 2 Solid Velvet Pencil Skirts Brand: NEUDIS Color: Black Category: Pencil Pattern: Solid Length: Knee length Hemline: Straight Top fabric: Polyester... |
| 25   | no  | 18629568   | -     | 0.421 | Product: IX IMPRESSION Women Gold Solid Pencil Above Knee Straight Skirts Brand: IX IMPRESSION Color: Gold Category: Pencil Pattern: Solid Length: Above knee Hemline: Straight T... |
| 26   | no  | 17694116   | -     | 0.411 | Product: Antheaa Women Black Solid Pleated Pencil Skirt Brand: Antheaa Color: Black Category: Pencil Pattern: Solid Length: Above knee Hemline: Tulip Top fabric: Cotton blend Oc... |
| 27   | no  | 17927414   | -     | 0.409 | Product: PATRORNA Women Sea Green Solid Above Knee Length Pencil Skirts Brand: PATRORNA Color: Sea Green Category: Pencil Pattern: Solid Length: Above knee Hemline: Curved Top f... |
| 28   | no  | 16042324   | -     | 0.407 | Product: STYL CO. Women Green & Orange Graphic Printed Above Knee Length Pencil Skirt Brand: STYL CO. Color: Green Category: Pencil Pattern: Graphic printed Length: Above knee H... |
| 29   | no  | 17899190   | -     | 0.386 | Product: PATRORNA Women Purple Solid Pencil Above Knee-Length Skirts Brand: PATRORNA Color: Purple Category: Pencil Pattern: Solid Length: Above knee Hemline: Curved Top fabric:... |
| 30   | yes | 15940138   | -     | 0.385 | Product: SASSAFRAS Burgundy Metallic Twisted Pencil Skirt Brand: SASSAFRAS Color: Burgundy Category: Pencil Pattern: Solid Length: Above knee Hemline: Straight Top fabric: Polye... |

### Question 14/50

**Query:** Do you have any Mustard Blouson for everyday wear?

**Relevant docs:** `['13532718']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 0.167 | 0.356 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 14935802   | -     | 1.000 | Product: Roadster Women Deep Mustard Solid Ruched Top Brand: Roadster Color: Mustard Category: Blouson Pattern: Solid Neck: V-neck Sleeves: Long flared sleeves Length: Crop Top ... |
| 2    | no  | 14400678   | -     | 0.802 | Product: BLANC9 Women Mustard Yellow Solid Cotton Shirt with Trousers Brand: BLANC9 Color: Mustard Category: Top Top type: Top Bottom type: Trousers Pattern: Solid Neck: Shirt c... |
| 3    | no  | 11184982   | -     | 0.745 | Product: Mast & Harbour Women Off-White & Mustard Yellow Pleated Candy-Striped Blouson Pure Cotton Top Brand: Mast & Harbour Color: Off White Category: Blouson Pattern: Vertical... |
| 4    | no  | 13018002   | -     | 0.731 | Product: Blissta Mustard Yellow & Gold-Toned Silk Blend Unstitched Dress Material Brand: Blissta Color: Mustard Category: Dress Pattern: Paisley Bottom fabric: Shantoon Occasion... |
| 5    | no  | 19361356   | -     | 0.706 | Product: BoStreet Women Mustard Yellow Solid Tailored Jacket Brand: BoStreet Color: Mustard Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemlin... |
| 6    | yes | 13532718   | -     | 0.665 | Product: Harpa Women Mustard Printed Blouson Top Brand: Harpa Color: Mustard Category: Blouson Pattern: Floral printed Neck: Round neck Sleeves: Long bishop sleeves Length: Regu... |
| 7    | no  | 16470574   | -     | 0.641 | Product: armure Women Mustard Striped Lightweight Crop Tailored Jacket Brand: armure Color: Mustard Category: Tailored jacket Pattern: Solid striped Sleeves: Three-quarter sleev... |
| 8    | no  | 14231200   | -     | 0.622 | Product: all about you Women Mustard Brown Solid Shawl Collar Open Front Jacket Brand: all about you Color: Mustard Category: Open front jacket Pattern: Solid Sleeves: Long slee... |
| 9    | no  | 13023122   | -     | 0.612 | Product: Athena Women Mustard Yellow Solid Blazer with Trousers Brand: Athena Color: Mustard Category: Coat Top type: Coat Bottom type: Trousers Pattern: Solid Neck: Shirt colla... |
| 10   | no  | 13861554   | -     | 0.575 | Product: mf Mustard & Pink Cotton Blend Unstitched Dress Material Brand: mf Color: Mustard Category: Dress Pattern: Floral Bottom fabric: Cotton blend Dupatta fabric: Poly chiff... |
| 11   | no  | 1694433    | -     | 0.568 | Product: SASSAFRAS Mustard Yellow Peplum Jacket Brand: SASSAFRAS Color: Mustard Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Curved To... |
| 12   | no  | 7942995    | -     | 0.552 | Product: Mustard Yellow Textured Blouse Brand: Annabelle by Pantaloons Color: Yellow Category: Blouson Pattern: Solid Neck: Round neck Sleeves: Short regular sleeves Length: Reg... |
| 13   | no  | 16774898   | -     | 0.538 | Product: Kraus Jeans Women Mustard Puffer Jacket Brand: Kraus Jeans Color: Mustard Category: Puffer jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight... |
| 14   | no  | 14906974   | -     | 0.534 | Product: Zink London Women Mustard Shrug Brand: Zink London Color: Mustard Pattern: Self design Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Acrylic Occas... |
| 15   | no  | 8441465    | -     | 0.533 | Product: Bossini Mustard Yellow Printed Open Front Shrug Brand: Bossini Color: Mustard Pattern: Printed Sleeves: Three-quarter sleeves Length: Regular Hemline: Straight Top fabr... |
| 16   | no  | 14485256   | -     | 0.515 | Product: Mast & Harbour Women Mustard Yellow & Navy Blue Colourblocked Padded Jacket Brand: Mast & Harbour Color: Mustard Category: Padded jacket Pattern: Colourblocked Sleeves:... |
| 17   | no  | 14364272   | -     | 0.503 | Product: Mast & Harbour Women Mustard Solid Full Sleeved Sweatshirt Brand: Mast & Harbour Color: Mustard Category: Open front jacket Pattern: Solid Sleeves: Long sleeves Length:... |
| 18   | no  | 17157806   | -     | 0.502 | Product: Monte Carlo Women Mustard Lightweight Sleeveless Puffer Jacket Brand: Monte Carlo Color: Mustard Category: Puffer jacket Pattern: Solid Sleeves: Sleeveless Length: Regu... |
| 19   | no  | 17064994   | -     | 0.490 | Product: VEIRDO Woman Mustard Padded Jacket Brand: VEIRDO Color: Mustard Category: Padded jacket Pattern: Solid Sleeves: Sleeveless Length: Regular Hemline: Curved Top fabric: P... |
| 20   | no  | 2248780    | -     | 0.480 | Product: Belle Fille Women Mustard Yellow Solid Lightweight Bomber Jacket Brand: Belle Fille Color: Mustard Category: Bomber Pattern: Solid Sleeves: Long sleeves Length: Regular... |
| 21   | no  | 12737836   | -     | 0.479 | Product: SASSAFRAS Women Mustard Yellow Solid Puffer Jacket Brand: SASSAFRAS Color: Mustard Category: Puffer jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline:... |
| 22   | no  | 10891582   | -     | 0.462 | Product: Alsace Lorraine Paris Women Mustard Yellow Solid Hooded Sweatshirt Brand: Alsace Lorraine Paris Color: Mustard Category: Front-open Pattern: Solid Neck: Hood Sleeves: L... |
| 23   | no  | 13997512   | -     | 0.459 | Product: plusS Women Mustard Brown Pure Cotton Solid Tailored Jacket Brand: plusS Color: Mustard Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular H... |
| 24   | no  | 10597802   | -     | 0.441 | Product: Alsace Lorraine Paris Women Mustard Yellow & White Colourblocked Hooded Sweatshirt Brand: Alsace Lorraine Paris Color: Mustard Category: Front-open Pattern: Colourblock... |
| 25   | no  | 14862378   | -     | 0.440 | Product: Campus Sutra Women Mustard Windcheater Outdoor Tailored Jacket Brand: Campus Sutra Color: Mustard Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length:... |
| 26   | no  | 16154384   | -     | 0.422 | Product: JC Mode Women Mustard Yellow Solid Padded Jacket Brand: JC Mode Color: Mustard Category: Padded jacket Pattern: Solid Sleeves: Sleeveless Length: Regular Hemline: Strai... |
| 27   | no  | 13982600   | -     | 0.407 | Product: VOXATI Women Mustard Printed Tailored Jacket with Patchwork Brand: VOXATI Color: Mustard Category: Tailored jacket Pattern: Graphic printed Sleeves: Long sleeves Length... |
| 28   | no  | 11364534   | -     | 0.380 | Product: SASSAFRAS Women Mustard Yellow Solid Longline Shirt Style Shrug Brand: SASSAFRAS Color: Mustard Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: Straight ... |
| 29   | no  | 18839638   | -     | 0.378 | Product: Styli Beige Blouson Top Brand: Styli Color: Beige Category: Blouson Pattern: Solid Neck: Round neck Sleeves: Sleeveless cold-shoulder Length: Regular Top fabric: Polyes... |
| 30   | no  | 16034762   | -     | 0.374 | Product: Cottinfab Women Mustard Black Checked Tailored Jacket Brand: Cottinfab Color: Mustard Category: Tailored jacket Pattern: Checked Sleeves: Long sleeves Length: Regular H... |

### Question 15/50

**Query:** I need Blue Joggers by STREET 9.

**Relevant docs:** `['13038932', '13071994']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.067     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 13071994   | -     | 1.000 | Product: STREET 9 Women Blue Regular Fit Solid Joggers Brand: STREET 9 Color: Blue Category: Joggers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets: ... |
| 2    | yes | 13038932   | -     | 0.941 | Product: STREET 9 Women Blue Regular Fit Solid Joggers Brand: STREET 9 Color: Blue Category: Joggers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: ... |
| 3    | no  | 13038926   | -     | 0.721 | Product: STREET 9 Women Green & Black Regular Fit Solid Joggers Brand: STREET 9 Color: Green Category: Joggers Pattern: Colourblocked solid Length: Regular Top fabric: Cotton Oc... |
| 4    | no  | 13071970   | -     | 0.658 | Product: STREET 9 Women Green Solid Cargo Joggers Brand: STREET 9 Color: Green Category: Joggers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 4 Wa... |
| 5    | no  | 13038960   | -     | 0.647 | Product: STREET 9 Women Black & Yellow Regular Fit Printed Joggers Brand: STREET 9 Color: Black Category: Joggers Pattern: Colourblocked printed Length: Regular Top fabric: Cott... |
| 6    | no  | 13038922   | -     | 0.642 | Product: STREET 9 Women Yellow Regular Fit Solid Joggers Brand: STREET 9 Color: Yellow Category: Joggers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pocke... |
| 7    | no  | 13071980   | -     | 0.637 | Product: STREET 9 Women Yellow Regular Fit Printed Joggers Brand: STREET 9 Color: Yellow Category: Joggers Pattern: Typography printed Length: Regular Top fabric: Cotton Occasio... |
| 8    | no  | 13738666   | -     | 0.603 | Product: STREET 9 Women Olive Green & Black Regular Fit Printed Joggers Brand: STREET 9 Color: Olive Category: Joggers Pattern: Conversational printed Length: Regular Top fabric... |
| 9    | no  | 5389019    | -     | 0.564 | Product: STREET 9 Women Blue Striped Culotte Jumpsuit Brand: STREET 9 Color: Blue Category: Culotte jumpsuit Pattern: Striped Neck: Round neck Sleeves: Sleeveless Top fabric: Co... |
| 10   | no  | 16336020   | -     | 0.555 | Product: STREET 9 Women Bright Orange Typography Gym Kit Trousers Brand: STREET 9 Color: Orange Category: Joggers Pattern: Typography printed Length: Three-fourth length Top fab... |
| 11   | no  | 15803276   | -     | 0.537 | Product: STREET 9 Blue Basic Jumpsuit Brand: STREET 9 Color: Blue Category: Basic jumpsuit Pattern: Solid Neck: Shirt collar Sleeves: Long sleeves Top fabric: Cotton Occasion: C... |
| 12   | no  | 13041492   | -     | 0.512 | Product: STREET 9 Women Blue Solid Sweatshirt Brand: STREET 9 Color: Blue Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Strai... |
| 13   | no  | 13038878   | -     | 0.511 | Product: STREET 9 Women Blue Solid Sweatshirt Brand: STREET 9 Color: Blue Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Strai... |
| 14   | no  | 14136072   | -     | 0.503 | Product: STREET 9 Women Blue Flared Faded Parallel Trousers Brand: STREET 9 Color: Blue Category: Parallel trousers Pattern: Solid Length: Cropped Top fabric: Denim Occasion: Ca... |
| 15   | no  | 19361312   | -     | 0.485 | Product: STREET 9 Women Brown Printed Smart Loose Fit High-Rise Joggers Trousers Brand: STREET 9 Color: Brown Category: Joggers Pattern: Animal printed Length: Regular Top fabri... |
| 16   | no  | 12682016   | -     | 0.474 | Product: STREET 9 Women Blue Skinny Fit Mid-Rise Clean Look Stretchable Jeans Brand: STREET 9 Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash car... |
| 17   | no  | 17904100   | -     | 0.465 | Product: STREET 9 Women Blue Hottie Relaxed Fit High-Rise Pure Cotton Dual Tone Jeans Brand: STREET 9 Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 4 ... |
| 18   | no  | 12682038   | -     | 0.464 | Product: STREET 9 Women Blue Skinny Fit Mid-Rise Clean Look Stretchable Jeans Brand: STREET 9 Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash car... |
| 19   | no  | 12693476   | -     | 0.462 | Product: STREET 9 Women Blue Straight Fit Mid-Rise Clean Look Stretchable Jeans Brand: STREET 9 Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 20   | no  | 12693490   | -     | 0.457 | Product: STREET 9 Women Blue Straight Fit Mid-Rise Clean Look Stretchable Jeans Brand: STREET 9 Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 21   | no  | 14136188   | -     | 0.431 | Product: STREET 9 Women Blue Relaxed Fit Mid-Rise Highly Distressed Jeans Brand: STREET 9 Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 4 Wash care: M... |
| 22   | no  | 12277584   | -     | 0.416 | Product: STREET 9 Women Navy Blue Regular Fit Solid Cargos Brand: STREET 9 Color: Navy Blue Category: Cargos Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual P... |
| 23   | no  | 6608510    | -     | 0.406 | Product: STREET 9 Navy Blue Solid Basic Jumpsuit Brand: STREET 9 Color: Navy Blue Category: Basic jumpsuit Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless Top fabric: P... |
| 24   | no  | 9340267    | -     | 0.335 | Product: STREET 9 Black & White Striped Cropped Basic Jumpsuit Brand: STREET 9 Color: Black Category: Basic jumpsuit Pattern: Striped Neck: V-neck Sleeves: Sleeveless Top fabric... |
| 25   | no  | 13738560   | -     | 0.329 | Product: STREET 9 Women Turquoise Blue Lightweight Jacket Brand: STREET 9 Color: Turquoise Blue Category: Sporty jacket Sleeves: Three-quarter sleeves Length: Crop Hemline: Curv... |
| 26   | no  | 18987460   | -     | 0.322 | Product: BoStreet Women Fluorescent Green Tapered Fit Joggers Brand: BoStreet Color: Fluorescent Green Category: Joggers Pattern: Solid Length: Regular Top fabric: Polyester Occ... |
| 27   | no  | 14136152   | -     | 0.316 | Product: STREET 9 Women Navy Blue Solid Cotton Denim Jumpsuit Brand: STREET 9 Color: Navy Blue Category: Basic jumpsuit Pattern: Solid Neck: Square neck Sleeves: Sleeveless Top ... |
| 28   | no  | 18143380   | -     | 0.300 | Product: STREET 9 Women Attractive Lime Green Striped Trousers Brand: STREET 9 Color: Lime Green Category: Peg trousers Pattern: Striped printed Length: Regular Top fabric: Cott... |
| 29   | no  | 12277606   | -     | 0.289 | Product: STREET 9 Women Olive Green & Brown Camouflage Print Cargos Brand: STREET 9 Color: Olive Category: Cargos Pattern: Camouflage printed Length: Regular Occasion: Casual Po... |
| 30   | no  | 8694599    | -     | 0.288 | Product: STREET 9 Green & Black Colourblocked Cold Shoulder Basic Jumpsuit Brand: STREET 9 Color: Green Category: Basic jumpsuit Pattern: Colourblocked Neck: V-neck Sleeves: Sho... |

### Question 16/50

**Query:** Show me Front-open within a budget of 2800.

**Relevant docs:** `['16382036', '16382150', '5829334', '5829327', '11991214', '15007832', '14328000', '16461758']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.000     | 0.000  | 0.000 | 0.000 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 17685090   | -     | 1.000 | Product: BUY NEW TREND Women Red Black Colourblocked Lightweight Crop Open Front Jacket Brand: BUY NEW TREND Color: Red Category: Open front jacket Pattern: Colourblocked Sleeve... |
| 2    | no  | 19087856   | -     | 0.678 | Product: ONLY Women Beige & Navy Blue Colourblocked Front-Open Longline Brand: ONLY Color: Beige Category: Front-open Pattern: Colourblocked Neck: Round neck Sleeves: Long sleev... |
| 3    | no  | 15137944   | -     | 0.471 | Product: AND Women Black & White Geometric Open Front Jacket Brand: AND Color: Black Category: Open front jacket Pattern: Geometric printed Sleeves: Long sleeves Length: Regular... |
| 4    | no  | 17685350   | -     | 0.452 | Product: BUY NEW TREND Women Maroon Lightweight Crop Open Front Jacket Brand: BUY NEW TREND Color: Maroon Category: Open front jacket Pattern: Abstract solid Sleeves: Three-quar... |
| 5    | no  | 17226172   | -     | 0.451 | Product: SHOWOFF Women Orange Mom Fit High-Rise Clean Look Stretchable Jeans Brand: SHOWOFF Color: Orange Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 2 Wash c... |
| 6    | no  | 14070682   | -     | 0.402 | Product: Zink London Women Blue Solid Open Front Jacket Brand: Zink London Color: Blue Category: Open front jacket Pattern: Solid Sleeves: Three-quarter sleeves Length: Crop Hem... |
| 7    | no  | 15940140   | -     | 0.400 | Product: SASSAFRAS Women Green Corduroy Crop Open Front Jacket Brand: SASSAFRAS Color: Green Category: Open front jacket Pattern: Solid Sleeves: Long sleeves Length: Crop Hemlin... |
| 8    | no  | 14093992   | -     | 0.379 | Product: Hangup Women Mustard Yellow Printed Lightweight Open Front Jacket Brand: Hangup Color: Mustard Category: Open front jacket Pattern: Geometric printed Sleeves: Three-qua... |
| 9    | no  | 18601482   | -     | 0.377 | Product: MONTREZ Women White Black Open Front Jacket Brand: MONTREZ Color: White Category: Open front jacket Pattern: Graphic printed Sleeves: Long sleeves Length: Regular Hemli... |
| 10   | no  | 14094008   | -     | 0.344 | Product: Hangup Women Gold-Toned Printed Lightweight Open Front Jacket Brand: Hangup Color: Gold Category: Open front jacket Pattern: Floral printed Sleeves: Sleeveless Length: ... |
| 11   | no  | 16917270   | -     | 0.336 | Product: Cloth Haus India Women Black & Red Floral Longline Open Front Jacket Brand: Cloth Haus India Color: Black Category: Open front jacket Pattern: Floral printed Sleeves: L... |
| 12   | no  | 15354744   | -     | 0.331 | Product: FurryFlair Women Red Open Front Jacket Brand: FurryFlair Color: Red Category: Open front jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight T... |
| 13   | no  | 2223198    | -     | 0.324 | Product: W Women Red Solid Front-Open Longline Sweater Brand: W Color: Red Category: Front-open Pattern: Solid Neck: Round neck Sleeves: Long sleeves Hemline: Straight Top fabri... |
| 14   | no  | 16044812   | -     | 0.323 | Product: Forever New Women Green Solid Comfort-Fit Open-Front Casual Blazer Brand: Forever New Color: Green Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Poly... |
| 15   | no  | 16971668   | -     | 0.317 | Product: Soch Women Orange Geometric Longline Open Front Jacket Brand: Soch Color: Orange Category: Open front jacket Pattern: Geometric printed Sleeves: Three-quarter sleeves L... |
| 16   | no  | 14094028   | -     | 0.315 | Product: Hangup Women Black & Blue Printed Open Front Jacket Brand: Hangup Color: Black Category: Open front jacket Pattern: Floral printed Sleeves: Sleeveless Length: Regular H... |
| 17   | no  | 16917280   | -     | 0.304 | Product: Cloth Haus India Women Black & Orange Longline Open Front Jacket Brand: Cloth Haus India Color: Black Category: Open front jacket Pattern: Abstract printed Sleeves: Lon... |
| 18   | no  | 16971666   | -     | 0.295 | Product: Soch Women Blue Geometric Colourblocked Longline Open Front Jacket with Embroidered Brand: Soch Color: Blue Category: Open front jacket Pattern: Geometric colourblocked... |
| 19   | no  | 17570446   | -     | 0.288 | Product: SHOWOFF Women Blue Boyfriend Fit High-Rise Low Distress Light Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Po... |
| 20   | no  | 14080856   | -     | 0.276 | Product: DressBerry Women Stylish Mustard Solid Quirky Outerwear Sweatshirt Brand: DressBerry Color: Mustard Category: Front-open Pattern: Solid Neck: Hood Sleeves: Long sleeves... |
| 21   | no  | 17570328   | -     | 0.273 | Product: SHOWOFF Women Blue Wide Leg High-Rise Low Distress Heavy Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Pockets... |
| 22   | no  | 15257760   | -     | 0.266 | Product: Campus Sutra Women Blue White Colourblocked Windcheater Open Front Jacket Brand: Campus Sutra Color: Blue Category: Open front jacket Pattern: Colourblocked Sleeves: Lo... |
| 23   | no  | 14039732   | -     | 0.265 | Product: Diwaah Women Gold-Toned Embellished Open Front Jacket Brand: Diwaah Color: Gold Category: Open front jacket Pattern: Self design printed Sleeves: Sleeveless Length: Cro... |
| 24   | no  | 14382336   | -     | 0.253 | Product: DressBerry Women Pink Melange Effect Longline Front-Open Brand: DressBerry Color: Pink Category: Front-open Pattern: Solid Neck: V-neck Sleeves: Long sleeves Length: Lo... |
| 25   | no  | 15940702   | -     | 0.252 | Product: Label Ritu Kumar Women Black White Floral Crop Open Front Jacket Brand: Label Ritu Kumar Color: Black Category: Open front jacket Pattern: Floral printed Sleeves: Long ... |
| 26   | no  | 15088844   | -     | 0.251 | Product: Roadster Women Red Open Front Jacket Brand: Roadster Color: Red Category: Open front jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top f... |
| 27   | no  | 11952000   | -     | 0.249 | Product: DressBerry Women Navy Blue Ribbed Longline Front-Open Sweater Brand: DressBerry Color: Navy Blue Category: Front-open Pattern: Solid ribbed Neck: V-neck Sleeves: Long s... |
| 28   | no  | 14199270   | -     | 0.248 | Product: Hangup Women White & Pink Printed Lightweight Jacquard Open Front Jacket Brand: Hangup Color: White Category: Open front jacket Pattern: Floral printed Sleeves: Three-q... |
| 29   | no  | 14094010   | -     | 0.243 | Product: Hangup Women Yellow Printed Lightweight Ethnic Open Front Jacket Brand: Hangup Color: Yellow Category: Open front jacket Pattern: Self design printed Sleeves: Sleeveles... |
| 30   | no  | 7736701    | -     | 0.234 | Product: W Women Teal Blue Solid Front-Open Longline Sweater Brand: W Color: Teal Category: Front-open Pattern: Solid Neck: Shawl collar Sleeves: Long sleeves Length: Longline H... |

### Question 17/50

**Query:** Do you have anything from FILA in Red for everyday wear?

**Relevant docs:** `['13255768']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 13255768   | -     | 1.000 | Product: FILA Women Red & Grey Colourblocked Sweatshirt Brand: FILA Color: Red Category: Pullover Pattern: Colourblocked Neck: Round neck Sleeves: Long sleeves Length: Regular H... |
| 2    | no  | 16705336   | -     | 0.662 | Product: FILA Women Blue Colourblocked Running Padded Jacket Brand: FILA Color: Blue Category: Padded jacket Pattern: Colourblocked Sleeves: Sleeveless Length: Regular Hemline: ... |
| 3    | no  | 16705334   | -     | 0.642 | Product: FILA Women Blue White Colourblocked Running Puffer Jacket Brand: FILA Color: Blue Category: Puffer jacket Pattern: Colourblocked Sleeves: Long sleeves Length: Regular H... |
| 4    | no  | 16705280   | -     | 0.555 | Product: FILA Women Off White Colourblocked Running Puffer Jacket Brand: FILA Color: Off White Category: Puffer jacket Pattern: Colourblocked Sleeves: Long sleeves Length: Regul... |
| 5    | no  | 16705296   | -     | 0.544 | Product: FILA Women Grey Printed Sweatshirt Brand: FILA Color: Grey Category: Front-open Pattern: Alphanumeric printed Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: ... |
| 6    | no  | 19324666   | -     | 0.277 | Product: FASHOR Women Red Ethnic Motifs Thread Work Kurta Brand: FASHOR Color: Red Pattern: Ethnic motifs solid Shape: A-line Neck: Round neck Sleeves: Long regular sleeves Leng... |
| 7    | no  | 19194932   | -     | 0.276 | Product: Puma Women Red solid Sporty Jacket Brand: Puma Color: Red Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Crop Hemline: Straight Top fabric: Cotton... |
| 8    | no  | 16175534   | -     | 0.231 | Product: H&M Women Red Cotton Blend Sweatpants Brand: H&M Color: Red Category: Joggers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 2 Wash care: M... |
| 9    | no  | 16421286   | -     | 0.226 | Product: Kappa Women Red Colourblocked Sporty Jacket Brand: Kappa Color: Red Category: Sporty jacket Pattern: Solid colourblocked Sleeves: Sleeveless Length: Regular Hemline: St... |
| 10   | no  | 1010455    | -     | 0.195 | Product: Belle Fille Red Jacket Brand: Belle Fille Color: Red Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Occasion: Casual Poc... |
| 11   | no  | 15730234   | -     | 0.184 | Product: AGIL ATHLETICA Women Red Geometric Lightweight Tailored Jacket Brand: AGIL ATHLETICA Color: Red Category: Tailored jacket Pattern: Geometric solid Sleeves: Three-quarte... |
| 12   | no  | 1010488    | -     | 0.180 | Product: Belle Fille Red Hooded Jacket Brand: Belle Fille Color: Red Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Occasion: Cas... |
| 13   | no  | 17988988   | -     | 0.180 | Product: FABNEST Women Red Floral Printed Relaxed Trousers Brand: FABNEST Color: Red Category: Regular trousers Pattern: Floral printed Length: Regular Top fabric: Cotton Occasi... |
| 14   | no  | 11421530   | -     | 0.175 | Product: Ginni Arora Label Women Red Slim Fit Solid Regular Trousers Brand: Ginni Arora Label Color: Red Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Co... |
| 15   | no  | 15354744   | -     | 0.172 | Product: FurryFlair Women Red Open Front Jacket Brand: FurryFlair Color: Red Category: Open front jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight T... |
| 16   | no  | 14048980   | -     | 0.172 | Product: Leather Retail Women Red Lightweight Longline Faux Leather Jacket Brand: Leather Retail Color: Red Category: Leather jacket Pattern: Solid Sleeves: Long sleeves Length:... |
| 17   | no  | 18875952   | -     | 0.168 | Product: URBANIC Women Red Slim Fit High-Rise Sports Shorts Brand: URBANIC Color: Red Category: Sports shorts Pattern: Solid Length: Above knee Top fabric: Polyester Occasion: C... |
| 18   | no  | 17348134   | -     | 0.166 | Product: Fabindia Red & Beige Paisley Printed Pure Cotton Dupatta Brand: Fabindia Color: Red Pattern: Paisley printed Top fabric: Pure cotton Occasion: Daily Wash care: Hand wash   |
| 19   | no  | 14447520   | -     | 0.163 | Product: Dupatta Bazaar Red & Silver-Toned Linen Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Solid Top fabric: Linen Occasion: Daily Wash care: Machine wash                   |
| 20   | no  | 12309376   | -     | 0.156 | Product: RIVI Women Red Regular Fit Solid Regular Trousers Brand: RIVI Color: Red Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion: Casual W... |
| 21   | no  | 14348874   | -     | 0.154 | Product: Tokyo Talkies Women Red Solid Regular Shorts Brand: Tokyo Talkies Color: Red Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Cas... |
| 22   | no  | 16585584   | -     | 0.147 | Product: Biba Women Red Ethnic Motifs Printed Kurta Brand: Biba Color: Red Pattern: Ethnic motifs printed Shape: A-line Neck: Mandarin collar Sleeves: Three-quarter regular slee... |
| 23   | no  | 14976268   | -     | 0.146 | Product: FASHOR Women Red Bandhani Printed & Zari Embroidered Kurta Brand: FASHOR Color: Red Pattern: Bandhani printed Shape: Straight Neck: Round neck Sleeves: Three-quarter re... |
| 24   | no  | 17348528   | -     | 0.144 | Product: Fabindia Women Red & Blue Floral Printed Regular Fit Trousers Brand: Fabindia Color: Red Category: Parallel trousers Pattern: Floral printed Length: Regular Top fabric:... |
| 25   | no  | 12918478   | -     | 0.140 | Product: AGIL ATHLETICA Women Navy Blue & Red Colourblocked Tailored Jacket Brand: AGIL ATHLETICA Color: Navy Blue Category: Tailored jacket Pattern: Colourblocked Sleeves: Long... |
| 26   | no  | 596488     | -     | 0.134 | Product: Belle Fille Women Red Hooded Jacket Brand: Belle Fille Color: Red Pattern: Solid Sleeves: Long sleeves Top fabric: Wool Occasion: Casual                                    |
| 27   | no  | 17393956   | -     | 0.133 | Product: Fabindia Women Beige & Red Striped Cotton Regular Trousers Brand: Fabindia Color: Beige Category: Regular trousers Pattern: Striped Length: Regular Top fabric: Cotton O... |
| 28   | no  | 11102126   | -     | 0.132 | Product: Alcis Women Red Brand Logo Print Running Sweatshirt Brand: Alcis Color: Red Category: Pullover Pattern: Brand logo printed Neck: Round neck Sleeves: Long sleeves Length... |
| 29   | no  | 11064260   | -     | 0.130 | Product: SASSAFRAS Women Red Solid Tailored Jacket Brand: SASSAFRAS Color: Red Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Curved Top... |
| 30   | no  | 16641130   | -     | 0.129 | Product: RIVI Women Red Solid Mid-Rise Cropped Trousers Brand: RIVI Color: Red Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Polyester Occasion: Casual P... |

### Question 18/50

**Query:** I'm looking for products that cost no more than 1100.

**Relevant docs:** `['13135238', '15241584', '13181706', '17739302', '15218838', '11579058', '17113756', '13951522']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.000     | 0.000  | 0.000 | 0.000 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 2117164    | -     | 1.000 | Product: Noi Cream-Coloured & Brown Printed Shawl Brand: Noi Color: Cream Pattern: Animal printed Top fabric: Wool Occasion: Daily                                                   |
| 2    | no  | 16524266   | -     | 0.656 | Product: LOOKNBOOK ART Orange Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: LOOKNBOOK ART Color: Orange Dupatta: With dupatta Pattern: Woven design Neck: Round n... |
| 3    | no  | 15266700   | -     | 0.436 | Product: max Beige Pure Cotton Dupatta Brand: max Color: Beige Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash                                        |
| 4    | no  | 15312982   | -     | 0.421 | Product: LOOKNBOOK ART Black & Beige Embellished Sequinned Semi-Stitched Lehenga Set Brand: LOOKNBOOK ART Color: Black Pattern: Embellished Neck: Round neck Sleeves: Sleeveless ... |
| 5    | no  | 16217482   | -     | 0.409 | Product: max Women Orange Palazzos Brand: max Color: Orange Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion: Western Wash care: Machine wash                       |
| 6    | no  | 14443728   | -     | 0.375 | Product: max Orange Dupatta with Beads and Stones Brand: max Color: Orange Pattern: Solid Top fabric: Poly chiffon Occasion: Daily Wash care: Hand wash                              |
| 7    | no  | 18997238   | -     | 0.345 | Product: IRIDAA JAIPUR Beige & Red Mandarin Collar Printed Tunic Brand: IRIDAA JAIPUR Color: Beige Pattern: Printed Neck: Mandarin collar Sleeves: Three-quarter sleeves Top fabr... |
| 8    | no  | 15748944   | -     | 0.340 | Product: LOOKNBOOK ART Cream-Coloured Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: LOOKNBOOK ART Color: Cream Dupatta: With dupatta Patter... |
| 9    | no  | 18838938   | -     | 0.326 | Product: LOOKNBOOK ART Pink Embellished Sequinned Semi-Stitched Lehenga Set Brand: LOOKNBOOK ART Color: Pink Dupatta: With dupatta Pattern: Embellished Neck: Scoop neck Sleeves:... |
| 10   | no  | 18310306   | -     | 0.320 | Product: LOOKNBOOK ART Black & White Printed Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: LOOKNBOOK ART Color: Black Dupatta: With dupatta Pattern: Printed Neck... |
| 11   | no  | 17647778   | -     | 0.319 | Product: LOOKNBOOK ART Red Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: LOOKNBOOK ART Color: Red Dupatta: With dupatta Pattern: Embellishe... |
| 12   | no  | 14497102   | -     | 0.315 | Product: Ishin Women White Ethnic Motifs Embroidered Layered Pure Cotton Kurta with Salwar & With Dupatta Brand: Ishin Color: White Category: Kurta set Top type: Kurta Bottom ty... |
| 13   | no  | 15748940   | -     | 0.301 | Product: LOOKNBOOK ART White & Pink Embellished Mirror Work Shibori Made to Measure Lehenga & Unstitched Blouse With Brand: LOOKNBOOK ART Color: White Dupatta: With dupatta Patt... |
| 14   | no  | 17060030   | -     | 0.285 | Product: NDS Niharikaa Designer Studio Women Off White Sequinned Padded Blouse Brand: NDS Niharikaa Designer Studio Color: Off White Pattern: Embellished Neck: Square neck Sleev... |
| 15   | no  | 11624038   | -     | 0.284 | Product: Ishin White & Gold-Toned Woven Design Dupatta Brand: Ishin Color: White Pattern: Ethnic motifs woven design Top fabric: Cotton silk Occasion: Party Wash care: Dry clean    |
| 16   | no  | 14921732   | -     | 0.279 | Product: Ishin Women Black & Silver-Toned Striped Shimmer A-Line Top Brand: Ishin Color: Black Category: A-line Pattern: Shimmer striped Neck: High neck Sleeves: Long regular sl... |
| 17   | no  | 12040878   | -     | 0.275 | Product: Indo Era Orange & Pink Striped Dupatta Brand: Indo Era Color: Orange Pattern: Striped Top fabric: Art silk Occasion: Daily Wash care: Hand wash                             |
| 18   | no  | 14745736   | -     | 0.272 | Product: Baby Lakshmi Girls Orange & Off White Ready to Wear Lehenga With Blouse Brand: Baby Lakshmi Color: Orange Pattern: Solid Neck: Round neck Sleeves: Sleeveless no Hemline... |
| 19   | no  | 11149776   | -     | 0.270 | Product: Style Quotient Women Red & Black Checked Shawl Brand: Style Quotient Color: Red Pattern: Checked woven design Top fabric: Acrylic Occasion: Daily                           |
| 20   | no  | 18196776   | -     | 0.269 | Product: LOOKNBOOK ART White Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: LOOKNBOOK ART Color: White Dupatta: With dupatta Pattern: Embroidered Neck... |
| 21   | no  | 11256044   | -     | 0.256 | Product: Ethnicity Beige Solid Dupatta Brand: Ethnicity Color: Beige Pattern: Solid Top fabric: Net Occasion: Daily Wash care: Machine wash                                          |
| 22   | no  | 19112000   | -     | 0.247 | Product: INDIAN HERITAGE Brown & Orange Printed Silk Crepe Unstitched Dress Material Brand: INDIAN HERITAGE Color: Brown Category: Dress Pattern: Other Bottom fabric: Silk crepe... |
| 23   | no  | 17748850   | -     | 0.246 | Product: max Black Pure Cotton Dupatta Brand: max Color: Black Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash                                        |
| 24   | no  | 17060082   | -     | 0.234 | Product: NDS Niharikaa Designer Studio Women Cream-colored Sequinned Padded Blouse Brand: NDS Niharikaa Designer Studio Color: Cream Pattern: Embellished Neck: Round neck Sleeve... |
| 25   | no  | 17662996   | -     | 0.233 | Product: Dupatta Bazaar Orange Solid Pure Cotton Dupatta Brand: Dupatta Bazaar Color: Orange Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash          |
| 26   | no  | 17647770   | -     | 0.225 | Product: LOOKNBOOK ART Black & Red Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: LOOKNBOOK ART Color: Black Dupatta: With dupatta Pattern: ... |
| 27   | no  | 11081716   | -     | 0.214 | Product: Vastraa Fusion Women Beige Chikankari Embroidered Straight Palazzos Brand: Vastraa Fusion Color: Beige Pattern: Ethnic motifs embroidered Length: Regular Top fabric: Co... |
| 28   | no  | 16119706   | -     | 0.211 | Product: SOUNDARYA Orange & White Striped Pure Cotton Leheriya Dupatta Brand: SOUNDARYA Color: Orange Pattern: Leheriya striped Top fabric: Pure cotton Occasion: Daily Wash care... |
| 29   | no  | 16945862   | -     | 0.208 | Product: Anouk Orange Ethnic Motifs Zari Silk Blend Banarasi Saree Brand: Anouk Color: Orange Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Traditional Wash c... |
| 30   | no  | 14432282   | -     | 0.205 | Product: max White Regular Top Brand: max Color: White Category: Regular Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless shoulder straps Length: Regular Top fabric: Pur... |

### Question 19/50

**Query:** Do you have anything from Bhama Couture in A-line?

**Relevant docs:** `['12151804', '10355827', '10356731', '12151824', '10717820', '9430103', '9430109', '10355839']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.267     | 1.000  | 0.167 | 0.549 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 13969870   | -     | 1.000 | Product: Bhama Couture Navy Blue & Red Embroidered Detail A-Line Top Brand: Bhama Couture Color: Navy Blue Category: A-line Pattern: Solid Neck: Round neck Sleeves: Three-quarte... |
| 2    | no  | 9717189    | -     | 0.998 | Product: Bhama Couture Women Navy Blue Embroidered A-Line Pure Cotton Top Brand: Bhama Couture Color: Navy Blue Category: A-line Pattern: Floral embellished Neck: Tie-up neck Sl... |
| 3    | no  | 9430121    | -     | 0.977 | Product: Bhama Couture Black Embroidered A-Line Pure Cotton Top Brand: Bhama Couture Color: Black Category: A-line Pattern: Ethnic motifs embellished Neck: V-neck Sleeves: Three... |
| 4    | no  | 13969820   | -     | 0.963 | Product: Bhama Couture Maroon & Black Embroidered Bell Sleeves A-Line Top Brand: Bhama Couture Color: Maroon Category: A-line Pattern: Ethnic motifs embroidered Neck: Round neck... |
| 5    | no  | 9430115    | -     | 0.962 | Product: Bhama Couture Women Navy Blue Embroidered A-Line Top Brand: Bhama Couture Color: Navy Blue Category: A-line Pattern: Ethnic motifs embellished Neck: Round neck Sleeves:... |
| 6    | yes | 12151804   | -     | 0.956 | Product: Bhama Couture Women Blue & Pink Floral Print A-Line Pure Cotton Top Brand: Bhama Couture Color: Blue Category: A-line Pattern: Ethnic motifs printed Neck: Keyhole neck ... |
| 7    | no  | 11672988   | -     | 0.954 | Product: Bhama Couture Women White & Green Floral Print A-Line Top Brand: Bhama Couture Color: White Category: A-line Pattern: Floral printed Neck: Round neck Sleeves: Sleeveles... |
| 8    | no  | 4380660    | -     | 0.936 | Product: Bhama Couture Women Peach-Coloured Printed A-Line Top Brand: Bhama Couture Color: Peach Category: A-line Pattern: Floral printed Neck: Tie-up neck Sleeves: Three-quarte... |
| 9    | yes | 10355827   | -     | 0.936 | Product: Bhama Couture Women Blue Embroidered A-Line Pure Cotton Top Brand: Bhama Couture Color: Blue Category: A-line Pattern: Ethnic motifs embellished Neck: Round neck Sleeve... |
| 10   | yes | 10717820   | -     | 0.933 | Product: Bhama Couture Women Blue Embroidered Detail Chambray A-Line Pure Cotton Top Brand: Bhama Couture Color: Navy Blue Category: A-line Pattern: Solid Neck: Tie-up neck Slee... |
| 11   | no  | 11625546   | -     | 0.923 | Product: Bhama Couture Women Red & White Striped A-Line Top Brand: Bhama Couture Color: Red Category: A-line Pattern: Vertical stripes striped Neck: Round neck Sleeves: Three-qu... |
| 12   | yes | 12151824   | -     | 0.922 | Product: Bhama Couture Women Maroon Printed A-Line Top Brand: Bhama Couture Color: Maroon Category: A-line Pattern: Ethnic motifs printed Neck: Tie-up neck Sleeves: Three-quarte... |
| 13   | no  | 4380652    | -     | 0.902 | Product: Bhama Couture Women Off-White Printed A-Line Top Brand: Bhama Couture Color: Off White Category: A-line Pattern: Geometric printed Neck: Boat neck Sleeves: Three-quarte... |
| 14   | no  | 8339967    | -     | 0.882 | Product: Bhama Couture Women Red Embroidered Detail A-Line Top Brand: Bhama Couture Color: Red Category: A-line Pattern: Geometric embellished Neck: Tie-up neck Sleeves: Short f... |
| 15   | yes | 10356731   | -     | 0.875 | Product: Bhama Couture Women Blue Embroidered Cotton A-Line Top Brand: Bhama Couture Color: Blue Category: A-line Pattern: Ethnic motifs embellished Neck: Tie-up neck Sleeves: T... |
| 16   | no  | 12795840   | -     | 0.872 | Product: Bhama Couture Women Black & Pink Yoke Design Pure Cotton High-Low Kurti Brand: Bhama Couture Color: Black Pattern: Ethnic motifs yoke design Shape: A-line Neck: Mandari... |
| 17   | yes | 10355839   | -     | 0.849 | Product: Bhama Couture Women Red Solid A-Line Pure Cotton Top Brand: Bhama Couture Color: Red Category: A-line Pattern: Solid Neck: Tie-up neck Sleeves: Three-quarter puff sleev... |
| 18   | yes | 9430103    | -     | 0.841 | Product: Bhama Couture Women Red Solid A-Line Pure Cotton Top Brand: Bhama Couture Color: Red Category: A-line Pattern: Solid Neck: Round neck Sleeves: Three-quarter regular sle... |
| 19   | no  | 13969880   | -     | 0.834 | Product: Bhama Couture Yellow & White Printed Tie-Up Neck Flared Sleeves A-Line Top Brand: Bhama Couture Color: Yellow Category: A-line Pattern: Ethnic motifs printed Neck: Tie-... |
| 20   | yes | 9430109    | -     | 0.807 | Product: Bhama Couture Mustard Yellow A-Line Pure Cotton Top Brand: Bhama Couture Color: Mustard Category: A-line Pattern: Solid Neck: Round neck Sleeves: Three-quarter regular ... |
| 21   | no  | 10745490   | -     | 0.741 | Product: Bhama Couture Women Mustard Yellow Solid Mirror Work A-Line Top Brand: Bhama Couture Color: Mustard Category: A-line Pattern: Geometric solid Neck: Tie-up neck Sleeves:... |
| 22   | no  | 18288422   | -     | 0.702 | Product: Bhama Couture Women Off White Floral Chanderi Silk Anarkali Kurta & Dupatta Brand: Bhama Couture Color: Off White Pattern: Floral printed Shape: Anarkali Neck: Round ne... |
| 23   | no  | 2294119    | -     | 0.677 | Product: Bhama Couture Women Black Solid Top Brand: Bhama Couture Color: Black Category: Regular Pattern: Solid Neck: Round neck Sleeves: Three-quarter regular sleeves Length: R... |
| 24   | no  | 2129862    | -     | 0.669 | Product: Bhama Couture Women Off-White Embroidered Top Brand: Bhama Couture Color: Off White Category: Regular Pattern: Floral self design Neck: Mandarin collar Sleeves: Long fl... |
| 25   | no  | 15367618   | -     | 0.664 | Product: Bhama Couture Women Purple & Gold-Toned Block Print Anarkali Kurta Brand: Bhama Couture Color: Purple Pattern: Woven design Shape: Anarkali Neck: Mandarin collar Sleeve... |
| 26   | no  | 1823751    | -     | 0.656 | Product: Bhama Couture Black Tunic with Embroidered Detail Brand: Bhama Couture Color: Black Pattern: Embroidered Neck: Round neck Sleeves: Three-quarter sleeves Top fabric: Cot... |
| 27   | no  | 11607374   | -     | 0.653 | Product: Bhama Couture Women Blue Printed Peplum Top Brand: Bhama Couture Color: Blue Category: Peplum Pattern: Floral printed Neck: V-neck Sleeves: Three-quarter regular sleeve... |
| 28   | no  | 2129857    | -     | 0.644 | Product: Bhama Couture Women Off-White Solid Pure Cotton Top Brand: Bhama Couture Color: Off White Category: Regular Pattern: Geometric solid Neck: Tie-up neck Sleeves: Three-qu... |
| 29   | no  | 12795854   | -     | 0.641 | Product: Bhama Couture Women Black & Golden Printed Pure Cotton Straight Kurti Brand: Bhama Couture Color: Black Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck ... |
| 30   | no  | 11607414   | -     | 0.632 | Product: Bhama Couture Women Blue Printed Peplum Top Brand: Bhama Couture Color: Blue Category: Peplum Pattern: Abstract printed Neck: Round neck Sleeves: Short no sleeves Lengt... |

### Question 20/50

**Query:** Do you have any Pink Peg trousers for everyday wear?

**Relevant docs:** `['15473916']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 0.500 | 0.631 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 13740956   | -     | 1.000 | Product: Oxolloxo Women Pink Regular Fit Solid Peg Trousers Brand: Oxolloxo Color: Pink Category: Peg trousers Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion:... |
| 2    | yes | 15473916   | -     | 0.975 | Product: People Women Pink Tapered Fit High-Rise Pleated Peg Trousers Brand: People Color: Pink Category: Peg trousers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion... |
| 3    | no  | 18342112   | -     | 0.491 | Product: Go Colors Women Pink Tapered Fit Trousers Brand: Go Colors Color: Pink Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Poc... |
| 4    | no  | 13459738   | -     | 0.472 | Product: Go Colors Women Pink Tapered Fit Solid Regular Trousers Brand: Go Colors Color: Pink Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasi... |
| 5    | no  | 18838276   | -     | 0.449 | Product: Styli Women Pink Skinny Fit High-Rise Trousers Brand: Styli Color: Pink Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual... |
| 6    | no  | 19299208   | -     | 0.417 | Product: Go Colors Women Pink Crepe Trousers Brand: Go Colors Color: Pink Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Pocket... |
| 7    | no  | 15049878   | -     | 0.406 | Product: Marks & Spencer Women Pink Solid Loose Fit Pleated Parallel Trousers Brand: Marks & Spencer Color: Pink Category: Parallel trousers Pattern: Solid Length: Regular Top f... |
| 8    | no  | 18838288   | -     | 0.399 | Product: Styli Women Pink Tapered Fit High-Rise Trousers Brand: Styli Color: Pink Category: Parallel trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casu... |
| 9    | no  | 1986896    | -     | 0.384 | Product: Indibelle Turquoise Blue Peg Leg Slim Fit Peg Trousers Brand: Indibelle Color: Turquoise Blue Category: Peg trousers Pattern: Solid Length: Cropped Top fabric: Cotton O... |
| 10   | no  | 18838374   | -     | 0.376 | Product: Styli Women Pink High-Rise Trousers Brand: Styli Color: Pink Category: Bootcut trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Wash care:... |
| 11   | no  | 18342122   | -     | 0.366 | Product: Go Colors Women Blue Tapered Fit Trousers Brand: Go Colors Color: Blue Category: Peg trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets... |
| 12   | no  | 11040098   | -     | 0.353 | Product: Oxolloxo Women Blue Regular Fit Solid Peg Trousers Brand: Oxolloxo Color: Blue Category: Peg trousers Pattern: Solid Length: Cropped Top fabric: Viscose rayon Occasion:... |
| 13   | no  | 18716468   | -     | 0.351 | Product: FableStreet Women Pink Trousers Brand: FableStreet Color: Pink Category: Parallel trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Formal Pockets: 4... |
| 14   | no  | 17197778   | -     | 0.313 | Product: Mast & Harbour Women Pink Pure Cotton Pleated Trousers Brand: Mast & Harbour Color: Pink Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Oc... |
| 15   | no  | 15743324   | -     | 0.306 | Product: PINKSKY Women Blue Embroidered Smart Slim Fit Chambray Trousers Brand: PINKSKY Color: Blue Category: Regular trousers Pattern: Solid embroidered Length: Cropped Top fab... |
| 16   | no  | 13493068   | -     | 0.290 | Product: Tokyo Talkies Women Green Regular Fit Solid Peg Trousers Brand: Tokyo Talkies Color: Green Category: Peg trousers Pattern: Solid Length: Regular Top fabric: Cotton Occa... |
| 17   | no  | 9686425    | -     | 0.283 | Product: RIVI Women Pink Regular Fit Solid Regular Trousers Brand: RIVI Color: Pink Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual... |
| 18   | no  | 16531320   | -     | 0.282 | Product: JC Mode Women Pink Solid Trousers Brand: JC Mode Color: Pink Category: Regular trousers Pattern: Solid Length: Cropped Top fabric: Polyester Occasion: Casual Wash care:... |
| 19   | no  | 8999489    | -     | 0.274 | Product: Bitterlime Women Grey Relaxed Peg Trousers Brand: Bitterlime Color: Grey Category: Peg trousers Pattern: Solid Length: Cropped Occasion: Casual Pockets: 2 Wash care: Ma... |
| 20   | no  | 8999463    | -     | 0.274 | Product: Bitterlime Women Grey Relaxed Regular Fit Self Design Peg Trousers Brand: Bitterlime Color: Grey Category: Peg trousers Pattern: Textured self design Length: Cropped To... |
| 21   | no  | 13942772   | -     | 0.268 | Product: akheri Women Pink Solid Cotton Regular Fit Trousers with Embroidered Detail Brand: akheri Color: Pink Category: Regular trousers Pattern: Solid Length: Regular Top fabr... |
| 22   | no  | 19186656   | -     | 0.263 | Product: FabAlley Women Pink Pleated Trousers Brand: FabAlley Color: Pink Category: Parallel trousers Pattern: Solid Length: Cropped Top fabric: Polyester Occasion: Casual Pocke... |
| 23   | no  | 18143380   | -     | 0.253 | Product: STREET 9 Women Attractive Lime Green Striped Trousers Brand: STREET 9 Color: Lime Green Category: Peg trousers Pattern: Striped printed Length: Regular Top fabric: Cott... |
| 24   | no  | 16350330   | -     | 0.247 | Product: Enchanted Drapes Women Pink Solid Trousers Brand: Enchanted Drapes Color: Pink Category: Parallel trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: C... |
| 25   | no  | 15743322   | -     | 0.247 | Product: PINKSKY Women Grey Smart Slim Fit Trousers Brand: PINKSKY Color: Grey Category: Regular trousers Pattern: Geometric self design Length: Cropped Top fabric: Cotton Occas... |
| 26   | no  | 17278034   | -     | 0.245 | Product: Tommy Hilfiger Women Pink Solid Mid-Rise Regular Shorts Brand: Tommy Hilfiger Color: Pink Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton ... |
| 27   | no  | 14075224   | -     | 0.244 | Product: RIVI Women Blue Slim Fit Solid Cotton Peg Trousers Brand: RIVI Color: Blue Category: Peg trousers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion: Casual Poc... |
| 28   | no  | 19049088   | -     | 0.237 | Product: H&M Pink Flared Lyocell-Blend Trousers Brand: H&M Color: Pink Category: Bootcut trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Pockets: ... |
| 29   | no  | 13602838   | -     | 0.236 | Product: ROOTED Women Pink Regular Fit Solid Parallel Trousers Brand: ROOTED Color: Pink Category: Parallel trousers Pattern: Solid Length: Regular Top fabric: Linen Occasion: C... |
| 30   | no  | 18876152   | -     | 0.225 | Product: Annabelle by Pantaloons Women Blue Pleated Trousers Brand: Annabelle by Pantaloons Color: Blue Category: Peg trousers Pattern: Solid Length: Cropped Top fabric: Polyest... |

### Question 21/50

**Query:** Show me Regular shorts within a budget of 1800.

**Relevant docs:** `['15402090', '14170730', '18283554', '18747132', '16164252', '11535910', '14609842', '15083714']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.100     | 0.375  | 0.111 | 0.181 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 14272032   | -     | 1.000 | Product: Oxolloxo Women Orange Solid Regular Fit Regular Shorts Brand: Oxolloxo Color: Orange Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occas... |
| 2    | no  | 14027018   | -     | 0.764 | Product: Oxolloxo Women Olive Green Solid Regular Fit Regular Shorts Brand: Oxolloxo Color: Olive Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton O... |
| 3    | no  | 14272016   | -     | 0.757 | Product: Oxolloxo Women Green Solid Regular Fit Regular Shorts Brand: Oxolloxo Color: Green Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasio... |
| 4    | no  | 14388576   | -     | 0.732 | Product: Oxolloxo Women Black & Yellow Polka Dot Print Regular Fit Shorts Brand: Oxolloxo Color: Black Category: Regular shorts Pattern: Geometric printed Length: Above knee Top... |
| 5    | no  | 19235420   | -     | 0.711 | Product: Oxolloxo Women Brown Shorts Brand: Oxolloxo Color: Brown Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wash ... |
| 6    | no  | 16836260   | -     | 0.585 | Product: Roadster Women Indigo Shaded Mid Rise Casual Shorts Brand: Roadster Color: Blue Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: ... |
| 7    | no  | 11012420   | -     | 0.535 | Product: HRX by Hrithik Roshan Women Black & Orange Colourblocked Regular Fit Lifestyle Shorts Brand: HRX by Hrithik Roshan Color: Black Category: Regular shorts Pattern: Colour... |
| 8    | no  | 18611674   | -     | 0.533 | Product: Honey by Pantaloons Women Khaki Striped High-Rise Linen Shorts Brand: Honey by Pantaloons Color: Khaki Category: Regular shorts Pattern: Striped Length: Above knee Top ... |
| 9    | yes | 15402090   | -     | 0.515 | Product: Oxolloxo Women Green Regular Shorts Brand: Oxolloxo Color: Green Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets:... |
| 10   | no  | 17855308   | -     | 0.497 | Product: H&M Women Orange Pointelle-Knit Cotton Shorts Brand: H&M Color: Orange Category: Regular shorts Pattern: Self design solid Length: Above knee Top fabric: Cotton Occasio... |
| 11   | no  | 17887492   | -     | 0.491 | Product: Xpose Women Blue Cotton Shorts Brand: Xpose Color: Blue Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wash c... |
| 12   | no  | 16247880   | -     | 0.458 | Product: Trend Arrest Women Brown & White Floral Printed Cotton Regular Shorts Brand: Trend Arrest Color: Brown Category: Regular shorts Pattern: Floral printed Length: Above kn... |
| 13   | no  | 18297812   | -     | 0.449 | Product: VARUSHKA Women Black Loose Fit Shorts Brand: VARUSHKA Color: Black Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Viscose rayon Occasion: Casual... |
| 14   | no  | 18765570   | -     | 0.448 | Product: MOD ECRU Women Yellow Slim Fit Shorts Brand: MOD ECRU Color: Yellow Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pocke... |
| 15   | no  | 13923576   | -     | 0.423 | Product: Oxolloxo Women Multicoloured Checked Paperbag Regular Shorts Brand: Oxolloxo Color: Multi Category: Regular shorts Pattern: Checked Length: Above knee Top fabric: Visco... |
| 16   | no  | 11772110   | -     | 0.404 | Product: Honey by Pantaloons Women Navy Blue Solid Regular Fit Shorts Brand: Honey by Pantaloons Color: Navy Blue Category: Regular shorts Pattern: Solid Length: Above knee Top ... |
| 17   | no  | 12969482   | -     | 0.395 | Product: Hypernation Women Olive Green Solid Slim Fit Regular Shorts Brand: Hypernation Color: Olive Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotto... |
| 18   | no  | 14219670   | -     | 0.393 | Product: DressBerry Women Navy Blue Shorts Brand: DressBerry Color: Navy Blue Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pock... |
| 19   | no  | 18747106   | -     | 0.392 | Product: H&M Women Orange Sweatshirt Shorts Brand: H&M Color: Orange Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wa... |
| 20   | no  | 17969870   | -     | 0.389 | Product: MANGO Women Red & Navy Blue Striped Pure Cotton Regular Shorts Brand: MANGO Color: Navy Blue Category: Regular shorts Pattern: Striped Length: Above knee Top fabric: Co... |
| 21   | no  | 12539994   | -     | 0.376 | Product: FableStreet Women Brown Solid Regular Shorts Brand: FableStreet Color: Brown Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Cas... |
| 22   | no  | 15883854   | -     | 0.369 | Product: Style Quotient Women Blue Checked Regular Shorts Brand: Style Quotient Color: Blue Category: Regular shorts Pattern: Checked Length: Above knee Top fabric: Cotton Occas... |
| 23   | no  | 13069040   | -     | 0.364 | Product: Bene Kleed Women Multicoloured Striped Slim Fit Regular Shorts Brand: Bene Kleed Color: Multi Category: Regular shorts Pattern: Striped Length: Above knee Top fabric: C... |
| 24   | no  | 15912162   | -     | 0.362 | Product: Ajile by Pantaloons Women Coral Pink Pure Cotton Regular Shorts Brand: Ajile by Pantaloons Color: Coral Category: Regular shorts Pattern: Solid Length: Above knee Top f... |
| 25   | no  | 18155594   | -     | 0.359 | Product: Hypernation Women Black Solid Slim Fit Outdoor Denim Shorts Brand: Hypernation Color: Black Category: Denim shorts Pattern: Solid Length: Above knee Top fabric: Cotton ... |
| 26   | yes | 16164252   | -     | 0.349 | Product: Honey by Pantaloons Women Green Striped Regular Shorts Brand: Honey by Pantaloons Color: Green Category: Regular shorts Pattern: Striped Length: Above knee Top fabric: ... |
| 27   | no  | 16279068   | -     | 0.334 | Product: 20Dresses Women Yellow Cotton Regular Shorts Brand: 20Dresses Color: Yellow Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casu... |
| 28   | no  | 14954482   | -     | 0.307 | Product: Roadster Women Olive Green Loose Fit High-Rise Shorts Brand: Roadster Color: Olive Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasio... |
| 29   | yes | 15083714   | -     | 0.297 | Product: DressBerry Women Green Striped Regular Shorts Brand: DressBerry Color: Green Category: Regular shorts Pattern: Striped Length: Above knee Top fabric: Polyester Occasion... |
| 30   | no  | 14375954   | -     | 0.295 | Product: The Dry State Women Pack of 2 Multicoloured Solid Regular Fit Regular Shorts Brand: The Dry State Color: Multi Category: Regular shorts Pattern: Solid Length: Above kne... |

### Question 22/50

**Query:** I'm looking for Regular by H&M.

**Relevant docs:** `['17964932', '17883620', '18652012', '14258606', '18084562', '18170658', '19074168', '17674588']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.167     | 0.625  | 1.000 | 0.528 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 17674588   | -     | 1.000 | Product: H&M Women Brown Mesh Top Brand: H&M Color: Brown Category: Regular Pattern: Solid Neck: Round neck Sleeves: Long regular sleeves Length: Regular Top fabric: Polyester O... |
| 2    | no  | 17965024   | -     | 0.797 | Product: H&M Orange Ankle-Length Trousers Brand: H&M Color: Orange Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Pockets: 2 Wa... |
| 3    | no  | 12383500   | -     | 0.637 | Product: H&M Women Black Solid Long-Sleeved Jersey Top Brand: H&M Color: Black Category: Regular Pattern: Solid Neck: Round neck Sleeves: Long regular sleeves Length: Regular To... |
| 4    | no  | 17842774   | -     | 0.549 | Product: H&M Beige Wide Linen-Blend Trousers Brand: H&M Color: Beige Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion: Casual Pockets... |
| 5    | no  | 17883650   | -     | 0.531 | Product: H&M Beige Pattern-Knit Trousers Brand: H&M Color: Beige Category: Regular trousers Pattern: Solid self design Length: Regular Top fabric: Polyester Occasion: Casual Was... |
| 6    | no  | 18131688   | -     | 0.518 | Product: H&M Women Black Wide Linen-blend Trousers Brand: H&M Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Viscose rayon Occasion: Casual W... |
| 7    | yes | 14258606   | -     | 0.495 | Product: H&M Girls White Solid Jersey Top Brand: H&M Color: White Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short cap sleeves Length: Regular Top fabric: Polyco... |
| 8    | no  | 17842776   | -     | 0.446 | Product: H&M Women Beige Striped Wide Linen-Blend Trousers Brand: H&M Color: Beige Category: Regular trousers Pattern: Striped Length: Regular Top fabric: Polyester Occasion: Ca... |
| 9    | yes | 17964932   | -     | 0.428 | Product: H&M Women Yellow Rapid-Dry Sports Top Brand: H&M Color: Yellow Category: Regular Pattern: Horizontal stripes striped Neck: Round neck Sleeves: Short regular sleeves Len... |
| 10   | no  | 17611544   | -     | 0.411 | Product: H&M Women Yellow Solid Zip-Through Hoodie Brand: H&M Color: Yellow Category: Front-open Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: Ribbed ... |
| 11   | no  | 17883622   | -     | 0.373 | Product: H&M Girls Beige Cotton Jersey Cropped Top Brand: H&M Color: Beige Category: Regular Pattern: Floral printed Neck: Round neck Sleeves: Short regular sleeves Length: Regu... |
| 12   | no  | 17855308   | -     | 0.368 | Product: H&M Women Orange Pointelle-Knit Cotton Shorts Brand: H&M Color: Orange Category: Regular shorts Pattern: Self design solid Length: Above knee Top fabric: Cotton Occasio... |
| 13   | no  | 18747130   | -     | 0.366 | Product: H&M Women Beige Sweatshirt Shorts Brand: H&M Color: Beige Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wash... |
| 14   | no  | 17185466   | -     | 0.360 | Product: H&M Women Beige & Grey Solid Sweatshirt Shorts Brand: H&M Color: Beige Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Po... |
| 15   | yes | 19074168   | -     | 0.359 | Product: H&M Women Green Ribbed Cropped Top Brand: H&M Color: Green Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short regular sleeves Length: Crop Top fabric: Cot... |
| 16   | no  | 17575906   | -     | 0.359 | Product: H&M Women Blue Solid Skinny Regular Jeans Brand: H&M Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Hand wash                        |
| 17   | no  | 16396394   | -     | 0.354 | Product: H&M Women Green Fine-Knit Joggers Brand: H&M Color: Green Category: Joggers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Wash care: Hand wash      |
| 18   | no  | 18747106   | -     | 0.341 | Product: H&M Women Orange Sweatshirt Shorts Brand: H&M Color: Orange Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wa... |
| 19   | no  | 16175534   | -     | 0.339 | Product: H&M Women Red Cotton Blend Sweatpants Brand: H&M Color: Red Category: Joggers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 2 Wash care: M... |
| 20   | no  | 17842452   | -     | 0.298 | Product: H&M Women Brown Single-Breasted Jacket Brand: H&M Color: Brown Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Polyester Occasion: Casual Wash care: Ma... |
| 21   | no  | 17759938   | -     | 0.293 | Product: H&M Black Short Twill Skirt Brand: H&M Color: Black Category: Straight Pattern: Solid Length: Mini Hemline: Straight Top fabric: Cotton blend Occasion: Casual Wash care... |
| 22   | no  | 18747132   | -     | 0.289 | Product: H&M Women Green Terry Shorts Brand: H&M Color: Green Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Pockets: 2 Wash care... |
| 23   | no  | 19175092   | -     | 0.288 | Product: H&M Women Beige Solid Pull-On Lyocell-Blend Trousers Brand: H&M Color: Beige Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: C... |
| 24   | no  | 17155520   | -     | 0.285 | Product: H&M Woman Grey Hoodie Brand: H&M Color: Grey Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Cotton Occ... |
| 25   | no  | 17185856   | -     | 0.283 | Product: H&M Women Blue Straight High Jeans Brand: H&M Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash                            |
| 26   | no  | 15960258   | -     | 0.280 | Product: H&M Women Beige Long Zip-Through Hoodie Brand: H&M Color: Beige Category: Front-open Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: Ribbed Top... |
| 27   | no  | 16928312   | -     | 0.279 | Product: H&M Women White Rib-knit Cardigan Brand: H&M Color: White Category: Cardigan Pattern: Solid Neck: V-neck Sleeves: Long sleeves Length: Regular Hemline: Curved Top fabri... |
| 28   | no  | 19266852   | -     | 0.277 | Product: H&M Women Black Short Skirt Brand: H&M Color: Black Category: Straight Pattern: Solid Length: Mini Hemline: Straight Top fabric: Polyester Occasion: Casual Pockets: 2 W... |
| 29   | no  | 19071780   | -     | 0.270 | Product: H&M Women Grey Ankle-Length Linen Trousers Brand: H&M Color: Grey Category: Parallel trousers Pattern: Striped Length: Regular Top fabric: Linen Occasion: Casual Pocket... |
| 30   | yes | 17883620   | -     | 0.268 | Product: H&M Yellow Puff-Sleeved Jersey Top Brand: H&M Color: Yellow Category: Regular Pattern: Floral printed Neck: Round neck Sleeves: Short regular sleeves Length: Regular To... |

### Question 23/50

**Query:** I need Pink Saree by KALINI.

**Relevant docs:** `['15858094', '17852902', '15102290', '14678908', '16421936']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.167     | 1.000  | 1.000 | 0.990 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 16421936   | -     | 1.000 | Product: KALINI Pink & Gold-Toned Paisley Saree Brand: KALINI Color: Pink Category: Saree Pattern: Paisley printed Occasion: Festive Wash care: Dry clean                            |
| 2    | yes | 15102290   | -     | 0.957 | Product: KALINI Pink & Gold-Toned Woven Design Zari Art Silk Saree Brand: KALINI Color: Pink Category: Saree Pattern: Woven design Occasion: Traditional Wash care: Hand wash        |
| 3    | yes | 14678908   | -     | 0.906 | Product: KALINI Pink & Yellow Floral Pure Chiffon Saree Brand: KALINI Color: Pink Category: Saree Pattern: Floral printed Occasion: Festive Wash care: Hand wash                     |
| 4    | yes | 17852902   | -     | 0.905 | Product: KALINI Pink & Gold-Toned Zari Saree Brand: KALINI Color: Pink Category: Saree Pattern: Solid Occasion: Festive Wash care: Hand wash                                         |
| 5    | no  | 16914910   | -     | 0.900 | Product: KALINI Pink Poly Georgette Casual Saree Brand: KALINI Color: Pink Category: Saree Pattern: Geometric printed Occasion: Daily Wash care: Hand wash                           |
| 6    | yes | 15858094   | -     | 0.834 | Product: KALINI Pack of 2 Pink & Blue Floral Sarees Brand: KALINI Color: Pink Category: Saree Pattern: Floral printed Occasion: Daily Wash care: Machine wash                        |
| 7    | no  | 16948530   | -     | 0.834 | Product: KALINI Pink & Grey Paisley Printed Chiffon Bandhani Saree Brand: KALINI Color: Pink Category: Bandhani Pattern: Paisley printed Occasion: Work Wash care: Hand wash         |
| 8    | no  | 14798392   | -     | 0.819 | Product: KALINI Pink & Green Ethnic Motifs Kota Saree Brand: KALINI Color: Pink Category: Kota Pattern: Ethnic motifs printed Occasion: Traditional Wash care: Hand wash             |
| 9    | no  | 12961094   | -     | 0.801 | Product: KALINI Pink & Navy Blue Half & Half Printed Kanjeevaram Saree Brand: KALINI Color: Pink Category: Kanjeevaram Pattern: Kalamkari printed Occasion: Traditional Wash care... |
| 10   | no  | 17414120   | -     | 0.799 | Product: KALINI Pink & White Batik Zari Block Print Cotton Saree Brand: KALINI Color: Pink Category: Block print Pattern: Batik printed Occasion: Traditional Wash care: Hand wash   |
| 11   | no  | 16915002   | -     | 0.729 | Product: KALINI Women Green & Pink Ethnic Motifs Art Silk Saree Brand: KALINI Color: Green Category: Saree Pattern: Ethnic motifs printed Occasion: Traditional Wash care: Hand wash |
| 12   | no  | 16989798   | -     | 0.693 | Product: KALINI Sea Green & Pink Ethnic Motifs Saree Brand: KALINI Color: Sea Green Category: Saree Pattern: Ethnic motifs printed Occasion: Daily Wash care: Dry clean              |
| 13   | no  | 15102284   | -     | 0.680 | Product: KALINI Green & Pink Ethnic Motifs Art Silk Saree Brand: KALINI Color: Green Category: Saree Pattern: Ethnic motifs printed Occasion: Festive Wash care: Hand wash           |
| 14   | no  | 14986192   | -     | 0.582 | Product: KALINI Blue & Yellow Floral Saree Brand: KALINI Color: Blue Category: Saree Pattern: Floral printed Occasion: Traditional Wash care: Dry clean                              |
| 15   | no  | 16505402   | -     | 0.560 | Product: KALINI Women Pink Bandhani Printed Anarkali Kurta Brand: KALINI Color: Pink Pattern: Bandhani printed Shape: Anarkali Neck: Round neck Sleeves: Sleeveless regular Lengt... |
| 16   | no  | 17118876   | -     | 0.536 | Product: KALINI Blue & Pink Checked Ikat Saree Brand: KALINI Color: Blue Category: Ikat Pattern: Checked Occasion: Traditional Wash care: Machine wash                               |
| 17   | no  | 12792140   | -     | 0.535 | Product: KALINI Cream-Coloured & Pink Pure Georgette Embroidered Saree Brand: KALINI Color: Cream Category: Saree Pattern: Floral embroidered Occasion: Daily Wash care: Dry clean   |
| 18   | no  | 14541316   | -     | 0.491 | Product: KALINI Orange & Gold-Toned Ethnic Motifs Art Silk Saree Brand: KALINI Color: Orange Category: Saree Pattern: Ethnic motifs woven design Occasion: Festive Wash care: Han... |
| 19   | no  | 18503778   | -     | 0.487 | Product: KALINI Women Pink Floral Embroidered Layered Gotta Patti Kurti with Sharara & With Dupatta Brand: KALINI Color: Pink Category: Kurti set Top type: Kurti Bottom type: Sh... |
| 20   | no  | 18952254   | -     | 0.470 | Product: KALINI Women Pink Ethnic Motifs Embroidered Keyhole Neck Georgette Kurta Brand: KALINI Color: Pink Pattern: Ethnic motifs embroidered Shape: Straight Neck: Keyhole neck... |
| 21   | no  | 14490860   | -     | 0.465 | Product: KALINI Orange & Gold-Toned Pure Chiffon Saree Brand: KALINI Color: Orange Category: Saree Pattern: Solid Occasion: Daily Wash care: Hand wash                               |
| 22   | no  | 15258754   | -     | 0.457 | Product: KALINI Purple & Grey Ethnic Motifs Art Silk Khadi Saree Brand: KALINI Color: Purple Category: Khadi Pattern: Ethnic motifs printed Occasion: Traditional Wash care: Mach... |
| 23   | no  | 16915122   | -     | 0.444 | Product: KALINI Green & White Bandhani Art Silk Saree Brand: KALINI Color: Green Category: Bandhani Pattern: Bandhani printed Occasion: Traditional Wash care: Hand wash             |
| 24   | no  | 18435860   | -     | 0.424 | Product: KALINI Red & Gold-Toned Embellished Saree Brand: KALINI Color: Red Category: Saree Pattern: Embellished Occasion: Festive Wash care: Hand wash                              |
| 25   | no  | 16848432   | -     | 0.421 | Product: KALINI Maroon & Gold-Toned Ethnic Motifs Foil Printed Zari Saree Brand: KALINI Color: Maroon Category: Saree Pattern: Ethnic motifs printed Occasion: Festive Wash care:... |
| 26   | no  | 18495710   | -     | 0.417 | Product: KALINI Teal & Pink Checked Zari Silk Cotton Uppada Saree Brand: KALINI Color: Teal Category: Uppada Pattern: Checked Occasion: Traditional Wash care: Dry clean             |
| 27   | no  | 14679542   | -     | 0.416 | Product: KALINI Off White & Purple Art Silk Ikat Saree Brand: KALINI Color: Off White Category: Ikat Pattern: Abstract printed Occasion: Daily Wash care: Hand wash                  |
| 28   | no  | 18878880   | -     | 0.407 | Product: KALINI Sea Green & Blue Bandhani Pure Georgette Bandhani Saree Brand: KALINI Color: Sea Green Category: Bandhani Pattern: Bandhani printed Occasion: Traditional Wash ca... |
| 29   | no  | 17407676   | -     | 0.391 | Product: KALINI Black & Beige Silk Blend Bandhani Saree Brand: KALINI Color: Black Category: Bandhani Pattern: Bandhani printed Occasion: Traditional Wash care: Dry clean           |
| 30   | no  | 18907070   | -     | 0.374 | Product: KALINI Women Red & Green Floral Embroidered Silk Cotton Jamdani Saree Brand: KALINI Color: Red Category: Jamdani Pattern: Floral embroidered Occasion: Traditional Wash ... |

### Question 24/50

**Query:** Show me products within a budget of 1800.

**Relevant docs:** `['17094636', '13905652', '13905672', '13905666', '2322905', '17423996', '14925534', '14925544']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.000     | 0.000  | 0.000 | 0.000 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 17226172   | -     | 1.000 | Product: SHOWOFF Women Orange Mom Fit High-Rise Clean Look Stretchable Jeans Brand: SHOWOFF Color: Orange Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 2 Wash c... |
| 2    | no  | 17570458   | -     | 0.944 | Product: SHOWOFF Women Brown Jogger High-Rise Stretchable Jogger Brand: SHOWOFF Color: Brown Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 4 Wash care: Dry clean   |
| 3    | no  | 18142596   | -     | 0.863 | Product: SHOWOFF Women Blue Jogger High-Rise Low Distress Heavy Fade Cuffed Hem Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casua... |
| 4    | no  | 17790642   | -     | 0.802 | Product: SHOWOFF Orange & White Printed Culotte Jumpsuit Brand: SHOWOFF Color: Orange Category: Culotte jumpsuit Pattern: Printed Neck: Round neck Sleeves: Three-quarter sleeves... |
| 5    | no  | 17685090   | -     | 0.801 | Product: BUY NEW TREND Women Red Black Colourblocked Lightweight Crop Open Front Jacket Brand: BUY NEW TREND Color: Red Category: Open front jacket Pattern: Colourblocked Sleeve... |
| 6    | no  | 17250550   | -     | 0.782 | Product: SHOWOFF Women Black Embellished Top with Trousers Brand: SHOWOFF Color: Black Category: Top Top type: Top Bottom type: Trousers Pattern: Embellished Neck: Round neck Sl... |
| 7    | no  | 18388758   | -     | 0.782 | Product: SHOWOFF Burgundy Solid Culotte Jumpsuit Brand: SHOWOFF Color: Burgundy Category: Culotte jumpsuit Pattern: Solid Neck: Round neck Sleeves: Short sleeves Top fabric: Pol... |
| 8    | no  | 18189378   | -     | 0.691 | Product: SHOWOFF Blue Strapless Capri Jumpsuit Brand: SHOWOFF Color: Blue Category: Capri jumpsuit Pattern: Solid Neck: Strapless Sleeves: Sleeveless Top fabric: Polyester Occas... |
| 9    | no  | 17672184   | -     | 0.650 | Product: SHOWOFF Women Blue High-Rise Heavy Fade Stretchable Jogger Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 5 Wash care: Dry clean |
| 10   | no  | 18338282   | -     | 0.550 | Product: SHOWOFF Women Blue Slim Fit High-Rise Mildly Distressed Light Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Po... |
| 11   | no  | 17570450   | -     | 0.542 | Product: SHOWOFF Women Black Slim Fit Stretchable Cropped Jeans Brand: SHOWOFF Color: Black Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 5 Wash care: Dry clean    |
| 12   | no  | 18263720   | -     | 0.532 | Product: SHOWOFF Women Grey & Maroon Floral Print Co-Ords Brand: SHOWOFF Color: Grey Category: Top Top type: Top Bottom type: Palazzos Pattern: Printed Neck: V-neck Sleeves: Thr... |
| 13   | no  | 18067038   | -     | 0.526 | Product: BUY NEW TREND Blue Flared Knitted Palazzos Brand: BUY NEW TREND Color: Blue Pattern: Solid Length: Regular Top fabric: Modal Occasion: Western Wash care: Machine wash      |
| 14   | no  | 17570446   | -     | 0.507 | Product: SHOWOFF Women Blue Boyfriend Fit High-Rise Low Distress Light Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Po... |
| 15   | no  | 18142614   | -     | 0.488 | Product: SHOWOFF Women Lavender Jogger High-Rise Cuffed Hem Stretchable Jeans Brand: SHOWOFF Color: Lavender Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 6 and... |
| 16   | no  | 17570328   | -     | 0.483 | Product: SHOWOFF Women Blue Wide Leg High-Rise Low Distress Heavy Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Pockets... |
| 17   | no  | 17570364   | -     | 0.479 | Product: SHOWOFF Women Blue Straight Fit High-Rise Low Distress Light Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Poc... |
| 18   | no  | 18067072   | -     | 0.449 | Product: BUY NEW TREND Brown Open-Front Shrug Brand: BUY NEW TREND Color: Brown Pattern: Solid Sleeves: Three-quarter sleeves Length: Regular Hemline: Straight Top fabric: Cotto... |
| 19   | no  | 18011278   | -     | 0.434 | Product: Inddus Orange & Gold-Toned Unstitched Dress Material Brand: Inddus Color: Orange Category: Dress Pattern: Floral Bottom fabric: Silk blend Dupatta fabric: Silk blend Oc... |
| 20   | no  | 18388752   | -     | 0.434 | Product: SHOWOFF Orange & White Printed Jumpsuit Brand: SHOWOFF Color: Orange Category: Playsuit Pattern: Printed Neck: Shoulder straps Sleeves: Sleeveless Top fabric: Cotton Oc... |
| 21   | no  | 18324286   | -     | 0.419 | Product: Fashion Basket Red & Black Embroidered Thread Work Semi-Stitched Lehenga & Blouse With Dupatta Brand: Fashion Basket Color: Red Dupatta: With dupatta Pattern: Embroider... |
| 22   | no  | 17685350   | -     | 0.419 | Product: BUY NEW TREND Women Maroon Lightweight Crop Open Front Jacket Brand: BUY NEW TREND Color: Maroon Category: Open front jacket Pattern: Abstract solid Sleeves: Three-quar... |
| 23   | no  | 16524266   | -     | 0.407 | Product: LOOKNBOOK ART Orange Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: LOOKNBOOK ART Color: Orange Dupatta: With dupatta Pattern: Woven design Neck: Round n... |
| 24   | no  | 17570416   | -     | 0.364 | Product: SHOWOFF Women Black Straight Fit Stretchable Jeans Brand: SHOWOFF Color: Black Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 6 and more Wash care: Dry ... |
| 25   | no  | 17716122   | -     | 0.349 | Product: Ahalyaa Geometric Crepe Top to Toe Fusion Kurta Set Brand: Ahalyaa Color: Burgundy Category: Kurta set Top type: Kurta Bottom type: Sharara Dupatta: With dupatta Patter... |
| 26   | no  | 18247990   | -     | 0.348 | Product: SHOWOFF Women Blue Washed Denim Jacket Brand: SHOWOFF Color: Blue Category: Denim jacket Pattern: Washed solid Sleeves: Long sleeves Length: Regular Hemline: Straight T... |
| 27   | no  | 18247980   | -     | 0.338 | Product: SHOWOFF Women Blue Washed Denim Jacket Brand: SHOWOFF Color: Blue Category: Denim jacket Pattern: Washed solid Sleeves: Long sleeves Length: Regular Hemline: Straight T... |
| 28   | no  | 18309022   | -     | 0.323 | Product: PURVAJA Olive Green & Red Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: PURVAJA Color: Olive Dupatta: With dupatta Pattern: Woven design Neck: Round nec... |
| 29   | no  | 18067068   | -     | 0.322 | Product: BUY NEW TREND Beige Open-Front Shrug Brand: BUY NEW TREND Color: Beige Pattern: Solid Sleeves: Three-quarter sleeves Length: Regular Hemline: Asymmetric Top fabric: Cot... |
| 30   | no  | 17226246   | -     | 0.316 | Product: SHOWOFF Women Charcoal Grey Wide Leg High-Rise Clean Look Jeans Brand: SHOWOFF Color: Charcoal Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care:... |

### Question 25/50

**Query:** I need product with a Other woven design pattern in Red.

**Relevant docs:** `['16379852', '16379914', '15768366']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.100     | 1.000  | 1.000 | 0.922 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 16379914   | -     | 1.000 | Product: Safaa Women Red Woven Design Acrylic Blend Shawl Brand: Safaa Color: Red Pattern: Other woven design Top fabric: Acrylic Occasion: Daily                                    |
| 2    | yes | 15768366   | -     | 0.998 | Product: VERO AMORE Women Red & Beige Woven-Design Jacquard Shawl Brand: VERO AMORE Color: Red Pattern: Other woven design Top fabric: Wool Occasion: Daily                          |
| 3    | no  | 19366710   | -     | 0.946 | Product: RIVAMA Red & Green Ethnic Motifs Woven Design Cotton Silk Foil Print Dupatta Brand: RIVAMA Color: Red Pattern: Ethnic motifs woven design Top fabric: Cotton silk Occasi... |
| 4    | no  | 13616810   | -     | 0.944 | Product: Dupatta Bazaar Red & Orange Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Striped woven design Top fabric: Cotton blend Occasion: Daily Wash care: Hand... |
| 5    | no  | 13497800   | -     | 0.939 | Product: InWeave Women Red Striped A-Line Top Brand: InWeave Color: Red Category: Regular Pattern: Vertical stripes self design Neck: Round neck Sleeves: Sleeveless no Length: R... |
| 6    | no  | 17662882   | -     | 0.870 | Product: Dupatta Bazaar Red Woven Design Dupatta with Sequinned Detail Brand: Dupatta Bazaar Color: Red Pattern: Geometric woven design Top fabric: Net Occasion: Party Wash care... |
| 7    | yes | 16379852   | -     | 0.863 | Product: Safaa Women Red & Black Woven Design Shawl Brand: Safaa Color: Red Pattern: Other woven design Top fabric: Acrylic Occasion: Daily                                          |
| 8    | no  | 2138931    | -     | 0.818 | Product: WEAVERS VILLA Coral Red & Beige Woven Design Shawl Brand: WEAVERS VILLA Color: Coral Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily                   |
| 9    | no  | 11379820   | -     | 0.698 | Product: SHINGORA Women Red & Blue Woven Design Pure Woolen Jacquard Weave Shawl Brand: SHINGORA Color: Red Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily     |
| 10   | no  | 15121622   | -     | 0.695 | Product: Cayman Women Red & Beige Woollen Woven Design Shawl Brand: Cayman Color: Red Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily                           |
| 11   | no  | 18205188   | -     | 0.680 | Product: Inddus Red & Gold-Toned Woven Design Silk Blend Patola Saree Brand: Inddus Color: Red Category: Patola Pattern: Ethnic motifs woven design Occasion: Traditional Wash ca... |
| 12   | no  | 18806012   | -     | 0.636 | Product: awesome Red & Gold-Toned Woven Design Zari Pure Silk Banarasi Saree Brand: awesome Color: Red Category: Banarasi Pattern: Woven design Occasion: Traditional Wash care: ... |
| 13   | no  | 15874790   | -     | 0.570 | Product: Pashmoda Women Red Woven Design Jamawar Shawl Brand: Pashmoda Color: Red Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily                               |
| 14   | no  | 8278529    | -     | 0.567 | Product: Faserz Red Woven Design Banarasi Dupatta Brand: Faserz Color: Red Pattern: Ethnic motifs woven design Top fabric: Silk blend Occasion: Party Wash care: Dry clean           |
| 15   | no  | 13104106   | -     | 0.566 | Product: Pashmoda Women Red Woven Design Shawl Brand: Pashmoda Color: Red Pattern: Paisley woven design Top fabric: Wool Occasion: Daily                                             |
| 16   | no  | 15393074   | -     | 0.555 | Product: Desi Weavess Red Art Silk Dupatta Brand: Desi Weavess Color: Red Pattern: Solid Top fabric: Art silk Occasion: Party Wash care: Dry clean                                   |
| 17   | no  | 4444074    | -     | 0.549 | Product: Dupatta Bazaar Red & Orange Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Paisley woven design Top fabric: Silk blend Occasion: Party Wash care: Dry clean |
| 18   | no  | 17764814   | -     | 0.518 | Product: Silk Land Red & Gold-Toned Ethnic Motifs Woven Design Dupatta with Zari Brand: Silk Land Color: Red Pattern: Ethnic motifs woven design Top fabric: Silk blend Occasion:... |
| 19   | no  | 16874574   | -     | 0.488 | Product: Mitera Red Woven Design Zari Silk Blend Paithani Saree Brand: Mitera Color: Red Category: Paithani Pattern: Woven design Occasion: Traditional Wash care: Dry clean         |
| 20   | no  | 10358133   | -     | 0.482 | Product: Dupatta Bazaar Red & Gold-Coloured Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Polka dots woven design Top fabric: Poly chiffon Occasion: Daily Wash ... |
| 21   | no  | 13552260   | -     | 0.462 | Product: Dupatta Bazaar Red & Yellow Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Bandhani woven design Top fabric: Pure silk Occasion: Party Wash care: Dry clean |
| 22   | no  | 15760840   | -     | 0.439 | Product: InWeave Red & Gold-Toned Regular Crop Top Brand: InWeave Color: Red Category: Regular Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Three-quarter flared slee... |
| 23   | no  | 6581979    | -     | 0.428 | Product: Dupatta Bazaar Red & Gold-Toned Woven Design Dupatta Brand: Dupatta Bazaar Color: Red Pattern: Floral woven design Top fabric: Pure silk Occasion: Party Wash care: Dry ... |
| 24   | no  | 16197692   | -     | 0.418 | Product: Pashmoda Womens Red Kaani Woven Design Shawl Brand: Pashmoda Color: Red Pattern: Floral woven design Top fabric: Wool Occasion: Daily                                       |
| 25   | no  | 13448688   | -     | 0.418 | Product: Honey by Pantaloons Women Red Self Design Cardigan Sweater Brand: Honey by Pantaloons Color: Red Category: Cardigan Pattern: Ribbed self design Neck: V-neck Sleeves: Lo... |
| 26   | no  | 17764826   | -     | 0.391 | Product: Silk Land Women Red Jacquared Banarasi Dupatta Brand: Silk Land Color: Red Pattern: Ethnic motifs woven design Top fabric: Silk blend Occasion: Party Wash care: Dry clean  |
| 27   | no  | 19029736   | -     | 0.369 | Product: Mitera Red & Gold-Toned Woven Design Zari Silk Blend Patola Saree Brand: Mitera Color: Red Category: Patola Pattern: Woven design Occasion: Traditional Wash care: Dry c... |
| 28   | no  | 17735542   | -     | 0.360 | Product: Iris Red Floral Net Saree Brand: Iris Color: Red Category: Saree Pattern: Floral woven design Occasion: Party Wash care: Hand wash                                          |
| 29   | no  | 17693086   | -     | 0.339 | Product: Silk Land Red & Gold-Toned Woven Design Zari Pure Silk Banarasi Saree Brand: Silk Land Color: Red Category: Banarasi Pattern: Woven design Occasion: Traditional Wash ca... |
| 30   | no  | 10814044   | -     | 0.320 | Product: WEAVERS VILLA Red & Yellow Phulkari Embroidered Dupatta Brand: WEAVERS VILLA Color: Red Pattern: Geometric embroidered Top fabric: Poly chiffon Occasion: Party Wash car... |

### Question 26/50

**Query:** Do you have anything from SERONA FABRICS in White for everyday wear?

**Relevant docs:** `['15917640']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 15917640   | -     | 1.000 | Product: SERONA FABRICS White & Pink Floral Embroidered Anarkali Kurti Brand: SERONA FABRICS Color: White Pattern: Floral embroidered Shape: Anarkali Neck: Round neck Sleeves: T... |
| 2    | no  | 18845142   | -     | 0.721 | Product: SERONA FABRICS Peach-Coloured & White Tunic Brand: SERONA FABRICS Color: Peach Pattern: Self design Neck: Round neck Sleeves: Three-quarter sleeves Top fabric: Cotton O... |
| 3    | no  | 18845144   | -     | 0.713 | Product: SERONA FABRICS Grey & Off White Tunic Brand: SERONA FABRICS Color: Grey Pattern: Self design Neck: Round neck Sleeves: Three-quarter sleeves Top fabric: Cotton Occasion... |
| 4    | no  | 15907476   | -     | 0.533 | Product: SERONA FABRICS Red & White Printed Unstitched Dress Material Brand: SERONA FABRICS Color: Red Category: Dress Pattern: Floral Bottom fabric: Shantoon Dupatta fabric: Si... |
| 5    | no  | 15907474   | -     | 0.457 | Product: SERONA FABRICS Women Peach Floral Printed Unstitched Dress Material Brand: SERONA FABRICS Color: Peach Category: Dress Pattern: Floral Bottom fabric: Shantoon Dupatta f... |
| 6    | no  | 16258082   | -     | 0.451 | Product: SERONA FABRICS Yellow Floral Embroidered Silk Blend Saree Brand: SERONA FABRICS Color: Yellow Category: Saree Pattern: Floral embroidered Occasion: Party Wash care: Dry... |
| 7    | no  | 15907480   | -     | 0.428 | Product: SERONA FABRICS Blue & Gold-Toned Embroidered Unstitched Dress Material Brand: SERONA FABRICS Color: Blue Category: Dress Pattern: Floral Bottom fabric: Shantoon Dupatta... |
| 8    | no  | 14238538   | -     | 0.411 | Product: Sera Women White & Black Printed Basic Jumpsuit Brand: Sera Color: White Category: Basic jumpsuit Pattern: Printed Neck: V-neck Sleeves: Sleeveless Top fabric: Polyeste... |
| 9    | no  | 14375990   | -     | 0.396 | Product: Sera Women Off White & Grey Printed Shrug Brand: Sera Color: Off White Pattern: Printed Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Polycotton O... |
| 10   | no  | 17784302   | -     | 0.374 | Product: Sera Women White Floral Print Georgette Crop Top Brand: Sera Color: White Category: Regular Pattern: Floral printed Neck: V-neck Sleeves: Three-quarter puff sleeves Len... |
| 11   | no  | 15907478   | -     | 0.369 | Product: SERONA FABRICS Red Embroidered Unstitched Dress Material Brand: SERONA FABRICS Color: Red Category: Dress Pattern: Floral Bottom fabric: Shantoon Dupatta fabric: Silk b... |
| 12   | no  | 18360202   | -     | 0.365 | Product: Sera Women Off-White Printed Co-Ord Set Brand: Sera Color: Off White Category: Top Top type: Top Bottom type: Skirt Pattern: Printed Neck: Halter neck Sleeves: Sleevele... |
| 13   | no  | 15907488   | -     | 0.364 | Product: SERONA FABRICS Pink Embroidered Chanderi Unstitched Dress Material Brand: SERONA FABRICS Color: Pink Category: Dress Pattern: Floral Bottom fabric: Shantoon Dupatta fab... |
| 14   | no  | 996729     | -     | 0.262 | Product: Dupatta Bazaar White Silk Dupatta Brand: Dupatta Bazaar Color: White Pattern: Solid Occasion: Daily                                                                         |
| 15   | no  | 10035883   | -     | 0.228 | Product: Sera Women Black Solid Loose Fit Regular Shorts Brand: Sera Color: Black Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Viscose rayon Occasion: ... |
| 16   | no  | 19005622   | -     | 0.221 | Product: ORUS White Solid Dupatta Brand: ORUS Color: White Pattern: Solid Top fabric: Poly chiffon Occasion: Daily Wash care: Machine wash                                           |
| 17   | no  | 14008468   | -     | 0.206 | Product: Sera Women Brown & White Printed Flared Mini Skirt Brand: Sera Color: Brown Category: Flared Pattern: Geometric printed Length: Mini Hemline: Flared Top fabric: Polyest... |
| 18   | no  | 17231652   | -     | 0.185 | Product: Clora Creation White & Beige Striped Dupatta Brand: Clora Creation Color: White Pattern: Striped Top fabric: Silk blend Occasion: Daily Wash care: Hand wash                |
| 19   | no  | 11275704   | -     | 0.184 | Product: ADA White Solid Mukaish Work Sustainable Dupatta Brand: ADA Color: White Pattern: Solid Top fabric: Poly chiffon Occasion: Daily Wash care: Hand wash                       |
| 20   | no  | 19338482   | -     | 0.175 | Product: Satrani White Embroidered Dupatta Brand: Satrani Color: White Pattern: Floral embroidered Top fabric: Net Occasion: Daily Wash care: Hand wash                              |
| 21   | no  | 17831112   | -     | 0.174 | Product: Senyora White Floral Embroidered Shirt Style Top Brand: Senyora Color: White Category: Shirt style Pattern: Floral solid Neck: Shirt collar Sleeves: Three-quarter regul... |
| 22   | no  | 10783332   | -     | 0.171 | Product: Sera Women Off-White & Pink Printed Basic Jumpsuit Brand: Sera Color: Off White Category: Basic jumpsuit Pattern: Printed Neck: Round neck Sleeves: Sleeveless Top fabri... |
| 23   | no  | 10496030   | -     | 0.170 | Product: Sera Women Black Solid Loose Fit Regular Shorts Brand: Sera Color: Black Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Viscose rayon Occasion: ... |
| 24   | no  | 10711448   | -     | 0.170 | Product: Dupatta Bazaar Women White Solid Dupatta Brand: Dupatta Bazaar Color: White Pattern: Solid Top fabric: Poly chiffon Occasion: Daily Wash care: Hand wash                    |
| 25   | no  | 19260118   | -     | 0.168 | Product: SALWAR STUDIO White & Blue Printed Unstitched Dress Material Brand: SALWAR STUDIO Color: White Category: Dress Pattern: Floral Bottom fabric: Poly crepe Dupatta fabric:... |
| 26   | no  | 2594438    | -     | 0.159 | Product: Sera Blue & White Striped Cinched Waist Top Brand: Sera Color: Blue Category: Cinched waist Pattern: Vertical stripes striped Neck: Boat neck Sleeves: Long puff sleeves... |
| 27   | no  | 12718796   | -     | 0.127 | Product: Sera Women Black & White Polka Dot Print Playsuit Brand: Sera Color: Black Category: Playsuit Pattern: Printed Neck: Off-shoulder Sleeves: Sleeveless Top fabric: Polyes... |
| 28   | no  | 14056588   | -     | 0.126 | Product: SOUNDARYA Yellow & Pink Striped Dupatta Brand: SOUNDARYA Color: Yellow Pattern: Leheriya striped Top fabric: Poly chiffon Occasion: Daily Wash care: Machine wash           |
| 29   | no  | 10358153   | -     | 0.126 | Product: Dupatta Bazaar White Solid Dupatta Brand: Dupatta Bazaar Color: White Pattern: Solid Top fabric: Cotton silk Occasion: Daily Wash care: Machine wash                        |
| 30   | no  | 16119706   | -     | 0.125 | Product: SOUNDARYA Orange & White Striped Pure Cotton Leheriya Dupatta Brand: SOUNDARYA Color: Orange Pattern: Leheriya striped Top fabric: Pure cotton Occasion: Daily Wash care... |

### Question 27/50

**Query:** Do you have any Green Kurta set for a festive occasion?

**Relevant docs:** `['17140156', '16505434', '14121912', '16825614', '16707970', '15677426', '17232410', '14920000']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.233     | 0.875  | 0.250 | 0.496 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 17447636   | -     | 1.000 | Product: Khushal K Women Green Ethnic Motifs Printed Gotta Patti Kurta with Trousers & Dupatta Brand: Khushal K Color: Green Category: Kurta set Top type: Kurta Bottom type: Tro... |
| 2    | no  | 15508896   | -     | 0.892 | Product: Indo Era Women Green Ethnic Motifs Yoke Design Kurta with Palazzos & With Dupatta Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos... |
| 3    | no  | 15258422   | -     | 0.840 | Product: Indo Era Floral Cotton Blend Calf Length Kurta Set Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta Pattern:... |
| 4    | yes | 16707970   | -     | 0.771 | Product: mokshi Ethnic Motifs Viscose Rayon Kurta Set Brand: mokshi Color: Green Category: Kurta set Top type: Kurta Bottom type: Skirt Pattern: Ethnic motifs printed Shape: Ana... |
| 5    | no  | 12989804   | -     | 0.761 | Product: mokshi Women Green & Maroon Foil Print Front Slit Kurta with Palazzos Brand: mokshi Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Pattern: Ethn... |
| 6    | no  | 15654150   | -     | 0.699 | Product: Indo Era Women Green Ethnic Motifs Yoke Design Regular Kurta with Trousers & With Dupatta Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: ... |
| 7    | no  | 15054430   | -     | 0.678 | Product: Biba Women Green Ethnic Motifs Printed Regular Pure Cotton Kurta with Palazzos & With Dupatta Brand: Biba Color: Green Category: Kurta set Top type: Kurta Bottom type: ... |
| 8    | yes | 17140156   | -     | 0.666 | Product: Myshka Women Green Kurta with Palazzos & With Dupatta Brand: Myshka Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With dupatta Pattern... |
| 9    | no  | 13392426   | -     | 0.634 | Product: Khushal K Women Lime Green Printed Kurta with Churidar & Dupatta Brand: Khushal K Color: Lime Green Category: Kurta set Top type: Kurta Bottom type: Churidar Dupatta: W... |
| 10   | yes | 16825614   | -     | 0.595 | Product: Stylum Women Green Embroidered Pure Cotton Kurta with Sharara & With Dupatta Brand: Stylum Color: Green Category: Kurta set Top type: Kurta Bottom type: Sharara Dupatta... |
| 11   | no  | 15026486   | -     | 0.587 | Product: W Women Green & Golden Regular Sequinned Kurta with Trousers & With Dupatta Brand: W Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: Wit... |
| 12   | no  | 17624906   | -     | 0.578 | Product: KAAJH Women Green Embroidered Chikankari Pure Cotton Kurti with Palazzos & With Dupatta Brand: KAAJH Color: Green Category: Kurti set Top type: Kurti Bottom type: Palaz... |
| 13   | no  | 18551726   | -     | 0.541 | Product: POONAM DESIGNER Women Lime Green Gotta Patti Pure Cotton Kurta with Trousers & With Dupatta Brand: POONAM DESIGNER Color: Lime Green Category: Kurta set Top type: Kurta... |
| 14   | yes | 14920000   | -     | 0.536 | Product: Indo Era Women Green Floral Embroidered Gotta Patti Liva Kurta with Trousers & Dupatta Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: Tro... |
| 15   | no  | 15258010   | -     | 0.534 | Product: Libas Women Green & White Floral Embroidered Kurta with Palazzos & Dupatta Brand: Libas Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: ... |
| 16   | no  | 17048604   | -     | 0.497 | Product: Khushal K Women Green & Pink Printed Pure Cotton Kurta with Palazzos & Dupatta Brand: Khushal K Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos D... |
| 17   | yes | 16505434   | -     | 0.479 | Product: KALINI Women Green Floral Printed Pure Cotton Straight Kurta with Trousers Brand: KALINI Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern:... |
| 18   | no  | 18810192   | -     | 0.477 | Product: GUNVANTI FAB Women Green Yoke Design Thread Work Kurti with Palazzos & With Dupatta Brand: GUNVANTI FAB Color: Green Category: Kurti set Top type: Kurti Bottom type: Pa... |
| 19   | no  | 16931552   | -     | 0.464 | Product: all about you Women Green Embroidered Kurta with Trousers Brand: all about you Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Pattern: Solid emb... |
| 20   | no  | 19040558   | -     | 0.463 | Product: KARAJ JAIPUR Women Green Floral Anarkali Pure Cotton Kurta with Pant & Dupatta Brand: KARAJ JAIPUR Color: Green Category: Kurta set Top type: Kurta Bottom type: Trouser... |
| 21   | no  | 18002690   | -     | 0.444 | Product: SINGNI Women Green Embroidered Printed Kurta with Trousers & dupatta Brand: SINGNI Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With ... |
| 22   | yes | 15677426   | -     | 0.439 | Product: SWAGG INDIA Women Green Floral Embroidered Regular Kurta with Trousers & With Dupatta Brand: SWAGG INDIA Color: Green Category: Kurta set Top type: Kurta Bottom type: T... |
| 23   | no  | 13810898   | -     | 0.438 | Product: Indo Era Women Blue & Green Printed Kurta with Palazzos & Dupatta Brand: Indo Era Color: Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With du... |
| 24   | no  | 13940072   | -     | 0.428 | Product: W Women Green Geometric Printed Kurta Brand: W Color: Green Pattern: Geometric printed Shape: A-line Neck: Mandarin collar Sleeves: Three-quarter regular sleeves Length... |
| 25   | no  | 14967448   | -     | 0.419 | Product: Indo Era Women Green Ethnic Motifs Printed Panelled Gotta Patti Pure Cotton Kurta with Trousers & With Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta ... |
| 26   | no  | 15714504   | -     | 0.416 | Product: Varanga Women Green Ethnic Motifs Embroidered Regular Kurti with Sharara & With Dupatta Brand: Varanga Color: Green Category: Kurti set Top type: Kurti Bottom type: Sha... |
| 27   | yes | 17232410   | -     | 0.415 | Product: InWeave Green Pure Cotton Print Parade Kurta Set Brand: InWeave Color: Green Category: Kurta set Top type: Kurta Bottom type: Sharara Pattern: Ethnic motifs printed Sha... |
| 28   | no  | 13771272   | -     | 0.399 | Product: Nayo Women Green Printed Kurta with Trousers & Dupatta Brand: Nayo Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta Pattern:... |
| 29   | no  | 15471926   | -     | 0.380 | Product: Kvsfab Women Green Embellished Bell Sleeves Georgette Anarkali Kurta Brand: Kvsfab Color: Green Pattern: Embellished Shape: Anarkali Neck: Round neck Sleeves: Three-qua... |
| 30   | no  | 19181470   | -     | 0.371 | Product: Baisacrafts Women Green Striped Pure Cotton Kurta with Trousers & With Dupatta Brand: Baisacrafts Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers... |

### Question 28/50

**Query:** I'm looking for something Black from URBANIC for everyday wear.

**Relevant docs:** `['15849954', '15634138', '18929182', '15086606', '15633414', '18866648', '18605954', '18907592']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.200     | 0.750  | 0.125 | 0.371 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 18328804   | -     | 1.000 | Product: URBANIC Women Black Jeans Brand: URBANIC Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Wash care: Machine wash                                           |
| 2    | no  | 18542924   | -     | 0.808 | Product: URBANIC Women Black Solid Mid-Rise Wide Leg Jeans Brand: URBANIC Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash        |
| 3    | no  | 19072596   | -     | 0.760 | Product: URBANIC Women Black Relaxed Fit Mildly Distressed Jeans Brand: URBANIC Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 4 Wash care: Machine wash  |
| 4    | no  | 18867438   | -     | 0.729 | Product: URBANIC Women Black Trousers Brand: URBANIC Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Casual Wash care: Mac... |
| 5    | no  | 18644820   | -     | 0.715 | Product: URBANIC Women Black Solid Blazers Brand: URBANIC Color: Black Pattern: Solid Sleeves: Long sleeves Length: Crop Top fabric: Polyester Occasion: Casual Wash care: Machin... |
| 6    | no  | 15845464   | -     | 0.694 | Product: URBANIC Women Black Solid Cotton Sweatshirt Brand: URBANIC Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Crop Hemline: S... |
| 7    | no  | 15851566   | -     | 0.692 | Product: URBANIC Women Black Padded Jacket Brand: URBANIC Color: Black Category: Padded jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric:... |
| 8    | yes | 18929182   | -     | 0.654 | Product: URBANIC Black Embroidered Halter Neck Top Brand: URBANIC Color: Black Category: Regular Pattern: Solid embroidered Neck: Halter neck Sleeves: Sleeveless no Length: Regu... |
| 9    | no  | 15852292   | -     | 0.648 | Product: URBANIC Women Black Cotton Solid Cropped Jeans Brand: URBANIC Color: Black Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash           |
| 10   | no  | 15844202   | -     | 0.641 | Product: URBANIC Women Black & Off White Solid Cardigan Brand: URBANIC Color: Black Category: Cardigan Pattern: Solid Neck: V-neck Sleeves: Long sleeves Length: Regular Hemline:... |
| 11   | no  | 15633286   | -     | 0.628 | Product: URBANIC Women Black Solid Skinny Fit Non-Stretchable Cotton Crop Jeans Brand: URBANIC Color: Black Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 12   | no  | 18875978   | -     | 0.604 | Product: URBANIC Women Black Denim Shorts Brand: URBANIC Color: Black Category: Denim shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Wash care: Mac... |
| 13   | no  | 18905328   | -     | 0.602 | Product: URBANIC Black Basic Jumpsuit Brand: URBANIC Color: Black Category: Basic jumpsuit Pattern: Solid Neck: Boat neck Sleeves: Short sleeves Top fabric: Polyester Occasion: ... |
| 14   | no  | 18905308   | -     | 0.594 | Product: URBANIC Black Basic Jumpsuit Brand: URBANIC Color: Black Category: Basic jumpsuit Pattern: Solid Neck: V-neck Sleeves: Sleeveless Top fabric: Polyester Occasion: Casual... |
| 15   | yes | 15634138   | -     | 0.589 | Product: URBANIC Women Black Tailored Jacket Brand: URBANIC Color: Black Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fab... |
| 16   | no  | 18907806   | -     | 0.556 | Product: URBANIC Women Black Solid Double-Breasted Button Vest Blazer Brand: URBANIC Color: Black Pattern: Solid Sleeves: Short sleeves Length: Regular Top fabric: Polyester Occ... |
| 17   | yes | 18605954   | -     | 0.555 | Product: URBANIC Women Black Solid Pure Cotton A-Line Skirts Brand: URBANIC Color: Black Category: A-line Pattern: Solid Length: Mini Hemline: Straight Top fabric: Pure cotton O... |
| 18   | no  | 15633046   | -     | 0.548 | Product: URBANIC Women Black Pure Cotton Slim Fit High-Rise Regular Shorts Brand: URBANIC Color: Black Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cot... |
| 19   | no  | 16102760   | -     | 0.540 | Product: URBANIC Black Solid Basic Jumpsuit with Lace Inserts Brand: URBANIC Color: Black Category: Basic jumpsuit Pattern: Solid Neck: V-neck Sleeves: Sleeveless Top fabric: Po... |
| 20   | yes | 15086606   | -     | 0.532 | Product: URBANIC Women Black Printed Sweatshirt Brand: URBANIC Color: Black Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length: Regular... |
| 21   | no  | 15082220   | -     | 0.530 | Product: URBANIC Black Ribbed Slim Fit Basic Jumpsuit Brand: URBANIC Color: Black Category: Basic jumpsuit Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless Top fabric: P... |
| 22   | no  | 15851868   | -     | 0.515 | Product: URBANIC Black & White Printed Basic Jumpsuit Brand: URBANIC Color: Black Category: Basic jumpsuit Pattern: Printed Neck: V-neck Sleeves: Sleeveless Top fabric: Polyeste... |
| 23   | yes | 15633414   | -     | 0.501 | Product: URBANIC Women Black Solid Cropped Basic Jumpsuit with Tie-Up Detail Brand: URBANIC Color: Black Category: Basic jumpsuit Pattern: Solid Neck: Scoop neck Sleeves: Sleeve... |
| 24   | yes | 18866648   | -     | 0.495 | Product: URBANIC Black Semi Sheer Crop Top Brand: URBANIC Color: Black Category: Regular Pattern: Self design Neck: V-neck Sleeves: Long regular sleeves Length: Crop Top fabric:... |
| 25   | no  | 15851740   | -     | 0.493 | Product: URBANIC Women Plus Size Black Solid Waistcoat Brand: URBANIC Color: Black Pattern: Solid Top fabric: Polyester Occasion: Casual Wash care: Dry clean                        |
| 26   | no  | 15851802   | -     | 0.470 | Product: URBANIC Women Black Solid Two-Piece Gym Suit with Cut Out Detail Brand: URBANIC Color: Black Category: Top Top type: Top Bottom type: Trousers Pattern: Solid Neck: Roun... |
| 27   | no  | 19093160   | -     | 0.470 | Product: URBANIC Women Black Checked Trousers Brand: URBANIC Color: Black Category: Bootcut trousers Pattern: Checked Length: Regular Top fabric: Polyester Occasion: Party Wash ... |
| 28   | no  | 15098700   | -     | 0.453 | Product: URBANIC Black Solid Mini Co-ordinate Sets Brand: URBANIC Color: Black Category: Top Top type: Top Bottom type: Skirt Pattern: Solid Neck: Shirt collar Sleeves: Sleevele... |
| 29   | no  | 15632460   | -     | 0.442 | Product: URBANIC Women Black Solid High-Rise Denim Shorts Brand: URBANIC Color: Black Category: Denim shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casua... |
| 30   | no  | 18643006   | -     | 0.440 | Product: URBANIC Women Black Solid Co-Ords Brand: URBANIC Color: Black Category: Top Top type: Top Bottom type: Skirt Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless To... |

### Question 29/50

**Query:** Show me Black products for everyday wear.

**Relevant docs:** `['9440729', '18207452', '18992236', '16612058', '9073715', '16728358', '7437296', '16728350']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.000     | 0.000  | 0.000 | 0.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 19270830   | -     | 1.000 | Product: Blamblack Women Black Solid Shirt & Pant Co-Ords Brand: Blamblack Color: Black Category: T-shirt Top type: T-shirt Bottom type: Trousers Pattern: Solid Neck: Round neck... |
| 2    | no  | 19187496   | -     | 0.861 | Product: Blamblack Women Black & Grey Solid Co-Ords Brand: Blamblack Color: Black Category: T-shirt Top type: T-shirt Bottom type: Trousers Pattern: Solid Neck: Round neck Sleev... |
| 3    | no  | 17570416   | -     | 0.790 | Product: SHOWOFF Women Black Straight Fit Stretchable Jeans Brand: SHOWOFF Color: Black Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 6 and more Wash care: Dry ... |
| 4    | no  | 12383500   | -     | 0.683 | Product: H&M Women Black Solid Long-Sleeved Jersey Top Brand: H&M Color: Black Category: Regular Pattern: Solid Neck: Round neck Sleeves: Long regular sleeves Length: Regular To... |
| 5    | no  | 13552234   | -     | 0.647 | Product: Dupatta Bazaar Black Solid Dupatta Brand: Dupatta Bazaar Color: Black Pattern: Solid Top fabric: Poly chiffon Occasion: Daily Wash care: Machine wash                       |
| 6    | no  | 17570450   | -     | 0.588 | Product: SHOWOFF Women Black Slim Fit Stretchable Cropped Jeans Brand: SHOWOFF Color: Black Length: Cropped Top fabric: Elastane Occasion: Casual Pockets: 5 Wash care: Dry clean    |
| 7    | no  | 18207362   | -     | 0.579 | Product: Dupatta Bazaar Black Linen Dupatta Brand: Dupatta Bazaar Color: Black Pattern: Solid Top fabric: Linen Occasion: Daily Wash care: Hand wash                                 |
| 8    | no  | 14263292   | -     | 0.556 | Product: AMERICAN EAGLE OUTFITTERS Women Black Solid Denim Jacket Brand: AMERICAN EAGLE OUTFITTERS Color: Black Category: Denim jacket Pattern: Washed solid Sleeves: Long sleeve... |
| 9    | no  | 16220586   | -     | 0.554 | Product: 20Dresses Women Black Biker Jacket Brand: 20Dresses Color: Black Category: Biker jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabri... |
| 10   | no  | 16379842   | -     | 0.545 | Product: Safaa Women Black & Beige Woven Design Shawl Brand: Safaa Color: Black Pattern: Other woven design Top fabric: Acrylic Occasion: Daily                                      |
| 11   | no  | 16379878   | -     | 0.530 | Product: Safaa Women Black & Blue Woven Design Shawl Brand: Safaa Color: Black Pattern: Other woven design Top fabric: Acrylic Occasion: Daily                                       |
| 12   | no  | 16860084   | -     | 0.528 | Product: DressBerry Women Black Solid Stretchable Jeans Brand: DressBerry Color: Black Category: Dress Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 4 Wash care: ... |
| 13   | no  | 14080898   | -     | 0.520 | Product: DressBerry Women Black Print Detail Sweatshirt Brand: DressBerry Color: Black Category: Pullover Pattern: Typography solid Neck: Round neck Sleeves: Long sleeves Length... |
| 14   | no  | 18328804   | -     | 0.470 | Product: URBANIC Women Black Jeans Brand: URBANIC Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Wash care: Machine wash                                           |
| 15   | no  | 16379928   | -     | 0.428 | Product: Safaa Women Black & Beige Woven Design Acrylic Blend Shawl Brand: Safaa Color: Black Pattern: Other woven design Top fabric: Acrylic Occasion: Daily                        |
| 16   | no  | 14225458   | -     | 0.418 | Product: The Dry State Women Black Solid Regular Shorts Brand: The Dry State Color: Black Category: Regular shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion:... |
| 17   | no  | 18875978   | -     | 0.413 | Product: URBANIC Women Black Denim Shorts Brand: URBANIC Color: Black Category: Denim shorts Pattern: Solid Length: Above knee Top fabric: Cotton Occasion: Casual Wash care: Mac... |
| 18   | no  | 18128680   | -     | 0.380 | Product: People Women Black Solid Denim Jacket Brand: People Color: Black Category: Denim jacket Pattern: Solid printed Sleeves: Long sleeves Length: Regular Hemline: Straight T... |
| 19   | no  | 19269372   | -     | 0.369 | Product: BoStreet Women Black Colourblocked Long Sleeves Sweatshirts Brand: BoStreet Color: Black Category: Pullover Pattern: Solid colourblocked Neck: Hood Sleeves: Long sleeve... |
| 20   | no  | 15341678   | -     | 0.369 | Product: Go Colors Women Black Cotton Tapered Fit Trousers Brand: Go Colors Color: Black Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: C... |
| 21   | no  | 13642436   | -     | 0.360 | Product: Alsace Lorraine Paris Women Black Solid Cotton Regular Fit Shorts With Belt Brand: Alsace Lorraine Paris Color: Black Category: Regular shorts Pattern: Solid Length: Ab... |
| 22   | no  | 14547528   | -     | 0.358 | Product: ZOLA Women Black Skinny Fit Light Fade Jeans Brand: ZOLA Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash                |
| 23   | no  | 16827106   | -     | 0.355 | Product: Ginger by Lifestyle Women Black High-Rise Denim Shorts Brand: Ginger by Lifestyle Color: Black Category: Denim shorts Pattern: Solid Length: Above knee Top fabric: Cott... |
| 24   | no  | 14080668   | -     | 0.346 | Product: DressBerry Women Black Solid Sweatshirt Brand: DressBerry Color: Black Category: Pullover Pattern: Solid Neck: Mock collar Sleeves: Long sleeves Length: Regular Hemline... |
| 25   | no  | 18542924   | -     | 0.340 | Product: URBANIC Women Black Solid Mid-Rise Wide Leg Jeans Brand: URBANIC Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash        |
| 26   | no  | 16736530   | -     | 0.333 | Product: SHINGORA Women Black & Brown Woven-Design Shawl Brand: SHINGORA Color: Black Pattern: Ethnic motifs woven design Top fabric: Wool Occasion: Daily                           |
| 27   | no  | 2082103    | -     | 0.312 | Product: Saree mall Black Unstitched Dress Material Brand: Saree mall Color: Black Category: Dress Pattern: Ethnic motifs Bottom fabric: Cotton blend Dupatta fabric: Poly chiffo... |
| 28   | no  | 19214734   | -     | 0.292 | Product: BoStreet Black Roll-Up Sleeves Shirt Style Top Brand: BoStreet Color: Black Category: Shirt style Pattern: Solid Neck: Shirt collar Sleeves: Long roll-up sleeves Length... |
| 29   | no  | 16583226   | -     | 0.291 | Product: 20Dresses Women Black Plus Size Cotton Sweatshirt Brand: 20Dresses Color: Black Category: Pullover Pattern: Solid Neck: High neck Sleeves: Long sleeves Length: Regular ... |
| 30   | no  | 18967478   | -     | 0.287 | Product: BoStreet Women Black Wide Leg Slits Jeans Brand: BoStreet Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash               |

### Question 30/50

**Query:** I'm looking for something Blue from Swasti for everyday wear.

**Relevant docs:** `['18819296']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 18819296   | -     | 1.000 | Product: Swasti Women Blue Ethnic Motifs Printed Mirror Work Floral Kurta Brand: Swasti Color: Blue Pattern: Ethnic motifs printed Shape: Straight Neck: Round neck Sleeves: Long... |
| 2    | no  | 19260152   | -     | 0.431 | Product: SALWAR STUDIO Blue & Purple Printed Unstitched Dress Material Brand: SALWAR STUDIO Color: Blue Category: Dress Pattern: Floral Bottom fabric: Poly crepe Dupatta fabric:... |
| 3    | no  | 19260114   | -     | 0.431 | Product: SALWAR STUDIO Blue & Grey Printed Unstitched Dress Material Brand: SALWAR STUDIO Color: Blue Category: Dress Pattern: Floral Bottom fabric: Poly crepe Dupatta fabric: P... |
| 4    | no  | 15228886   | -     | 0.415 | Product: Blissta Blue Unstitched Dress Material Brand: Blissta Color: Blue Category: Dress Pattern: Solid Bottom fabric: Shantoon Dupatta fabric: Silk blend Occasion: Festive Wa... |
| 5    | no  | 15635874   | -     | 0.409 | Product: SWAGG INDIA Blue Ethnic Motifs Embroidered Chikankari Kurti Brand: SWAGG INDIA Color: Blue Pattern: Ethnic motifs embroidered Shape: Straight Neck: Round neck Sleeves: ... |
| 6    | no  | 11536158   | -     | 0.392 | Product: INDYA Blue Solid Dupatta Brand: INDYA Color: Blue Pattern: Solid Top fabric: Net Occasion: Daily Wash care: Hand wash                                                       |
| 7    | no  | 18651648   | -     | 0.382 | Product: Swtantra Blue & Gold-Toned Satin Saree Brand: Swtantra Color: Blue Category: Saree Pattern: Solid Occasion: Party Wash care: Dry clean                                      |
| 8    | no  | 13869240   | -     | 0.370 | Product: Stylee LIFESTYLE Blue Cotton Blend Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Blue Category: Dress Pattern: Ethnic motifs Bottom fabric: Cotton blend Dupa... |
| 9    | no  | 18211888   | -     | 0.356 | Product: Iris Women Sky Blue & Light Blue Printed Unstitched Dress Material Brand: Iris Color: Blue Category: Dress Pattern: Floral Bottom fabric: Poly crepe Dupatta fabric: Pol... |
| 10   | no  | 16821580   | -     | 0.356 | Product: BharatSthali Blue & Silver Woven Design Unstitched Banarasi Dress Material Brand: BharatSthali Color: Blue Category: Dress Pattern: Ethnic motifs Bottom fabric: Cotton ... |
| 11   | no  | 18323552   | -     | 0.297 | Product: Swtantra Sea Green & Blue Ombre Pure Chiffon Saree Brand: Swtantra Color: Sea Green Category: Saree Pattern: Ombre solid Occasion: Festive Wash care: Dry clean             |
| 12   | no  | 18859092   | -     | 0.263 | Product: Unnati Silks Blue & Orange Dyed Pure Cotton Unstitched Dress Material Brand: Unnati Silks Color: Blue Category: Dress Pattern: Bandhani Bottom fabric: Pure cotton Dupat... |
| 13   | no  | 18887908   | -     | 0.257 | Product: swatika Green Woven Design Bhagalpuri Dupatta Brand: swatika Color: Green Pattern: Ethnic motifs woven design Top fabric: Art silk Occasion: Daily Wash care: Hand wash     |
| 14   | no  | 15071832   | -     | 0.243 | Product: all about you Blue & Violet Floral Organza Saree Brand: all about you Color: Blue Category: Saree Pattern: Floral printed Occasion: Daily Wash care: Dry clean              |
| 15   | no  | 15243952   | -     | 0.227 | Product: Suta Blue Green Colourblocked Cotton Blend Saree Brand: Suta Color: Blue Category: Saree Pattern: Colourblocked Occasion: Daily Wash care: Dry clean                        |
| 16   | no  | 18283286   | -     | 0.222 | Product: Swtantra Mustard & Blue Ombre Satin Saree Brand: Swtantra Color: Mustard Category: Saree Pattern: Ombre colourblocked Occasion: Festive Wash care: Dry clean                |
| 17   | no  | 13956726   | -     | 0.219 | Product: Anubhutee Blue & White Geometric Printed Kurti Brand: Anubhutee Color: Blue Pattern: Geometric printed Shape: Straight Neck: Mandarin collar Sleeves: Short regular slee... |
| 18   | no  | 17445574   | -     | 0.216 | Product: Vishudh Women Blue Floral Embroidered Thread Work Cotton Kurta Brand: Vishudh Color: Blue Pattern: Floral embroidered Shape: Straight Neck: V-neck Sleeves: Three-quarte... |
| 19   | no  | 17514330   | -     | 0.212 | Product: Vishudh Women Blue Printed Anarkali Kurta Brand: Vishudh Color: Turquoise Blue Pattern: Abstract printed Shape: Anarkali Neck: Mandarin collar Sleeves: Short roll-up sl... |
| 20   | no  | 15326556   | -     | 0.206 | Product: swatika White Striped Organza Bhagalpuri Handloom Dupatta Brand: swatika Color: White Pattern: Striped Top fabric: Organza Occasion: Daily Wash care: Hand wash             |
| 21   | no  | 16198966   | -     | 0.203 | Product: Arhi Blue Raga Saree Brand: Arhi Color: Blue Category: Saree Pattern: Solid Occasion: Daily Wash care: Dry clean                                                            |
| 22   | no  | 16336066   | -     | 0.199 | Product: all about you Blue Woven Design Silk Blend Saree Brand: all about you Color: Blue Category: Saree Pattern: Woven design Occasion: Festive Wash care: Dry clean              |
| 23   | no  | 15437594   | -     | 0.196 | Product: Stylum Women Turquoise Blue Geometric Printed Thread Work Kurta Brand: Stylum Color: Turquoise Blue Pattern: Geometric printed Shape: A-line Neck: Mandarin collar Sleev... |
| 24   | no  | 17215592   | -     | 0.184 | Product: Safaa Blue & White Unstitched Dress Material Brand: Safaa Color: Blue Category: Dress Pattern: Floral Bottom fabric: Cotton blend Dupatta fabric: Cotton blend Occasion:... |
| 25   | no  | 17751840   | -     | 0.174 | Product: SALWAR STUDIO Navy Blue Printed Unstitched Dress Material Brand: SALWAR STUDIO Color: Navy Blue Category: Dress Pattern: Ethnic motifs Bottom fabric: Poly crepe Dupatta... |
| 26   | no  | 7241429    | -     | 0.171 | Product: Dupatta Bazaar Blue Embroidered Dupatta Brand: Dupatta Bazaar Color: Blue Pattern: Floral embroidered Top fabric: Poly chiffon Occasion: Daily Wash care: Hand wash         |
| 27   | no  | 17788054   | -     | 0.166 | Product: Stylee LIFESTYLE Turquoise Blue & Pink Printed Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Turquoise Blue Category: Dress Pattern: Floral Bottom fabric: Co... |
| 28   | no  | 18753060   | -     | 0.165 | Product: Globus Women Blue & aquifer Thread Work Kurta Brand: Globus Color: Blue Pattern: Solid Shape: Straight Neck: Round neck Sleeves: Three-quarter regular sleeves Length: C... |
| 29   | no  | 19100460   | -     | 0.159 | Product: La Vastraa Blue & Yellow Paisley Dyed Art Silk Dupatta Brand: La Vastraa Color: Blue Pattern: Paisley dyed Top fabric: Art silk Occasion: Daily Wash care: Dry clean        |
| 30   | no  | 10328759   | -     | 0.154 | Product: Ishin Women Blue & White Printed Unstitched Dress Material Brand: Ishin Color: Blue Category: Dress Pattern: Geometric Bottom fabric: Polyester Dupatta fabric: Poly geo... |

### Question 31/50

**Query:** I need Shirt style with a Abstract printed pattern in Pink.

**Relevant docs:** `['13244594']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 13244594   | -     | 1.000 | Product: Mayra Women Pink Printed Shirt Style Top Brand: Mayra Color: Pink Category: Shirt style Pattern: Abstract printed Neck: Mandarin collar Sleeves: Three-quarter roll-up s... |
| 2    | no  | 19201936   | -     | 0.857 | Product: H&M Women Pink Pure Cotton Frill-Collared Blouse Brand: H&M Color: Pink Category: Shirt style Pattern: Solid Neck: Mandarin collar Sleeves: Short regular sleeves Length... |
| 3    | no  | 15841446   | -     | 0.787 | Product: URBANIC Pink & Beige Floral Print Shirt Style Top Brand: URBANIC Color: Pink Category: Shirt style Pattern: Floral printed Neck: V-neck Sleeves: Long regular sleeves Le... |
| 4    | no  | 19195222   | -     | 0.780 | Product: PRASTHAN Women Pink Floral Print Crepe Shirt Style Top Brand: PRASTHAN Color: Pink Category: Shirt style Pattern: Floral printed Neck: Shirt collar Sleeves: Long bishop... |
| 5    | no  | 18605378   | -     | 0.684 | Product: Vishal Prints Pink & Grey Abstract Print Saree Brand: Vishal Prints Color: Pink Category: Saree Pattern: Abstract printed Occasion: Daily Wash care: Machine wash           |
| 6    | no  | 19325284   | -     | 0.559 | Product: POONAM DESIGNER Women Pink Ethnic Motifs Printed Kurta Brand: POONAM DESIGNER Color: Pink Pattern: Ethnic motifs printed Shape: A-line Neck: Shirt collar Sleeves: Short... |
| 7    | no  | 19032532   | -     | 0.511 | Product: BUY NEW TREND Women Pink & Yellow Printed Tie-Up Shrug Brand: BUY NEW TREND Color: Pink Pattern: Printed Sleeves: Long sleeves Length: Regular Hemline: Straight Top fab... |
| 8    | no  | 9301311    | -     | 0.483 | Product: Tissu Women Pink & Off-White Floral Print Anarkali Kurta Brand: Tissu Color: Pink Pattern: Floral printed Shape: Anarkali Neck: Round neck Sleeves: Three-quarter regula... |
| 9    | no  | 11762378   | -     | 0.475 | Product: AKKRITI BY PANTALOONS Women Pink Printed Top Brand: AKKRITI BY PANTALOONS Color: Pink Category: Regular Pattern: Abstract printed Neck: Mandarin collar Sleeves: Three-q... |
| 10   | no  | 19280832   | -     | 0.473 | Product: VividArtsy Women Pink Tie & Dye Printed Co-Ords Brand: VividArtsy Color: Pink Category: Sweatshirt Top type: Sweatshirt Bottom type: Trousers Pattern: Dyed Neck: Hood S... |
| 11   | no  | 15632410   | -     | 0.454 | Product: URBANIC Women Pink Solid T-shirt with Shorts Brand: URBANIC Color: Pink Category: T-shirt Top type: T-shirt Bottom type: Shorts Pattern: Solid Neck: Round neck Sleeves:... |
| 12   | no  | 19188354   | -     | 0.431 | Product: Colour Me by Melange Women Pink Mandarin Collar Pleated Top Brand: Colour Me by Melange Color: Pink Category: Shirt style Pattern: Embellished Neck: Mandarin collar Sle... |
| 13   | no  | 16887876   | -     | 0.421 | Product: TANKHI Women Pink Floral Printed Tunic Brand: TANKHI Color: Pink Pattern: Printed Neck: Round neck Sleeves: Three-quarter sleeves Top fabric: Silk Occasion: Ethnic Wash... |
| 14   | no  | 15737958   | -     | 0.416 | Product: Fabindia Woman Pink & Beige Silk Organza Tunic Brand: Fabindia Color: Pink Pattern: Striped Neck: V-neck Sleeves: Three-quarter sleeves Top fabric: Silk Occasion: Ethni... |
| 15   | no  | 16071640   | -     | 0.376 | Product: Fabindia Women Pink Printed Front Open Shrug Brand: Fabindia Color: Pink Pattern: Printed Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Linen Occa... |
| 16   | no  | 18839688   | -     | 0.374 | Product: Styli Pink Print Top Brand: Styli Color: Pink Category: Regular Pattern: Solid printed Neck: Round neck Sleeves: Long regular sleeves Length: Regular Top fabric: Polyes... |
| 17   | no  | 16012516   | -     | 0.372 | Product: Fabindia Women Pink Striped Straight Silk Tunic Brand: Fabindia Color: Pink Pattern: Striped Neck: Mandarin collar Sleeves: Three-quarter sleeves Top fabric: Silk Occas... |
| 18   | no  | 10720170   | -     | 0.368 | Product: Style Quotient Women Pink Self Design Crop Shrug Brand: Style Quotient Color: Pink Pattern: Self design Sleeves: Three-quarter sleeves Length: Crop Hemline: Straight To... |
| 19   | no  | 15720246   | -     | 0.360 | Product: HIGHLIGHT FASHION EXPORT Pink Embroidered Regular Top Brand: HIGHLIGHT FASHION EXPORT Color: Pink Category: Regular Pattern: Abstract embroidered Neck: Round neck Sleev... |
| 20   | no  | 6582659    | -     | 0.343 | Product: W Women Pink Printed A-Line Layered Crop Top Brand: W Color: Pink Category: A-line Pattern: Tribal printed Neck: Round neck Sleeves: Sleeveless no Length: Crop Top fabr... |
| 21   | no  | 17777226   | -     | 0.325 | Product: Prakrti Pink & White Ethnic Motifs Printed Pure Cotton Pleated Kurti Brand: Prakrti Color: Pink Pattern: Ethnic motifs printed Shape: Straight Neck: Mandarin collar Sle... |
| 22   | no  | 17820020   | -     | 0.322 | Product: Mast & Harbour Pink Floral Print Mandarin Collar Shirt Style Top Brand: Mast & Harbour Color: Pink Category: Shirt style Pattern: Floral printed Neck: Mandarin collar S... |
| 23   | no  | 18076132   | -     | 0.317 | Product: Saree mall Pink & Black Printed Saree Brand: Saree mall Color: Pink Category: Saree Pattern: Abstract printed Occasion: Daily Wash care: Dry clean                          |
| 24   | no  | 12151836   | -     | 0.307 | Product: Bhama Couture Women Pink & Golden Printed Asymmetric Tunic Brand: Bhama Couture Color: Pink Pattern: Printed Neck: V-neck Sleeves: Three-quarter sleeves Top fabric: Sil... |
| 25   | no  | 15816496   | -     | 0.299 | Product: Fabindia Pink Yoke Design V-Neck Kurti Brand: Fabindia Color: Pink Pattern: Striped yoke design Shape: Straight Neck: V-neck Sleeves: Three-quarter regular sleeves Heml... |
| 26   | no  | 16071622   | -     | 0.298 | Product: Fabindia Women Pink & Cream-Coloured Printed Cotton Linen Shrug Brand: Fabindia Color: Pink Pattern: Printed Sleeves: Long sleeves Length: Regular Hemline: Straight Top... |
| 27   | no  | 19134302   | -     | 0.298 | Product: INDYA Women Pink Geometric Print Georgette Strappy Crop Top Brand: INDYA Color: Pink Category: Fitted Pattern: Geometric printed Neck: Shoulder straps Sleeves: Sleevele... |
| 28   | no  | 18244498   | -     | 0.296 | Product: W Women Pink Geometric Striped Keyhole Neck Flared Sleeves Thread Work Kurta Brand: W Color: Pink Pattern: Geometric striped Shape: Straight Neck: Keyhole neck Sleeves:... |
| 29   | no  | 14138684   | -     | 0.293 | Product: One of a Kind Women Pink Solid Kurtas Brand: One of a Kind Color: Pink Pattern: Solid printed Shape: Anarkali Neck: V-neck Sleeves: Three-quarter regular sleeves Hemlin... |
| 30   | no  | 15980892   | -     | 0.277 | Product: Shae by SASSAFRAS Pink Printed Regular Crop Top Brand: Shae by SASSAFRAS Color: Pink Category: Regular Pattern: Ethnic motifs printed Neck: V-neck Sleeves: Three-quarte... |

### Question 32/50

**Query:** I'm looking for products by Atsevam.

**Relevant docs:** `['17754230', '17754250', '17754248', '19217168', '19217170', '17584576', '19217176']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.233     | 1.000  | 1.000 | 0.982 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 17754230   | -     | 1.000 | Product: Atsevam Cream-Coloured & Red Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Cream Dupatta: With dupatta Pattern: Woven design Neck: V-neck... |
| 2    | yes | 19217170   | -     | 0.956 | Product: Atsevam Red & Gold-Toned Embroidered Thread Work Tie and Dye Semi-Stitched Lehenga & Unstitched Blouse With Brand: Atsevam Color: Red Dupatta: With dupatta Pattern: Emb... |
| 3    | yes | 17754248   | -     | 0.920 | Product: Atsevam Red Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Red Dupatta: With dupatta Pattern: Embroidered Neck: Ro... |
| 4    | yes | 17584576   | -     | 0.906 | Product: Atsevam Orange & Red Printed Tie and Dye Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Orange Dupatta: With dupatta Pattern: Printed Neck... |
| 5    | yes | 19217168   | -     | 0.892 | Product: Atsevam Green & Gold-Toned Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Green Dupatta: With dupatta Pattern: Emb... |
| 6    | no  | 19217186   | -     | 0.883 | Product: Atsevam Women Green & Pink Printed Tie and Dye Semi-Stitched Lehenga Choli Brand: Atsevam Color: Green Dupatta: With dupatta Pattern: Printed Neck: Round neck Sleeves: ... |
| 7    | yes | 19217176   | -     | 0.849 | Product: Atsevam White & Pink Tie and Dye Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: White Dupatta: With dupatta Pattern: Woven design Neck: V-... |
| 8    | no  | 17834516   | -     | 0.839 | Product: Atsevam Blue & Pink Ready to Wear Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Blue Dupatta: With dupatta Pattern: Woven design Neck: Round neck Sleev... |
| 9    | no  | 19217196   | -     | 0.825 | Product: Atsevam Pink Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Atsevam Color: Pink Dupatta: With dupatta Pattern: Embroidered Neck: ... |
| 10   | yes | 17754250   | -     | 0.791 | Product: Atsevam Women Pink Embroidered Semi-Stitched Lehenga Unstitched Choli & Dupatta Brand: Atsevam Color: Pink Dupatta: With dupatta Pattern: Embroidered Neck: Round neck S... |
| 11   | no  | 19162224   | -     | 0.350 | Product: aturabi Peach-Coloured & White Halter Neck Top Brand: aturabi Color: Peach Category: A-line Pattern: Self design Neck: Halter neck Sleeves: Sleeveless no Length: Regula... |
| 12   | no  | 15107864   | -     | 0.260 | Product: Ives Sea Green Foil Printed A-Line Top Brand: Ives Color: Sea Green Category: A-line Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Short regular sleeves Leng... |
| 13   | no  | 16504020   | -     | 0.230 | Product: ANVI Be Yourself Women Attractive Peach Floral Fantasy Skirt Brand: ANVI Be Yourself Color: Peach Category: A-line Pattern: Floral printed Length: Midi Hemline: Straigh... |
| 14   | no  | 14440146   | -     | 0.218 | Product: AASI - HOUSE OF NAYO Navy Blue Striped Bell Sleeve Crepe Regular Top Brand: AASI - HOUSE OF NAYO Color: Navy Blue Category: Regular Pattern: Vertical stripes striped Ne... |
| 15   | no  | 19232812   | -     | 0.197 | Product: aturabi Green Georgette Top Brand: aturabi Color: Green Category: Regular Pattern: Solid Neck: Round neck Sleeves: Sleeveless no Length: Regular Top fabric: Polyester O... |
| 16   | no  | 19160198   | -     | 0.186 | Product: aturabi Women Grey Solid Knee Length A-Line Pleated Skirts Brand: aturabi Color: Grey Category: A-line Pattern: Solid Length: Knee length Hemline: Straight Top fabric: ... |
| 17   | no  | 14440118   | -     | 0.181 | Product: AASI - HOUSE OF NAYO Navy Blue Crepe Bardot Top Brand: AASI - HOUSE OF NAYO Color: Navy Blue Category: Bardot Pattern: Conversational printed Neck: Shoulder straps Slee... |
| 18   | no  | 17757300   | -     | 0.165 | Product: itse Maroon & Golden Printed A-Line Top Brand: itse Color: Maroon Category: A-line Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Three-quarter cuffed sleeves... |
| 19   | no  | 14440122   | -     | 0.160 | Product: AASI - HOUSE OF NAYO Pink Floral Bell Sleeve Peplum Top Brand: AASI - HOUSE OF NAYO Color: Pink Category: Peplum Pattern: Floral printed Neck: Round neck Sleeves: Three... |
| 20   | no  | 18512872   | -     | 0.147 | Product: Amrutam Fab Cream-Coloured & Navy Blue Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Brand: Amrutam Fab Color: Cream Dupatta: With dupatta Patter... |
| 21   | no  | 19160174   | -     | 0.147 | Product: aturabi Women Black Checked Asymmetric Skirts Brand: aturabi Color: Black Category: A-line Pattern: Checked Length: Above knee Hemline: Asymmetric Top fabric: Polyester... |
| 22   | no  | 17394300   | -     | 0.147 | Product: ANVI Be Yourself Women Beige & Brown Leopard Printed Straight Mini Skirt Brand: ANVI Be Yourself Color: Beige Category: Straight Pattern: Animal printed Length: Mini He... |
| 23   | no  | 17359094   | -     | 0.146 | Product: Amrutam Fab Peach-Coloured & Purple Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Brand: Amrutam Fab Color: Peach Dupatta: With dupatta Pattern... |
| 24   | no  | 12135374   | -     | 0.126 | Product: Anouk Beige & Red Antiviral Finish Ethnic Motifs Anti-Viral Pure Cotton Top Brand: Anouk Color: Beige Category: Regular Pattern: Ethnic motifs printed Neck: Round neck ... |
| 25   | no  | 15509516   | -     | 0.124 | Product: VASTRANAND Peach-Coloured Floral Mirror Work Organza Saree Brand: VASTRANAND Color: Peach Category: Saree Pattern: Floral embellished Occasion: Party Wash care: Dry clean  |
| 26   | no  | 17150536   | -     | 0.123 | Product: VASTRANAND Peach-Coloured & Multicoloured Kalamkari Sequinned Linen Blend Block Print Saree Brand: VASTRANAND Color: Peach Category: Block print Pattern: Kalamkari prin... |
| 27   | no  | 19184810   | -     | 0.119 | Product: VASTRAMAY Girls Cream-Coloured Embroidered Sequinned Ready to Wear Lehenga & Brand: VASTRAMAY Color: Cream Pattern: Embroidered Neck: Square neck Sleeves: Sleeveless sh... |
| 28   | no  | 15107870   | -     | 0.117 | Product: Ives Blue Printed Crepe A-Line Top Brand: Ives Color: Blue Category: A-line Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Short regular sleeves Length: Regul... |
| 29   | no  | 10414130   | -     | 0.115 | Product: AASI - HOUSE OF NAYO Women Off-White & Pink Printed Pure Cotton Top Brand: AASI - HOUSE OF NAYO Color: Off White Category: Regular Pattern: Floral printed Neck: Round n... |
| 30   | no  | 19160178   | -     | 0.109 | Product: aturabi Women's Green Solid Knee Length A-Line Skirts Brand: aturabi Color: Green Category: A-line Pattern: Solid Length: Knee length Hemline: Straight Top fabric: Poly... |

### Question 33/50

**Query:** What do you have from panchhi in products and color Pink?

**Relevant docs:** `['19046346', '12003682']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.067     | 1.000  | 0.500 | 0.693 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 18070000   | -     | 1.000 | Product: panchhi Pink Embroidered Sequinned Unstitched Lehenga & Blouse With Dupatta Brand: panchhi Color: Pink Dupatta: With dupatta Pattern: Embroidered Neck: V-neck Sleeves: ... |
| 2    | yes | 12003682   | -     | 0.931 | Product: panchhi Pink & Beige Embellished Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Pink Dupatta: With dupatta Pattern: Embellished Neck: V-ne... |
| 3    | yes | 19046346   | -     | 0.920 | Product: panchhi Pink & Sea Green Embellished Sequinned Semi-Stitched Lehenga & Ready to Wear Blouse With Dupatta Brand: panchhi Color: Pink Dupatta: With dupatta Pattern: Embel... |
| 4    | no  | 18175384   | -     | 0.915 | Product: panchhi Pink Net Embroidered Sequinned Semi-Stitched Lehenga & Blouse With Dupatta Brand: panchhi Color: Pink Dupatta: With dupatta Pattern: Embroidered Neck: Round nec... |
| 5    | no  | 13872486   | -     | 0.795 | Product: panchhi Mustard & Pink Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Mustard Dupatta: With dupatta Pattern: Embroidered Neck:... |
| 6    | no  | 18175352   | -     | 0.784 | Product: panchhi Lavender & Red Embroidered Sequinned Unstitched Lehenga & Blouse With Dupatta Brand: panchhi Color: Lavender Dupatta: With dupatta Pattern: Embroidered Neck: Ro... |
| 7    | no  | 13421470   | -     | 0.783 | Product: panchhi Mustard & Pink Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Mustard Dupatta: With dupatta Pattern: Embroidered Neck:... |
| 8    | no  | 19046338   | -     | 0.751 | Product: panchhi Blue & Pink Embellished Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Blue Dupatta: With dupatta Pattern: Embellished Neck: Round... |
| 9    | no  | 13421500   | -     | 0.750 | Product: panchhi Lime Green & Lime Green Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Lime Green Dupatta: With dupatta Pattern: Embro... |
| 10   | no  | 19046370   | -     | 0.745 | Product: panchhi Lime Green & Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Lime Green Dupatta: With dupatta Pattern: Embroi... |
| 11   | no  | 18730470   | -     | 0.740 | Product: panchhi Peach-Coloured & Blue Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Peach Dupatta: With dupatta Pattern: ... |
| 12   | no  | 13872488   | -     | 0.736 | Product: panchhi Cream-Coloured & Yellow Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Cream Dupatta: With dupatta Pattern: Embroidere... |
| 13   | no  | 17848104   | -     | 0.730 | Product: panchhi Nude-Coloured Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Nude Dupatta: With dupatta Pattern: Embellished... |
| 14   | no  | 15393564   | -     | 0.726 | Product: panchhi Beige & Peach-Coloured Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Beige Dupatta: With dupatta Pattern: E... |
| 15   | no  | 12668254   | -     | 0.712 | Product: panchhi Red Codding Embroidered Semi-Stitched Lehenga & Unstitched Choli With Dupatta Brand: panchhi Color: Red Dupatta: With dupatta Pattern: Embellished Neck: Round n... |
| 16   | no  | 12003688   | -     | 0.707 | Product: panchhi Green & Yellow Embellished Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Green Dupatta: With dupatta Pattern: Embellished Neck: S... |
| 17   | no  | 12668248   | -     | 0.697 | Product: panchhi Peach-Coloured & Green Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Peach Dupatta: With dupatta Pattern: Embroidered Neck: Round... |
| 18   | no  | 18624652   | -     | 0.693 | Product: panchhi Green & Gold Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Green Dupatta: With dupatta Pattern: Embroidered Neck: Round... |
| 19   | no  | 16676710   | -     | 0.689 | Product: panchhi Maroon & Silver-Toned Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Maroon Dupatta: With dupatta Pattern: E... |
| 20   | no  | 16676694   | -     | 0.682 | Product: panchhi Sea Green & Gold-Toned Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Sea Green Dupatta: With dupatta Patter... |
| 21   | no  | 12003618   | -     | 0.675 | Product: panchhi Green & Green Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Green Dupatta: With dupatta Pattern: Solid Neck: Round ne... |
| 22   | no  | 19046354   | -     | 0.664 | Product: panchhi Maroon Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Maroon Dupatta: With dupatta Pattern: Embellished Neck... |
| 23   | no  | 18069992   | -     | 0.657 | Product: panchhi Maroon Embroidered Sequinned Unstitched Lehenga & Blouse With Dupatta Brand: panchhi Color: Maroon Dupatta: With dupatta Pattern: Embroidered Neck: Round neck S... |
| 24   | no  | 19046358   | -     | 0.651 | Product: panchhi Sea Green & Red Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Sea Green Dupatta: With dupatta Pattern: Embr... |
| 25   | no  | 19046340   | -     | 0.649 | Product: panchhi Yellow & Teal Embellished Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Yellow Dupatta: With dupatta Pattern: Embellished Neck: R... |
| 26   | no  | 18624644   | -     | 0.642 | Product: panchhi Olive Green Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Olive Dupatta: With dupatta Pattern: Embroidered ... |
| 27   | no  | 18069988   | -     | 0.636 | Product: panchhi Coral & Embroidered Sequinned Unstitched Lehenga & Blouse With Dupatta Brand: panchhi Color: Coral Dupatta: With dupatta Pattern: Embroidered Neck: Round neck S... |
| 28   | no  | 14764064   | -     | 0.623 | Product: panchhi Mustard & Orange Embroidered Mirror Work Ready to Wear Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Mustard Dupatta: With dupatta Pattern: Emb... |
| 29   | no  | 13515246   | -     | 0.623 | Product: panchhi Blue Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: panchhi Color: Blue Dupatta: With dupatta Pattern: Embroidered Neck: Mandarin col... |
| 30   | no  | 19046324   | -     | 0.621 | Product: panchhi Navy Blue & Mustard Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: panchhi Color: Navy Blue Dupatta: With dupatta Pattern: ... |

### Question 34/50

**Query:** What do you have in products under 2500?

**Relevant docs:** `['11765970', '17662818', '15514544', '18068482', '16989998', '16563320', '15011850', '15266776']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.000     | 0.000  | 0.000 | 0.000 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 17612960   | -     | 1.000 | Product: 250 DESIGNS Women Navy Blue Floral Co-Ord Set Brand: 250 DESIGNS Color: Navy Blue Category: Top Top type: Top Bottom type: Palazzos Pattern: Printed Neck: V-neck Sleeve... |
| 2    | no  | 2507000    | -     | 0.567 | Product: Roadster Pink Knitted Lace Top Brand: Roadster Color: Pink Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short regular sleeves Length: Regular Occasion: Ca... |
| 3    | no  | 18290992   | -     | 0.501 | Product: Superminis Girls Brown & Embroidered Ready to Wear Lehenga & Blouse With Dupatta Brand: Superminis Color: Brown Dupatta: With dupatta Pattern: Embroidered Neck: Round n... |
| 4    | no  | 17209256   | -     | 0.451 | Product: Unnati Silks Cream-Coloured & Black Ethnic Motifs Embroidered Tissue Banarasi Saree Brand: Unnati Silks Color: Cream Category: Banarasi Pattern: Ethnic motifs embroider... |
| 5    | no  | 16372904   | -     | 0.447 | Product: Netram Beige Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Net Dupatta Brand: Netram Color: Beige Dupatta: With dupatta Pattern: Embroidered Sleeves: Short... |
| 6    | no  | 18512872   | -     | 0.436 | Product: Amrutam Fab Cream-Coloured & Navy Blue Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Brand: Amrutam Fab Color: Cream Dupatta: With dupatta Patter... |
| 7    | no  | 18290988   | -     | 0.418 | Product: Superminis Girls Lime Green & Beige Embroidered Ready to Wear Lehenga & Blouse With Dupatta Brand: Superminis Color: Lime Green Dupatta: With dupatta Pattern: Embroider... |
| 8    | no  | 15589086   | -     | 0.396 | Product: Netram Lavender & Silver-Toned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Netram Color: Lavender Dupatta: With dupatta Pattern: Embroidered Sleeves: ... |
| 9    | no  | 17725246   | -     | 0.393 | Product: DIVASTRI Red & Mustard Banarasi Silk Semi-Stitched Lehenga & Unstitched Blouse & Dupatta Brand: DIVASTRI Color: Red Dupatta: With dupatta Pattern: Woven design Neck: Bo... |
| 10   | no  | 18258322   | -     | 0.382 | Product: Netram Red & Gold-Toned Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Netram Color: Red Dupatta: With dupatta Pattern: Embroidered Neck: Rou... |
| 11   | no  | 18309022   | -     | 0.372 | Product: PURVAJA Olive Green & Red Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: PURVAJA Color: Olive Dupatta: With dupatta Pattern: Woven design Neck: Round nec... |
| 12   | no  | 19104000   | -     | 0.354 | Product: Granthva Fab Blue & White Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Granthva Fab Color: Blue Dupatta: With dupatta Pattern: Em... |
| 13   | no  | 17638538   | -     | 0.353 | Product: V SALES Grey & Orange Embellished Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: V SALES Color: Grey Dupatta: With dupatta Pattern: Embellished Neck: Rou... |
| 14   | no  | 18549594   | -     | 0.322 | Product: Amrutam Fab Mustard & Green Printed Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Amrutam Fab Color: Mustard Dupatta: With dupatta Pattern: Printed Neck... |
| 15   | no  | 18309012   | -     | 0.310 | Product: PURVAJA Navy Blue & Red Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: PURVAJA Color: Navy Blue Dupatta: With dupatta Pattern: Woven design Neck: Round n... |
| 16   | no  | 19104050   | -     | 0.301 | Product: Granthva Fab Green & Black Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Granthva Fab Color: Green Dupatta: With dupatta Pattern: ... |
| 17   | no  | 18258324   | -     | 0.292 | Product: Netram Peach-Coloured & Copper-Toned Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Netram Color: Peach Dupatta: With dupatta Pattern: Embroi... |
| 18   | no  | 18258316   | -     | 0.290 | Product: Netram Red Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Netram Color: Red Dupatta: With dupatta Pattern: Embroidered Neck: Round neck Sleev... |
| 19   | no  | 18008128   | -     | 0.286 | Product: Superminis Girls Maroon & Beige Embroidered Ready to Wear Lehenga & Blouse With Dupatta Brand: Superminis Color: Maroon Dupatta: With dupatta Pattern: Embroidered Neck:... |
| 20   | no  | 14501272   | -     | 0.282 | Product: PURVAJA Navy Blue & Silver-Toned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: PURVAJA Color: Navy Blue Dupatta: With dupatta Pattern: Woven design Slee... |
| 21   | no  | 15543206   | -     | 0.281 | Product: V SALES Turquoise Blue & Grey Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: V SALES Color: Turquoise Blue Dupatta: With dupatta ... |
| 22   | no  | 19103994   | -     | 0.276 | Product: Granthva Fab Peach-Coloured & Gold-Toned Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse Brand: Granthva Fab Color: Peach Dupatta: With dupatta Pattern:... |
| 23   | no  | 19104006   | -     | 0.273 | Product: Granthva Fab Blue & Silver-Toned Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Brand: Granthva Fab Color: Blue Dupatta: With dupatta Pattern: Emb... |
| 24   | no  | 13617704   | -     | 0.271 | Product: Satrani Red & Silver-Toned Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Satrani Color: Red Dupatta: With dupatta Pattern: Embroidered Sleev... |
| 25   | no  | 19104074   | -     | 0.268 | Product: Granthva Fab White & Maroon Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Granthva Fab Color: White Dupatta: With dupatta Pattern:... |
| 26   | no  | 17359094   | -     | 0.265 | Product: Amrutam Fab Peach-Coloured & Purple Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Brand: Amrutam Fab Color: Peach Dupatta: With dupatta Pattern... |
| 27   | no  | 19083864   | -     | 0.236 | Product: Amrutam Fab Blue & White Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Amrutam Fab Color: Blue Dupatta: With dupatta Pattern: Em... |
| 28   | no  | 18095156   | -     | 0.236 | Product: Warthy Ent Cream-Coloured Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Warthy Ent Color: Cream Dupatta: With dupatta Pattern: Embellished Sle... |
| 29   | no  | 15451514   | -     | 0.219 | Product: V SALES Red Embroidered Thread Work Semi-Stitched Lehenga & Unstitched Choli With Dupatta Brand: V SALES Color: Red Dupatta: With dupatta Pattern: Embroidered Neck: U-n... |
| 30   | no  | 18309016   | -     | 0.207 | Product: PURVAJA Teal & Mustard Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: PURVAJA Color: Teal Dupatta: With dupatta Pattern: Woven design Neck: Round neck Sl... |

### Question 35/50

**Query:** Show me products from Indo Era.

**Relevant docs:** `['14239788', '11459668', '12040868', '15520698', '12040878', '12122360', '13250074', '17553564']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.067     | 0.250  | 0.167 | 0.170 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 14869156   | -     | 1.000 | Product: Indo Era Deep Black Solid Lehenga with Embroidered Choli Brand: Indo Era Color: Black Pattern: Embroidered Neck: V-neck Sleeves: Three-quarter regular sleeves Hemline: ... |
| 2    | no  | 17553556   | -     | 0.986 | Product: Indo Era Green & Gold-Toned Woven Design Dupatta Brand: Indo Era Color: Green Pattern: Solid woven design Top fabric: Silk blend Occasion: Daily Wash care: Hand wash       |
| 3    | no  | 17473346   | -     | 0.923 | Product: Indo Era Green & Gold-Toned Ethnic Motifs Printed Dupatta Brand: Indo Era Color: Green Pattern: Ethnic motifs printed Top fabric: Cotton blend Occasion: Party Wash care... |
| 4    | no  | 13810898   | -     | 0.909 | Product: Indo Era Women Blue & Green Printed Kurta with Palazzos & Dupatta Brand: Indo Era Color: Blue Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With du... |
| 5    | no  | 16188740   | -     | 0.898 | Product: Indo Era Women Green Solid Cotton Palazzos Brand: Indo Era Color: Green Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Western Pockets: 2 Wash care: Hand wash |
| 6    | yes | 12122360   | -     | 0.896 | Product: Indo Era Brown & Golden Woven Design Dupatta Brand: Indo Era Color: Brown Pattern: Geometric woven design Top fabric: Art silk Occasion: Daily Wash care: Hand wash         |
| 7    | no  | 16950290   | -     | 0.893 | Product: Indo Era Sea Green Floral Print Tie-Up Neck Top Brand: Indo Era Color: Sea Green Category: Regular Pattern: Floral printed Neck: Tie-up neck Sleeves: Three-quarter regu... |
| 8    | yes | 13250074   | -     | 0.889 | Product: Indo Era Maroon & Beige Woven Design Dupatta Brand: Indo Era Color: Maroon Pattern: Floral woven design Top fabric: Cotton silk Occasion: Daily Wash care: Hand wash        |
| 9    | no  | 16713198   | -     | 0.888 | Product: Indo Era Grey Silk Blend Scalloped Edge Kurta Set Brand: Indo Era Color: Grey Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta Pattern: E... |
| 10   | no  | 14197506   | -     | 0.886 | Product: Indo Era Orange & Turquoise Blue Woven Design Dupatta Brand: Indo Era Color: Orange Pattern: Striped woven design Top fabric: Art silk Occasion: Party Wash care: Dry clean |
| 11   | no  | 16682770   | -     | 0.885 | Product: Indo Era Women Orange & Gold Striped Woven Design Art Silk Dupatta Brand: Indo Era Color: Orange Pattern: Striped woven design Top fabric: Art silk Occasion: Party Wash... |
| 12   | no  | 17069054   | -     | 0.880 | Product: Indo Era Women Black Ethnic Motifs Yoke Design Thread Work Kurta with Trousers & With Dupatta Brand: Indo Era Color: Black Category: Kurta set Top type: Kurta Bottom ty... |
| 13   | no  | 12122358   | -     | 0.874 | Product: Indo Era Women Black & Teal Blue Yoke Design Kurta with Palazzos & Dupatta Brand: Indo Era Color: Black Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatt... |
| 14   | no  | 15258422   | -     | 0.873 | Product: Indo Era Floral Cotton Blend Calf Length Kurta Set Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta Pattern:... |
| 15   | no  | 16310880   | -     | 0.870 | Product: Indo Era Women Black Ethnic Motifs Yoke Design Pure Cotton Kurta with Palazzos & With Dupatta Brand: Indo Era Color: Black Category: Kurta set Top type: Kurta Bottom ty... |
| 16   | no  | 14197518   | -     | 0.869 | Product: Indo Era Red & Golden Woven Design Dupatta Brand: Indo Era Color: Red Pattern: Striped woven design Top fabric: Art silk Occasion: Party Wash care: Dry clean               |
| 17   | no  | 15798284   | -     | 0.854 | Product: Indo Era Women Beige Floral Embroidered Regular Kurta with Trousers & With Dupatta Brand: Indo Era Color: Beige Category: Kurta set Top type: Kurta Bottom type: Trouser... |
| 18   | no  | 15508896   | -     | 0.853 | Product: Indo Era Women Green Ethnic Motifs Yoke Design Kurta with Palazzos & With Dupatta Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: Palazzos... |
| 19   | no  | 16950218   | -     | 0.851 | Product: Indo Era Blue Ethnic Motif Printed Peplum Top Brand: Indo Era Color: Blue Category: Peplum Pattern: Ethnic motifs printed Neck: Round neck Sleeves: Three-quarter regula... |
| 20   | no  | 14235030   | -     | 0.842 | Product: Indo Era Women Black Floral Printed Pure Cotton Kurta with Trousers & With Dupatta Brand: Indo Era Color: Black Category: Kurta set Top type: Kurta Bottom type: Trouser... |
| 21   | no  | 14323728   | -     | 0.840 | Product: Indo Era Women Black & Golden Ethnic Motifs Yoke Design Kurta with Palazzos & With Dupatta Brand: Indo Era Color: Black Category: Kurta set Top type: Kurta Bottom type:... |
| 22   | no  | 11675882   | -     | 0.840 | Product: Indo Era Grey & White Printed Ready to Wear Lehenga with Blouse Brand: Indo Era Color: Grey Pattern: Solid Neck: Mandarin collar Sleeves: Three-quarter sleeves Hemline:... |
| 23   | no  | 15654150   | -     | 0.838 | Product: Indo Era Women Green Ethnic Motifs Yoke Design Regular Kurta with Trousers & With Dupatta Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta Bottom type: ... |
| 24   | no  | 12418804   | -     | 0.836 | Product: Indo Era Women Maroon & Orange Yoke Design Kurta with Palazzos & Dupatta Brand: Indo Era Color: Maroon Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta... |
| 25   | no  | 17911130   | -     | 0.833 | Product: Indo Era Women Burgundy Sequined Kurta with Palazzos & Dupatta Brand: Indo Era Color: Burgundy Category: Kurta set Top type: Kurta Bottom type: Palazzos Dupatta: With d... |
| 26   | no  | 14967448   | -     | 0.830 | Product: Indo Era Women Green Ethnic Motifs Printed Panelled Gotta Patti Pure Cotton Kurta with Trousers & With Brand: Indo Era Color: Green Category: Kurta set Top type: Kurta ... |
| 27   | no  | 14239768   | -     | 0.830 | Product: Indo Era Women Brown Solid Straight Palazzos Brand: Indo Era Color: Brown Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Ethnic Pockets: 1 Wash care: Hand ... |
| 28   | no  | 17577456   | -     | 0.829 | Product: Indo Era Women Classic Off-White Ethnic Motifs Nuovo Sleeves Top Brand: Indo Era Color: Off White Category: A-line Pattern: Ethnic motifs solid Neck: Round neck Sleeves... |
| 29   | no  | 15390174   | -     | 0.828 | Product: Indo Era Women Blue Floral Printed Regular Pure Cotton Kurta with Palazzos & With Dupatta Brand: Indo Era Color: Blue Category: Kurta set Top type: Kurta Bottom type: P... |
| 30   | no  | 11459658   | -     | 0.826 | Product: Indo Era Folksy Floral Screen Print Cotton Kurta Set Brand: Indo Era Color: Burgundy Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta: With dupatta Pat... |

### Question 36/50

**Query:** Show me products like "ONLY Women Blue Straight Fit High-Rise Mildly Distressed Jeans".

**Relevant docs:** `['18626222']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 18626222   | -     | 1.000 | Product: ONLY Women Blue Straight Fit High-Rise Mildly Distressed Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine... |
| 2    | no  | 16372376   | -     | 0.986 | Product: ONLY Women Blue Slim Fit High-Rise Mildly Distressed Heavy Fade Stretchable Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5... |
| 3    | no  | 19089666   | -     | 0.967 | Product: ONLY Women Blue Slim Fit High-Rise Low Distress Heavy Fade Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machi... |
| 4    | no  | 18620390   | -     | 0.957 | Product: ONLY Women Blue Skinny Fit High-Rise Mildly Distressed Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care... |
| 5    | no  | 19089668   | -     | 0.937 | Product: ONLY Women Blue Straight Fit High-Rise Low Distress Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: M... |
| 6    | no  | 18626210   | -     | 0.937 | Product: ONLY Women Blue Skinny Fit High-Rise Mildly Distressed Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 7    | no  | 19089706   | -     | 0.929 | Product: ONLY Women Blue Slim Fit High-Rise Mildly Distressed Heavy Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: ... |
| 8    | no  | 17914728   | -     | 0.922 | Product: ONLY Women Blue Straight Fit High-Rise Low Distress Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: M... |
| 9    | no  | 19089694   | -     | 0.897 | Product: ONLY Women Blue Straight Fit High-Rise Low Distress Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash    |
| 10   | no  | 16699772   | -     | 0.883 | Product: ONLY Women Blue High-Rise Mildly Distressed Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 11   | no  | 19143972   | -     | 0.844 | Product: ONLY Women Blue Straight Fit High-Rise Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash                 |
| 12   | no  | 18620400   | -     | 0.827 | Product: ONLY Women Blue Skinny Fit High-Rise Low Distress Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash      |
| 13   | no  | 18626254   | -     | 0.811 | Product: ONLY Women Blue Bootcut High-Rise Low Distress Light Fade Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machin... |
| 14   | no  | 16916588   | -     | 0.721 | Product: ONLY Women Blue Mom-Fit High-Rise Light Fade Printed Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash   |
| 15   | no  | 18626232   | -     | 0.708 | Product: ONLY Women Blue Skinny Fit High-Rise Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash        |
| 16   | no  | 18620404   | -     | 0.704 | Product: ONLY Women Blue Skinny Fit High-Rise Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash        |
| 17   | no  | 19089710   | -     | 0.695 | Product: ONLY Women Blue Flared Mildly Distressed Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash    |
| 18   | no  | 18626248   | -     | 0.682 | Product: ONLY Women Blue Skinny Fit High-Rise Slash Knee Jeans Brand: ONLY Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash        |
| 19   | no  | 17914732   | -     | 0.682 | Product: ONLY Women Blue Skinny Fit High-Rise Slash Knee Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machi... |
| 20   | no  | 18626226   | -     | 0.677 | Product: ONLY Women Blue Straight Fit High-Rise Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash                 |
| 21   | no  | 19089662   | -     | 0.543 | Product: ONLY Women Blue Skinny Fit High-Rise Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash                   |
| 22   | no  | 18809310   | -     | 0.501 | Product: ONLY Women Blue Skinny Fit Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash                  |
| 23   | no  | 18809318   | -     | 0.494 | Product: ONLY Women Blue Skinny Fit Light Fade Jeans Brand: ONLY Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash                  |
| 24   | no  | 17570364   | -     | 0.469 | Product: SHOWOFF Women Blue Straight Fit High-Rise Low Distress Light Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Poc... |
| 25   | no  | 18822974   | -     | 0.429 | Product: RAREISM Women Blue High-Rise Mildly Distressed Light Fade Jeans Brand: RAREISM Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Han... |
| 26   | no  | 18338282   | -     | 0.426 | Product: SHOWOFF Women Blue Slim Fit High-Rise Mildly Distressed Light Fade Stretchable Jeans Brand: SHOWOFF Color: Blue Length: Cropped Top fabric: Elastane Occasion: Casual Po... |
| 27   | no  | 17541860   | -     | 0.422 | Product: RAREISM Women Blue High-Rise Mildly Distress Light Fade Jeans Brand: RAREISM Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Hand ... |
| 28   | no  | 19089682   | -     | 0.375 | Product: ONLY Women Black Straight Fit Low-Rise Highly Distressed Jeans Brand: ONLY Color: Black Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machin... |
| 29   | no  | 16653658   | -     | 0.352 | Product: Levis Women Blue 311 Shaping Skinny Fit Mid Rise Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wa... |
| 30   | no  | 16653786   | -     | 0.333 | Product: Levis Women Blue 714 Straight Fit High-Rise Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash ca... |

### Question 37/50

**Query:** Do you have anything from Uptownie Lite in Flared?

**Relevant docs:** `['17944738', '16608122', '11511460', '11425704', '13467524']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.167     | 1.000  | 1.000 | 0.899 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 11425704   | -     | 1.000 | Product: Uptownie Lite Brown Satin Pleated Flared Midi Skirt Brand: Uptownie Lite Color: Brown Category: Flared Pattern: Solid Length: Midi Hemline: Flared Occasion: Party Wash ... |
| 2    | no  | 11425706   | -     | 0.984 | Product: Uptownie Lite Black Satin Pleated Flared Midi Skirt Brand: Uptownie Lite Color: Black Category: Flared Pattern: Solid Length: Midi Hemline: Flared Occasion: Party Wash ... |
| 3    | yes | 13467524   | -     | 0.936 | Product: Uptownie Lite Women Red Solid Pleated Midi Flare Skirt Brand: Uptownie Lite Color: Red Category: Flared Pattern: Solid Length: Midi Hemline: Flared Top fabric: Polyeste... |
| 4    | yes | 17944738   | -     | 0.916 | Product: Uptownie Lite Grey Solid Pleated Form Skirt Brand: Uptownie Lite Color: Grey Category: Flared Pattern: Solid Length: Midi Hemline: Flared Top fabric: Silk blend Occasio... |
| 5    | yes | 11511460   | -     | 0.893 | Product: Uptownie Lite Women Maroon Solid Pleated Flared Midi Crepe Skirt Brand: Uptownie Lite Color: Maroon Category: Flared Pattern: Solid Length: Midi Hemline: Flared Top fab... |
| 6    | no  | 15355338   | -     | 0.826 | Product: Uptownie Lite Girls Black Crepe Printed Pleated Skirt Brand: Uptownie Lite Color: Black Category: Flared Pattern: Floral printed Length: Midi Hemline: Flared Top fabric... |
| 7    | yes | 16608122   | -     | 0.821 | Product: Uptownie Lite Girls Black & Pink Printed Accordian Pleated Flared Knee-Length Skirt Brand: Uptownie Lite Color: Black Category: Flared Pattern: Floral printed Length: K... |
| 8    | no  | 11335786   | -     | 0.802 | Product: Uptownie Lite Women Gold-Coloured Solid Accordion Pleated Flared Midi Skirt Brand: Uptownie Lite Color: Gold Category: Flared Pattern: Solid Length: Midi Hemline: Flare... |
| 9    | no  | 19169942   | -     | 0.640 | Product: Uptownie Lite Women Yellow Crepe Smocked Strapless Basic Jumpsuit Brand: Uptownie Lite Color: Yellow Category: Basic jumpsuit Pattern: Solid Neck: Strapless Sleeves: Sl... |
| 10   | no  | 17267836   | -     | 0.632 | Product: Uptownie Lite Red & Yellow Striped Basic Jumpsuit Brand: Uptownie Lite Color: Red Category: Basic jumpsuit Pattern: Striped Neck: Round neck Sleeves: Sleeveless Top fab... |
| 11   | no  | 11322090   | -     | 0.626 | Product: Uptownie Lite Women Black Solid Basic Ruffle Jumpsuit Brand: Uptownie Lite Color: Black Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves: Short sleeves ... |
| 12   | no  | 13501842   | -     | 0.553 | Product: Uptownie Lite Women Black Solid Dhoti Jumpsuit Brand: Uptownie Lite Color: Black Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves: Sleeveless Top fabric... |
| 13   | no  | 11234642   | -     | 0.546 | Product: Uptownie Lite Women Black Solid Basic Jumpsuit with Belt Brand: Uptownie Lite Color: Black Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves: Sleeveless ... |
| 14   | no  | 10418102   | -     | 0.528 | Product: Uptownie Lite Women Maroon Solid Ruffled Relaxed Fit Basic Jumpsuit Brand: Uptownie Lite Color: Maroon Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves:... |
| 15   | no  | 11234652   | -     | 0.458 | Product: Uptownie Lite Women Burgundy Solid Basic Jumpsuit with Belt Brand: Uptownie Lite Color: Burgundy Category: Basic jumpsuit Pattern: Solid Neck: Round neck Sleeves: Sleev... |
| 16   | no  | 15852580   | -     | 0.235 | Product: URBANIC Black & White Printed Ruffle Detail Flared Mini Skirt Brand: URBANIC Color: Black Category: Flared Pattern: Floral printed Length: Mini Hemline: Flared Top fabr... |
| 17   | no  | 13792342   | -     | 0.211 | Product: U&F Purple Flared Maxi Skirt Brand: U&F Color: Green Category: Flared Pattern: Solid Length: Maxi Hemline: Flared Occasion: Casual Wash care: Machine wash                  |
| 18   | no  | 15633536   | -     | 0.194 | Product: URBANIC Women White & Coffee Brown Abstract Printed Flared Midi Skirt Brand: URBANIC Color: White Category: Flared Pattern: Abstract printed Length: Midi Hemline: Flare... |
| 19   | no  | 18542846   | -     | 0.194 | Product: URBANIC Women Navy Blue Simplicity Flare Leg Jeans Brand: URBANIC Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 4 Wash care: Machine wash   |
| 20   | no  | 15227004   | -     | 0.192 | Product: U&F Womens Green Flared Skirt Brand: U&F Color: Green Category: A-line Pattern: Solid Length: Knee length Hemline: Flared Top fabric: Polyester Occasion: Casual Wash ca... |
| 21   | no  | 13792352   | -     | 0.191 | Product: U&F Peach-Coloured Flared Maxi Skirt Brand: U&F Color: Peach Category: Flared Pattern: Solid Length: Maxi Hemline: Flared Top fabric: Polyester Occasion: Casual Wash ca... |
| 22   | no  | 13792332   | -     | 0.191 | Product: U&F Purple Flared Pleated Maxi Skirt Brand: U&F Color: Purple Category: Flared Pattern: Solid Length: Maxi Hemline: Flared Occasion: Casual Wash care: Machine wash         |
| 23   | no  | 13792392   | -     | 0.179 | Product: U&F Women Mustard Yellow Solid Accordion Pleated Maxi Flared Skirt Brand: U&F Color: Mustard Category: Flared Pattern: Solid Length: Mini Hemline: Flared Top fabric: Po... |
| 24   | no  | 13792344   | -     | 0.173 | Product: U&F Woman's Purple Solid Skirt Brand: U&F Color: Mustard Category: Flared Pattern: Solid Length: Maxi Hemline: Flared Top fabric: Polyester Occasion: Casual Wash care: ... |
| 25   | no  | 15850624   | -     | 0.171 | Product: URBANIC Dusty Pink Cut-Out Styled Back Crop Top Brand: URBANIC Color: Rose Category: Styled back Pattern: Solid Neck: Round neck Sleeves: Short regular sleeves Length: ... |
| 26   | no  | 16542580   | -     | 0.162 | Product: U&F Women Charming Lavender Solid Tiered Skirt Brand: U&F Color: Lavender Category: Flared Pattern: Solid Length: Mini Hemline: Flared Top fabric: Polyester Occasion: C... |
| 27   | no  | 18872440   | -     | 0.156 | Product: URBANIC Women Blue Heavy Fade Jeans Brand: URBANIC Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Wash care: Machine wash                                  |
| 28   | no  | 15852504   | -     | 0.154 | Product: URBANIC Women Blue Cotton Mildly Distressed Light Fade Cropped Jeans Brand: URBANIC Color: Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care... |
| 29   | no  | 15957650   | -     | 0.152 | Product: U&F Women Maroon Solid Accordion Pleated Maxi Skirt Brand: U&F Color: Maroon Category: Flared Pattern: Solid Length: Maxi Hemline: Flared Top fabric: Polyester Occasion... |
| 30   | no  | 13792346   | -     | 0.145 | Product: U&F Woman's Maroon Solid Skirt Brand: U&F Color: Maroon Category: Flared Pattern: Solid Length: Knee length Hemline: Flared Top fabric: Polyester Occasion: Casual Wash ... |

### Question 38/50

**Query:** Can you find something similar to "Mitera Grey Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta"?

**Relevant docs:** `['16950080']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 16950080   | -     | 1.000 | Product: Mitera Grey Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Grey Dupatta: With dupatta Pattern: Embellished Neck: Roun... |
| 2    | no  | 16950082   | -     | 0.750 | Product: Mitera Green & Grey Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Green Dupatta: With dupatta Pattern: Embroidered N... |
| 3    | no  | 18787332   | -     | 0.714 | Product: Mitera Mauve & Silver-Toned Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Mauve Dupatta: With dupatta Pattern: Embro... |
| 4    | no  | 16950094   | -     | 0.692 | Product: Mitera Red & Silver-Toned Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Red Dupatta: With dupatta Pattern: Embellish... |
| 5    | no  | 18813862   | -     | 0.666 | Product: Mitera White & Green Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: White Dupatta: With dupatta Pattern: Embroidered ... |
| 6    | no  | 18813860   | -     | 0.664 | Product: Mitera White & Green Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: White Dupatta: With dupatta Pattern: Embroidered ... |
| 7    | no  | 18759692   | -     | 0.641 | Product: Mitera Blue Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Blue Dupatta: With dupatta Pattern: Embroidered Neck: Boat... |
| 8    | no  | 18726440   | -     | 0.610 | Product: Mitera Green & White Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Green Dupatta: With dupatta Pattern: Embroidered ... |
| 9    | no  | 16950086   | -     | 0.605 | Product: Mitera Pink Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Pink Dupatta: With dupatta Pattern: Embellished Neck: Roun... |
| 10   | no  | 18813850   | -     | 0.604 | Product: Mitera White & Maroon Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: White Dupatta: With dupatta Pattern: Embroidered... |
| 11   | no  | 17414454   | -     | 0.581 | Product: Mitera Women Black & Golden Embroidered Sequinned Unstitched Lehenga with Blouse & Dupatta Brand: Mitera Color: Black Dupatta: With dupatta Pattern: Embroidered Neck: V... |
| 12   | no  | 18759676   | -     | 0.559 | Product: Mitera Green & Gold-Toned Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Green Dupatta: With dupatta Pattern: Embroidered Neck:... |
| 13   | no  | 18813864   | -     | 0.551 | Product: Mitera Peach-Coloured & Silver-Toned Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Brand: Mitera Color: Peach Dupatta: With dupatta Pattern: Embr... |
| 14   | no  | 16950084   | -     | 0.544 | Product: Mitera Magenta Embroidered Sequinned Foil Print Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Magenta Dupatta: With dupatta Pattern: Embro... |
| 15   | no  | 18726438   | -     | 0.540 | Product: Mitera Rust & White Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Rust Dupatta: With dupatta Pattern: Embroidered Ne... |
| 16   | no  | 16291316   | -     | 0.538 | Product: Mitera Green & Golden Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Green Dupatta: With dupatta Pattern: Embroidered Neck: Rou... |
| 17   | no  | 13515390   | -     | 0.520 | Product: Mitera Blue & Gold-Toned Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Blue Dupatta: With dupatta Pattern: Embroidered Sleeves... |
| 18   | no  | 16316606   | -     | 0.517 | Product: Mitera Black Velvet Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Black Dupatta: With dupatta Pattern: Solid Sleeves: Short regu... |
| 19   | no  | 16877304   | -     | 0.504 | Product: Mitera Women Black & Silver Embroidered Lehenga & Blouse With Dupatta Brand: Mitera Color: Black Dupatta: With dupatta Pattern: Embroidered Neck: Round neck Sleeves: Sl... |
| 20   | no  | 16219572   | -     | 0.498 | Product: Mitera Beige Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Beige Dupatta: With dupatta Pattern: Woven design Neck: Round neck Sleeves: Sho... |
| 21   | no  | 11753804   | -     | 0.491 | Product: Mitera Mustard Green & Pink Mirror Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Green Dupatta: With dupatta Pattern: Embroidered Sleeves:... |
| 22   | no  | 12622760   | -     | 0.488 | Product: Mitera Blue & Gold-Toned Embroidered Semi-Stitched Lehenga & Blouse with Dupatta Brand: Mitera Color: Blue Dupatta: With dupatta Pattern: Embroidered Neck: Round neck S... |
| 23   | no  | 16877280   | -     | 0.479 | Product: Mitera Women Maroon & Silver Embroidered Lehenga & Blouse With Dupatta Brand: Mitera Color: Maroon Dupatta: With dupatta Pattern: Embroidered Neck: Round neck Sleeves: ... |
| 24   | no  | 16950076   | -     | 0.477 | Product: Mitera Yellow Embroidered Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Yellow Dupatta: With dupatta Pattern: Embroidered Neck: ... |
| 25   | no  | 11530674   | -     | 0.473 | Product: Mitera Green & Pink Woven Design Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Teal Dupatta: With dupatta Pattern: Woven design Neck: Roun... |
| 26   | no  | 16291342   | -     | 0.457 | Product: Mitera Red & Golden Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Red Dupatta: With dupatta Pattern: Embroidered Sleeves: Shor... |
| 27   | no  | 12622736   | -     | 0.456 | Product: Mitera Navy Blue Embroidered Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Navy Blue Dupatta: With dupatta Pattern: Embroidered Neck: Roun... |
| 28   | no  | 16219596   | -     | 0.443 | Product: Mitera Maroon Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Maroon Dupatta: With dupatta Pattern: Woven design Neck: Round neck Sleeves: S... |
| 29   | no  | 16291330   | -     | 0.439 | Product: Mitera Red & Golden Embroidered Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Red Dupatta: With dupatta Pattern: Embroidered Sleeves: Shor... |
| 30   | no  | 12668574   | -     | 0.429 | Product: Mitera Blue & Gold-Toned Woven Design Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Blue Dupatta: With dupatta Pattern: Woven design Sleev... |

### Question 39/50

**Query:** Do you have anything similar to "Suta Beige & White Pure Linen Zari Saree"?

**Relevant docs:** `['15243956']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 15243956   | -     | 1.000 | Product: Suta Beige & White Pure Linen Zari Saree Brand: Suta Color: Beige Category: Saree Pattern: Solid Occasion: Festive Wash care: Dry clean                                     |
| 2    | no  | 14988280   | -     | 0.506 | Product: Suta Beige & Black Pure Cotton solid Ruffle Saree Brand: Suta Color: Beige Category: Saree Pattern: Solid Occasion: Party Wash care: Hand wash                              |
| 3    | no  | 16909300   | -     | 0.484 | Product: Suta Off White & Black Zari Silk Cotton Maheshwari Saree Brand: Suta Color: Off White Category: Maheshwari Pattern: Solid Occasion: Traditional Wash care: Dry clean        |
| 4    | no  | 14988194   | -     | 0.479 | Product: Suta Gold-Toned Solid Zari Pure Linen Saree Brand: Suta Color: Gold Category: Saree Pattern: Solid Occasion: Daily Wash care: Dry clean                                     |
| 5    | no  | 15244224   | -     | 0.475 | Product: Suta Beige & White Floral Embroidered Saree Brand: Suta Color: Beige Category: Saree Pattern: Floral embroidered Occasion: Festive Wash care: Dry clean                     |
| 6    | no  | 15244002   | -     | 0.445 | Product: Suta Pink & Gold-Toned Zari Pure Linen Saree Brand: Suta Color: Pink Category: Saree Pattern: Solid Occasion: Work Wash care: Dry clean                                     |
| 7    | no  | 17638770   | -     | 0.431 | Product: Silk Land Beige & Red Ethnic Motifs Zari Pure Silk Kanjeevaram Saree Brand: Silk Land Color: Beige Category: Kanjeevaram Pattern: Ethnic motifs printed Occasion: Tradit... |
| 8    | no  | 15244024   | -     | 0.397 | Product: Suta Beige Pink Floral Motifs PolyCotton Saree Brand: Suta Color: Beige Category: Saree Pattern: Floral embroidered Occasion: Daily Wash care: Dry clean                    |
| 9    | no  | 17781762   | -     | 0.386 | Product: Silk Land Beige & Pink Woven Design Zari Jute Silk Tussar Saree Brand: Silk Land Color: Beige Category: Tussar Pattern: Geometric woven design Occasion: Traditional Was... |
| 10   | no  | 15244106   | -     | 0.338 | Product: Suta White & Pink Polka Dot Printed Pure Cotton Saree Brand: Suta Color: White Category: Saree Pattern: Polka dots printed Occasion: Daily Wash care: Hand wash             |
| 11   | no  | 15244118   | -     | 0.334 | Product: Suta White & Black Ethnic Motifs Jamdani Polycotton Saree Brand: Suta Color: White Category: Saree Pattern: Ethnic motifs printed Occasion: Work Wash care: Dry clean       |
| 12   | no  | 18262236   | -     | 0.332 | Product: Silk Land Beige & Navy Blue Kalamkari Pure Cotton Chanderi Saree Brand: Silk Land Color: Beige Category: Chanderi Pattern: Kalamkari printed Occasion: Daily Wash care: ... |
| 13   | no  | 16909578   | -     | 0.316 | Product: Suta Violet & Green Embellished Zari Pure Cotton Saree Brand: Suta Color: Violet Category: Saree Pattern: Embellished Occasion: Festive Wash care: Dry clean                |
| 14   | no  | 17638792   | -     | 0.310 | Product: Silk Land White & Blue Zari Pure Silk Kanjeevaram Saree Brand: Silk Land Color: White Category: Kanjeevaram Pattern: Abstract printed Occasion: Party Wash care: Dry clean  |
| 15   | no  | 15511808   | -     | 0.306 | Product: Suta Grey & Maroon Colourblocked Pure Cotton Saree Brand: Suta Color: Multi Category: Saree Pattern: Colourblocked Occasion: Work Wash care: Hand wash                      |
| 16   | no  | 14988276   | -     | 0.296 | Product: Suta Peach Blue Warli Printed Pure Cotton Saree Brand: Suta Color: Peach Category: Saree Pattern: Ethnic motifs printed Occasion: Daily Wash care: Hand wash                |
| 17   | no  | 16909636   | -     | 0.286 | Product: Suta Maroon & Pink Colourblocked Zari Pure Cotton Saree Brand: Suta Color: Maroon Category: Saree Pattern: Checked colourblocked Occasion: Festive Wash care: Dry clean     |
| 18   | no  | 16909486   | -     | 0.285 | Product: Suta Blue & Yellow Colourblocked Zari Saree Brand: Suta Color: Blue Category: Saree Pattern: Checked colourblocked Occasion: Daily Wash care: Dry clean                     |
| 19   | no  | 15243974   | -     | 0.270 | Product: Suta Maroon White Hand Blocked Pure Cotton Saree Brand: Suta Color: Maroon Category: Saree Pattern: Floral printed Occasion: Daily Wash care: Hand wash                     |
| 20   | no  | 17876884   | -     | 0.264 | Product: Silk Land Navy Blue Ethnic Motifs Zari Pure Silk Banarasi Saree Brand: Silk Land Color: Navy Blue Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Tradi... |
| 21   | no  | 15244104   | -     | 0.263 | Product: Suta Lavender Solid Pure Cotton Ruffle Saree Brand: Suta Color: Lavender Category: Saree Pattern: Solid Occasion: Party Wash care: Hand wash                                |
| 22   | no  | 18390702   | -     | 0.261 | Product: Suta Off White & Golden Striped Saree Brand: Suta Color: Off White Category: Saree Pattern: Striped Occasion: Festive Wash care: Dry clean                                  |
| 23   | no  | 15243916   | -     | 0.231 | Product: Suta Olive Green & Black Solid Pure Cotton Saree Brand: Suta Color: Olive Category: Saree Pattern: Solid Occasion: Work Wash care: Hand wash                                |
| 24   | no  | 15435724   | -     | 0.224 | Product: Suta Navy Blue & Pink Colourblocked Mul Saree Brand: Suta Color: Navy Blue Category: Saree Pattern: Colourblocked Occasion: Festive Wash care: Hand wash                    |
| 25   | no  | 17902892   | -     | 0.222 | Product: Silk Land Navy Blue & Golden Ethnic Motifs Zari Pure Silk Banarasi Saree Brand: Silk Land Color: Navy Blue Category: Banarasi Pattern: Ethnic motifs woven design Occasi... |
| 26   | no  | 15244114   | -     | 0.218 | Product: Suta Mustard Yellow & Pink Solid Cotton Striped Saree Brand: Suta Color: Mustard Category: Saree Pattern: Solid Occasion: Festive Wash care: Dry clean                      |
| 27   | no  | 18166926   | -     | 0.211 | Product: Suta Women White Embroidered Cotton Saree Blouse Brand: Suta Color: White Category: Saree Pattern: Embroidered Neck: Boat neck Sleeves: Short sleeves Top fabric: Cotton... |
| 28   | no  | 15243876   | -     | 0.201 | Product: Suta Brown & Black Polka Dots Printed Pure Cotton Saree Brand: Suta Color: Brown Category: Saree Pattern: Polka dots printed Occasion: Daily Wash care: Hand wash           |
| 29   | no  | 18676682   | -     | 0.200 | Product: Ethnic Yard Beige & Grey Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Ethnic Yard Color: Beige Dupatta: With dupatta Pattern: Solid Sleeves: Long regul... |
| 30   | no  | 17638756   | -     | 0.200 | Product: Silk Land Green & Red Floral Zari Pure Silk Ikat Saree Brand: Silk Land Color: Green Category: Ikat Pattern: Floral woven design Occasion: Traditional Wash care: Dry clean |

### Question 40/50

**Query:** Show me options from Levis for everyday wear, preferably in Blue.

**Relevant docs:** `['18069226', '16532142', '18069298', '18069260', '16653678', '16653750', '16653608', '16653786']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.267     | 1.000  | 0.500 | 0.618 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 18069150   | -     | 1.000 | Product: Levis Women Blue Skinny Fit Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash    |
| 2    | yes | 16653786   | -     | 0.991 | Product: Levis Women Blue 714 Straight Fit High-Rise Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash ca... |
| 3    | no  | 18069276   | -     | 0.987 | Product: Levis Women Blue Skinny Fit Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash    |
| 4    | no  | 18903336   | -     | 0.985 | Product: Levis Women Blue 725 Bootcut Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash   |
| 5    | no  | 16653698   | -     | 0.968 | Product: Levis Women Blue Straight Fit High-Rise Light Fade Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash    |
| 6    | no  | 18903198   | -     | 0.967 | Product: Levis Women Blue Skinny Fit Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash    |
| 7    | no  | 18903182   | -     | 0.959 | Product: Levis Women Blue Straight Fit High-Rise Light Fade Stretchable Casual Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash... |
| 8    | yes | 16653608   | -     | 0.956 | Product: Levis Women Blue Skinny Fit Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash    |
| 9    | no  | 16653772   | -     | 0.953 | Product: Levis Women Blue Skinny Fit Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash    |
| 10   | yes | 18069298   | -     | 0.947 | Product: Levis Women Blue 710 Super Skinny Fit Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Ma... |
| 11   | no  | 16653658   | -     | 0.946 | Product: Levis Women Blue 311 Shaping Skinny Fit Mid Rise Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wa... |
| 12   | yes | 18069260   | -     | 0.944 | Product: Levis Women Blue 710 Super Skinny Fit Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Ma... |
| 13   | yes | 18069226   | -     | 0.940 | Product: Levis Women Blue 710 Super Skinny Fit Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Ma... |
| 14   | no  | 18069202   | -     | 0.937 | Product: Levis Women Blue 710 Super Skinny Fit Mid-Rise Heavy Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash... |
| 15   | no  | 13326354   | -     | 0.931 | Product: Levis Women Blue Super Skinny Fit High-Rise Clean Look Sustainable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash ca... |
| 16   | no  | 16794836   | -     | 0.926 | Product: Levis Women Blue 721 Skinny Fit High-Rise Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash |
| 17   | no  | 12259048   | -     | 0.921 | Product: Levis Women Blue 710 Super Skinny Fit High-Rise Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Was... |
| 18   | no  | 18903152   | -     | 0.921 | Product: Levis Women Blue Skinny Fit High-Rise Light Fade Stretchable Casual Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 19   | yes | 16653750   | -     | 0.907 | Product: Levis Women Blue 711 Skinny Fit Mid Rise Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care:... |
| 20   | no  | 16653760   | -     | 0.903 | Product: Levis Women Blue 711 Skinny Fit Mid Rise Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care:... |
| 21   | yes | 16532142   | -     | 0.898 | Product: Levis Women Blue 711 Skinny Fit Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine ... |
| 22   | no  | 18903286   | -     | 0.892 | Product: Levis Women Blue 711 Skinny Fit Light Fade Mid Rise Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care:... |
| 23   | yes | 16653678   | -     | 0.880 | Product: Levis Women Blue 711 Skinny Fit Heavy Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine ... |
| 24   | no  | 16865718   | -     | 0.835 | Product: Levis X Deepika Padukone Women Blue 70S Wide Leg High-Rise Light Fade Stretchable Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Poc... |
| 25   | no  | 16794818   | -     | 0.835 | Product: Levis Women Blue 501 Straight Fit High-Rise Clean Look Jeans Brand: Levis Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine ... |
| 26   | no  | 15022668   | -     | 0.664 | Product: Levis Women Navy Blue Super Skinny Fit Stretchable Jeans 710 Brand: Levis Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Mac... |
| 27   | no  | 15506368   | -     | 0.606 | Product: Levi's x Deepika Padukone Women Navy Blue Pleated High Loose Straight Fit High-Rise Jeans Brand: Levis Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Cas... |
| 28   | no  | 18069146   | -     | 0.557 | Product: Levis Women Blue Printed Drop-Shoulder Sweatshirt Brand: Levis Color: Blue Category: Pullover Pattern: Brand logo printed Neck: Round neck Sleeves: Long sleeves Length:... |
| 29   | no  | 16781554   | -     | 0.504 | Product: Levis X Deepika Padukone Blue Ribbed Fitted Top Brand: Levis Color: Blue Category: Fitted Pattern: Vertical stripes striped Neck: High neck Sleeves: Sleeveless no Lengt... |
| 30   | no  | 14860462   | -     | 0.481 | Product: Levis Women Blue Round Neck Printed Sweatshirt Brand: Levis Color: Blue Category: Pullover Pattern: Graphic printed Neck: Round neck Sleeves: Long sleeves Length: Regul... |

### Question 41/50

**Query:** Show me Pullover that are Black and have Solid print.

**Relevant docs:** `['16707678', '16124454', '13534776', '15964092', '15274016', '15963804', '15198584', '15243336']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.067     | 0.250  | 0.111 | 0.129 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 19266888   | -     | 1.000 | Product: H&M Women Black Solid Collared Sweatshirt Brand: H&M Color: Black Category: Pullover Pattern: Solid Neck: Mock collar Sleeves: Long sleeves Length: Regular Hemline: Rib... |
| 2    | no  | 14080898   | -     | 0.912 | Product: DressBerry Women Black Print Detail Sweatshirt Brand: DressBerry Color: Black Category: Pullover Pattern: Typography solid Neck: Round neck Sleeves: Long sleeves Length... |
| 3    | no  | 15845464   | -     | 0.905 | Product: URBANIC Women Black Solid Cotton Sweatshirt Brand: URBANIC Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Crop Hemline: S... |
| 4    | no  | 18004440   | -     | 0.859 | Product: Aeropostale Women Black Printed Hooded Sweatshirt Brand: Aeropostale Color: Black Category: Pullover Pattern: Typography printed Neck: Hood Sleeves: Long sleeves Length... |
| 5    | no  | 15642616   | -     | 0.851 | Product: Aesthetic Bodies Women Black Cotton Sweatshirt Brand: Aesthetic Bodies Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Cro... |
| 6    | no  | 15630060   | -     | 0.845 | Product: H&M Women Black Solid Hoodie Brand: H&M Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Longline Hemline: Straight Top fabric: C... |
| 7    | no  | 14512956   | -     | 0.829 | Product: Powerpuff Girls by Kook N Keech Women Black Solid Sweatshirt Brand: Powerpuff Girls by Kook N Keech Color: Black Category: Pullover Pattern: Solid Neck: Round neck Slee... |
| 8    | no  | 19269372   | -     | 0.795 | Product: BoStreet Women Black Colourblocked Long Sleeves Sweatshirts Brand: BoStreet Color: Black Category: Pullover Pattern: Solid colourblocked Neck: Hood Sleeves: Long sleeve... |
| 9    | yes | 15198584   | -     | 0.761 | Product: H&M Women Black Sweatshirt Brand: H&M Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Ribbed Top fabric: ... |
| 10   | no  | 10611428   | -     | 0.761 | Product: Alsace Lorraine Paris Women Black Solid Hooded Sweatshirt Brand: Alsace Lorraine Paris Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves L... |
| 11   | no  | 18962138   | -     | 0.757 | Product: Nike Women Black CLUB FLC GX STD CREW Brand Logo Printed Sweatshirt Brand: Nike Color: Black Category: Pullover Pattern: Brand logo printed Neck: Round neck Sleeves: Lo... |
| 12   | no  | 15870014   | -     | 0.748 | Product: New Balance Women Black Sweatshirt Brand: New Balance Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Str... |
| 13   | no  | 14080668   | -     | 0.746 | Product: DressBerry Women Black Solid Sweatshirt Brand: DressBerry Color: Black Category: Pullover Pattern: Solid Neck: Mock collar Sleeves: Long sleeves Length: Regular Hemline... |
| 14   | no  | 12048466   | -     | 0.735 | Product: INVICTUS Women Black Solid Pullover Brand: INVICTUS Color: Black Category: Pullover Pattern: Solid Neck: V-neck Sleeves: Long sleeves Length: Regular Hemline: Ribbed To... |
| 15   | no  | 10714640   | -     | 0.733 | Product: Taanz Women Black Solid Sweatshirt Brand: Taanz Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Straight ... |
| 16   | no  | 15086606   | -     | 0.718 | Product: URBANIC Women Black Printed Sweatshirt Brand: URBANIC Color: Black Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length: Regular... |
| 17   | no  | 6726577    | -     | 0.708 | Product: Mast & Harbour Women Black Solid Pullover Brand: Mast & Harbour Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Hemline: Ribbed To... |
| 18   | no  | 13615048   | -     | 0.681 | Product: Flying Machine Women Black Solid Sweatshirt Brand: Flying Machine Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemlin... |
| 19   | no  | 10683730   | -     | 0.667 | Product: STREET 9 Women Black Solid Sweater Brand: STREET 9 Color: Black Category: Pullover Pattern: Solid Neck: Turtle neck Sleeves: Long sleeves Hemline: Straight Top fabric: ... |
| 20   | no  | 9478497    | -     | 0.607 | Product: The Roadster Lifestyle Co Women Black Solid Sweater Brand: Roadster Color: Black Category: Pullover Pattern: Solid Neck: V-neck Sleeves: Long sleeves Hemline: Ribbed To... |
| 21   | no  | 15869386   | -     | 0.591 | Product: New Balance Women Black Solid Hooded Sweatshirt Brand: New Balance Color: Black Category: Front-open Pattern: Brand logo solid Neck: Hood Sleeves: Long sleeves Length: ... |
| 22   | no  | 16533910   | -     | 0.586 | Product: RAREISM Women Black Hooded Sweatshirt Brand: RAREISM Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: Straight T... |
| 23   | no  | 18144562   | -     | 0.570 | Product: Marks & Spencer Women Black Sherpa Sweatshirt Brand: Marks & Spencer Color: Black Category: Pullover Pattern: Solid Neck: Shirt collar Sleeves: Long sleeves Length: Reg... |
| 24   | no  | 10575458   | -     | 0.556 | Product: The Roadster Lifestyle Co Women Black Solid Sweater Brand: Roadster Color: Black Category: Pullover Pattern: Solid Neck: Turtle neck Sleeves: Long sleeves Hemline: Curv... |
| 25   | no  | 10791506   | -     | 0.554 | Product: The Vanca Women Black & Navy Blue Solid Longline Pullover Sweatshirt Brand: The Vanca Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Three-qua... |
| 26   | no  | 15778944   | -     | 0.544 | Product: ONLY Women Black & Pink Striped Pullover Sweater Brand: ONLY Color: Black Category: Pullover Pattern: Striped Neck: Round neck Sleeves: Long sleeves Length: Regular Hem... |
| 27   | yes | 15963804   | -     | 0.538 | Product: MANGO Women Black Solid Pullover Sweater Brand: MANGO Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Rib... |
| 28   | no  | 16583226   | -     | 0.538 | Product: 20Dresses Women Black Plus Size Cotton Sweatshirt Brand: 20Dresses Color: Black Category: Pullover Pattern: Solid Neck: High neck Sleeves: Long sleeves Length: Regular ... |
| 29   | no  | 13593756   | -     | 0.537 | Product: BEVERLY BLUES Women Black Solid Sweatshirt Brand: BEVERLY BLUES Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Crop Hemli... |
| 30   | no  | 14518558   | -     | 0.531 | Product: Powerpuff Girls by Kook N Keech Women Black & Blue Printed Sweatshirt Brand: Powerpuff Girls by Kook N Keech Color: Black Category: Pullover Pattern: Typography printed... |

### Question 42/50

**Query:** I'm looking for Dress that cost no more than 5300.

**Relevant docs:** `['13878542', '17705690', '18365368', '16921564', '16921510', '16921508', '16921524', '16921550']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.000     | 0.000  | 0.000 | 0.000 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 13843640   | -     | 1.000 | Product: Stylee LIFESTYLE Navy Blue & Gold-Toned Velvet Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Navy Blue Category: Dress Pattern: Ethnic motifs Bottom fabri... |
| 2    | no  | 18750730   | -     | 0.825 | Product: Stylee LIFESTYLE Olive Green & Red Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Olive Category: Dress Pattern: Other Bottom fabric: Silk blend Dupatta fabri... |
| 3    | no  | 19392350   | -     | 0.801 | Product: Ethnic Yard Green & Grey Embroidered Semi-Stitched Dress Material Brand: Ethnic Yard Color: Green Category: Dress Pattern: Ethnic motifs Occasion: Festive Wash care: Dr... |
| 4    | no  | 17287376   | -     | 0.783 | Product: Stylee LIFESTYLE Yellow & Gold-Toned Embellished Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Yellow Category: Dress Pattern: Ethnic motifs Bottom fabric: P... |
| 5    | no  | 18766164   | -     | 0.741 | Product: Stylee LIFESTYLE Black & Gold-Toned Pure Silk Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Black Category: Dress Pattern: Floral Bottom fabric: Pure silk Du... |
| 6    | no  | 19396408   | -     | 0.697 | Product: Stylee LIFESTYLE Womens Beige Embroidered Pure Silk Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Beige Category: Dress Pattern: Striped Bottom fabric: Pure ... |
| 7    | no  | 16533888   | -     | 0.670 | Product: Ethnic Junction Navy Blue & Gold-Toned Embroidered Unstitched Dress Material Brand: Ethnic Junction Color: Navy Blue Category: Dress Pattern: Floral Bottom fabric: Shan... |
| 8    | no  | 17287346   | -     | 0.661 | Product: Stylee LIFESTYLE Blue & Silver-Toned Embroidered Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Blue Category: Dress Pattern: Ethnic motifs Bottom fabric: Pol... |
| 9    | no  | 14482774   | -     | 0.660 | Product: Stylee LIFESTYLE Yellow Embroidered Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Yellow Category: Dress Pattern: Geometric Bottom fabric: Poly chiffon Du... |
| 10   | no  | 16275034   | -     | 0.659 | Product: Stylee LIFESTYLE Navy Blue & Coral Printed Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Navy Blue Category: Dress Pattern: Ethnic motifs Bottom fabric: Pash... |
| 11   | no  | 15224706   | -     | 0.657 | Product: Stylee LIFESTYLE Green Embellished Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Green Category: Dress Pattern: Ethnic motifs Bottom fabric: Satin Dupatta... |
| 12   | no  | 13185960   | -     | 0.653 | Product: Stylee LIFESTYLE Women Navy Blue Embroidered Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Navy Blue Category: Dress Pattern: Ethnic motifs Bottom fabric: Si... |
| 13   | no  | 18750736   | -     | 0.589 | Product: Stylee LIFESTYLE Beige & Red Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Beige Category: Dress Pattern: Floral Bottom fabric: Silk blend Dupatta fabric: Po... |
| 14   | no  | 18190664   | -     | 0.568 | Product: Stylee LIFESTYLE Maroon & Gold-Toned Embroidered Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Maroon Category: Dress Pattern: Floral Bottom fabric: Poly ... |
| 15   | no  | 19239046   | -     | 0.554 | Product: Stylee LIFESTYLE Women Off White Embroidered Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Off White Category: Dress Pattern: Ethnic motifs Bottom fabric:... |
| 16   | no  | 15144126   | -     | 0.552 | Product: Stylee LIFESTYLE Maroon & Gold-Toned Embroidered Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Maroon Category: Dress Pattern: Other Bottom fabric: Shanto... |
| 17   | no  | 19342368   | -     | 0.544 | Product: MORLY Beige & Gold-Toned Woven Design Dupion Silk Unstitched Dress Material Brand: MORLY Color: Beige Category: Dress Pattern: Floral Bottom fabric: Satin Dupatta fabri... |
| 18   | no  | 17149844   | -     | 0.504 | Product: Stylee LIFESTYLE Women Teal & Red Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Teal Category: Dress Pattern: Ethnic motifs Bottom fabric: Pure silk Dupatta ... |
| 19   | no  | 12024994   | -     | 0.480 | Product: Ethnic Junction Green Cotton Blend Unstitched Dress Material Brand: Ethnic Junction Color: Green Category: Dress Pattern: Floral Bottom fabric: Cotton blend Dupatta fab... |
| 20   | no  | 13843642   | -     | 0.472 | Product: Stylee LIFESTYLE Navy Blue & White Satin Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Navy Blue Category: Dress Pattern: Geometric Occasion: Festive Wash... |
| 21   | no  | 17149842   | -     | 0.463 | Product: Stylee LIFESTYLE Navy Blue & Yellow Printed Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Navy Blue Category: Dress Pattern: Ethnic motifs Bottom fabric: Pur... |
| 22   | no  | 13185952   | -     | 0.462 | Product: Stylee LIFESTYLE Women Green & Brown Embroidered Dress Material Brand: Stylee LIFESTYLE Color: Green Category: Dress Pattern: Ethnic motifs Bottom fabric: Silk blend Du... |
| 23   | no  | 13996506   | -     | 0.456 | Product: Stylee LIFESTYLE Blue & Gold-Toned Net Semi-Stitched Dress Material Brand: Stylee LIFESTYLE Color: Blue Category: Dress Pattern: Floral Dupatta fabric: Net Occasion: Fe... |
| 24   | no  | 13869240   | -     | 0.451 | Product: Stylee LIFESTYLE Blue Cotton Blend Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Blue Category: Dress Pattern: Ethnic motifs Bottom fabric: Cotton blend Dupa... |
| 25   | no  | 14990142   | -     | 0.439 | Product: Stylee LIFESTYLE Turquoise Blue Embroidered Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Turquoise Blue Category: Dress Pattern: Ethnic motifs Bottom fabric... |
| 26   | no  | 18967572   | -     | 0.431 | Product: Lilots Maroon & Gold-Toned Unstitched Dress Material Brand: Lilots Color: Maroon Category: Dress Pattern: Floral Bottom fabric: Silk blend Dupatta fabric: Silk blend Oc... |
| 27   | no  | 13856418   | -     | 0.422 | Product: Safaa Off-White & Gold-Toned Cotton Blend Woven Design Unstitched Dress Material For Summer Brand: Safaa Color: Off White Category: Dress Pattern: Ethnic motifs Bottom ... |
| 28   | no  | 11253802   | -     | 0.406 | Product: Ishin Navy Blue & White Embroidered Unstitched Dress Material Brand: Ishin Color: Navy Blue Category: Dress Pattern: Floral Bottom fabric: Cotton blend Dupatta fabric: ... |
| 29   | no  | 17287372   | -     | 0.394 | Product: Stylee LIFESTYLE Grey & Silver-Toned Embroidered Unstitched Dress Material Brand: Stylee LIFESTYLE Color: Grey Category: Dress Pattern: Ethnic motifs Bottom fabric: Sha... |
| 30   | no  | 14358624   | -     | 0.385 | Product: Ethnic Junction Green & Gold-Toned Silk Blend Unstitched Dress Material Brand: Ethnic Junction Color: Green Category: Dress Pattern: Paisley Bottom fabric: Shantoon Dup... |

### Question 43/50

**Query:** I'm looking for something Pink from Mitera for a traditional occasion.

**Relevant docs:** `['15012182', '11454958', '11244988', '18302880']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.133     | 1.000  | 0.200 | 0.474 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 13886174   | -     | 1.000 | Product: Mitera Pink & White Pure Cotton Woven Design Taant Saree Brand: Mitera Color: Pink Category: Taant Pattern: Woven design Occasion: Traditional Wash care: Dry clean         |
| 2    | no  | 18287324   | -     | 0.957 | Product: Mitera Floral Saree Brand: Mitera Color: Pink Category: Saree Pattern: Floral printed Occasion: Party Wash care: Dry clean                                                  |
| 3    | no  | 12668502   | -     | 0.947 | Product: Mitera Pink & Blue Woven Design Semi-Stitched Lehenga & Unstitched Blouse with Dupatta Brand: Mitera Color: Pink Dupatta: With dupatta Pattern: Woven design Sleeves: Th... |
| 4    | no  | 17552342   | -     | 0.920 | Product: Mitera Floral Saree with Embroidered Border Brand: Mitera Color: Pink Category: Saree Pattern: Floral embroidered Occasion: Party Wash care: Dry clean                      |
| 5    | yes | 11244988   | -     | 0.919 | Product: Mitera Pink & Gold-Toned Silk Blend Woven Design Kanjeevaram Saree Brand: Mitera Color: Pink Category: Kanjeevaram Pattern: Ethnic motifs woven design Occasion: Traditi... |
| 6    | no  | 11218670   | -     | 0.906 | Product: Mitera Pink & Gold-Toned Silk Blend Woven Design Kanjeevaram Saree Brand: Mitera Color: Pink Category: Kanjeevaram Pattern: Woven design Occasion: Traditional Wash care... |
| 7    | yes | 18302880   | -     | 0.882 | Product: Mitera Pink & Gold-Toned Woven Design Zari Silk Blend Kanjeevaram Saree Brand: Mitera Color: Pink Category: Kanjeevaram Pattern: Woven design Occasion: Traditional Wash... |
| 8    | no  | 18802314   | -     | 0.880 | Product: Mitera Pink & Green Ethnic Motifs Woven Design Dupatta with Zari Brand: Mitera Color: Pink Pattern: Ethnic motifs woven design Top fabric: Silk blend Occasion: Daily Wa... |
| 9    | no  | 16125582   | -     | 0.875 | Product: Mitera Pink Embellished Mirror Work Heavy Work Saree Brand: Mitera Color: Pink Category: Saree Pattern: Embellished Occasion: Party Wash care: Dry clean                    |
| 10   | no  | 12679536   | -     | 0.859 | Product: Mitera Pink & White Pure Georgette Embroidered Saree Brand: Mitera Color: Pink Category: Saree Pattern: Paisley embroidered Occasion: Festive Wash care: Dry clean          |
| 11   | no  | 17044538   | -     | 0.818 | Product: Mitera Tie and Dye Pleated Saree Brand: Mitera Color: Pink Category: Saree Pattern: Tie and dye printed Occasion: Party Wash care: Hand wash                                |
| 12   | no  | 16950086   | -     | 0.814 | Product: Mitera Pink Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Pink Dupatta: With dupatta Pattern: Embellished Neck: Roun... |
| 13   | yes | 15012182   | -     | 0.755 | Product: Mitera Pink & Silver-Toned Paisley Zari Silk Blend Banarasi Saree Brand: Mitera Color: Pink Category: Banarasi Pattern: Paisley woven design Occasion: Traditional Wash ... |
| 14   | no  | 16219622   | -     | 0.752 | Product: Mitera Pink Thread Work Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Pink Dupatta: With dupatta Pattern: Woven design Neck: Round neck Sl... |
| 15   | no  | 14850332   | -     | 0.749 | Product: Mitera Pink & Gold-Toned Woven Design Silk Blend Banarasi Saree Brand: Mitera Color: Pink Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Traditional W... |
| 16   | no  | 11530714   | -     | 0.737 | Product: Mitera Pink & Gold-Toned Woven Design Semi-Stitched Lehenga Choli Brand: Mitera Color: Pink Dupatta: With dupatta Pattern: Woven design Neck: Round neck Sleeves: Short ... |
| 17   | no  | 15012204   | -     | 0.727 | Product: Mitera Pink & Gold-Toned Woven Design Zari Silk Blend Banarasi Saree Brand: Mitera Color: Pink Category: Banarasi Pattern: Woven design Occasion: Festive Wash care: Dry... |
| 18   | no  | 16291288   | -     | 0.715 | Product: Mitera Pink & Green Printed Block Print Semi-Stitched Lehenga & Unstitched Lehenga Choli Brand: Mitera Color: Pink Pattern: Printed Neck: V-neck Sleeves: Long puffed sl... |
| 19   | yes | 11454958   | -     | 0.679 | Product: Mitera Pink & Golden Woven Design Banarasi Saree Brand: Mitera Color: Pink Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Traditional Wash care: Dry c... |
| 20   | no  | 16877306   | -     | 0.675 | Product: Mitera Women Pink & Purple Embroidered Lehenga & Blouse With Dupatta Brand: Mitera Color: Pink Dupatta: With dupatta Pattern: Embroidered Neck: Round neck Sleeves: Slee... |
| 21   | no  | 15098912   | -     | 0.659 | Product: Mitera Pink & Maroon Khari Print Semi-Stitched Lehenga & Unstitched Blouse With Dupatta Brand: Mitera Color: Pink Dupatta: With dupatta Pattern: Woven design Neck: Roun... |
| 22   | no  | 16576222   | -     | 0.629 | Product: Mitera Pink & Golden Ethnic Motifs Banarasi Saree with Zari Border Brand: Mitera Color: Pink Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Festive Wa... |
| 23   | no  | 17669470   | -     | 0.528 | Product: Mitera Colourblocked Satin Saree Brand: Mitera Color: Pink Category: Saree Pattern: Colourblocked Occasion: Daily Wash care: Hand wash                                      |
| 24   | no  | 16286086   | -     | 0.501 | Product: Mitera Green & Pink Unstitched Dress Material Brand: Mitera Color: Green Category: Dress Pattern: Floral Bottom fabric: Silk blend Dupatta fabric: Silk blend Occasion: ... |
| 25   | no  | 18585472   | -     | 0.443 | Product: Mitera Black & Pink Floral Pure Linen Saree Brand: Mitera Color: Black Category: Saree Pattern: Floral woven design Occasion: Festive Wash care: Dry clean                  |
| 26   | no  | 11096590   | -     | 0.416 | Product: Mitera Orange & Pink Silk Blend Woven Design Kanjeevaram Saree Brand: Mitera Color: Orange Category: Kanjeevaram Pattern: Woven design Occasion: Traditional Wash care: ... |
| 27   | no  | 17898990   | -     | 0.379 | Product: Mitera Fuchsia Striped Sequinned Saree Brand: Mitera Color: Fuchsia Category: Saree Pattern: Striped Occasion: Party Wash care: Dry clean                                   |
| 28   | no  | 15519332   | -     | 0.370 | Product: Mitera Purple & Pink Bandhani Saree Brand: Mitera Color: Purple Category: Bandhani Pattern: Bandhani printed Occasion: Traditional Wash care: Dry clean                     |
| 29   | no  | 16286120   | -     | 0.348 | Product: Mitera Red & Green Silk Blend Unstitched Dress Material Brand: Mitera Color: Red Category: Dress Pattern: Floral Bottom fabric: Silk blend Dupatta fabric: Silk blend Oc... |
| 30   | no  | 17325496   | -     | 0.344 | Product: Mitera Green & Off-White Embroidered Unstitched Dress Material Brand: Mitera Color: Green Category: Dress Pattern: Ethnic motifs Bottom fabric: Poly georgette Dupatta f... |

### Question 44/50

**Query:** I'm looking for Pullover from max for everyday wear under 600.

**Relevant docs:** `['19204850', '15878996', '16156132']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.100     | 1.000  | 0.200 | 0.471 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 18782606   | -     | 1.000 | Product: max Women Black Printed Sweatshirt Brand: max Color: Black Category: Pullover Pattern: Alphanumeric printed Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: St... |
| 2    | no  | 15878938   | -     | 0.975 | Product: max Women Grey Printed Round Neck Sweatshirt Brand: max Color: Grey Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length: Regula... |
| 3    | no  | 18995122   | -     | 0.955 | Product: max Women Black Printed Sweatshirt Brand: max Color: Black Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline... |
| 4    | no  | 15878978   | -     | 0.917 | Product: max Women Green Solid Round Neck Sweatshirt Brand: max Color: Green Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: St... |
| 5    | yes | 15878996   | -     | 0.861 | Product: max Women Olive Green Printed Round neck Sweatshirt Brand: max Color: Olive Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length... |
| 6    | no  | 15673658   | -     | 0.823 | Product: max Women Peach-Coloured Printed Sweatshirt Brand: max Color: Peach Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length: Regula... |
| 7    | no  | 15670702   | -     | 0.818 | Product: max Women Rust Pullover with Embellished Detail Brand: max Color: Rust Category: Pullover Pattern: Geometric self design Neck: Turtle neck Sleeves: Long sleeves Length:... |
| 8    | yes | 19204850   | -     | 0.803 | Product: max Women Peach-Coloured Printed Slip on Sweatshirt Brand: max Color: Peach Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length... |
| 9    | yes | 16156132   | -     | 0.719 | Product: max Women Olive Green Printed Sweatshirt Brand: max Color: Olive Category: Pullover Pattern: Graphic printed Neck: Round neck Sleeves: Long sleeves Length: Regular Heml... |
| 10   | no  | 19204868   | -     | 0.636 | Product: max Women Lime Green Printed Sweatshirt Brand: max Color: Lime Green Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length: Regul... |
| 11   | no  | 17748850   | -     | 0.360 | Product: max Black Pure Cotton Dupatta Brand: max Color: Black Pattern: Solid Top fabric: Pure cotton Occasion: Daily Wash care: Machine wash                                        |
| 12   | no  | 15630060   | -     | 0.328 | Product: H&M Women Black Solid Hoodie Brand: H&M Color: Black Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Longline Hemline: Straight Top fabric: C... |
| 13   | no  | 17155520   | -     | 0.326 | Product: H&M Woman Grey Hoodie Brand: H&M Color: Grey Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Cotton Occ... |
| 14   | no  | 18992236   | -     | 0.313 | Product: max Women Black Monochrome Shrug Brand: max Color: Black Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Polyester Occasion: Casual W... |
| 15   | no  | 15869842   | -     | 0.296 | Product: New Balance Women Charcoal Grey Drop-Shoulder Sleeves Solid Hooded Sweatshirt Brand: New Balance Color: Charcoal Category: Pullover Pattern: Solid Neck: Hood Sleeves: L... |
| 16   | no  | 13185846   | -     | 0.287 | Product: OFF LIMITS Women Grey Melange Solid Hooded Sweatshirt Brand: OFF LIMITS Color: Grey Melange Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: R... |
| 17   | no  | 16499970   | -     | 0.273 | Product: Puma Women Blue Hooded Sweatshirt Brand: Puma Color: Blue Category: Pullover Pattern: Brand logo solid Neck: Hood Sleeves: Long sleeves Length: Regular Hemline: Ribbed ... |
| 18   | no  | 15633514   | -     | 0.264 | Product: URBANIC Women Khaki Cold-Shoulder Longline Pullover Brand: URBANIC Color: Khaki Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Longlin... |
| 19   | no  | 6726577    | -     | 0.240 | Product: Mast & Harbour Women Black Solid Pullover Brand: Mast & Harbour Color: Black Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Hemline: Ribbed To... |
| 20   | no  | 15007890   | -     | 0.230 | Product: Hubberholme Women Navy Blue Solid Cropped Sweatshirt Brand: Hubberholme Color: Navy Blue Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length... |
| 21   | no  | 15844902   | -     | 0.226 | Product: URBANIC Women Grey Ripped Longline Pullover Sweater Brand: URBANIC Color: Grey Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Longline... |
| 22   | no  | 17155514   | -     | 0.226 | Product: H&M Women Grey Solid Long Sweatshirt Brand: H&M Color: Grey Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: Ribbed Top... |
| 23   | no  | 16596744   | -     | 0.224 | Product: max Women Black Sporty Jacket Brand: max Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Polyest... |
| 24   | no  | 14432282   | -     | 0.222 | Product: max White Regular Top Brand: max Color: White Category: Regular Pattern: Solid Neck: Shoulder straps Sleeves: Sleeveless shoulder straps Length: Regular Top fabric: Pur... |
| 25   | no  | 18743524   | -     | 0.220 | Product: max Off-White Self Design Ruffles Puff Sleeves Monochrome Top Brand: max Color: Off White Category: Regular Pattern: Self design Neck: Round neck Sleeves: Short puff sl... |
| 26   | no  | 19195576   | -     | 0.218 | Product: max Black Lace Top Brand: max Color: Black Category: Regular Pattern: Solid Neck: Round neck Sleeves: Long puff sleeves Length: Regular Top fabric: Polyester Occasion: ... |
| 27   | no  | 15596280   | -     | 0.216 | Product: PUMA Women Black & Yellow Colourblocked Loose Fit Hoodie Brand: Puma Color: Black Category: Pullover Pattern: Colourblocked Neck: Hood Sleeves: Long sleeves Length: Reg... |
| 28   | no  | 17686848   | -     | 0.214 | Product: FOREVER 21 Women Brown Solid Cold Shoulder Pullover Brand: FOREVER 21 Color: Brown Category: Pullover Pattern: Solid Neck: Mock collar Sleeves: Long sleeves Length: Reg... |
| 29   | no  | 17570152   | -     | 0.205 | Product: max Purple Solid Regular Top Brand: max Color: Purple Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short regular sleeves Length: Regular Top fabric: Cotto... |
| 30   | no  | 19176852   | -     | 0.204 | Product: H&M Men Grey Crew-Neck Sweatshirt Brand: H&M Color: Grey Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length: Regular Hemline: ... |

### Question 45/50

**Query:** What do you have from Roadster in products and color Navy Blue?

**Relevant docs:** `['12278640', '11987092', '8803831', '8963467', '12278652', '14094106', '16187090', '15897498']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.233     | 0.875  | 1.000 | 0.749 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 15897498   | -     | 1.000 | Product: The Roadster Lifestyle Co Women Navy Blue Cotton Wide Leg High-Rise Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: ... |
| 2    | no  | 14331672   | -     | 0.945 | Product: Roadster Women Navy Blue & Pink Striped Pullover Brand: Roadster Color: Navy Blue Category: Pullover Pattern: Striped Neck: Turtle neck Sleeves: Long sleeves Length: Re... |
| 3    | yes | 16187090   | -     | 0.945 | Product: The Roadster Lifestyle Co Women Navy Blue Straight Fit High-Rise Light Fade Cotton Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: C... |
| 4    | yes | 14094106   | -     | 0.943 | Product: Roadster Women Deep Navy Blue High-Rise Regular Fit Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 4 Wa... |
| 5    | no  | 13334168   | -     | 0.895 | Product: The Roadster Lifestyle Co Blue Solid Pure Cotton Top Brand: Roadster Color: Blue Category: Regular Pattern: Solid Neck: Scoop neck Sleeves: Short cap sleeves Length: Re... |
| 6    | no  | 17074032   | -     | 0.838 | Product: Roadster Women Navy Blue & White Striped High Neck Regular Top Brand: Roadster Color: Navy Blue Category: Regular Pattern: Horizontal stripes striped Neck: High neck Sl... |
| 7    | no  | 5447351    | -     | 0.814 | Product: Roadster Women Navy Blue Striped Cardigan Brand: Roadster Color: Navy Blue Category: Cardigan Pattern: Striped Neck: Round neck Sleeves: Long sleeves Hemline: Ribbed To... |
| 8    | yes | 12278652   | -     | 0.800 | Product: Roadster Women Navy Blue Bootcut Mid-Rise Clean Look Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 W... |
| 9    | no  | 11296068   | -     | 0.780 | Product: Roadster Women Navy Blue Solid Bell Sleeves Top Brand: Roadster Color: Navy Blue Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short bell sleeves Length: R... |
| 10   | no  | 14356168   | -     | 0.772 | Product: Roadster Women Navy Blue & Maroon Colourblocked Padded Jacket Brand: Roadster Color: Navy Blue Category: Padded jacket Pattern: Colourblocked Sleeves: Long sleeves Leng... |
| 11   | yes | 12278640   | -     | 0.744 | Product: Roadster Women Navy Blue Flared Fit High-Rise Clean Look Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets:... |
| 12   | no  | 14356146   | -     | 0.727 | Product: Roadster Women Navy Blue Convertible Tailored Jacket Brand: Roadster Color: Navy Blue Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hem... |
| 13   | no  | 14535784   | -     | 0.701 | Product: Roadster Women Deep Navy Blue Solid Denim Trucker Jacket Brand: Roadster Color: Navy Blue Category: Denim jacket Pattern: Solid Sleeves: Long sleeves Length: Regular He... |
| 14   | no  | 13700180   | -     | 0.664 | Product: Roadster Women Navy Blue Solid Straight Fit Skirt Brand: Roadster Color: Navy Blue Category: Straight Pattern: Solid Length: Knee length Hemline: Straight Top fabric: P... |
| 15   | no  | 11542060   | -     | 0.618 | Product: Roadster Women Blue Regular Fit Mid-Rise Clean Look Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 4 Wash care: Machine ... |
| 16   | no  | 14925764   | -     | 0.600 | Product: Roadster Women Navy Blue Pure Cotton Jogger Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 2 Wash care:... |
| 17   | no  | 14954422   | -     | 0.574 | Product: Roadster Women Blue Solid Light Fade Stretchable Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 4 Wash care: Machine wash   |
| 18   | no  | 14356150   | -     | 0.570 | Product: Roadster Women Navy Blue Grey Striped Bomber Jacket Brand: Roadster Color: Navy Blue Category: Bomber Pattern: Striped Sleeves: Long sleeves Length: Regular Hemline: St... |
| 19   | no  | 16835136   | -     | 0.560 | Product: Roadster Women Indigo Wide Leg Light Fade Stretchable Casual Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Organic cotton Occasion: Casual Pockets: 5 Wa... |
| 20   | yes | 8963467    | -     | 0.554 | Product: The Roadster Lifestyle Co Women Navy Blue Skinny Fit Mid-Rise Mildly Distressed Stretchable Cropped Jeans Brand: Roadster Color: Navy Blue Length: Cropped Top fabric: C... |
| 21   | no  | 15773298   | -     | 0.535 | Product: Roadster Women Blue Flared Mildly Distressed Light Fade Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Mach... |
| 22   | no  | 13756834   | -     | 0.534 | Product: Roadster Women Blue Dropped Yoke Slim Fit Mid-Rise Light Fade Acid Wash Jeans With A Belt Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casua... |
| 23   | no  | 16835218   | -     | 0.492 | Product: Roadster Women Blue Straight Fit High-Rise Light Fade Stretchable Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Organic cotton Occasion: Casual Pockets:... |
| 24   | no  | 14094050   | -     | 0.476 | Product: Roadster Women Deep Navy Blue High-Rise Straight Cropped Stretchable Jeans Brand: Roadster Color: Navy Blue Length: Cropped Top fabric: Cotton Occasion: Casual Pockets:... |
| 25   | no  | 11688534   | -     | 0.475 | Product: Roadster Women Blue Skinny Fit Mid-Rise Clean Look Stretchable Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash car... |
| 26   | yes | 8803831    | -     | 0.470 | Product: Roadster Women Navy Blue Skinny Fit Mid-Rise Clean Look Stretchable Cropped Jeans Brand: Roadster Color: Navy Blue Length: Cropped Top fabric: Cotton Occasion: Casual P... |
| 27   | no  | 13756932   | -     | 0.468 | Product: Roadster Women Blue Dropped Yoke Slim Fit Mid-Rise Clean Look Jeans With A Belt Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets:... |
| 28   | no  | 15773232   | -     | 0.465 | Product: Roadster Women Blue Flared Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Machine wash                         |
| 29   | no  | 14535816   | -     | 0.447 | Product: Roadster Women Pure Cotton Navy Blue Denim Jacket Brand: Roadster Color: Navy Blue Category: Denim jacket Pattern: Geometric self design Sleeves: Long sleeves Length: R... |
| 30   | no  | 14925804   | -     | 0.446 | Product: Roadster Women Blue Slim Fit Light Fade Stretchable Jeans with Belt Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care... |

### Question 46/50

**Query:** Show me Orange Saree from KALINI.

**Relevant docs:** `['14490860']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 0.500 | 0.631 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 14541316   | -     | 1.000 | Product: KALINI Orange & Gold-Toned Ethnic Motifs Art Silk Saree Brand: KALINI Color: Orange Category: Saree Pattern: Ethnic motifs woven design Occasion: Festive Wash care: Han... |
| 2    | yes | 14490860   | -     | 0.828 | Product: KALINI Orange & Gold-Toned Pure Chiffon Saree Brand: KALINI Color: Orange Category: Saree Pattern: Solid Occasion: Daily Wash care: Hand wash                               |
| 3    | no  | 18390376   | -     | 0.503 | Product: KALINI Women Orange Printed Pure Cotton Kurta with Trouser & With Dupatta Brand: KALINI Color: Orange Category: Kurta set Top type: Kurta Bottom type: Trousers Dupatta:... |
| 4    | no  | 14986192   | -     | 0.471 | Product: KALINI Blue & Yellow Floral Saree Brand: KALINI Color: Blue Category: Saree Pattern: Floral printed Occasion: Traditional Wash care: Dry clean                              |
| 5    | no  | 16915002   | -     | 0.451 | Product: KALINI Women Green & Pink Ethnic Motifs Art Silk Saree Brand: KALINI Color: Green Category: Saree Pattern: Ethnic motifs printed Occasion: Traditional Wash care: Hand wash |
| 6    | no  | 16848432   | -     | 0.446 | Product: KALINI Maroon & Gold-Toned Ethnic Motifs Foil Printed Zari Saree Brand: KALINI Color: Maroon Category: Saree Pattern: Ethnic motifs printed Occasion: Festive Wash care:... |
| 7    | no  | 17066888   | -     | 0.446 | Product: KALINI Brown & Orange Abstract Printed Pure Georgette Saree Brand: KALINI Color: Brown Category: Saree Pattern: Abstract printed Occasion: Daily Wash care: Hand wash       |
| 8    | no  | 16421936   | -     | 0.440 | Product: KALINI Pink & Gold-Toned Paisley Saree Brand: KALINI Color: Pink Category: Saree Pattern: Paisley printed Occasion: Festive Wash care: Dry clean                            |
| 9    | no  | 18435860   | -     | 0.422 | Product: KALINI Red & Gold-Toned Embellished Saree Brand: KALINI Color: Red Category: Saree Pattern: Embellished Occasion: Festive Wash care: Hand wash                              |
| 10   | no  | 17035752   | -     | 0.411 | Product: KALINI Coral & Golden Woven Design Saree Brand: KALINI Color: Coral Category: Saree Pattern: Solid Occasion: Party Wash care: Dry clean                                     |
| 11   | no  | 19167336   | -     | 0.408 | Product: KALINI womens Yellow & Orange Dyed Cotton Silk Dupatta with Zari Brand: KALINI Color: Yellow Pattern: Striped dyed Top fabric: Cotton silk Occasion: Party Wash care: Ha... |
| 12   | no  | 15102284   | -     | 0.396 | Product: KALINI Green & Pink Ethnic Motifs Art Silk Saree Brand: KALINI Color: Green Category: Saree Pattern: Ethnic motifs printed Occasion: Festive Wash care: Hand wash           |
| 13   | no  | 16989798   | -     | 0.386 | Product: KALINI Sea Green & Pink Ethnic Motifs Saree Brand: KALINI Color: Sea Green Category: Saree Pattern: Ethnic motifs printed Occasion: Daily Wash care: Dry clean              |
| 14   | no  | 17810904   | -     | 0.385 | Product: KALINI Cream-Coloured & Gold-Toned Striped Cotton Silk Saree Brand: KALINI Color: Cream Category: Saree Pattern: Striped Occasion: Festive Wash care: Dry clean             |
| 15   | no  | 15102290   | -     | 0.371 | Product: KALINI Pink & Gold-Toned Woven Design Zari Art Silk Saree Brand: KALINI Color: Pink Category: Saree Pattern: Woven design Occasion: Traditional Wash care: Hand wash        |
| 16   | no  | 17852902   | -     | 0.363 | Product: KALINI Pink & Gold-Toned Zari Saree Brand: KALINI Color: Pink Category: Saree Pattern: Solid Occasion: Festive Wash care: Hand wash                                         |
| 17   | no  | 17584716   | -     | 0.361 | Product: KALINI Purple & Orange Floral Bagh Saree Brand: KALINI Color: Purple Category: Bagh Pattern: Floral printed Occasion: Traditional Wash care: Hand wash                      |
| 18   | no  | 14679542   | -     | 0.361 | Product: KALINI Off White & Purple Art Silk Ikat Saree Brand: KALINI Color: Off White Category: Ikat Pattern: Abstract printed Occasion: Daily Wash care: Hand wash                  |
| 19   | no  | 16915122   | -     | 0.358 | Product: KALINI Green & White Bandhani Art Silk Saree Brand: KALINI Color: Green Category: Bandhani Pattern: Bandhani printed Occasion: Traditional Wash care: Hand wash             |
| 20   | no  | 14798392   | -     | 0.356 | Product: KALINI Pink & Green Ethnic Motifs Kota Saree Brand: KALINI Color: Pink Category: Kota Pattern: Ethnic motifs printed Occasion: Traditional Wash care: Hand wash             |
| 21   | no  | 16697004   | -     | 0.346 | Product: KALINI Green & Gold-Toned Woven Design Silk Blend Banarasi Saree Brand: KALINI Color: Green Category: Banarasi Pattern: Woven design Occasion: Traditional Wash care: Dr... |
| 22   | no  | 14678908   | -     | 0.334 | Product: KALINI Pink & Yellow Floral Pure Chiffon Saree Brand: KALINI Color: Pink Category: Saree Pattern: Floral printed Occasion: Festive Wash care: Hand wash                     |
| 23   | no  | 16697006   | -     | 0.328 | Product: KALINI Maroon & Gold Ethnic Motifs Zari Silk Blend Banarasi Saree Brand: KALINI Color: Maroon Category: Banarasi Pattern: Ethnic motifs woven design Occasion: Tradition... |
| 24   | no  | 17035744   | -     | 0.314 | Product: KALINI Black & Golden Woven Design Saree Brand: KALINI Color: Black Category: Saree Pattern: Geometric woven design Occasion: Festive Wash care: Dry clean                  |
| 25   | no  | 17118876   | -     | 0.312 | Product: KALINI Blue & Pink Checked Ikat Saree Brand: KALINI Color: Blue Category: Ikat Pattern: Checked Occasion: Traditional Wash care: Machine wash                               |
| 26   | no  | 15530056   | -     | 0.308 | Product: KALINI Green & White Leheriya Saree Brand: KALINI Color: Green Category: Leheriya Pattern: Leheriya printed Occasion: Traditional Wash care: Dry clean                      |
| 27   | no  | 18907070   | -     | 0.307 | Product: KALINI Women Red & Green Floral Embroidered Silk Cotton Jamdani Saree Brand: KALINI Color: Red Category: Jamdani Pattern: Floral embroidered Occasion: Traditional Wash ... |
| 28   | no  | 15258754   | -     | 0.307 | Product: KALINI Purple & Grey Ethnic Motifs Art Silk Khadi Saree Brand: KALINI Color: Purple Category: Khadi Pattern: Ethnic motifs printed Occasion: Traditional Wash care: Mach... |
| 29   | no  | 18265998   | -     | 0.297 | Product: KALINI Teal Green & Gold-Toned Striped Zari Silk Cotton Fusion Saree Brand: KALINI Color: Teal Category: Saree Pattern: Striped Occasion: Festive Wash care: Machine wash   |
| 30   | no  | 12754022   | -     | 0.289 | Product: KALINI Black & Red Jute Silk Embroidered Saree Brand: KALINI Color: Black Category: Saree Pattern: Embellished embroidered Occasion: Festive Wash care: Hand wash           |

### Question 47/50

**Query:** Do you have any Black Tailored jacket for sports?

**Relevant docs:** `['14646546']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 0.750             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 14646546   | -     | 1.000 | Product: HRX By Hrithik Roshan Outdoor Women Winter Moss Rapid-Dry Colourblock Jackets Brand: HRX by Hrithik Roshan Color: Black Category: Tailored jacket Pattern: Colourblocked... |
| 2    | no  | 15789142   | -     | 0.942 | Product: Slazenger Women Black Running Sporty Rapid-Dry Jacket Brand: Slazenger Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline... |
| 3    | no  | 17069364   | -     | 0.929 | Product: Jockey Women Black Solid Hooded Sporty Jacket Brand: Jockey Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight ... |
| 4    | no  | 15789256   | -     | 0.876 | Product: Slazenger Women Grey Brand Logo Running Tailored Rapid-Dry Jacket Brand: Slazenger Color: Grey Category: Tailored jacket Pattern: Brand logo solid Sleeves: Long sleeves... |
| 5    | no  | 18522690   | -     | 0.773 | Product: H&M Women Black & White Baseball-Style Shacket Brand: H&M Color: Black Category: Tailored jacket Pattern: Graphic printed Sleeves: Short sleeves Length: Regular Hemline... |
| 6    | no  | 14957090   | -     | 0.717 | Product: Zastraa Women Black Lightweight Tailored Jacket Brand: Zastraa Color: Black Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Curv... |
| 7    | no  | 15634138   | -     | 0.715 | Product: URBANIC Women Black Tailored Jacket Brand: URBANIC Color: Black Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fab... |
| 8    | no  | 13609880   | -     | 0.709 | Product: HRX by Hrithik Roshan Men Jet Black Solid Packable Rapid-Dry Hooded Running Jacket Brand: HRX by Hrithik Roshan Color: Black Category: Sporty jacket Pattern: Solid Slee... |
| 9    | no  | 18282028   | -     | 0.705 | Product: CL SPORT Women Black Reversible Longline Sporty Jacket Brand: CL SPORT Color: Black Category: Sporty jacket Pattern: Checked printed Sleeves: Sleeveless Length: Longlin... |
| 10   | no  | 16191476   | -     | 0.688 | Product: H&M Woman Black Faux-fur-trimmed jacket Brand: H&M Color: Black Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fab... |
| 11   | no  | 15743742   | -     | 0.680 | Product: ADIDAS Women Black Solid Essential Insulated Vest Sporty Jacket Brand: ADIDAS Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Sleeveless Length: Regular He... |
| 12   | no  | 11383846   | -     | 0.676 | Product: Alcis Nari Women Black Solid Lightweight Sporty Jacket Brand: Alcis Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: S... |
| 13   | no  | 17069368   | -     | 0.665 | Product: Jockey Women Navy Blue Longline Tailored Jacket Brand: Jockey Color: Navy Blue Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Longline Hemline: ... |
| 14   | no  | 15389978   | -     | 0.636 | Product: PERFKT-U Women Black & Mustard Yellow Colourblocked Lightweight Sporty Jacket Brand: PERFKT-U Color: Black Category: Sporty jacket Pattern: Colourblocked Sleeves: Long ... |
| 15   | no  | 18144568   | -     | 0.609 | Product: Marks & Spencer Women Black Padded Jacket Brand: Marks & Spencer Color: Black Category: Padded jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Stra... |
| 16   | no  | 17069340   | -     | 0.609 | Product: Jockey Women Purple Tailored Jacket Brand: Jockey Color: Purple Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Curved Top fabri... |
| 17   | no  | 12918452   | -     | 0.568 | Product: AGIL ATHLETICA Women Black Solid Sporty Jacket Brand: AGIL ATHLETICA Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: ... |
| 18   | no  | 17491608   | -     | 0.560 | Product: Silvertraq Women Black Camouflage Printed Longline Sporty Jacket Brand: Silvertraq Color: Black Category: Sporty jacket Pattern: Camouflage printed Sleeves: Long sleeve... |
| 19   | no  | 15684018   | -     | 0.557 | Product: Puma x FIRST MILE Women Purple & White Woven Training Relaxed Jacket Brand: Puma Color: Purple Category: Tailored jacket Pattern: Colourblocked Sleeves: Long sleeves Le... |
| 20   | no  | 15730230   | -     | 0.544 | Product: AGIL ATHLETICA Women Navy Blue & Red Colourblocked Tailored Jacket Brand: AGIL ATHLETICA Color: Navy Blue Category: Tailored jacket Pattern: Colourblocked solid Sleeves... |
| 21   | no  | 16100814   | -     | 0.532 | Product: Reich Color Women Black Fleece Lightweight Longline Tailored Jacket with Embroidered Brand: Reich Color Color: Black Category: Tailored jacket Pattern: Solid Sleeves: T... |
| 22   | no  | 15869352   | -     | 0.527 | Product: New Balance Women Black Brand Logo Print Detail Sporty Jacket Brand: New Balance Color: Black Category: Sporty jacket Pattern: Brand logo solid Sleeves: Long sleeves Le... |
| 23   | no  | 19267030   | -     | 0.525 | Product: H&M Women Black Short Jacket Brand: H&M Color: Black Category: Tailored jacket Pattern: Abstract solid Sleeves: Three-quarter sleeves Length: Regular Hemline: Straight ... |
| 24   | no  | 15849954   | -     | 0.517 | Product: URBANIC Women Black & White Houndstooth Pattern Tailored Jacket Brand: URBANIC Color: Black Category: Tailored jacket Pattern: Houndstooth checked Sleeves: Long sleeves... |
| 25   | no  | 15953824   | -     | 0.504 | Product: Columbia Women Black Joy Peak Mid Hooded Reflective Stripe Padded Jacket Brand: Columbia Color: Black Category: Padded jacket Pattern: Solid Sleeves: Long sleeves Lengt... |
| 26   | no  | 17391422   | -     | 0.497 | Product: Fabindia Women Black Woolen Tailored Jacket Brand: Fabindia Color: Black Category: Tailored jacket Pattern: Solid printed Sleeves: Long sleeves Length: Regular Hemline:... |
| 27   | no  | 15836646   | -     | 0.493 | Product: Puma Women Black White Brand Logo Sporty Jacket Brand: Puma Color: Black Category: Sporty jacket Pattern: Brand logo printed Sleeves: Long sleeves Length: Regular Hemli... |
| 28   | no  | 1052282    | -     | 0.472 | Product: SASSAFRAS Black Embellished Slim Fit Jacket Brand: SASSAFRAS Color: Black Category: Tailored jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straig... |
| 29   | no  | 16596744   | -     | 0.457 | Product: max Women Black Sporty Jacket Brand: max Color: Black Category: Sporty jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight Top fabric: Polyest... |
| 30   | no  | 11862698   | -     | 0.442 | Product: Jockey Women Charcoal Grey Melange Effect Sporty Jacket Brand: Jockey Color: Charcoal Category: Sporty jacket Pattern: Self design Sleeves: Long sleeves Length: Regular... |

### Question 48/50

**Query:** Do you have anything from Roadster in Grey for everyday wear?

**Relevant docs:** `['13756948', '8319213', '13339544', '14954872', '10388213', '16835166', '16835204', '16835178']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.267     | 1.000  | 1.000 | 0.917 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 16835166   | -     | 1.000 | Product: The Roadster Lifestyle Co Women Grey Wide Leg Stretchable Jeans Brand: Roadster Color: Grey Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: Ma... |
| 2    | yes | 16835204   | -     | 0.972 | Product: Roadster Women Grey Slim Flared High-Rise Heavy Fade Stretchable Jeans Brand: Roadster Color: Grey Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 3    | yes | 16835178   | -     | 0.938 | Product: Roadster Women Grey Slim Flared High-Rise Heavy Fade Stretchable Jeans Brand: Roadster Color: Grey Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 4    | no  | 14536020   | -     | 0.917 | Product: Roadster Woman Beautiful Grey Solid Denim Trucker Jacket Brand: Roadster Color: Grey Category: Denim jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline... |
| 5    | yes | 13339544   | -     | 0.898 | Product: The Roadster Lifestyle Co Women Grey Slim Fit Mid-Rise Clean Look Stretchable Jeans Brand: Roadster Color: Grey Length: Cropped Top fabric: Cotton Occasion: Casual Pock... |
| 6    | no  | 14954602   | -     | 0.863 | Product: Roadster Women Alluring Grey High-Rise Boyfriend Fit Stretchable Jeans Brand: Roadster Color: Grey Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 7    | no  | 14535994   | -     | 0.858 | Product: Roadster Women Grey Solid Denim Trucker Jacket Brand: Roadster Color: Grey Category: Denim jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight... |
| 8    | no  | 15441284   | -     | 0.750 | Product: The Roadster Lifestyle Co Women Grey Straight Fit High-Rise Cargos Trousers Brand: Roadster Color: Grey Category: Cargos Pattern: Solid Length: Regular Top fabric: Cott... |
| 9    | yes | 13756948   | -     | 0.722 | Product: Roadster Women Alluring Grey Mid-Rise Boyfriend Fit Stretchable Jeans Brand: Roadster Color: Grey Length: Cropped Top fabric: Cotton Occasion: Casual Wash care: Machine... |
| 10   | yes | 14954872   | -     | 0.715 | Product: Roadster Women Grey Slouchy Fit Mid-Rise Acid Wash Stretchable Jeans Brand: Roadster Color: Grey Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash car... |
| 11   | no  | 14535748   | -     | 0.678 | Product: Roadster Women Alluring Grey Washed Denim Trucker Jacket Brand: Roadster Color: Grey Category: Denim jacket Pattern: Washed solid Sleeves: Long sleeves Length: Regular ... |
| 12   | no  | 11672562   | -     | 0.626 | Product: Roadster Women Grey Regular Fit Solid Cropped Joggers Brand: Roadster Color: Grey Category: Joggers Pattern: Solid Length: Cropped Top fabric: Cotton Occasion: Casual P... |
| 13   | yes | 8319213    | -     | 0.609 | Product: Roadster Women Grey Skinny Fit Mid-Rise Clean Look Stretchable Cropped Jeans Brand: Roadster Color: Grey Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 ... |
| 14   | yes | 10388213   | -     | 0.587 | Product: Roadster Women Grey Skinny Fit Mid-Rise Low Distress Stretchable Jeans Brand: Roadster Color: Grey Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 5 Wash c... |
| 15   | no  | 11990670   | -     | 0.477 | Product: Roadster Women Grey & Green Colourblocked Bomber Brand: Roadster Color: Grey Category: Bomber Pattern: Graphic colourblocked Sleeves: Long sleeves Length: Regular Hemli... |
| 16   | no  | 14535802   | -     | 0.463 | Product: Roadster Women Beautiful Grey Self-Design Bomber Jacket Brand: Roadster Color: Grey Category: Bomber Pattern: Self design Sleeves: Long sleeves Length: Regular Hemline:... |
| 17   | no  | 11697384   | -     | 0.429 | Product: Roadster Black Round Neck Pure Cotton Top Brand: Roadster Color: Black Category: Regular Pattern: Solid Neck: Round neck Sleeves: Short extended sleeves Length: Regular... |
| 18   | no  | 14356152   | -     | 0.421 | Product: Roadster Women Grey & White Faux Fur Bomber Jacket Brand: Roadster Color: Grey Category: Bomber Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight T... |
| 19   | no  | 15773476   | -     | 0.384 | Product: The Roadster Lifestyle Co. Women Black Light Fade Flared Stretchable Jeans Brand: Roadster Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 W... |
| 20   | no  | 14954702   | -     | 0.356 | Product: Roadster Women Black Boyfriend Fit Light Fade Stretchable Jeans Brand: Roadster Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash care: M... |
| 21   | no  | 14536056   | -     | 0.323 | Product: Roadster Women Charcoal Grey Pure Cotton Hooded Denim Jacket Brand: Roadster Color: Charcoal Category: Denim jacket Pattern: Solid Sleeves: Long sleeves Length: Regular... |
| 22   | no  | 14954642   | -     | 0.293 | Product: Roadster Women Black Boyfriend Fit Mid Rise Clean Look Stretchable Jeans Brand: Roadster Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 3 Was... |
| 23   | no  | 14356304   | -     | 0.291 | Product: Roadster Women Charcoal Grey Solid Corduroy Tailored Jacket Brand: Roadster Color: Charcoal Category: Tailored jacket Pattern: Solid Sleeves: Short sleeves Length: Regu... |
| 24   | no  | 14954422   | -     | 0.276 | Product: Roadster Women Blue Solid Light Fade Stretchable Jeans Brand: Roadster Color: Blue Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 4 Wash care: Machine wash   |
| 25   | no  | 13334168   | -     | 0.265 | Product: The Roadster Lifestyle Co Blue Solid Pure Cotton Top Brand: Roadster Color: Blue Category: Regular Pattern: Solid Neck: Scoop neck Sleeves: Short cap sleeves Length: Re... |
| 26   | no  | 13346740   | -     | 0.260 | Product: The Roadster Lifestyle Co Women Black Regular Fit Solid Cargos with D-Ring at Hem Brand: Roadster Color: Black Category: Cargos Pattern: Solid Length: Regular Top fabri... |
| 27   | no  | 14954878   | -     | 0.258 | Product: Roadster Women Charcoal Mid-Rise Straight Fit Jeans Brand: Roadster Color: Charcoal Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 6 and more Wash care: M... |
| 28   | no  | 14535904   | -     | 0.255 | Product: Roadster Women Stylish Black Solid Denim Trucker Jacket Brand: Roadster Color: Black Category: Denim jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline... |
| 29   | no  | 17005816   | -     | 0.250 | Product: Roadster Women Charcoal Grey Pure Cotton Mid rise Slouchy Jogger Jeans Brand: Roadster Color: Charcoal Length: Cropped Top fabric: Cotton Occasion: Casual Pockets: 2 Wa... |
| 30   | no  | 4451422    | -     | 0.246 | Product: Roadster Women Black Regular Fit Mid-Rise Clean Look Stretchable Jeans Brand: Roadster Color: Black Length: Regular Top fabric: Cotton Occasion: Casual Pockets: 5 Wash ... |

### Question 49/50

**Query:** I need Peplum with a Self design solid pattern in Blue.

**Relevant docs:** `['16504028']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 0.111 | 0.301 | 0.500             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | no  | 16931960   | -     | 1.000 | Product: all about you Teal Blue Self Design Keyhole Neck Peplum Top Brand: all about you Color: Teal Category: Peplum Pattern: Self design Neck: Keyhole neck Sleeves: Three-qua... |
| 2    | no  | 18514120   | -     | 0.976 | Product: Paralians Turquoise Blue Peplum Top Brand: Paralians Color: Turquoise Blue Category: Peplum Pattern: Ethnic motifs solid Neck: Round neck Sleeves: Three-quarter regular... |
| 3    | no  | 14641744   | -     | 0.962 | Product: FabAlley Blue Puff Sleeve Chambray Peplum Top Brand: FabAlley Color: Blue Category: Peplum Pattern: Solid Neck: Round neck Sleeves: Short puff sleeves Length: Regular T... |
| 4    | no  | 11607414   | -     | 0.917 | Product: Bhama Couture Women Blue Printed Peplum Top Brand: Bhama Couture Color: Blue Category: Peplum Pattern: Abstract printed Neck: Round neck Sleeves: Short no sleeves Lengt... |
| 5    | no  | 11607374   | -     | 0.863 | Product: Bhama Couture Women Blue Printed Peplum Top Brand: Bhama Couture Color: Blue Category: Peplum Pattern: Floral printed Neck: V-neck Sleeves: Three-quarter regular sleeve... |
| 6    | no  | 18805426   | -     | 0.728 | Product: BoStreet Blue Checked Peplum Top Brand: BoStreet Color: Blue Category: Peplum Pattern: Checked Neck: Round neck Sleeves: Short regular sleeves Length: Regular Top fabri... |
| 7    | no  | 17627582   | -     | 0.680 | Product: kipek Women Deep Navy Blue Solid Top with Palazzos Brand: kipek Color: Navy Blue Category: Top Top type: Top Bottom type: Palazzos Pattern: Solid Neck: Shoulder straps ... |
| 8    | no  | 15766290   | -     | 0.668 | Product: Pepe Jeans Women Blue Pure Cotton Trousers Brand: Pepe Jeans Color: Blue Category: Regular trousers Pattern: Solid Length: Regular Top fabric: Cotton Occasion: Casual P... |
| 9    | yes | 16504028   | -     | 0.665 | Product: ANVI Be Yourself Women Stunning Blue Self-Design Ruffled Skirt Brand: ANVI Be Yourself Color: Blue Category: Peplum Pattern: Self design solid Length: Mini Hemline: Asy... |
| 10   | no  | 4374524    | -     | 0.660 | Product: RARE Women Green Self Design Peplum Top Brand: RARE Color: Green Category: Peplum Pattern: Self design Neck: Mandarin collar Sleeves: Sleeveless no Length: Regular Top ... |
| 11   | no  | 5617740    | -     | 0.640 | Product: plusS Sea Green Self Design Peplum Top Brand: plusS Color: Sea Green Category: Peplum Pattern: Self design Neck: Tie-up neck Sleeves: Three-quarter bell sleeves Length:... |
| 12   | no  | 17445656   | -     | 0.599 | Product: Vishudh Blue Floral Print Peplum Top Brand: Vishudh Color: Blue Category: Peplum Pattern: Floral printed Neck: Round neck Sleeves: Three-quarter regular sleeves Length:... |
| 13   | no  | 10783322   | -     | 0.582 | Product: Sera Women Navy Blue Printed Peplum Pure Cotton Top Brand: Sera Color: Navy Blue Category: Peplum Pattern: Floral printed Neck: Round neck Sleeves: Sleeveless no Length... |
| 14   | no  | 8715089    | -     | 0.501 | Product: plusS Women Blue Printed Peplum Top Brand: plusS Color: Blue Category: Peplum Pattern: Floral printed Neck: V-neck Sleeves: Three-quarter regular sleeves Length: Regula... |
| 15   | no  | 16935640   | -     | 0.495 | Product: flaher Women Blue Solid Art Silk Padded Blouse Brand: flaher Color: Blue Pattern: Solid Neck: Halter neck Sleeves: Sleeveless Top fabric: Dupion Occasion: Festive          |
| 16   | no  | 14658916   | -     | 0.472 | Product: Pepe Jeans Women Blue Washed Mid-Rise Regular Shorts Brand: Pepe Jeans Color: Blue Category: Regular shorts Pattern: Solid washed Length: Above knee Top fabric: Cotton ... |
| 17   | no  | 13013166   | -     | 0.430 | Product: SALWAR STUDIO Women Orange Solid Peplum Top Brand: SALWAR STUDIO Color: Orange Category: Peplum Pattern: Solid Neck: Round neck Sleeves: Short raglan sleeves Length: Re... |
| 18   | no  | 17872080   | -     | 0.419 | Product: Taavi Women Indigo & White Indigo Print Pure Cotton Casual Peplum Top Brand: Taavi Color: Blue Category: Peplum Pattern: Ethnic motifs printed Neck: Round neck Sleeves:... |
| 19   | no  | 14867398   | -     | 0.416 | Product: Janasya Women Blue & White Floral Ruffles Peplum Top Brand: Janasya Color: Blue Category: Peplum Pattern: Floral printed Neck: Round neck Sleeves: Sleeveless no Length:... |
| 20   | no  | 17557370   | -     | 0.406 | Product: Pepe Jeans Women Navy Blue Printed Shorts Brand: Pepe Jeans Color: Navy Blue Category: Regular shorts Pattern: Graphic printed Length: Above knee Top fabric: Cotton Occ... |
| 21   | no  | 13382002   | -     | 0.386 | Product: plusS Women Black Self-Design Smocked Peplum Top Brand: plusS Color: Black Category: Peplum Pattern: Self design Neck: Square neck Sleeves: Three-quarter puff sleeves L... |
| 22   | no  | 14424654   | -     | 0.345 | Product: ROOTED Navy Blue Printed Peplum Top Brand: ROOTED Color: Navy Blue Category: Peplum Pattern: Abstract printed Neck: Round neck Sleeves: Long regular sleeves Length: Reg... |
| 23   | no  | 18604646   | -     | 0.340 | Product: Zink London Women Blue Floral Lace Design Skirts Brand: Zink London Color: Blue Category: A-line Pattern: Self design solid Length: Knee length Hemline: Straight Top fa... |
| 24   | no  | 12504862   | -     | 0.327 | Product: Pepe Jeans Women Teal & White Striped Round-Neck Pullover Sweater Brand: Pepe Jeans Color: Teal Category: Pullover Pattern: Striped Neck: Round neck Sleeves: Long sleev... |
| 25   | no  | 14602502   | -     | 0.324 | Product: Vishudh Black Geometric Mandarin Collar Peplum Top Brand: Vishudh Color: Black Category: Peplum Pattern: Geometric self design Neck: Mandarin collar Sleeves: Three-quar... |
| 26   | no  | 17566228   | -     | 0.305 | Product: Inddus Women Blue Woven Design Top & Solid Palazzos with Jacket Brand: Inddus Color: Blue Category: Top Top type: Top Bottom type: Palazzos Pattern: Self design Neck: V... |
| 27   | no  | 17132282   | -     | 0.300 | Product: Athena Women Pretty Pink Self-Design Schiffli Top Brand: Athena Color: Pink Category: Peplum Pattern: Self design Neck: Square neck Sleeves: Short puff sleeves Length: ... |
| 28   | no  | 10717820   | -     | 0.291 | Product: Bhama Couture Women Blue Embroidered Detail Chambray A-Line Pure Cotton Top Brand: Bhama Couture Color: Navy Blue Category: A-line Pattern: Solid Neck: Tie-up neck Slee... |
| 29   | no  | 10627950   | -     | 0.277 | Product: Magnetic Designs Women Blue Solid Basic Jumpsuit Brand: Magnetic Designs Color: Blue Category: Basic jumpsuit Pattern: Solid Neck: V-neck Sleeves: Sleeveless Top fabric... |
| 30   | no  | 14231406   | -     | 0.276 | Product: all about you Women Blue Self-Design Pullover Brand: all about you Color: Blue Category: Pullover Pattern: Geometric self design Neck: Turtle neck Sleeves: Long sleeves... |

### Question 50/50

**Query:** I need Peach Pullover by Madame.

**Relevant docs:** `['16533076']`

Metrics:

| precision | recall | mrr   | ndcg  | context_relevance |
| --------- | ------ | ----- | ----- | ----------------- |
| 0.033     | 1.000  | 1.000 | 1.000 | 1.000             |

Retrieved documents:

| rank | hit | section_id | title | score | preview                                                                                                                                                                              |
| ---- | --- | ---------- | ----- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | yes | 16533076   | -     | 1.000 | Product: Madame Women Peach-Coloured Self Designed Wool Pullover Brand: Madame Color: Peach Category: Pullover Pattern: Open knit self design Neck: Round neck Sleeves: Long slee... |
| 2    | no  | 18948340   | -     | 0.772 | Product: Madame Peach-Coloured Cuffed Sleeves Styled Back Crop Top Brand: Madame Color: Peach Category: Styled back Pattern: Solid Neck: High neck Sleeves: Long cuffed sleeves L... |
| 3    | no  | 14556346   | -     | 0.607 | Product: Madame Women White Solid Fuzzy Pullover Brand: Madame Color: White Category: Pullover Pattern: Solid Neck: V-neck Sleeves: Long sleeves Length: Regular Hemline: Straigh... |
| 4    | no  | 15756110   | -     | 0.590 | Product: Madame Women Pink Pullover Woolen Sweater Brand: Madame Color: Pink Category: Pullover Pattern: Solid Neck: V-neck Sleeves: Long sleeves Length: Regular Hemline: Ribbed... |
| 5    | no  | 16566862   | -     | 0.536 | Product: Madame Women Mauve Lightweight Puffer Jacket Brand: Madame Color: Mauve Category: Puffer jacket Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Curved Top... |
| 6    | no  | 16512732   | -     | 0.527 | Product: Madame Women Beige Self Design Pullover Sweater Brand: Madame Color: Beige Category: Pullover Pattern: Ribbed Neck: Round neck Sleeves: Long sleeves Length: Regular Hem... |
| 7    | no  | 15964118   | -     | 0.502 | Product: Madame Women Charcoal Front-Open Sweater Brand: Madame Color: Charcoal Category: Front-open Pattern: Solid Neck: Mock collar Sleeves: Long sleeves Length: Regular Hemli... |
| 8    | no  | 15997770   | -     | 0.468 | Product: Madame Women Yellow & White Checked Pullover Brand: Madame Color: Yellow Category: Pullover Pattern: Checked Neck: Round neck Sleeves: Long sleeves Length: Regular Heml... |
| 9    | no  | 16512720   | -     | 0.394 | Product: Madame Women Grey Solid Cardigan Sweater Brand: Madame Color: Grey Category: Cardigan Pattern: Solid Neck: Shawl collar Sleeves: Long sleeves Length: Regular Hemline: R... |
| 10   | no  | 10611424   | -     | 0.392 | Product: Alsace Lorraine Paris Women Peach-Coloured Solid Hooded Sweatshirt Brand: Alsace Lorraine Paris Color: Peach Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long ... |
| 11   | no  | 10611410   | -     | 0.374 | Product: Alsace Lorraine Paris Women Peach-Coloured Solid Sweatshirt Brand: Alsace Lorraine Paris Color: Peach Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long s... |
| 12   | no  | 18846880   | -     | 0.366 | Product: Madame Rust Orange Mandarin Collar Top Brand: Madame Color: Rust Category: Regular Pattern: Solid Neck: Mandarin collar Sleeves: Long cuffed sleeves Length: Regular Top... |
| 13   | no  | 10891532   | -     | 0.352 | Product: Alsace Lorraine Paris Women Peach-Coloured Solid Ruched Sweatshirt Brand: Alsace Lorraine Paris Color: Peach Category: Pullover Pattern: Solid Neck: Round neck Sleeves:... |
| 14   | no  | 15616452   | -     | 0.347 | Product: The Dry State Women Peach-Coloured Hooded Sweatshirt Brand: The Dry State Color: Peach Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: Regula... |
| 15   | no  | 18948328   | -     | 0.338 | Product: Madame Pink Solid Crop Top Brand: Madame Color: Pink Category: Regular Pattern: Solid Neck: V-neck Sleeves: Short flared sleeves Length: Crop Top fabric: Polyester Occa... |
| 16   | no  | 11991442   | -     | 0.328 | Product: Roadster Women Peach-Coloured Solid Oversized Hooded Sweatshirt Brand: Roadster Color: Peach Category: Pullover Pattern: Solid Neck: Hood Sleeves: Long sleeves Length: ... |
| 17   | no  | 19269812   | -     | 0.324 | Product: Madame Women Green Tie-Up Shrug Brand: Madame Color: Green Pattern: Solid Sleeves: Short sleeves Length: Regular Hemline: Dipped Top fabric: Polyester Occasion: Casual ... |
| 18   | no  | 15158394   | -     | 0.323 | Product: Roadster Women Peach-Coloured Drop-Shoulder Sleeves Solid Sweatshirt Brand: Roadster Color: Peach Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleev... |
| 19   | no  | 13534832   | -     | 0.301 | Product: MANGO Women Peach-Coloured Self-Design Pullover Brand: MANGO Color: Peach Category: Pullover Pattern: Cable knit self design Neck: Round neck Sleeves: Long sleeves Leng... |
| 20   | no  | 14231418   | -     | 0.294 | Product: all about you Women Peach-Coloured Open-Knit Pullover Brand: all about you Color: Peach Category: Pullover Pattern: Open knit self design Neck: Turtle neck Sleeves: Lon... |
| 21   | no  | 18846868   | -     | 0.280 | Product: Madame Black Studded Top Brand: Madame Color: Black Category: Regular Pattern: Solid Neck: Round neck Sleeves: Three-quarter flared sleeves Length: Regular Top fabric: ... |
| 22   | no  | 15963876   | -     | 0.268 | Product: MANGO Women Peach-Coloured Cable Knit Pullover Brand: MANGO Color: Peach Category: Pullover Pattern: Cable knit self design Neck: Round neck Sleeves: Long sleeves Lengt... |
| 23   | no  | 14516092   | -     | 0.253 | Product: Kook N Keech Marvel Women Peach-Coloured Sequinned Hooded Sweatshirt Brand: Kook N Keech Marvel Color: Peach Category: Pullover Pattern: Superhero embellished Neck: Hoo... |
| 24   | no  | 14312170   | -     | 0.250 | Product: Sztori Women Plus Size Peach-Coloured Sweatshirt Brand: Sztori Color: Peach Category: Pullover Pattern: Solid Neck: Round neck Sleeves: Long sleeves Length: Regular Hem... |
| 25   | no  | 15673658   | -     | 0.226 | Product: max Women Peach-Coloured Printed Sweatshirt Brand: max Color: Peach Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length: Regula... |
| 26   | no  | 16351896   | -     | 0.190 | Product: Missguided Women Peach-Coloured Solid Blazer Brand: Missguided Color: Peach Pattern: Solid Sleeves: Long sleeves Length: Regular Top fabric: Polyester Occasion: Casual ... |
| 27   | no  | 8027069    | -     | 0.186 | Product: Peppermint Girls Peach-Coloured Straight Solid Palazzos Brand: Peppermint Color: Peach Pattern: Solid Length: Regular Top fabric: Polyester Occasion: Western Wash care:... |
| 28   | no  | 16472932   | -     | 0.175 | Product: Juelle Women Peach-Coloured Corduroy Bomber Jacket Brand: Juelle Color: Peach Category: Bomber Pattern: Solid Sleeves: Long sleeves Length: Regular Hemline: Straight To... |
| 29   | no  | 14824280   | -     | 0.174 | Product: LilPicks Girls Peach-Coloured & Green Ready to Wear Lehenga & Blouse With Dupatta Brand: LilPicks Color: Peach Pattern: Solid Sleeves: Short no sleeves Hemline: Flared     |
| 30   | no  | 19204850   | -     | 0.173 | Product: max Women Peach-Coloured Printed Slip on Sweatshirt Brand: max Color: Peach Category: Pullover Pattern: Typography printed Neck: Round neck Sleeves: Long sleeves Length... |
