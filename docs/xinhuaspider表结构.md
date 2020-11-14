## xinhuaspider 表结构

#### 1、 bi_go_id

印尼央行

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` | 发布日期 |   datetime   |      | YES  |      |        |
|     `name`     | 表头名称 | varchar(255) |      | YES  |      |        |
|     `buy`      |  购买率  | varchar(255) |      | YES  |      |        |
|     `sell`     |  售卖率  | varchar(255) |      | YES  |      |        |
|   `average`    |  中间价  | varchar(255) |      | YES  |      |        |

#### 2、 bnm_gov_my

马来西亚央行

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   日期   | varchar(255) |      | YES  |      |        |
|     `name`     | 表头名称 | varchar(255) |      | YES  |      |        |
|     `rate`     |   汇率   | varchar(255) |      | YES  |      |        |

#### 3、 bol_gov_la

老挝央行

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   日期   |   datetime   |      | YES  |      |        |
|     `name`     | 表头名称 | varchar(255) |      | YES  |      |        |
|     `buy`      |  购买率  | varchar(255) |      | YES  |      |        |
|     `sell`     |  售卖率  | varchar(255) |      | YES  |      |        |
|   `average`    |  中间价  | varchar(255) |      | YES  |      |        |

#### 4、 bot_or_th

泰国央行

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   日期   |   datetime   |      | YES  |      |        |
|     `name`     | 表头名称 | varchar(255) |      | YES  |      |        |
|     `buy`      |  购买率  | varchar(255) |      | YES  |      |        |
|     `sell`     |  售卖率  | varchar(255) |      | YES  |      |        |
|   `average`    |  中间价  | varchar(255) |      | YES  |      |        |

#### 5、 bsp_gov_ph

菲律宾央行

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   日期   | varchar(255) |      | YES  |      |        |
|     `name`     | 表头名称 | varchar(255) |      | YES  |      |        |
|   `average`    |  中间价  | varchar(255) |      | YES  |      |        |

#### 6、 cbm_gov_mm

缅甸央行

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   日期   | varchar(255) |      | YES  |      |        |
|     `name`     | 表头名称 | varchar(255) |      | YES  |      |        |
|   `average`    |  中间价  | varchar(255) |      | YES  |      |        |

#### 7、 cdmjgzs

中价•柴达木氯化钾价格指数

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` | 指数日期 | varchar(255) |      | YES  |      |        |
|     `name`     | 指数名称 | varchar(255) |      | YES  |      |        |
|    `index`     | 指数数值 | varchar(255) |      | YES  |      |        |

#### 8、 cdmjgzs2

中价•柴达木纯碱价格指数

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` | 指数日期 | varchar(255) |      | YES  |      |        |
|     `name`     | 指数名称 | varchar(255) |      | YES  |      |        |
|    `index`     | 指数数值 | varchar(255) |      | YES  |      |        |

#### 9、 cnhnb

惠农网的花椒价格

|      名称      |   描述    |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :-------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   时间    |   datetime   |      | YES  |      |        |
|     `name`     | 表头名称  | varchar(255) |      | YES  |      |        |
|   `product`    | 产品/品种 | varchar(255) |      | YES  |      |        |
|    `place`     | 所在产地  | varchar(255) |      | YES  |      |        |
|    `price`     |   价格    | varchar(255) |      | YES  |      |        |
|     `rate`     |   升/降   | varchar(255) |      | YES  |      |        |
|    `state`     |   走势    | varchar(255) |      | YES  |      |        |

#### 10、 e658

中国辣椒网相关信息

|   名称   |    描述    |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------: | :--------: | :----------: | :--: | :--: | :--: | :----: |
| `place`  |    地区    | varchar(255) |      | YES  |      |        |
| `source` |    货源    | varchar(255) |      | YES  |      |        |
|  `name`  |    品种    | varchar(255) |      | YES  |      |        |
|  `unit`  |    单位    | varchar(255) |      | YES  |      |        |
|  `low`   | 价格区间低 | varchar(255) |      | YES  |      |        |
|  `high`  | 价格区间高 | varchar(255) |      | YES  |      |        |
| `level`  |    品质    | varchar(255) |      | YES  |      |        |
|  `date`  |    日期    | varchar(255) |      | YES  |      |        |

#### 11、 gjjgzs

国际大宗商品价格指数

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` | 指数日期 | varchar(255) |      | YES  |      |        |
|     `name`     | 指数名称 | varchar(255) |      | YES  |      |        |
|    `index`     | 指数数值 | varchar(255) |      | YES  |      |        |

#### 12、 huajiao

中国花椒网的花椒价格

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
|    `market`    |   市场   | varchar(255) |      | YES  |      |        |
|    `region`    |   地区   | varchar(255) |      | YES  |      |        |
|    `source`    | 报价公司 | varchar(255) |      | YES  |      |        |
|    `remark`    |   备注   | varchar(255) |      | YES  |      |        |
|     `name`     |   品名   | varchar(255) |      | YES  |      |        |
|    `price`     | 最新报价 | varchar(255) |      | YES  |      |        |
|     `unit`     |   单位   | varchar(255) |      | YES  |      |        |
| `publish_time` | 报价时间 |   datetime   |      | YES  |      |        |

#### 13、 lssgjgzs

中价•粮食收购价格指数

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` | 发布时间 | varchar(255) |      | YES  |      |        |
|     `name`     | 指数名称 | varchar(255) |      | YES  |      |        |
|    `index`     | 指数数值 |  bigint(20)  |      | YES  |      |        |

#### 14、 mas_gov_sg

新加坡央行

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   日期   | varchar(255) |      | YES  |      |        |
|     `name`     | 表头名称 | varchar(255) |      | YES  |      |        |
|     `rate`     |   汇率   | varchar(255) |      | YES  |      |        |

#### 15、 mkdatapfx

外汇交易中心人民币兑美元即期

|      名称       |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :-------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time`  | 更新时间 | varchar(255) |      | YES  |      |        |
|   `lastDate`    | 更新日期 | varchar(255) |      | YES  |      |        |
| `spotPriceStr`  |  成交价  | varchar(255) |      | YES  |      |        |
| `spotAmountStr` | 日成交量 | varchar(255) |      | YES  |      |        |

#### 16、 mtdexbond

外汇交易中心活跃债券统计

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    统计日期    | varchar(255) |      | YES  |      |        |
|    `index`     |      名次      | varchar(255) |      | YES  |      |        |
|    `bondNm`    |    债券简称    | varchar(255) |      | YES  |      |        |
|   `dealVol`    | 成交金额(亿元) | varchar(255) |      | YES  |      |        |
|   `dealCnt`    |      笔数      | varchar(255) |      | YES  |      |        |
|  `yieldRate`   | 到期收益率(%)  | varchar(255) |      | YES  |      |        |

#### 17、 mtdexdaily_bond

外汇交易中心统计日报_债券分类成交情况(按债券类型分类)

|        名称         |       描述        |     类型     |  键  | 为空 | 额外 | 默认值 |
| :-----------------: | :---------------: | :----------: | :--: | :--: | :--: | :----: |
|   `publish_time`    |     发布时间      | varchar(255) |      | YES  |      |        |
|     `bondType`      |     债券种类      | varchar(255) |      | YES  |      |        |
|      `dealAmt`      |  成交金额(亿元)   | varchar(255) |      | YES  |      |        |
|    `dealAmtIncr`    |    增减(亿元)     | varchar(255) |      | YES  |      |        |
| `dealAmtRatioOnTtl` | 占总成交的比例(%) | varchar(255) |      | YES  |      |        |
|      `dealCnt`      |   成交笔数(笔)    | varchar(255) |      | YES  |      |        |
|    `dealCntIncr`    |     增减(笔)      | varchar(255) |      | YES  |      |        |

#### 18、 mtdexdaily_compen

外汇交易中心统计日报_债券分类成交情况(按待偿期分类)

|        名称         |       描述        |     类型     |  键  | 为空 | 额外 | 默认值 |
| :-----------------: | :---------------: | :----------: | :--: | :--: | :--: | :----: |
|   `publish_time`    |     发布时间      | varchar(255) |      | YES  |      |        |
|      `dealAmt`      |  成交金额(亿元)   | varchar(255) |      | YES  |      |        |
|    `dealAmtIncr`    |    增减(亿元)     | varchar(255) |      | YES  |      |        |
| `dealAmtRatioOnTtl` | 占总成交的比例(%) | varchar(255) |      | YES  |      |        |
|      `dealCnt`      |   成交笔数(笔)    | varchar(255) |      | YES  |      |        |
|    `dealCntIncr`    |     增减(笔)      | varchar(255) |      | YES  |      |        |
|  `termToMtrtyCde`   |    待偿期(年)     | varchar(255) |      | YES  |      |        |

#### 19、 mtdexdaily_interest

外汇交易中心统计日报_债券分类成交情况(按计息方式分类)

|        名称         |       描述        |     类型     |  键  | 为空 | 额外 | 默认值 |
| :-----------------: | :---------------: | :----------: | :--: | :--: | :--: | :----: |
|   `publish_time`    |     发布时间      | varchar(255) |      | YES  |      |        |
|     `bondName`      |     债券类型      | varchar(255) |      | YES  |      |        |
|      `dealAmt`      |  成交金额(亿元)   | varchar(255) |      | YES  |      |        |
|    `dealAmtIncr`    |    增减(亿元)     | varchar(255) |      | YES  |      |        |
| `dealAmtRatioOnTtl` | 占总成交的比例(%) | varchar(255) |      | YES  |      |        |
|      `dealCnt`      |   成交笔数(笔)    | varchar(255) |      | YES  |      |        |
|    `dealCntIncr`    |     增减(笔)      | varchar(255) |      | YES  |      |        |

#### 20、 mtdexdaily_mark

外汇交易中心统计日报_市场成交情况

|        名称        |      描述       |     类型     |  键  | 为空 | 额外 | 默认值 |
| :----------------: | :-------------: | :----------: | :--: | :--: | :--: | :----: |
|   `publish_time`   |    更新时间     |   datetime   |      | YES  |      |        |
|     `dealCnt`      |  成交笔数(笔)   | varchar(255) |      | YES  |      |        |
|   `dealCntIncr`    |    增减(笔)     | varchar(255) |      | YES  |      |        |
|     `dealAmt`      | 成交金额(亿元)  | varchar(255) |      | YES  |      |        |
|   `dealAmtIncr`    |   增减(亿元)    | varchar(255) |      | YES  |      |        |
|   `weigthedRate`   | 加权平均利率(%) | varchar(255) |      | YES  |      |        |
| `weigthedRateIncr` |   升降(基点)    | varchar(255) |      | YES  |      |        |
|    `memberCnt`     | 参与成员数(家)  | varchar(255) |      | YES  |      |        |

#### 21、 mtdexdaily_rate

外汇交易中心统计日报_利率互换日报

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` | 更新时间 |   datetime   |      | YES  |      |        |
|   `refRate`    | 参考利率 | varchar(255) |      | YES  |      |        |
|     `term`     |   期限   | varchar(255) |      | YES  |      |        |
|   `fixRate`    | 固定利率 | varchar(255) |      | YES  |      |        |

#### 22、 mtdexdaily_sbf_mark

外汇交易中心统计日报_标准债券远期成交情况(standardized bond forward)

|      名称      |       描述       |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :--------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |     发布时间     | varchar(255) |      | YES  |      |        |
|     `dlNo`     |   成交笔数(笔)   | varchar(255) |      | YES  |      |        |
| `dlNoDiffQnty` |     增减(笔)     | varchar(255) |      | YES  |      |        |
|  `prtcpntNo`   |  参与成员数(家)  | varchar(255) |      | YES  |      |        |
|    `trdVol`    | 成交金额(百万元) | varchar(255) |      | YES  |      |        |
| `volDiffQnty`  |   增减(百万元)   | varchar(255) |      | YES  |      |        |
| `wghtdTrdPrc`  |  加权成交价(元)  | varchar(255) |      | YES  |      |        |

#### 23、 mtdexdaily_sbf_term

外汇交易中心统计日报_标准债券远期分类成交情况(按交易品种分类)(standardized bond forward)

|      名称      |       描述        |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :---------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |     发布时间      | varchar(255) |      | YES  |      |        |
|   `instrmnt`   |     交易品种      | varchar(255) |      | YES  |      |        |
|  `cntrctVrty`  |     合约品种      | varchar(255) |      | YES  |      |        |
|     `dlNo`     |   成交笔数(笔)    | varchar(255) |      | YES  |      |        |
| `dlNoDiffQnty` |     增减(笔)      | varchar(255) |      | YES  |      |        |
|    `trdVol`    | 成交金额(百万元)  | varchar(255) |      | YES  |      |        |
|  `trdngRate`   | 占总成交的比例(%) | varchar(255) |      | YES  |      |        |
| `volDiffQnty`  |   增减(百万元)    | varchar(255) |      | YES  |      |        |

#### 24、 mtdexdaily_term

外汇交易中心统计日报_各期限品种成交情况

|        名称        |       描述       |     类型     |  键  | 为空 | 额外 | 默认值 |
| :----------------: | :--------------: | :----------: | :--: | :--: | :--: | :----: |
|   `publish_time`   |     更新时间     |   datetime   |      | YES  |      |        |
|    `trdPrdCde`     |       品种       | varchar(255) |      | YES  |      |        |
|     `operRate`     |   开盘利率(%)    | varchar(255) |      | YES  |      |        |
|    `closeRate`     |   收盘利率(%)    | varchar(255) |      | YES  |      |        |
|   `weightedRate`   |   加权利率(%)    | varchar(255) |      | YES  |      |        |
| `weightedRateIncr` |    升降(基点)    | varchar(255) |      | YES  |      |        |
| `rssAvgLimitDate`  | 平均拆借期限(天) | varchar(255) |      | YES  |      |        |
|     `dealCnt`      |   成交笔数(笔)   | varchar(255) |      | YES  |      |        |
|   `dealCntIncr`    |     增减(笔)     | varchar(255) |      | YES  |      |        |
|     `dealAmt`      |  成交金额(亿元)  | varchar(255) |      | YES  |      |        |
|   `dealAmtIncr`    |    增减(亿元)    | varchar(255) |      | YES  |      |        |

#### 25、 mtdexorgtrade

外汇交易中心机构交易情况

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    更新时间    | varchar(255) |      | YES  |      |        |
|     `type`     |    机构类别    | varchar(255) |      | YES  |      |        |
|    `amount`    | 成交金额(亿元) | varchar(255) |      | YES  |      |        |
|     `rate`     |    占比(%)     | varchar(255) |      | YES  |      |        |

#### 26、 mtmoncjgl_bondforwarddeal

外汇交易中心统计月报-成交概览_标准债券远期成交情况

|      名称      |       描述       |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :--------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |     发布时间     | varchar(255) |      | YES  |      |        |
|     `dlNo`     |   成交笔数(笔)   | varchar(255) |      | YES  |      |        |
| `dlNoDiffQnty` |     增减(笔)     | varchar(255) |      | YES  |      |        |
|  `prtcpntNo`   |  参与成员数(家)  | varchar(255) |      | YES  |      |        |
|    `trdVol`    | 成交金额(百万元) | varchar(255) |      | YES  |      |        |
| `volDiffQnty`  |   增减(百万元)   | varchar(255) |      | YES  |      |        |
| `wghtdTrdPrc`  |  加权成交价(元)  | varchar(255) |      | YES  |      |        |

#### 27、 mtmoncjgl_bondforwardtrd

外汇交易中心统计月报-成交概览_标准债券远期分类成交情况(按交易品种分类)

|      名称      |       描述        |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :---------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |     发布时间      | varchar(255) |      | YES  |      |        |
|   `instrmnt`   |     交易品种      | varchar(255) |      | YES  |      |        |
|     `dlNo`     |   成交笔数(笔)    | varchar(255) |      | YES  |      |        |
| `dlNoDiffQnty` |     增减(笔)      | varchar(255) |      | YES  |      |        |
|    `trdVol`    | 成交金额(百万元)  | varchar(255) |      | YES  |      |        |
| `volDiffQnty`  |   增减(百万元)    | varchar(255) |      | YES  |      |        |
|  `trdngRate`   | 占总成交的比例(%) | varchar(255) |      | YES  |      |        |

#### 28、 mtmoncjgl_btvo

外汇交易中心统计月报-成交概览_按债券类别分类统计

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    发布时间    | varchar(255) |      | YES  |      |        |
|     `amt`      | 成交金额(亿元) | varchar(255) |      | YES  |      |        |
|     `cnt`      |  成交笔数(笔)  | varchar(255) |      | YES  |      |        |
|     `rate`     | 到期收益率(%)  | varchar(255) |      | YES  |      |        |
|     `term`     |    债券种类    | varchar(255) |      | YES  |      |        |

#### 29、 mtmoncjgl_cbtmthbltn

外汇交易中心统计月报-成交概览_按机构类别分类

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    发布时间    | varchar(255) |      | YES  |      |        |
|     `amt`      | 成交金额(亿元) | varchar(255) |      | YES  |      |        |
|     `cnt`      |  成交笔数(笔)  | varchar(255) |      | YES  |      |        |
|     `rate`     | 到期收益率(%)  | varchar(255) |      | YES  |      |        |
|     `term`     |    机构类型    | varchar(255) |      | YES  |      |        |

#### 30、 mtmoncjgl_cpairmthbltn

外汇交易中心统计月报-成交概览_外币对即期

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    发布时间    | varchar(255) |      | YES  |      |        |
|  `ccyPairCd`   |      外币      | varchar(255) |      | YES  |      |        |
|  `cnyAmntStr`  | 交易金额(亿元) | varchar(255) |      | YES  |      |        |
|   `ratIoStr`   |    占比(%)     | varchar(255) |      | YES  |      |        |

#### 31、 mtmoncjgl_cpvo

外汇交易中心统计月报-成交概览_按待偿期分类统计

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    发布时间    | varchar(255) |      | YES  |      |        |
|     `amt`      | 成交金额(亿元) | varchar(255) |      | YES  |      |        |
|     `cnt`      |  成交笔数(笔)  | varchar(255) |      | YES  |      |        |
|     `rate`     | 到期收益率(%)  | varchar(255) |      | YES  |      |        |
|     `term`     |   待偿期(年)   | varchar(255) |      | YES  |      |        |

#### 32、 mtmoncjgl_dealtype

外汇交易中心统计月报-成交概览_按交易品种

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    发布时间    | varchar(255) |      | YES  |      |        |
|     `amt`      | 成交金额(亿元) | varchar(255) |      | YES  |      |        |
|     `cnt`      |    成交笔数    | varchar(255) |      | YES  |      |        |
|     `rate`     |  加权利率(%)   | varchar(255) |      | YES  |      |        |
|     `type`     |      品种      | varchar(255) |      | YES  |      |        |

#### 33、 mtmoncjgl_fxcl

外汇交易中心统计月报-成交概览_外币拆借

|      名称      |       描述       |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :--------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |     发布时间     | varchar(255) |      | YES  |      |        |
|     `ccy`      |       币种       | varchar(255) |      | YES  |      |        |
|     `dlNo`     |     成交笔数     | varchar(255) |      | YES  |      |        |
|   `trdAmnt`    | 成交金额(亿美元) | varchar(255) |      | YES  |      |        |

#### 34、 mtmoncjgl_imvo

外汇交易中心统计月报-成交概览_按计息方式分类

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    发布时间    | varchar(255) |      | YES  |      |        |
|     `amt`      | 成交金额(亿元) | varchar(255) |      | YES  |      |        |
|     `cnt`      |  成交笔数(笔)  | varchar(255) |      | YES  |      |        |
|     `rate`     | 到期收益率(%)  | varchar(255) |      | YES  |      |        |
|     `term`     |    债券类型    | varchar(255) |      | YES  |      |        |

#### 35、 mtmoncjgl_ittvo

外汇交易中心统计月报-成交概览_按机构类别余额统计

|      名称      |    描述    |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :--------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |  发布时间  | varchar(255) |      | YES  |      |        |
|     `type`     |  机构类型  | varchar(255) |      | YES  |      |        |
|     `rate`     | 余额(亿元) | varchar(255) |      | YES  |      |        |

#### 36、 mtmoncjgl_organdeal

外汇交易中心统计月报-成交概览_按机构类别交易统计

|      名称      |      描述       |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :-------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    发布时间     | varchar(255) |      | YES  |      |        |
|     `amt`      | 成交金额(亿元)  | varchar(255) |      | YES  |      |        |
|     `cnt`      |    成交笔数     | varchar(255) |      | YES  |      |        |
|     `rate`     | 加权平均利率(%) | varchar(255) |      | YES  |      |        |
|     `type`     |    机构类型     | varchar(255) |      | YES  |      |        |

#### 37、 mtmoncjgl_ormthbltn

外汇交易中心统计月报-成交概览_按券种统计

|      名称      |     描述     |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :----------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   发布时间   | varchar(255) |      | YES  |      |        |
|     `amt`      | 成交量(亿元) | varchar(255) |      | YES  |      |        |
|     `type`     |   债券种类   | varchar(255) |      | YES  |      |        |

#### 38、 mtmoncjgl_rate

外汇交易中心统计月报-成交概览_利率互换

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    发布时间    | varchar(255) |      | YES  |      |        |
|     `rate`     |    参考利率    | varchar(255) |      | YES  |      |        |
|     `term`     |      期限      | varchar(255) |      | YES  |      |        |
|   `fixRate`    |    固定利率    | varchar(255) |      | YES  |      |        |
|   `notional`   | 名义本金(亿元) | varchar(255) |      | YES  |      |        |

#### 39、 mtmoncjgl_rfxfwmthbltn

外汇交易中心统计月报-成交概览_人民币外汇远期

|          名称          |           描述           |     类型     |  键  | 为空 | 额外 | 默认值 |
| :--------------------: | :----------------------: | :----------: | :--: | :--: | :--: | :----: |
|     `publish_time`     |         发布时间         | varchar(255) |      | YES  |      |        |
|      `cnyAmntStr`      | 合计折元成交金额(百万元) | varchar(255) |      | YES  |      |        |
|       `dlNumStr`       |     合计折元成交笔数     | varchar(255) |      | YES  |      |        |
|        `tnrCd`         |         期限品种         | varchar(255) |      | YES  |      |        |
|    `usdCnyDlNumStr`    |     USD.CNY成交笔数      | varchar(255) |      | YES  |      |        |
| `usdCnyNlegCnyAmntStr` | USD.CNY成交金额(百万元)  | varchar(255) |      | YES  |      |        |

#### 40、 mtmoncjgl_rfxsomthbltn

外汇交易中心统计月报-成交概览_人民币外汇期权

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    发布时间    | varchar(255) |      | YES  |      |        |
|   `dealAmt`    | 成交金额(亿元) | varchar(255) |      | YES  |      |        |
|   `dealCnt`    |    成交笔数    | varchar(255) |      | YES  |      |        |
|    `tnrCd`     |    期权期限    | varchar(255) |      | YES  |      |        |

#### 41、 mtmoncjgl_rfxspmthbltn

外汇交易中心统计月报-成交概览_人民币外汇即期

|        名称        |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :----------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
|   `publish_time`   |    发布时间    | varchar(255) |      | YES  |      |        |
|    `ccyPairCd`     |      币种      | varchar(255) |      | YES  |      |        |
|    `cnyAmntStr`    | 成交金额(亿元) | varchar(255) |      | YES  |      |        |
|     `dlNumStr`     |    成交笔数    | varchar(255) |      | YES  |      |        |
| `wghtdAvgPriceStr` |     加权价     | varchar(255) |      | YES  |      |        |

#### 42、 mtmoncjgl_rmbfxswap

外汇交易中心统计月报-成交概览_人民币外汇掉期外汇货币掉期

|          名称          |          描述          |     类型     |  键  | 为空 | 额外 | 默认值 |
| :--------------------: | :--------------------: | :----------: | :--: | :--: | :--: | :----: |
|     `publish_time`     |        发布时间        | varchar(255) |      | YES  |      |        |
|      `cnyAmntStr`      | 合计折元成交金额(亿元) | varchar(255) |      | YES  |      |        |
|       `dlNumStr`       |    合计折元成交笔数    | varchar(255) |      | YES  |      |        |
|        `tnrCd`         |        期限品种        | varchar(255) |      | YES  |      |        |
|    `usdCnyDlNumStr`    |    USD.CNY成交笔数     | varchar(255) |      | YES  |      |        |
| `usdCnyNlegCnyAmntStr` | USD.CNY成交金额(亿元)  | varchar(255) |      | YES  |      |        |

#### 43、 mtmondqtj

外汇交易中心统计月报-地区统计

|      名称      |      描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    更新时间    | varchar(255) |      | YES  |      |        |
|   `province`   |     省/市      | varchar(255) |      | YES  |      |        |
|      `in`      | 融入金额(亿元) | varchar(255) |      | YES  |      |        |
|    `in_per`    | 融入占市场(%)  | varchar(255) |      | YES  |      |        |
|     `out`      | 融出金额(亿元) | varchar(255) |      | YES  |      |        |
|   `put_per`    | 融出占市场(%)  | varchar(255) |      | YES  |      |        |
|    `month`     |    统计月份    | varchar(255) |      | YES  |      |        |

#### 44、 nafmii_org_cn

银行间交易商协会

|      名称      | 描述 |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :--: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` | 日期 |   datetime   |      | YES  |      |        |
|    `class`     | 分类 | varchar(255) |      | YES  |      |        |
|   `deadline`   | 期限 | varchar(255) |      | YES  |      |        |
|  `valuation`   | 估值 | varchar(255) |      | YES  |      |        |

#### 45、 nafmii_org_cn_detailshowframe

银行间交易商协会各估值机构原始报价

|      名称      | 描述 |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :--: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` | 日期 |   datetime   |      | YES  |      |        |
|     `bank`     | 银行 | varchar(255) |      | YES  |      |        |
|    `class`     | 分类 | varchar(255) |      | YES  |      |        |
|   `deadline`   | 期限 | varchar(255) |      | YES  |      |        |
|  `valuation`   | 估值 | varchar(255) |      | YES  |      |        |

#### 46、 news_attachment_a

附件A资讯网站

|           名称           |                       描述                        |        类型         |  键  | 为空 |            额外             |      默认值       |
| :----------------------: | :-----------------------------------------------: | :-----------------: | :--: | :--: | :-------------------------: | :---------------: |
|           `id`           |                                                   | bigint(11) unsigned | PRI  |  NO  |       auto_increment        |                   |
|       `news_type`        |           新闻类型（资讯，公告，纰漏）            |    varchar(255)     |      | YES  |                             |                   |
|         `title`          |                       标题                        |    varchar(255)     | MUL  | YES  |                             |                   |
|        `content`         |                     新闻详情                      |      longtext       |      | YES  |                             |                   |
|      `content_html`      |                新闻详情带html标签                 |      longtext       |      | YES  |                             |                   |
|      `content_md5`       |                  新闻详情内容md5                  |    varchar(255)     | MUL  | YES  |                             |                   |
|        `abstract`        |                     新闻摘要                      |        text         |      | YES  |                             |                   |
|          `tag`           |                       标签                        |    varchar(255)     |      | YES  |                             |                   |
|        `language`        |                     新闻语言                      |     varchar(10)     |      | YES  |                             |                   |
|      `opinion_tag`       |                     舆情标签                      |    varchar(255)     |      | YES  |                             |                   |
|       `risk_type`        |                   一级风险标签                    |    varchar(255)     |      | YES  |                             |                   |
|       `risk_score`       |                     风险分数                      |    varchar(255)     |      | YES  |                             |                   |
|        `risk_tag`        |                     风险标签                      |    varchar(512)     |      | YES  |                             |                   |
|      `publish_org`       |                   新闻发布来源                    |    varchar(255)     |      | YES  |                             |                   |
|      `publish_time`      |                   新闻发布时间                    |      datetime       | MUL  | YES  |                             |                   |
|      `positive_org`      |                  正面舆情公司名                   |    varchar(255)     |      | YES  |                             |                   |
|   `positive_org_score`   |                 正面舆情公司分数                  |    varchar(255)     |      | YES  |                             |                   |
|      `negative_org`      |                  负面舆情公司名                   |    varchar(255)     |      | YES  |                             |                   |
|       `neutra_org`       |                  中性舆情公司名                   |        text         |      | YES  |                             |                   |
|    `neutra_org_score`    |                 中性舆情公司分数                  |    varchar(255)     |      | YES  |                             |                   |
|   `negative_org_score`   |                 负面舆情公司分数                  |    varchar(255)     |      | YES  |                             |                   |
|   `article_file_name`    |                     附件名称                      |        text         |      | YES  |                             |                   |
|    `article_file_url`    |                     附件地址                      |        text         |      | YES  |                             |                   |
|      `create_time`       |                     入库时间                      |      datetime       | MUL  | YES  |                             | CURRENT_TIMESTAMP |
|      `update_time`       |                     更新时间                      |      datetime       |      | YES  | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
|         `status`         |                  0未清洗 1已清洗                  |       int(11)       |      | YES  |                             |         0         |
|       `is_delete`        |                  0未删除 1已删除                  |       int(11)       |      | YES  |                             |         0         |
|         `author`         |                       作者                        |    varchar(255)     |      | YES  |                             |                   |
|      `author_info`       |                     作者简介                      |    varchar(255)     |      | YES  |                             |                   |
|        `company`         |                   新闻涉及公司                    |        text         |      | YES  |                             |                   |
|        `web_site`        |                来源网站，如财经网                 |    varchar(255)     | MUL  | YES  |                             |                   |
|       `event_tag`        |                     事件标签                      |    varchar(255)     |      | YES  |                             |                   |
|      `emotion_tag`       |                     情感标签                      |    varchar(255)     |      | YES  |                             |                   |
|       `region_tag`       |                     地区标签                      |    varchar(255)     |      | YES  |                             |                   |
|         `likes`          |                      点赞数                       |       int(11)       |      | YES  |                             |                   |
|          `hits`          |                   点击量访问量                    |       int(11)       |      | YES  |                             |                   |
|      `web_site_url`      |                   来源网站地址                    |    varchar(255)     |      | YES  |                             |                   |
|      `content_url`       |                    正文详情url                    |    varchar(1000)    |      | YES  |                             |                   |
|     `office_account`     |                      公众号                       |    varchar(255)     |      | YES  |                             |                   |
|  `office_account_info`   |                    公众号简介                     |    varchar(255)     |      | YES  |                             |                   |
|        `replies`         |                      评论数                       |       int(11)       |      | YES  |                             |                   |
|       `batch_date`       |                     批次时间                      |        date         | MUL  | YES  |                             |                   |
|         `run_id`         |               采集系统内置的run_id                |     bigint(20)      | MUL  | YES  |                             |                   |
|       `is_company`       |             0不是公司资讯1是公司资讯              |       int(11)       |      | YES  |                             |                   |
|        `emotion`         |                     资讯情感                      |    varchar(255)     |      | YES  |                             |                   |
|     `emotion_score`      |                     情感分数                      |    varchar(255)     |      | YES  |                             |                   |
|       `company_id`       |                   对应的公司id                    |    varchar(255)     |      | YES  |                             |                   |
|         `extra`          |                附加数据，json格式                 |        text         |      | YES  |                             |                   |
| `local_article_file_url` |                 本地附件存放地址                  |        text         |      | YES  |                             |                   |
|      `source_type`       | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） |       int(11)       |      | YES  |                             |         1         |
|       `copyright`        |          0:不存在版权问题，1存在版权问题          |       int(11)       |      | YES  |                             |         0         |
|      `product_tag`       |                     产品标签                      |    varchar(1024)    |      | YES  |                             |                   |
|      `industry_tag`      |                     行业标签                      |    varchar(1024)    |      | YES  |                             |                   |

#### 47、 sbv_gov_vn

越南央行

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   日期   | varchar(255) |      | YES  |      |        |
|     `name`     | 表头名称 | varchar(255) |      | YES  |      |        |
|   `average`    |  中间价  | varchar(255) |      | YES  |      |        |

#### 48、 shclearing_dqsylqx

上海清算所债券收益率曲线

|      名称      |     描述     |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :----------: | :----------: | :--: | :--: | :--: | :----: |
|  `curvedate`   |   曲线日期   | varchar(255) |      | YES  |      |        |
|  `curveName`   |   曲线名称   | varchar(255) |      | YES  |      |        |
| `standardterm` | 曲线标准期限 | varchar(255) |      | YES  |      |        |
|    `yield`     |    收益率    | varchar(255) |      | YES  |      |        |
|  `nyearValue`  |     N值      | varchar(255) |      | YES  |      |        |
|  `kyearValue`  |     K值      | varchar(255) |      | YES  |      |        |
|   `termdesc`   |   期限描述   | varchar(255) |      | YES  |      |        |
| `webCurveType` |   曲线类型   | varchar(255) |      | YES  |      |        |

#### 49、 shclearing_zqgz

上海清算所债券估值

|         名称          |     描述     |     类型     |  键  | 为空 | 额外 | 默认值 |
| :-------------------: | :----------: | :----------: | :--: | :--: | :--: | :----: |
|      `bondcode`       |   债券代码   | varchar(255) |      | YES  |      |        |
|      `bondAbbr`       |   债券简称   | varchar(255) |      | YES  |      |        |
|        `vdate`        |   估值日期   | varchar(255) |      | YES  |      |        |
|  `circulationplace`   |   流通场所   | varchar(255) |      | YES  |      |        |
|     `claimperiod`     |    待偿期    | varchar(255) |      | YES  |      |        |
|     `vfullprice`      | 日间估价全价 | varchar(255) |      | YES  |      |        |
| `dayaccruedinterest`  | 日间应计利息 | varchar(255) |      | YES  |      |        |
|  `estimatenetprice`   |   估价净价   | varchar(255) |      | YES  |      |        |
|    `estimateyield`    |  估价收益率  | varchar(255) |      | YES  |      |        |
|   `vfixedduration`    | 估价修正久期 | varchar(255) |      | YES  |      |        |
|     `vconvexity`      |   估价凸性   | varchar(255) |      | YES  |      |        |
|  `vbasispointvalue`   | 估价基点价值 | varchar(255) |      | YES  |      |        |
|  `vcarrylongperiod`   | 估价利差久期 | varchar(255) |      | YES  |      |        |
|  `vspreadsconvexity`  | 估价利差凸性 | varchar(255) |      | YES  |      |        |
|    `realfullprice`    |   真实全价   | varchar(255) |      | YES  |      |        |
|    `realnetprice`     |   真实净价   | varchar(255) |      | YES  |      |        |
|      `realyield`      |  真实收益率  | varchar(255) |      | YES  |      |        |
|  `realfixedduration`  | 真实修正久期 | varchar(255) |      | YES  |      |        |
|    `realconvexity`    |   真实凸性   | varchar(255) |      | YES  |      |        |
|  `rbasispointvalue`   | 真实基点价值 | varchar(255) |      | YES  |      |        |
|  `rcarrylongperiod`   | 真实利差久期 | varchar(255) |      | YES  |      |        |
|  `rspreadsconvexity`  | 真实利差凸性 | varchar(255) |      | YES  |      |        |
|     `credibility`     |    可信度    | varchar(255) |      | YES  |      |        |
|   `vratelongperiod`   | 估价利率久期 | varchar(255) |      | YES  |      |        |
|   `vrateconvexity`    | 估价利率凸性 | varchar(255) |      | YES  |      |        |
|   `rratelongperiod`   | 真实利率久期 | varchar(255) |      | YES  |      |        |
|   `rrateconvexity`    | 真实利率凸性 | varchar(255) |      | YES  |      |        |
|    `edayfullprice`    | 日终估价全价 | varchar(255) |      | YES  |      |        |
| `edayaccruedinterest` | 日终应计利息 | varchar(255) |      | YES  |      |        |
| `remainingprincipal`  |   剩余本金   | varchar(255) |      | YES  |      |        |

#### 50、 shclearing_zshq

上海清算所债券指数

|          名称           |        描述        |     类型     |  键  | 为空 | 额外 | 默认值 |
| :---------------------: | :----------------: | :----------: | :--: | :--: | :--: | :----: |
|       `indexdate`       |      指数日期      | varchar(255) |      | YES  |      |        |
|       `indexCode`       |      指数代码      | varchar(255) |      | YES  |      |        |
|     `indexNameChs`      |  指数名称（中文）  | varchar(255) |      | YES  |      |        |
|     `indexNameEng`      |  指数名称（英文）  | varchar(255) |      | YES  |      |        |
|       `indexAbbr`       |      指数简称      | varchar(255) |      | YES  |      |        |
|       `indexType`       |      指数类型      | varchar(255) |      | YES  |      |        |
|       `baseValue`       |        基数        | varchar(255) |      | YES  |      |        |
|        `divisor`        |      最新除数      | varchar(255) |      | YES  |      |        |
|      `indexValue`       |      指数数值      | varchar(255) |      | YES  |      |        |
|      `indexExtent`      |   指数涨跌幅(%)    | varchar(255) |      | YES  |      |        |
|     `indexQuantity`     |    指数样本数量    | varchar(255) |      | YES  |      |        |
|    `indexTotalValue`    |  指数总市值(亿元)  | varchar(255) |      | YES  |      |        |
|  `reinvestTotalValue`   | 再投资总市值(亿元) | varchar(255) |      | YES  |      |        |
|   `indexAverageYield`   | 指数平均收益率(%)  | varchar(255) |      | YES  |      |        |
|   `indexAverageCycle`   |  指数平均修正久期  | varchar(255) |      | YES  |      |        |
| `indexAverageConvexity` |    指数平均凸性    | varchar(255) |      | YES  |      |        |
| `indexAverageBaseValue` |  指数平均基点价值  | varchar(255) |      | YES  |      |        |

#### 51、 wh_bank_whpj

外汇交易中心部分-银行外汇牌价

|      名称      |    描述    |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :--------: | :----------: | :--: | :--: | :--: | :----: |
|     `hbmc`     |  货币名称  | varchar(255) |      | YES  |      |        |
|    `xhmrj`     | 现汇买入价 | varchar(255) |      | YES  |      |        |
|    `xcmrj`     | 现钞买入价 | varchar(255) |      | YES  |      |        |
|    `xhmcj`     | 现汇卖出价 | varchar(255) |      | YES  |      |        |
|    `xcmcj`     | 现钞卖出价 | varchar(255) |      | YES  |      |        |
|     `zsj`      |   折算价   | varchar(255) |      | YES  |      |        |
| `publish_time` |  发布日期  |     date     |      | YES  |      |        |
|     `time`     |  发布时间  |     time     |      | YES  |      |        |
| `publish_org`  |    来源    | varchar(255) |      | YES  |      |        |

#### 52、 wh_bank_xgwbckll

外汇交易中心部分-银行小额外币存款利率

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   时间   |   datetime   |      | YES  |      |        |
|   `hb_name`    |   货币   | varchar(255) |      | YES  |      |        |
|      `hq`      |   活期   | varchar(255) |      | YES  |      |        |
|     `qttz`     | 七天通知 | varchar(255) |      | YES  |      |        |
|  `one_month`   |  一个月  | varchar(255) |      | YES  |      |        |
| `three_month`  |  三个月  | varchar(255) |      | YES  |      |        |
|  `six_month`   |  六个月  | varchar(255) |      | YES  |      |        |
|   `one_year`   |   一年   | varchar(255) |      | YES  |      |        |
|   `two_year`   |   两年   | varchar(255) |      | YES  |      |        |

#### 53、 wh_rmbpjhl

外汇交易中心人民币(月/年)平均汇率

|      名称      |     描述      |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :-----------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |     时间      | varchar(255) |      | YES  |      |        |
|     `hbd`      |    货币对     | varchar(255) |      | YES  |      |        |
|      `pj`      | 月平均/年平均 | varchar(255) |      | YES  |      |        |
|      `zd`      |     涨跌      | varchar(255) |      | YES  |      |        |

#### 54、 wh_tjyb_hyzqtj

外汇交易中心统计月报-活跃债券统计(成交前十位债券交易情况)

|      名称      |       描述       |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :--------------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` | xxx注意修改类型  |   datetime   |      | YES  |      |        |
|      `mc`      |       名次       | varchar(255) |      | YES  |      |        |
|     `zqjc`     |     债券简称     | varchar(255) |      | YES  |      |        |
|     `cjje`     | 成交金额（亿元） | varchar(255) |      | YES  |      |        |
|      `bs`      |       笔数       | varchar(255) |      | YES  |      |        |
|    `dqsyl`     | 到期收益率（%）  | varchar(255) |      | YES  |      |        |
|     `tjyf`     |     统计月份     | varchar(255) |      | YES  |      |        |

#### 55、 wh_tjyb_mysjyl

外汇交易中心统计月报-每月数据一览

|      名称      |    描述     |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :---------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |    时间     |   datetime   |      | YES  |      |        |
|    `title`     |    标题     | varchar(255) |      | YES  |      |        |
| `content_url`  |    链接     | varchar(255) |      | YES  |      |        |
|   `file_url`   | PDF文件链接 | varchar(255) |      | YES  |      |        |
|  `file_name`   |  PDF文件名  | varchar(255) |      | YES  |      |        |
|     `tjyf`     |  统计月份   | varchar(255) |      | YES  |      |        |

#### 56、 zdscxx

农产品批发价格200指数

|      名称      |   描述   |     类型     |  键  | 为空 | 额外 | 默认值 |
| :------------: | :------: | :----------: | :--: | :--: | :--: | :----: |
| `publish_time` |   时间   | varchar(255) |      | YES  |      |        |
|   `product`    |   品类   | varchar(255) |      | YES  |      |        |
|     `item`     | 指标名称 | varchar(255) |      | YES  |      |        |
|    `value`     | 指标数值 | varchar(255) |      | YES  |      |        |