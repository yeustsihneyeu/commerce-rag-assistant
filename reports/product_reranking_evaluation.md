# FAQ Reranking Evaluation Report

Source notebook: `notebooks/product/07_product_reranking.ipynb`

## Overview

- Evaluated questions: 100
- Mean precision: 0.166 -> 0.187
- Mean recall: 0.646 -> 0.675
- Mean MRR: 0.605 -> 0.683
- Mean nDCG: 0.573 -> 0.646

## Summary Tables

### Final Metrics

| questions | precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 0.166 | 0.187 | 0.646 | 0.675 | 0.605 | 0.683 | 0.573 | 0.646 |

## Detailed Results

### Question 1

**Query:** Show me Regular trousers within a budget of 2000.

**Relevant docs:** ['17817750', '18770002', '18769968', '18769944', '18769702', '15026996', '15092120', '16814696']

**Retrieved docs:** ['16279046', '14220194', '13523706', '13647622', '13769372', '11421530', '17393956', '16044098', '18770032', '17378344']

**Reranked docs:** ['16279046', '19011990', '18867438', '18770032', '18769616', '18770054', '17046802', '17864146', '18838300', '17197754']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 2

**Query:** Can you find something similar to "Athena Women Burgundy Solid Tailored Suede Jacket"?

**Relevant docs:** ['11166548']

**Retrieved docs:** ['11166548', '16752820', '16154596', '16565622', '10856152', '16420446', '10758214', '12086086', '12402376', '11634534']

**Reranked docs:** ['11166548', '10758214', '11634534', '11634536', '12086086', '12402376', '7779375', '10856152', '14356158', '11151684']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 3

**Query:** Show me products like "InWeave Women Red Printed A-Line Skirt".

**Relevant docs:** ['18921114']

**Retrieved docs:** ['18921114', '17168254', '15322490', '15447990', '17168250', '15760840', '15542594', '16524698', '17355370', '18922178']

**Reranked docs:** ['18921114', '17168254', '15322490', '17168250', '15542594', '17168268', '13497800', '18769480', '16524698', '13020628']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 4

**Query:** I need product with a Woven design pattern in Mustard.

**Relevant docs:** ['12824928', '18262088']

**Retrieved docs:** ['10451734', '18122478', '19218994', '17663018', '16719554', '11117288', '18135092', '17365722', '18141434', '14159320']

**Reranked docs:** ['18141434', '16719554', '11117288', '19218994', '18122478', '18135092', '18196770', '18509068', '17663018', '18696924']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 5

**Query:** I'm looking for products from MANGO for everyday wear under 5600.

**Relevant docs:** ['15315768', '15265896', '15265898', '16892568', '15977044', '18257264', '16708118', '16708114']

**Retrieved docs:** ['14006764', '16124612', '17607938', '18321088', '18877470', '15274016', '19165458', '17336142', '18224860', '17808618']

**Reranked docs:** ['17607938', '16124404', '18319598', '16124612', '15274016', '17808618', '17270200', '14340718', '18778410', '13523706']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 6

**Query:** What do you have from Sweet Dreams in Playsuit and color Pink?

**Relevant docs:** ['11581420', '11581366']

**Retrieved docs:** ['11581420', '11581448', '11581366', '12882594', '13270464', '12882732', '14166398', '12459498', '16533336', '14568680']

**Reranked docs:** ['11581448', '11581366', '11581420', '12882594', '12882732', '16533336', '12459498', '19231232', '14166398', '13270464']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 0.500 | 0.920 | 0.693 |

### Question 7

**Query:** I'm looking for Kurta set by Vishudh.

**Relevant docs:** ['13536726', '15997054', '18262138', '13119222', '18263032', '15820432', '15639890', '18929144']

**Retrieved docs:** ['9867983', '13799826', '14860664', '18929144', '13536726', '7572969', '15997054', '7572958', '13119222', '13433674']

**Reranked docs:** ['15639890', '17656860', '18688392', '13433674', '14860664', '13119222', '17445358', '18261878', '18263032', '9673749']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.400 | 0.300 | 0.500 | 0.375 | 0.250 | 1.000 | 0.367 | 0.419 |

### Question 8

**Query:** I'm looking for A-line by Ancestry.

**Relevant docs:** ['15407228', '19152780', '14873702']

**Retrieved docs:** ['14873856', '15407228', '14873702', '19152780', '14873748', '16588088', '15407188', '19152792', '17149934', '19152772']

**Reranked docs:** ['19152780', '14873702', '15407228', '14873856', '19152792', '14873748', '17149934', '14159320', '15407188', '15407164']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.300 | 1.000 | 1.000 | 0.500 | 1.000 | 0.733 | 1.000 |

### Question 9

**Query:** Can you find something similar to "FASHOR Women Blue Geometric Printed Gotta Patti Khadi Kurta"?

**Relevant docs:** ['19140952']

**Retrieved docs:** ['19140952', '18964098', '11561972', '17487138', '18964110', '18116634', '10935118', '16486578', '14951330', '17251886']

**Reranked docs:** ['19140952', '18964098', '18787430', '18127962', '17487138', '16486578', '16773346', '18964110', '18116634', '11369528']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 10

**Query:** Show me Blue Tailored jacket from Darzi.

**Relevant docs:** ['14460680']

**Retrieved docs:** ['14460680', '17513236', '14460654', '14460662', '17666218', '17665710', '17666226', '14460688', '10321499', '1017828']

**Reranked docs:** ['14460680', '17666226', '14460662', '17665702', '17513236', '14460654', '17665710', '17666218', '15851900', '14460688']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 11

**Query:** Can you find something similar to "U.S. Polo Assn. Women Beige Solid Biker Jacket"?

**Relevant docs:** ['13703470']

**Retrieved docs:** ['13703470', '13690162', '2185647', '17983210', '15555424', '17038718', '16220536', '15555432', '15555446', '14355452']

**Reranked docs:** ['13703470', '13690162', '2185647', '16220536', '11933088', '17983210', '15673166', '14355452', '14355398', '14355346']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 12

**Query:** Does Mitera have any Bandhani for a festive occasion within 5500?

**Relevant docs:** ['15637468']

**Retrieved docs:** ['15637468', '17141480', '17141474', '15519332', '15519378', '15442988', '16311070', '16331704', '17392504', '17325496']

**Reranked docs:** ['15637468', '15442988', '17141480', '17141474', '15519332', '15519378', '16311070', '16331704', '16286120', '12668502']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 13

**Query:** Show me Pencil within a budget of 1500.

**Relevant docs:** ['15940138', '9552849', '15301318', '12086086', '18834976', '18454266', '15637548', '6629440']

**Retrieved docs:** ['14011652', '1294879', '18215398', '14798956', '17899166', '14372466', '17739956', '13496046', '17931744', '19072638']

**Reranked docs:** ['18629568', '15315920', '14011652', '17899166', '14372466', '17899190', '14024850', '17739956', '18034350', '17403200']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 14

**Query:** Do you have any Mustard Blouson for everyday wear?

**Relevant docs:** ['13532718']

**Retrieved docs:** ['14935802', '13532718', '11184982', '7942995', '19207552', '11364440', '18229566', '14231200', '13845674', '16931650']

**Reranked docs:** ['13532718', '14935802', '11184982', '7942995', '13861554', '12419366', '8474043', '16084334', '13581118', '18839638']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 15

**Query:** I need Blue Joggers by STREET 9.

**Relevant docs:** ['13038932', '13071994']

**Retrieved docs:** ['13071994', '13038932', '13038926', '13071970', '13038922', '13071980', '13038960', '16336020', '13738666', '5389019']

**Reranked docs:** ['13038932', '13071994', '13038926', '13738666', '13071970', '13038960', '19361312', '16336020', '13038922', '13071980']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 16

**Query:** Show me Front-open within a budget of 2800.

**Relevant docs:** ['16382036', '16382150', '5829334', '5829327', '11991214', '15007832', '14328000', '16461758']

**Retrieved docs:** ['14382336', '16082246', '17685090', '19087856', '2223198', '11952000', '7736701', '14071540', '15844140', '15137944']

**Reranked docs:** ['15844140', '15353040', '2223198', '15413660', '11952000', '16082246', '19087856', '11102094', '14210706', '14382336']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 17

**Query:** Do you have anything from FILA in Red for everyday wear?

**Relevant docs:** ['13255768']

**Retrieved docs:** ['13255768', '16705336', '16172382', '18489222', '16705334', '17255464', '16705280', '16705296', '18057660', '19324666']

**Reranked docs:** ['13255768', '16705334', '16705336', '16705280', '16705296', '19324666', '14381208', '19324656', '18806012', '16172382']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 18

**Query:** I'm looking for products that cost no more than 1100.

**Relevant docs:** ['13135238', '15241584', '13181706', '17739302', '15218838', '11579058', '17113756', '13951522']

**Retrieved docs:** ['17403640', '2117164', '17403254', '13452734', '17403434', '17365722', '17403428', '14159320', '17403380', '17403300']

**Reranked docs:** ['14159320', '13878270', '13452734', '11284776', '15474590', '17570416', '19097390', '19097392', '12629360', '15312982']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 19

**Query:** Do you have anything from Bhama Couture in A-line?

**Relevant docs:** ['12151804', '10355827', '10356731', '12151824', '10717820', '9430103', '9430109', '10355839']

**Retrieved docs:** ['12151824', '9430121', '9430115', '13969870', '11672988', '9717189', '10355827', '13969820', '8339967', '12151804']

**Reranked docs:** ['11672988', '12151824', '8339967', '13969870', '13969820', '4380660', '4380652', '10717820', '9717189', '10356731']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.300 | 0.375 | 0.375 | 1.000 | 0.500 | 0.410 | 0.313 |

### Question 20

**Query:** Do you have any Pink Peg trousers for everyday wear?

**Relevant docs:** ['15473916']

**Retrieved docs:** ['13740956', '15473916', '1986896', '11040098', '8999489', '13493068', '8999463', '14075224', '13204932', '19085128']

**Reranked docs:** ['15473916', '13740956', '13204932', '18416334', '18143380', '15441242', '19085128', '11412238', '18342122', '8999463']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 21

**Query:** Show me Regular shorts within a budget of 1800.

**Relevant docs:** ['15402090', '14170730', '18283554', '18747132', '16164252', '11535910', '14609842', '15083714']

**Retrieved docs:** ['13523706', '14272032', '13647622', '13769372', '9621439', '11101312', '17251600', '15083714', '16836260', '14027018']

**Reranked docs:** ['14672892', '13060194', '9621439', '13529198', '11101312', '17251600', '15103054', '14954482', '15083714', '16836260']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 0.125 | 0.125 | 0.125 | 0.111 | 0.080 | 0.076 |

### Question 22

**Query:** I'm looking for Regular by H&M.

**Relevant docs:** ['17964932', '17883620', '18652012', '14258606', '18084562', '18170658', '19074168', '17674588']

**Retrieved docs:** ['17674588', '17965024', '12383500', '17883650', '17883622', '17842774', '18131688', '14258606', '17964932', '17842776']

**Reranked docs:** ['12383500', '19074138', '17674588', '17883650', '17964932', '17842774', '19074168', '17883620', '14258606', '17883622']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.500 | 0.375 | 0.625 | 1.000 | 0.333 | 0.409 | 0.465 |

### Question 23

**Query:** I need Pink Saree by KALINI.

**Relevant docs:** ['15858094', '17852902', '15102290', '14678908', '16421936']

**Retrieved docs:** ['16914910', '16421936', '15102290', '16915002', '16948530', '14678908', '16989798', '17852902', '14798392', '12961094']

**Reranked docs:** ['14678908', '15858094', '17852902', '16914910', '15102290', '16421936', '12961094', '17414120', '12792140', '16948530']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.400 | 0.500 | 0.800 | 1.000 | 0.500 | 1.000 | 0.611 | 0.975 |

### Question 24

**Query:** Show me products within a budget of 1800.

**Relevant docs:** ['17094636', '13905652', '13905672', '13905666', '2322905', '17423996', '14925534', '14925544']

**Retrieved docs:** ['13523706', '17226172', '13647622', '13769372', '17570458', '18142596', '17790642', '17685090', '17250550', '18388758']

**Reranked docs:** ['17250550', '17790642', '17672184', '17570450', '18338282', '17570328', '18142596', '18388758', '17570364', '17570446']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 25

**Query:** I need product with a Other woven design pattern in Red.

**Relevant docs:** ['16379852', '16379914', '15768366']

**Retrieved docs:** ['16379914', '15768366', '16379852', '2138931', '11379820', '16608192', '13104106', '16608222', '15874790', '15768324']

**Reranked docs:** ['16379914', '16379852', '15768366', '15768324', '16608192', '11149776', '16608222', '11379820', '16874574', '15874790']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.300 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 26

**Query:** Do you have anything from SERONA FABRICS in White for everyday wear?

**Relevant docs:** ['15917640']

**Retrieved docs:** ['15917640', '16258082', '18845142', '18845144', '15907476', '15907474', '15907480', '15907478', '15907488', '18057660']

**Reranked docs:** ['15917640', '15907476', '18845144', '18845142', '15907480', '15907478', '15907488', '15907474', '16258082', '996729']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 27

**Query:** Do you have any Green Kurta set for a festive occasion?

**Relevant docs:** ['17140156', '16505434', '14121912', '16825614', '16707970', '15677426', '17232410', '14920000']

**Retrieved docs:** ['17447636', '15508896', '16707970', '15258422', '15054430', '13810898', '15654150', '17232410', '16931552', '17140156']

**Reranked docs:** ['17232410', '17140156', '15258422', '16505434', '14920000', '14121912', '18765612', '15677426', '15654150', '12989804']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.600 | 0.375 | 0.750 | 0.333 | 1.000 | 0.279 | 0.789 |

### Question 28

**Query:** I'm looking for something Black from URBANIC for everyday wear.

**Relevant docs:** ['15849954', '15634138', '18929182', '15086606', '15633414', '18866648', '18605954', '18907592']

**Retrieved docs:** ['15852292', '15632460', '16102760', '18542924', '15844202', '15086606', '15845464', '15851566', '18328804', '15633286']

**Reranked docs:** ['19072596', '18328804', '18867438', '15849954', '18542924', '15633286', '15852292', '15086606', '18644820', '15845464']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.200 | 0.125 | 0.250 | 0.167 | 0.250 | 0.090 | 0.189 |

### Question 29

**Query:** Show me Black products for everyday wear.

**Relevant docs:** ['9440729', '18207452', '18992236', '16612058', '9073715', '16728358', '7437296', '16728350']

**Retrieved docs:** ['14006764', '19270830', '18224860', '17351596', '19187496', '14912536', '19276886', '17570416', '18321088', '12383500']

**Reranked docs:** ['17570416', '17570450', '16379878', '17351596', '18207362', '13552234', '12383500', '19270830', '18224860', '19187496']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 30

**Query:** I'm looking for something Blue from Swasti for everyday wear.

**Relevant docs:** ['18819296']

**Retrieved docs:** ['18819296', '17403254', '17403428', '17403380', '17403300', '17403434', '19140952', '18321088', '18877470', '19165458']

**Reranked docs:** ['18819296', '15635874', '18651648', '19140952', '18964098', '19260114', '19260152', '17403428', '11536158', '17403254']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 31

**Query:** I need Shirt style with a Abstract printed pattern in Pink.

**Relevant docs:** ['13244594']

**Retrieved docs:** ['13244594', '15841446', '19195222', '12641134', '19201936', '10080283', '17547800', '18605378', '17268136', '13614956']

**Reranked docs:** ['13244594', '15841446', '19195222', '17820020', '12641134', '19325284', '13614956', '17547800', '18647784', '17348862']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 32

**Query:** I'm looking for products by Atsevam.

**Relevant docs:** ['17754230', '17754250', '17754248', '19217168', '19217170', '17584576', '19217176']

**Retrieved docs:** ['17754230', '17754248', '19217170', '17584576', '19217168', '19217186', '17834516', '19217176', '19217196', '17754250']

**Reranked docs:** ['19217170', '17584576', '17834516', '19217176', '19217186', '17754248', '19217168', '17754250', '17754230', '19217196']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.700 | 0.700 | 1.000 | 1.000 | 1.000 | 1.000 | 0.977 | 0.926 |

### Question 33

**Query:** What do you have from panchhi in products and color Pink?

**Relevant docs:** ['19046346', '12003682']

**Retrieved docs:** ['18070000', '19046346', '18175384', '19046338', '12003682', '18175352', '19046370', '18730470', '18624652', '19046354']

**Reranked docs:** ['12003682', '19046346', '18175384', '18070000', '19046338', '13872486', '13421470', '12003618', '18624652', '12003688']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 1.000 | 0.624 | 1.000 |

### Question 34

**Query:** What do you have in products under 2500?

**Relevant docs:** ['11765970', '17662818', '15514544', '18068482', '16989998', '16563320', '15011850', '15266776']

**Retrieved docs:** ['16858560', '17612960', '16172382', '18489222', '17255464', '18057660', '17336142', '2507000', '18290992', '18806012']

**Reranked docs:** ['17336142', '2507000', '19104000', '17209256', '17612960', '15071832', '16758920', '16311684', '16311568', '18309022']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 35

**Query:** Show me products from Indo Era.

**Relevant docs:** ['14239788', '11459668', '12040868', '15520698', '12040878', '12122360', '13250074', '17553564']

**Retrieved docs:** ['14869156', '16188740', '12122360', '16950290', '12040878', '16950218', '11459668', '12040868', '17577466', '17577464']

**Reranked docs:** ['12040868', '15520698', '14869156', '11459668', '12040878', '17577464', '17553556', '12122360', '16188740', '15098616']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.400 | 0.500 | 0.500 | 0.625 | 0.333 | 1.000 | 0.388 | 0.699 |

### Question 36

**Query:** Show me products like "ONLY Women Blue Straight Fit High-Rise Mildly Distressed Jeans".

**Relevant docs:** ['18626222']

**Retrieved docs:** ['18626222', '16372376', '18620390', '18626210', '19089706', '16699772', '19089710', '19089668', '17122946', '17914728']

**Reranked docs:** ['18626222', '18626210', '16372376', '19089706', '18620390', '16699772', '18338282', '19089694', '19089668', '17914728']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 37

**Query:** Do you have anything from Uptownie Lite in Flared?

**Relevant docs:** ['17944738', '16608122', '11511460', '11425704', '13467524']

**Retrieved docs:** ['17944738', '11425706', '11425704', '13467524', '11511460', '11335786', '15355338', '16608122', '11234642', '10418102']

**Reranked docs:** ['11425704', '11425706', '11335786', '11511460', '17944738', '13467524', '16608122', '15355338', '17267836', '10418102']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.500 | 0.500 | 1.000 | 1.000 | 1.000 | 1.000 | 0.893 | 0.850 |

### Question 38

**Query:** Can you find something similar to "Mitera Grey Embellished Sequinned Semi-Stitched Lehenga & Unstitched Blouse With Dupatta"?

**Relevant docs:** ['16950080']

**Retrieved docs:** ['16950080', '16950094', '16316606', '16950086', '18813862', '18813860', '18759692', '18813850', '18813864', '15390366']

**Reranked docs:** ['16950080', '16950082', '16950094', '16950086', '18813850', '18813860', '16316606', '18726438', '18726440', '18813862']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 39

**Query:** Do you have anything similar to "Suta Beige & White Pure Linen Zari Saree"?

**Relevant docs:** ['15243956']

**Retrieved docs:** ['15243956', '14988194', '15244002', '16909578', '14988280', '16909636', '16909300', '15244224', '17638770', '15244024']

**Reranked docs:** ['15243956', '15244002', '14988194', '16909300', '16909636', '15244224', '14988280', '16909578', '15244106', '15243974']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 40

**Query:** Show me options from Levis for everyday wear, preferably in Blue.

**Relevant docs:** ['18069226', '16532142', '18069298', '18069260', '16653678', '16653750', '16653608', '16653786']

**Retrieved docs:** ['18069150', '18903336', '18903198', '18903182', '18069260', '18903152', '18069202', '18069276', '18903286', '16653786']

**Reranked docs:** ['18903182', '18903152', '12259048', '13326354', '16794818', '16653658', '16653786', '18903286', '18069202', '16653750']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 0.250 | 0.250 | 0.200 | 0.143 | 0.171 | 0.157 |

### Question 41

**Query:** Show me Pullover that are Black and have Solid print.

**Relevant docs:** ['16707678', '16124454', '13534776', '15964092', '15274016', '15963804', '15198584', '15243336']

**Retrieved docs:** ['9478497', '15198584', '15845464', '15642616', '10575458', '6726577', '10714640', '17038044', '9477715', '10683730']

**Reranked docs:** ['14080898', '6726577', '15845464', '10683730', '16583226', '14331596', '17038044', '15630060', '15870014', '12048466']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.000 | 0.125 | 0.000 | 0.500 | 0.000 | 0.160 | 0.000 |

### Question 42

**Query:** I'm looking for Dress that cost no more than 5300.

**Relevant docs:** ['13878542', '17705690', '18365368', '16921564', '16921510', '16921508', '16921524', '16921550']

**Retrieved docs:** ['17403640', '13843640', '17403254', '13452734', '17403434', '17365722', '17403428', '14159320', '17403380', '17403300']

**Reranked docs:** ['13843640', '18750730', '14159320', '19396408', '16533888', '18766164', '17287376', '19392350', '17570416', '11284776']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 43

**Query:** I'm looking for something Pink from Mitera for a traditional occasion.

**Relevant docs:** ['15012182', '11454958', '11244988', '18302880']

**Retrieved docs:** ['11244988', '13886174', '11218670', '15012182', '18302880', '18287324', '11454958', '14850332', '17552342', '18377598']

**Reranked docs:** ['11244988', '18302880', '11218670', '14850332', '15012182', '11454958', '13886174', '11096590', '15519332', '11117288']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.400 | 0.400 | 1.000 | 1.000 | 1.000 | 1.000 | 0.840 | 0.927 |

### Question 44

**Query:** I'm looking for Pullover from max for everyday wear under 600.

**Relevant docs:** ['19204850', '15878996', '16156132']

**Retrieved docs:** ['18782606', '18995122', '19204850', '19204868', '15878938', '15878978', '15670702', '15878996', '15673658', '16156132']

**Reranked docs:** ['15670702', '16156132', '15878978', '18782606', '15878938', '19204868', '18995122', '15673658', '19204850', '15878996']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.300 | 1.000 | 1.000 | 0.333 | 0.500 | 0.518 | 0.573 |

### Question 45

**Query:** What do you have from Roadster in products and color Navy Blue?

**Relevant docs:** ['12278640', '11987092', '8803831', '8963467', '12278652', '14094106', '16187090', '15897498']

**Retrieved docs:** ['14094106', '11296068', '15897498', '5447351', '14094050', '12278652', '17074032', '12278640', '13700180', '14925764']

**Reranked docs:** ['12278652', '12278640', '8803831', '8963467', '14094050', '14925764', '16187090', '5447351', '17074032', '15897498']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.400 | 0.600 | 0.500 | 0.750 | 1.000 | 1.000 | 0.549 | 0.805 |

### Question 46

**Query:** Show me Orange Saree from KALINI.

**Relevant docs:** ['14490860']

**Retrieved docs:** ['14541316', '17066888', '14490860', '16915002', '16625250', '16421936', '16915122', '12754022', '16914910', '17035752']

**Reranked docs:** ['14541316', '14490860', '17584716', '17066888', '16915002', '16625250', '16989798', '14986192', '15102284', '14678908']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.333 | 0.500 | 0.500 | 0.631 |

### Question 47

**Query:** Do you have any Black Tailored jacket for sports?

**Relevant docs:** ['14646546']

**Retrieved docs:** ['15789256', '14646546', '11383846', '15684018', '15849954', '13095488', '14462864', '1052282', '18522690', '8067177']

**Reranked docs:** ['14646546', '15634138', '14462864', '18522690', '13095488', '15849954', '13039008', '18282028', '16191476', '11063538']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 48

**Query:** Do you have anything from Roadster in Grey for everyday wear?

**Relevant docs:** ['13756948', '8319213', '13339544', '14954872', '10388213', '16835166', '16835204', '16835178']

**Retrieved docs:** ['16835204', '16835178', '16835166', '13339544', '8319213', '14954602', '14954872', '14536020', '14535748', '16172382']

**Reranked docs:** ['14535748', '15441284', '14954602', '14536020', '16835166', '14535994', '14535802', '13756948', '16835178', '11990670']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.600 | 0.300 | 0.750 | 0.375 | 1.000 | 0.200 | 0.830 | 0.254 |

### Question 49

**Query:** I need Peplum with a Self design solid pattern in Blue.

**Relevant docs:** ['16504028']

**Retrieved docs:** ['16931960', '4374524', '5617740', '16504028', '18514120', '14641744', '13382002', '11607414', '11607374', '17132282']

**Reranked docs:** ['16504028', '16931960', '14641744', '5617740', '4374524', '18514120', '13382002', '14602502', '8715089', '17132282']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.250 | 1.000 | 0.431 | 1.000 |

### Question 50

**Query:** I need Peach Pullover by Madame.

**Relevant docs:** ['16533076']

**Retrieved docs:** ['16533076', '18948340', '14556346', '15756110', '16512732', '15997770', '16566862', '15964118', '16512720', '10891532']

**Reranked docs:** ['16533076', '14556346', '15756110', '18948340', '15997770', '16512732', '14231418', '14279444', '10891532', '10611410']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 51

**Query:** Show me Blue A-line for everyday wear.

**Relevant docs:** ['16604256', '19047464', '18925104', '18454274', '18254862', '17881038', '18856726', '13892666']

**Retrieved docs:** ['17881038', '19198414', '19140952', '18454242', '18100824', '18454272', '16379558', '17931384', '18778410', '19324666']

**Reranked docs:** ['17279494', '12133294', '19140952', '13369436', '15887108', '18656648', '19198414', '15749898', '18100824', '18454274']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 0.125 | 0.125 | 1.000 | 0.100 | 0.253 | 0.073 |

### Question 52

**Query:** What do you have from SHINOY in A-line and color Black?

**Relevant docs:** ['17347938']

**Retrieved docs:** ['17347938', '17346376', '18057660', '16172382', '18489222', '17255464', '16858560', '17347940', '17346372', '14913618']

**Reranked docs:** ['17347938', '17346376', '17347940', '17346372', '15953978', '14913618', '14921732', '19016206', '16931654', '16931538']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 53

**Query:** Do you have anything from SASSAFRAS in Green for everyday wear?

**Relevant docs:** ['15940140', '13935934', '16989930', '18337046', '17240142', '17240172', '11364424', '16989920']

**Retrieved docs:** ['12288210', '12221892', '13935934', '11364424', '16172382', '16989920', '18489222', '17511510', '17255464', '18057660']

**Reranked docs:** ['18110214', '17511510', '17787792', '15940140', '12221892', '18337046', '17985404', '11364424', '13935934', '19202952']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.400 | 0.375 | 0.500 | 0.333 | 0.250 | 0.326 | 0.355 |

### Question 54

**Query:** Do you have Beige Front-open with a Solid pattern?

**Relevant docs:** ['15960258', '17131030']

**Retrieved docs:** ['15960258', '16652156', '16102990', '17131030', '19087856', '10319989', '17238348', '10320039', '1087795', '16172382']

**Reranked docs:** ['16102990', '15960258', '16652156', '17131030', '18067068', '13913504', '16971682', '10319989', '10320039', '19087856']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 0.500 | 0.877 | 0.651 |

### Question 55

**Query:** I'm looking for Top from Bitterlime for everyday wear under 2000.

**Relevant docs:** ['15449738', '18957292', '13899658', '13899678']

**Retrieved docs:** ['16842760', '18957292', '14166356', '16842738', '13899678', '15449738', '13899658', '15449744', '8224951', '8999463']

**Reranked docs:** ['18957292', '13899678', '15449738', '13899658', '15449744', '14166356', '16842760', '16842738', '8231209', '2369587']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.400 | 0.400 | 1.000 | 1.000 | 0.500 | 1.000 | 0.667 | 1.000 |

### Question 56

**Query:** I'm looking for Saree by Inddus.

**Relevant docs:** ['16472014', '11387498', '15443712', '17500906', '11423192', '17500900', '17500926', '15443704']

**Retrieved docs:** ['13427900', '15443724', '13843398', '14994266', '12631338', '11423192', '16472014', '17760526', '15443702', '12631378']

**Reranked docs:** ['17500906', '17760526', '15443704', '8927013', '13843398', '17760514', '11387498', '11423192', '12631338', '17500926']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.500 | 0.250 | 0.625 | 0.167 | 1.000 | 0.174 | 0.617 |

### Question 57

**Query:** I'm looking for Top from Bannos Swagger for everyday wear under 2600.

**Relevant docs:** ['19286742']

**Retrieved docs:** ['16854862', '18256196', '19286742', '17371472', '17371476', '17336142', '18321088', '18877470', '19165458', '18224860']

**Reranked docs:** ['19286742', '16854862', '18256196', '17371472', '17371476', '15047458', '18778410', '14811738', '14159320', '13452734']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.333 | 1.000 | 0.500 | 1.000 |

### Question 58

**Query:** Show me products by Souchii for everyday wear if you have any under 400.

**Relevant docs:** ['12313104', '12313110']

**Retrieved docs:** ['12313114', '12313110', '12313104', '18696386', '12313954', '19207552', '16858560', '17238348', '19276886', '18806012']

**Reranked docs:** ['12313110', '12313104', '12313114', '18696386', '12313954', '16931578', '17336142', '19046346', '16858560', '19165458']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 1.000 | 0.693 | 1.000 |

### Question 59

**Query:** I need Pullover with a Typography printed pattern in Black.

**Relevant docs:** ['14518558', '15086606', '16099978', '15300778', '10623674', '15241884', '12767154', '12767178']

**Retrieved docs:** ['15086606', '17268386', '18004440', '15241884', '18995122', '12476708', '15300778', '12767154', '14518516', '16099978']

**Reranked docs:** ['15086606', '12767154', '12767178', '18995122', '15300778', '18004440', '12476708', '17268386', '10623674', '16043950']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.500 | 0.500 | 0.625 | 0.625 | 1.000 | 1.000 | 0.599 | 0.713 |

### Question 60

**Query:** I need Maroon Basic jumpsuit by Roadster.

**Relevant docs:** ['11396694']

**Retrieved docs:** ['11396716', '11396694', '14935148', '14935160', '11396690', '13339510', '12712588', '13339842', '13339506', '14935172']

**Reranked docs:** ['11396694', '11396716', '16465456', '13339510', '15907934', '10308583', '11466786', '15773220', '16356804', '13339842']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.500 | 1.000 | 0.631 | 1.000 |

### Question 61

**Query:** Show me products like "SCORPIUS Women White & Blue Floral Printed Open-Front Longline Shrug".

**Relevant docs:** ['13167060']

**Retrieved docs:** ['13167060', '2977056', '11120366', '11120368', '2254373', '9338421', '9338423', '9338433', '9338259', '9338279']

**Reranked docs:** ['13167060', '11120366', '11120368', '2977056', '13167052', '2254373', '12098992', '9338421', '9338423', '9338433']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 62

**Query:** Show me products like "MANGO Blue Solid Basic Jumpsuit".

**Relevant docs:** ['14340700']

**Retrieved docs:** ['14340700', '15728226', '14340876', '15315456', '18319512', '17968376', '18319358', '15315224', '15315208', '11842368']

**Reranked docs:** ['14340700', '13099860', '17968376', '14340876', '15728226', '15315456', '18319640', '15035500', '11706008', '11842368']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 63

**Query:** Show me products within a budget of 2000.

**Relevant docs:** ['18980894', '19130900', '17653922', '18324370', '17652944', '17651410', '19298212', '18507630']

**Retrieved docs:** ['13523706', '17685090', '13647622', '13769372', '17226246', '17570450', '17250550', '17570446', '17570328', '17226172']

**Reranked docs:** ['17570470', '18338282', '17250550', '17570450', '17672184', '17570364', '17570328', '17570446', '17226246', '18142596']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 64

**Query:** Do you have any Maroon Cardigan for everyday wear?

**Relevant docs:** ['15124958', '15121522', '18775992', '14470038', '16378560', '19286442', '19286088']

**Retrieved docs:** ['15121522', '19286088', '19286442', '14966352', '15124958', '16378560', '18775992', '14231232', '19207552', '14470038']

**Reranked docs:** ['19286088', '16378560', '14470038', '15124958', '18775992', '14966352', '15121522', '19286442', '13300756', '16931736']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.700 | 0.700 | 1.000 | 1.000 | 1.000 | 1.000 | 0.961 | 0.989 |

### Question 65

**Query:** What do you have from SOUNDARYA in Wrap and color Pink?

**Relevant docs:** ['17063728', '1921003']

**Retrieved docs:** ['1921003', '17063728', '1718761', '1718753', '1718757', '16587512', '1921005', '16587510', '17063708', '1619866']

**Reranked docs:** ['17063728', '1921003', '16587512', '18073686', '17178062', '1718753', '14178358', '1619866', '12034032', '11908290']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 66

**Query:** Can you find something similar to "Mitera Yellow Silk Blend Woven Design Kanjeevaram Saree"?

**Relevant docs:** ['11458584']

**Retrieved docs:** ['11458584', '11096590', '11117288', '18302884', '11117398', '11327746', '11076732', '11218670', '18377598', '10321833']

**Reranked docs:** ['11458584', '11117398', '10321833', '11076732', '11244988', '11218670', '11096590', '11117288', '18302880', '18377598']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 67

**Query:** Do you have anything from Iti in Pink for everyday wear?

**Relevant docs:** ['16065144']

**Retrieved docs:** ['16065144', '16172382', '18489222', '17255464', '18057660', '19165458', '17238348', '18321088', '16224212', '18877470']

**Reranked docs:** ['16065144', '16224212', '16263962', '19324656', '14708328', '17553498', '16311576', '16828018', '16984006', '16311702']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 68

**Query:** I need Regular shorts with a Solid pattern in Black.

**Relevant docs:** ['17774198', '19357434', '15221870', '14063026', '16531520', '18611668', '19047410', '14225458']

**Retrieved docs:** ['16531520', '19174870', '18305296', '19357434', '17251600', '18721660', '14225458', '13642464', '17774198', '19047410']

**Reranked docs:** ['14225458', '15633046', '16531520', '19047410', '12431562', '10035883', '17066978', '18721660', '12419386', '19174870']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.500 | 0.300 | 0.625 | 0.375 | 1.000 | 1.000 | 0.595 | 0.488 |

### Question 69

**Query:** Show me Basic jumpsuit that are Navy Blue and have Solid print.

**Relevant docs:** ['15979192', '13923936', '16946284', '17933184', '7846795', '15508760', '2046268', '14136152']

**Retrieved docs:** ['2046268', '10923656', '6608510', '11148578', '18664198', '9038769', '15634238', '18395218', '11053950', '14340876']

**Reranked docs:** ['13923936', '11148578', '15634238', '6608510', '18395218', '15287420', '2046268', '16946284', '16555904', '9038769']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.300 | 0.125 | 0.375 | 1.000 | 1.000 | 0.253 | 0.417 |

### Question 70

**Query:** I'm looking for Flared from Span for an ethnic look under 3000.

**Relevant docs:** ['13172786']

**Retrieved docs:** ['13172786', '13669924', '11005018', '15723626', '15132474', '15150430', '11808928', '13669932', '15150438', '12390826']

**Reranked docs:** ['13172786', '15723626', '15723614', '11005018', '11808928', '15150430', '18179894', '13669924', '13669932', '15150438']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 71

**Query:** What do you have in products under 2300?

**Relevant docs:** ['9660683', '14061718', '15474560', '15559842', '9660675', '12722434', '13646276', '15204772']

**Retrieved docs:** ['16858560', '16372904', '18258324', '15589086', '18258322', '18258334', '16172382', '18258316', '18489222', '17255464']

**Reranked docs:** ['17336142', '16034502', '18258330', '15381904', '18008128', '16372904', '18290988', '17053210', '18290992', '18057660']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 72

**Query:** I'm looking for products that cost no more than 1000.

**Relevant docs:** ['19021648', '11305458', '15047068', '17532972', '14319300', '18782898', '17055336', '18782896']

**Retrieved docs:** ['17403640', '15312982', '17403254', '13452734', '17403434', '17365722', '17403428', '14159320', '17403380', '17403300']

**Reranked docs:** ['14159320', '13452734', '11284776', '18757336', '17570416', '12629360', '14925780', '17403300', '19097390', '17365720']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 73

**Query:** I need Chanderi with a Solid pattern in Red.

**Relevant docs:** ['16331746']

**Retrieved docs:** ['16331746', '18323532', '16331730', '17976750', '18100060', '18686216', '17771942', '1411010', '18262236', '18198266']

**Reranked docs:** ['16331746', '17904824', '18323532', '16331730', '18100060', '18960514', '18724196', '18686204', '18686216', '13791612']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 74

**Query:** Does MANGO have any Straight for everyday wear within 2800?

**Relevant docs:** ['18259676', '19120116', '19120276']

**Retrieved docs:** ['17019168', '18327896', '17808496', '18327874', '18259672', '17608058', '17607798', '17969902', '17270106', '17808850']

**Reranked docs:** ['17808850', '19120276', '19100800', '17608010', '18327896', '17808496', '17969902', '18327908', '17608058', '18327916']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.100 | 0.000 | 0.333 | 0.000 | 0.500 | 0.000 | 0.296 |

### Question 75

**Query:** Show me Pink products for everyday wear.

**Relevant docs:** ['18872530', '13047934', '18454258', '18454262', '11928776', '16837772', '16334412', '16701486']

**Retrieved docs:** ['19357994', '15372566', '18697010', '19324656', '16984006', '14006764', '18342112', '14912536', '19276886', '19165458']

**Reranked docs:** ['19324656', '19357994', '13078244', '15372566', '16172498', '15943076', '14122722', '17163984', '18342112', '13459738']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 76

**Query:** Show me Green Kurta set for a festive occasion.

**Relevant docs:** ['14920000', '15654150', '16505434', '14121912', '16825614', '16707970', '15677426', '17232410']

**Retrieved docs:** ['17447636', '16707970', '15054430', '15508896', '15258422', '12989804', '15654150', '17232410', '13810898', '17140156']

**Reranked docs:** ['17232410', '14121912', '17140156', '18765612', '14920000', '16825614', '16505434', '15258422', '12989804', '15654150']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.600 | 0.375 | 0.750 | 0.500 | 1.000 | 0.324 | 0.758 |

### Question 77

**Query:** I need product with a Ethnic motifs embroidered pattern in Orange.

**Relevant docs:** ['18213450', '14016110', '18213274', '17662984']

**Retrieved docs:** ['17662984', '18213274', '14016110', '18213450', '16945802', '14994384', '16945876', '17017792', '14444602', '16945862']

**Reranked docs:** ['18213274', '14016110', '18213450', '17662984', '17405764', '18351148', '16945862', '8832069', '19366966', '16945802']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.400 | 0.400 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 78

**Query:** Show me products like "The Dry State Women Olive Solid Loose Fit Shorts".

**Relevant docs:** ['13883906']

**Retrieved docs:** ['13883906', '14225456', '13515226', '14375954', '14225458', '14954482', '14357542', '14380984', '13515222', '12900742']

**Reranked docs:** ['13883906', '14225456', '14375954', '14380984', '13515226', '13515222', '14225458', '14357542', '14954482', '12969482']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 79

**Query:** I'm looking for Kurta set from Indo Era for everyday wear under 7000.

**Relevant docs:** ['13962368', '13962360', '14967448', '11459658', '14208496', '15227066']

**Retrieved docs:** ['13962368', '11459658', '13810898', '12122358', '13962360', '17069054', '13962300', '18165350', '14208496', '14967448']

**Reranked docs:** ['13962360', '11459658', '15227066', '14208496', '13962368', '15654150', '14235030', '14967448', '15258422', '15508918']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.500 | 0.600 | 0.833 | 1.000 | 1.000 | 1.000 | 0.789 | 0.988 |

### Question 80

**Query:** Do you have anything similar to "Athena Black Jumpsuit with Waist Cutout Detail"?

**Relevant docs:** ['15301002']

**Retrieved docs:** ['15301002', '18121952', '15300980', '18121942', '18121946', '19405492', '18121932', '18121954', '15980662', '14827892']

**Reranked docs:** ['15301002', '18121952', '18121942', '19405492', '11288550', '14827892', '11634534', '18121954', '14164210', '14164138']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 81

**Query:** Do you have anything from VASTRANAND in products?

**Relevant docs:** ['16631248', '13842596', '16631260', '13068108', '16631252', '14674694', '14674638', '13914012']

**Retrieved docs:** ['17291456', '16244404', '16630850', '17101266', '17101240', '17829832', '16630950', '17291526', '16630864', '12806402']

**Reranked docs:** ['17291456', '13914012', '13914066', '14674694', '14674638', '13914030', '14674674', '17150532', '12806398', '12806384']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.300 | 0.000 | 0.375 | 0.000 | 0.500 | 0.000 | 0.366 |

### Question 82

**Query:** I'm looking for Red Regular trousers for everyday wear.

**Relevant docs:** ['18289836', '12400438', '7272029', '15204108', '14099282', '12294280', '16945138', '14985192']

**Retrieved docs:** ['7197283', '11421530', '16175534', '17842774', '17965024', '19097390', '18289836', '12309376', '19097392', '11434632']

**Reranked docs:** ['17430638', '18289836', '7197283', '15204108', '18157926', '12309376', '12400438', '16641130', '11421530', '14985192']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.400 | 0.125 | 0.500 | 0.143 | 0.500 | 0.084 | 0.426 |

### Question 83

**Query:** I'm looking for Regular trousers that cost no more than 1800.

**Relevant docs:** ['16858560', '18290008', '12822698', '13243422', '13913404', '16910904', '14944516', '15341678']

**Retrieved docs:** ['17965024', '17842774', '19097390', '18131688', '19097392', '17393956', '16279046', '16220618', '17378342', '17883650']

**Reranked docs:** ['19097390', '16279046', '19097392', '13981424', '16220618', '17965024', '17842774', '17883650', '5803888', '18131688']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 84

**Query:** I'm looking for Dress that cost no more than 9000.

**Relevant docs:** ['17157864', '15888364', '15815438', '15839544', '16017444', '15202008', '16017464', '18536294']

**Retrieved docs:** ['18839214', '13856418', '13843640', '18766164', '17403640', '17403254', '13452734', '17403434', '17365722', '17403428']

**Reranked docs:** ['13869240', '18750730', '13843640', '14159320', '14859228', '17215246', '13843642', '13856438', '18766164', '13856418']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 85

**Query:** I'm looking for Regular shorts from KASSUALLY for everyday wear under 1400.

**Relevant docs:** ['17739118', '17295878']

**Retrieved docs:** ['18003804', '17405640', '17295878', '17739118', '12564282', '12564274', '18947602', '17365722', '17062466', '17336142']

**Reranked docs:** ['17295878', '17739118', '18947602', '12564274', '12564282', '11937460', '11937456', '17062466', '17062446', '17405640']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.333 | 1.000 | 0.571 | 1.000 |

### Question 86

**Query:** Do you have Black product with a Solid embroidered pattern?

**Relevant docs:** ['18157218', '17824864', '18308702', '15155512']

**Retrieved docs:** ['1823751', '8899693', '14381182', '13552234', '14869156', '17876634', '16172382', '18489222', '17255464', '18929182']

**Reranked docs:** ['18929182', '8899693', '14869156', '14381182', '17876634', '13552234', '14707932', '16931654', '16931538', '1823751']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 87

**Query:** I need Flared with a Geometric printed pattern in Cream.

**Relevant docs:** ['13957498', '13955684', '10698576']

**Retrieved docs:** ['13957498', '12663974', '13955684', '10698576', '18848596', '17763430', '13955648', '18054680', '17189512', '13955736']

**Reranked docs:** ['10698576', '13957498', '12663974', '13955684', '18848596', '18054680', '14008468', '17189512', '15646542', '17763430']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.300 | 1.000 | 1.000 | 1.000 | 1.000 | 0.906 | 0.967 |

### Question 88

**Query:** Do you have any Peach products for a festive occasion?

**Relevant docs:** ['11530694', '17241032', '19216558', '11369410', '18068574', '13619506']

**Retrieved docs:** ['16311564', '11369410', '16961024', '17287334', '13619506', '17242612', '14381366', '17788058', '14231418', '18766176']

**Reranked docs:** ['16311564', '13670106', '11530694', '17788058', '17242612', '17287334', '16893670', '18766176', '18668348', '18115934']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.100 | 0.333 | 0.167 | 0.500 | 0.333 | 0.308 | 0.151 |

### Question 89

**Query:** Do you have anything from Pistaa in White for everyday wear?

**Relevant docs:** ['16493984']

**Retrieved docs:** ['16493984', '18057660', '16172382', '18489222', '17255464', '17238348', '18321088', '18877470', '18057656', '19165458']

**Reranked docs:** ['16493984', '19324656', '14231350', '19324666', '19140952', '18964098', '18057660', '18778410', '19198378', '19230136']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 90

**Query:** I need Beige Culotte jumpsuit by AND.

**Relevant docs:** ['11636588']

**Retrieved docs:** ['11636588', '11284684', '11284562', '9070213', '16388974', '2472444', '16899590', '11712920', '5389019', '5389041']

**Reranked docs:** ['11636588', '9070213', '16388974', '16899590', '15115296', '16931816', '11284684', '11284562', '11545812', '15082260']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 91

**Query:** Does Sangria have any product for everyday wear within 2500?

**Relevant docs:** ['17777396', '9370965', '16844760', '16844758', '17777400', '16848726', '13882506', '16630086']

**Retrieved docs:** ['14469954', '15546696', '16630054', '12539406', '19014544', '13833448', '13258020', '13833262', '19284218', '8350257']

**Reranked docs:** ['15546696', '8350257', '12539406', '16630086', '16871740', '9370965', '13258020', '19066150', '17449508', '13833448']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.200 | 0.000 | 0.250 | 0.000 | 0.250 | 0.000 | 0.199 |

### Question 92

**Query:** Show me A-line from Ives.

**Relevant docs:** ['15107870', '15107902', '13515100']

**Retrieved docs:** ['13515100', '15107902', '15107870', '15107864', '8375271', '13515064', '13932504', '18210214', '18057660', '18963012']

**Reranked docs:** ['13515100', '15107864', '15107902', '15107870', '13515064', '13932504', '8375271', '15921728', '18848596', '18057660']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.300 | 0.300 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.906 |

### Question 93

**Query:** What do you have from BoStreet in Tailored jacket and color Brown?

**Relevant docs:** ['19269442', '19269448']

**Retrieved docs:** ['19269448', '19269442', '19269384', '19269426', '19361356', '19269412', '16752820', '16706804', '14231172', '13326900']

**Reranked docs:** ['19269442', '19269448', '19361064', '19361356', '18811274', '19269412', '19269426', '19269384', '19082572', '19215762']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 94

**Query:** I need Black Regular trousers by Anouk.

**Relevant docs:** ['17469034', '13913404']

**Retrieved docs:** ['13913404', '15578002', '17469034', '12134668', '16899332', '17090216', '14925560', '17094600', '17093788', '14224034']

**Reranked docs:** ['13913404', '17469034', '14925560', '15578002', '17090216', '12134668', '14224034', '16899332', '17104874', '17093788']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 0.920 | 1.000 |

### Question 95

**Query:** I need Navy Blue Top by JC Collection.

**Relevant docs:** ['17348840', '15496388']

**Retrieved docs:** ['18529842', '15496388', '17348840', '18529880', '17348778', '17372692', '17348896', '17348852', '15496352', '16012788']

**Reranked docs:** ['15496388', '17348840', '18529842', '17372692', '17348778', '16154348', '18529880', '15496352', '17348896', '17348852']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 0.500 | 1.000 | 0.693 | 1.000 |

### Question 96

**Query:** Do you have Grey Regular with a Solid pattern?

**Relevant docs:** ['8802067', '2075014', '14076362', '14424638', '18518336', '15816572']

**Retrieved docs:** ['16311568', '16893050', '16172382', '18489222', '17255464', '18290002', '14658100', '13452734', '16503948', '18057660']

**Reranked docs:** ['14658100', '15855506', '2196419', '18290002', '17155514', '16856174', '16856178', '16003226', '16893050', '16395934']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 97

**Query:** I need Blue Shirt style by Stylo Bug.

**Relevant docs:** ['18473086', '14673176']

**Retrieved docs:** ['18473086', '14673176', '17613206', '18839616', '18841004', '18841010', '15803556', '18839830', '19292568', '17209144']

**Reranked docs:** ['18473086', '14673176', '17613206', '18839830', '18841008', '18841004', '18841010', '18839616', '18888648', '19292568']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.200 | 0.200 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |

### Question 98

**Query:** Show me products that are Mustard and have Ethnic motifs woven design print.

**Relevant docs:** ['17663018']

**Retrieved docs:** ['18509068', '18135092', '17663018', '14402632', '16945802', '10513948', '14088428', '12151840', '16827438', '18287618']

**Reranked docs:** ['18509068', '18135092', '17663018', '10513948', '18226112', '18287618', '14367932', '14444766', '16589242', '14088428']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 0.333 | 0.333 | 0.500 | 0.500 |

### Question 99

**Query:** Do you have any Green products for an ethnic look?

**Relevant docs:** ['18085512', '16608648', '17914962', '15160688', '13837098', '17870798', '9967233', '12980336']

**Retrieved docs:** ['16931644', '17589238', '13915012', '18069514', '12867304', '16172382', '19392350', '18489222', '12348718', '17172058']

**Reranked docs:** ['19392350', '17172058', '12024994', '16931644', '14358624', '13185952', '15224706', '16931578', '14381366', '16931618']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

### Question 100

**Query:** Show me Red Regular from Marie Claire.

**Relevant docs:** ['11550408']

**Retrieved docs:** ['11550408', '1731802', '10888848', '11155552', '16588670', '16588672', '11155510', '2213582', '17586398', '17586422']

**Reranked docs:** ['11550408', '1731802', '17586398', '2213582', '10888848', '16588670', '16588672', '11155552', '13168412', '11155510']

Metrics:

| precision | RERANKED_precision | recall | RERANKED_recall | mrr | RERANKED_mrr | ndcg | RERANKED_ndcg |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.100 | 0.100 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
