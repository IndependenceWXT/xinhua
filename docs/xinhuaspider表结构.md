## xinhuaspider 表结构
#### 1、 bi_go_id
印尼央行

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布日期 | datetime |  | YES |  |  |
| 9 | `name` | 表头名称 | varchar(255) |  | YES |  |  |
| 10 | `buy` | 购买率 | varchar(255) |  | YES |  |  |
| 11 | `sell` | 售卖率 | varchar(255) |  | YES |  |  |
| 12 | `average` | 中间价 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 2、 bnm_gov_my
马来西亚央行

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 日期 | varchar(255) |  | YES |  |  |
| 9 | `name` | 表头名称 | varchar(255) |  | YES |  |  |
| 10 | `rate` | 汇率 | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 3、 bol_gov_la
老挝央行

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 日期 | datetime |  | YES |  |  |
| 9 | `name` | 表头名称 | varchar(255) |  | YES |  |  |
| 10 | `buy` | 购买率 | varchar(255) |  | YES |  |  |
| 11 | `sell` | 售卖率 | varchar(255) |  | YES |  |  |
| 12 | `average` | 中间价 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 4、 bot_or_th
泰国央行

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 日期 | datetime |  | YES |  |  |
| 9 | `name` | 表头名称 | varchar(255) |  | YES |  |  |
| 10 | `buy` | 购买率 | varchar(255) |  | YES |  |  |
| 11 | `sell` | 售卖率 | varchar(255) |  | YES |  |  |
| 12 | `average` | 中间价 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 5、 bsp_gov_ph
菲律宾央行

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 日期 | varchar(255) |  | YES |  |  |
| 9 | `name` | 表头名称 | varchar(255) |  | YES |  |  |
| 10 | `average` | 中间价 | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 6、 cbm_gov_mm
缅甸央行

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 日期 | varchar(255) |  | YES |  |  |
| 9 | `name` | 表头名称 | varchar(255) |  | YES |  |  |
| 10 | `average` | 中间价 | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 7、 cdmjgzs
中价•柴达木氯化钾价格指数

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 指数日期 | varchar(255) |  | YES |  |  |
| 9 | `name` | 指数名称 | varchar(255) |  | YES |  |  |
| 10 | `index` | 指数数值 | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 8、 cdmjgzs2
中价•柴达木纯碱价格指数

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 指数日期 | varchar(255) |  | YES |  |  |
| 9 | `name` | 指数名称 | varchar(255) |  | YES |  |  |
| 10 | `index` | 指数数值 | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 9、 cnhnb
惠农网的花椒价格

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 时间 | datetime |  | YES |  |  |
| 9 | `name` | 表头名称 | varchar(255) |  | YES |  |  |
| 10 | `product` | 产品/品种 | varchar(255) |  | YES |  |  |
| 11 | `place` | 所在产地 | varchar(255) |  | YES |  |  |
| 12 | `price` | 价格 | varchar(255) |  | YES |  |  |
| 13 | `rate` | 升/降 | varchar(255) |  | YES |  |  |
| 14 | `state` | 走势 | varchar(255) |  | YES |  |  |
| 15 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 16 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 17 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 18 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 19 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 20 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 10、 e658
中国辣椒网相关信息

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `place` | 地区 | varchar(255) |  | YES |  |  |
| 9 | `source` | 货源 | varchar(255) |  | YES |  |  |
| 10 | `name` | 品种 | varchar(255) |  | YES |  |  |
| 11 | `unit` | 单位 | varchar(255) |  | YES |  |  |
| 12 | `low` | 价格区间低 | varchar(255) |  | YES |  |  |
| 13 | `high` | 价格区间高 | varchar(255) |  | YES |  |  |
| 14 | `level` | 品质 | varchar(255) |  | YES |  |  |
| 15 | `date` | 日期 | varchar(255) |  | YES |  |  |
| 16 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 17 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 18 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 19 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 20 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 21 | `extra` | 附加数据，json格式 | text |  | YES |  |  |
| 22 | `content_url` | 正文详情url | varchar(1000) |  | YES |  |  |


#### 11、 gjjgzs
国际大宗商品价格指数

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 指数日期 | varchar(255) |  | YES |  |  |
| 9 | `name` | 指数名称 | varchar(255) |  | YES |  |  |
| 10 | `index` | 指数数值 | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 12、 huajiao
中国花椒网的花椒价格

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `market` | 市场 | varchar(255) |  | YES |  |  |
| 9 | `region` | 地区 | varchar(255) |  | YES |  |  |
| 10 | `source` | 报价公司 | varchar(255) |  | YES |  |  |
| 11 | `remark` | 备注 | varchar(255) |  | YES |  |  |
| 12 | `name` | 品名 | varchar(255) |  | YES |  |  |
| 13 | `price` | 最新报价 | varchar(255) |  | YES |  |  |
| 14 | `unit` | 单位 | varchar(255) |  | YES |  |  |
| 15 | `publish_time` | 报价时间 | datetime |  | YES |  |  |
| 16 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 17 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 18 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 19 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 20 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 21 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 13、 lssgjgzs
中价•粮食收购价格指数

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `name` | 指数名称 | varchar(255) |  | YES |  |  |
| 10 | `index` | 指数数值 | bigint(20) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 14、 mas_gov_sg
新加坡央行

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 日期 | varchar(255) |  | YES |  |  |
| 9 | `name` | 表头名称 | varchar(255) |  | YES |  |  |
| 10 | `rate` | 汇率 | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 15、 mkdatapfx
外汇交易中心人民币兑美元即期

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 更新时间 | varchar(255) |  | YES |  |  |
| 9 | `lastDate` | 更新日期 | varchar(255) |  | YES |  |  |
| 10 | `spotPriceStr` | 成交价 | varchar(255) |  | YES |  |  |
| 11 | `spotAmountStr` | 日成交量 | varchar(255) |  | YES |  |  |
| 12 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 13 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 14 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 15 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 16 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 17 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 16、 mtdexbond
外汇交易中心活跃债券统计

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 统计日期 | varchar(255) |  | YES |  |  |
| 9 | `index` | 名次 | varchar(255) |  | YES |  |  |
| 10 | `bondNm` | 债券简称 | varchar(255) |  | YES |  |  |
| 11 | `dealVol` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 12 | `dealCnt` | 笔数 | varchar(255) |  | YES |  |  |
| 13 | `yieldRate` | 到期收益率(%) | varchar(255) |  | YES |  |  |
| 14 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 15 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 16 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 17 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 18 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 19 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 17、 mtdexdaily_bond
外汇交易中心统计日报_债券分类成交情况(按债券类型分类)

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `bondType` | 债券种类 | varchar(255) |  | YES |  |  |
| 10 | `dealAmt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 11 | `dealAmtIncr` | 增减(亿元) | varchar(255) |  | YES |  |  |
| 12 | `dealAmtRatioOnTtl` | 占总成交的比例(%) | varchar(255) |  | YES |  |  |
| 13 | `dealCnt` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 14 | `dealCntIncr` | 增减(笔) | varchar(255) |  | YES |  |  |
| 15 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 16 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 17 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 18 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 19 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 20 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 18、 mtdexdaily_compen
外汇交易中心统计日报_债券分类成交情况(按待偿期分类)

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `dealAmt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 10 | `dealAmtIncr` | 增减(亿元) | varchar(255) |  | YES |  |  |
| 11 | `dealAmtRatioOnTtl` | 占总成交的比例(%) | varchar(255) |  | YES |  |  |
| 12 | `dealCnt` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 13 | `dealCntIncr` | 增减(笔) | varchar(255) |  | YES |  |  |
| 14 | `termToMtrtyCde` | 待偿期(年) | varchar(255) |  | YES |  |  |
| 15 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 16 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 17 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 18 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 19 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 20 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 19、 mtdexdaily_interest
外汇交易中心统计日报_债券分类成交情况(按计息方式分类)

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `bondName` | 债券类型 | varchar(255) |  | YES |  |  |
| 10 | `dealAmt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 11 | `dealAmtIncr` | 增减(亿元) | varchar(255) |  | YES |  |  |
| 12 | `dealAmtRatioOnTtl` | 占总成交的比例(%) | varchar(255) |  | YES |  |  |
| 13 | `dealCnt` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 14 | `dealCntIncr` | 增减(笔) | varchar(255) |  | YES |  |  |
| 15 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 16 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 17 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 18 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 19 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 20 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 20、 mtdexdaily_mark
外汇交易中心统计日报_市场成交情况

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 更新时间 | datetime |  | YES |  |  |
| 9 | `dealCnt` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 10 | `dealCntIncr` | 增减(笔) | varchar(255) |  | YES |  |  |
| 11 | `dealAmt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 12 | `dealAmtIncr` | 增减(亿元) | varchar(255) |  | YES |  |  |
| 13 | `weigthedRate` | 加权平均利率(%) | varchar(255) |  | YES |  |  |
| 14 | `weigthedRateIncr` | 升降(基点) | varchar(255) |  | YES |  |  |
| 15 | `memberCnt` | 参与成员数(家) | varchar(255) |  | YES |  |  |
| 16 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 17 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 18 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 19 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 20 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 21 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 21、 mtdexdaily_rate
外汇交易中心统计日报_利率互换日报

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 更新时间 | datetime |  | YES |  |  |
| 9 | `refRate` | 参考利率 | varchar(255) |  | YES |  |  |
| 10 | `term` | 期限 | varchar(255) |  | YES |  |  |
| 11 | `fixRate` | 固定利率 | varchar(255) |  | YES |  |  |
| 12 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 13 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 14 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 15 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 16 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 17 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 22、 mtdexdaily_sbf_mark
外汇交易中心统计日报_标准债券远期成交情况(standardized bond forward)

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `dlNo` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 10 | `dlNoDiffQnty` | 增减(笔) | varchar(255) |  | YES |  |  |
| 11 | `prtcpntNo` | 参与成员数(家) | varchar(255) |  | YES |  |  |
| 12 | `trdVol` | 成交金额(百万元) | varchar(255) |  | YES |  |  |
| 13 | `volDiffQnty` | 增减(百万元) | varchar(255) |  | YES |  |  |
| 14 | `wghtdTrdPrc` | 加权成交价(元) | varchar(255) |  | YES |  |  |
| 15 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 16 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 17 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 18 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 19 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 20 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 23、 mtdexdaily_sbf_term
外汇交易中心统计日报_标准债券远期分类成交情况(按交易品种分类)(standardized bond forward)

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `instrmnt` | 交易品种 | varchar(255) |  | YES |  |  |
| 10 | `cntrctVrty` | 合约品种 | varchar(255) |  | YES |  |  |
| 11 | `dlNo` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 12 | `dlNoDiffQnty` | 增减(笔) | varchar(255) |  | YES |  |  |
| 13 | `trdVol` | 成交金额(百万元) | varchar(255) |  | YES |  |  |
| 14 | `trdngRate` | 占总成交的比例(%) | varchar(255) |  | YES |  |  |
| 15 | `volDiffQnty` | 增减(百万元) | varchar(255) |  | YES |  |  |
| 16 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 17 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 18 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 19 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 20 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 21 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 24、 mtdexdaily_term
外汇交易中心统计日报_各期限品种成交情况

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 更新时间 | datetime |  | YES |  |  |
| 9 | `trdPrdCde` | 品种 | varchar(255) |  | YES |  |  |
| 10 | `operRate` | 开盘利率(%) | varchar(255) |  | YES |  |  |
| 11 | `closeRate` | 收盘利率(%) | varchar(255) |  | YES |  |  |
| 12 | `weightedRate` | 加权利率(%) | varchar(255) |  | YES |  |  |
| 13 | `weightedRateIncr` | 升降(基点) | varchar(255) |  | YES |  |  |
| 14 | `rssAvgLimitDate` | 平均拆借期限(天) | varchar(255) |  | YES |  |  |
| 15 | `dealCnt` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 16 | `dealCntIncr` | 增减(笔) | varchar(255) |  | YES |  |  |
| 17 | `dealAmt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 18 | `dealAmtIncr` | 增减(亿元) | varchar(255) |  | YES |  |  |
| 19 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 20 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 21 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 22 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 23 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 24 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 25、 mtdexorgtrade
外汇交易中心机构交易情况

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 更新时间 | varchar(255) |  | YES |  |  |
| 9 | `type` | 机构类别 | varchar(255) |  | YES |  |  |
| 10 | `amount` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 11 | `rate` | 占比(%) | varchar(255) |  | YES |  |  |
| 12 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 13 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 14 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 15 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 16 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 17 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 26、 mtmoncjgl_bondforwarddeal
外汇交易中心统计月报-成交概览_标准债券远期成交情况

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `dlNo` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 10 | `dlNoDiffQnty` | 增减(笔) | varchar(255) |  | YES |  |  |
| 11 | `prtcpntNo` | 参与成员数(家) | varchar(255) |  | YES |  |  |
| 12 | `trdVol` | 成交金额(百万元) | varchar(255) |  | YES |  |  |
| 13 | `volDiffQnty` | 增减(百万元) | varchar(255) |  | YES |  |  |
| 14 | `wghtdTrdPrc` | 加权成交价(元) | varchar(255) |  | YES |  |  |
| 15 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 16 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 17 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 18 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 19 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 20 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 27、 mtmoncjgl_bondforwardtrd
外汇交易中心统计月报-成交概览_标准债券远期分类成交情况(按交易品种分类)

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `instrmnt` | 交易品种 | varchar(255) |  | YES |  |  |
| 10 | `dlNo` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 11 | `dlNoDiffQnty` | 增减(笔) | varchar(255) |  | YES |  |  |
| 12 | `trdVol` | 成交金额(百万元) | varchar(255) |  | YES |  |  |
| 13 | `volDiffQnty` | 增减(百万元) | varchar(255) |  | YES |  |  |
| 14 | `trdngRate` | 占总成交的比例(%) | varchar(255) |  | YES |  |  |
| 15 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 16 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 17 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 18 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 19 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 20 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 28、 mtmoncjgl_btvo
外汇交易中心统计月报-成交概览_按债券类别分类统计

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `amt` | 成交金额(亿元)	 | varchar(255) |  | YES |  |  |
| 10 | `cnt` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 11 | `rate` | 到期收益率(%) | varchar(255) |  | YES |  |  |
| 12 | `term` | 债券种类 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 29、 mtmoncjgl_cbtmthbltn
外汇交易中心统计月报-成交概览_按机构类别分类

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `amt` | 成交金额(亿元)	 | varchar(255) |  | YES |  |  |
| 10 | `cnt` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 11 | `rate` | 到期收益率(%) | varchar(255) |  | YES |  |  |
| 12 | `term` | 机构类型 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 30、 mtmoncjgl_cpairmthbltn
外汇交易中心统计月报-成交概览_外币对即期

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `ccyPairCd` | 外币 | varchar(255) |  | YES |  |  |
| 10 | `cnyAmntStr` | 交易金额(亿元) | varchar(255) |  | YES |  |  |
| 11 | `ratIoStr` | 占比(%) | varchar(255) |  | YES |  |  |
| 12 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 13 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 14 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 15 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 16 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 17 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 31、 mtmoncjgl_cpvo
外汇交易中心统计月报-成交概览_按待偿期分类统计

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `amt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 10 | `cnt` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 11 | `rate` | 到期收益率(%) | varchar(255) |  | YES |  |  |
| 12 | `term` | 待偿期(年) | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 32、 mtmoncjgl_dealtype
外汇交易中心统计月报-成交概览_按交易品种

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `amt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 10 | `cnt` | 成交笔数 | varchar(255) |  | YES |  |  |
| 11 | `rate` | 加权利率(%) | varchar(255) |  | YES |  |  |
| 12 | `type` | 品种 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 33、 mtmoncjgl_fxcl
外汇交易中心统计月报-成交概览_外币拆借

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `ccy` | 币种 | varchar(255) |  | YES |  |  |
| 10 | `dlNo` | 成交笔数 | varchar(255) |  | YES |  |  |
| 11 | `trdAmnt` | 成交金额(亿美元) | varchar(255) |  | YES |  |  |
| 12 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 13 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 14 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 15 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 16 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 17 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 34、 mtmoncjgl_imvo
外汇交易中心统计月报-成交概览_按计息方式分类

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `amt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 10 | `cnt` | 成交笔数(笔) | varchar(255) |  | YES |  |  |
| 11 | `rate` | 到期收益率(%) | varchar(255) |  | YES |  |  |
| 12 | `term` | 债券类型 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 35、 mtmoncjgl_ittvo
外汇交易中心统计月报-成交概览_按机构类别余额统计

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `type` | 机构类型 | varchar(255) |  | YES |  |  |
| 10 | `rate` | 余额(亿元) | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 36、 mtmoncjgl_organdeal
外汇交易中心统计月报-成交概览_按机构类别交易统计

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `amt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 10 | `cnt` | 成交笔数 | varchar(255) |  | YES |  |  |
| 11 | `rate` | 加权平均利率(%) | varchar(255) |  | YES |  |  |
| 12 | `type` | 机构类型 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 37、 mtmoncjgl_ormthbltn
外汇交易中心统计月报-成交概览_按券种统计

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `amt` | 成交量(亿元) | varchar(255) |  | YES |  |  |
| 10 | `type` | 债券种类 | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 38、 mtmoncjgl_rate
外汇交易中心统计月报-成交概览_利率互换

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `rate` | 参考利率 | varchar(255) |  | YES |  |  |
| 10 | `term` | 期限 | varchar(255) |  | YES |  |  |
| 11 | `fixRate` | 固定利率 | varchar(255) |  | YES |  |  |
| 12 | `notional` | 名义本金(亿元) | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 39、 mtmoncjgl_rfxfwmthbltn
外汇交易中心统计月报-成交概览_人民币外汇远期

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `cnyAmntStr` | 合计折元成交金额(百万元) | varchar(255) |  | YES |  |  |
| 10 | `dlNumStr` | 合计折元成交笔数 | varchar(255) |  | YES |  |  |
| 11 | `tnrCd` | 期限品种 | varchar(255) |  | YES |  |  |
| 12 | `usdCnyDlNumStr` | USD.CNY成交笔数 | varchar(255) |  | YES |  |  |
| 13 | `usdCnyNlegCnyAmntStr` | USD.CNY成交金额(百万元) | varchar(255) |  | YES |  |  |
| 14 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 15 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 16 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 17 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 18 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 19 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 40、 mtmoncjgl_rfxsomthbltn
外汇交易中心统计月报-成交概览_人民币外汇期权

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `dealAmt` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 10 | `dealCnt` | 成交笔数 | varchar(255) |  | YES |  |  |
| 11 | `tnrCd` | 期权期限 | varchar(255) |  | YES |  |  |
| 12 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 13 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 14 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 15 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 16 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 17 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 41、 mtmoncjgl_rfxspmthbltn
外汇交易中心统计月报-成交概览_人民币外汇即期

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `ccyPairCd` | 币种 | varchar(255) |  | YES |  |  |
| 10 | `cnyAmntStr` | 成交金额(亿元) | varchar(255) |  | YES |  |  |
| 11 | `dlNumStr` | 成交笔数 | varchar(255) |  | YES |  |  |
| 12 | `wghtdAvgPriceStr` | 加权价 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 42、 mtmoncjgl_rmbfxswap
外汇交易中心统计月报-成交概览_人民币外汇掉期外汇货币掉期

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 发布时间 | varchar(255) |  | YES |  |  |
| 9 | `cnyAmntStr` | 合计折元成交金额(亿元) | varchar(255) |  | YES |  |  |
| 10 | `dlNumStr` | 合计折元成交笔数 | varchar(255) |  | YES |  |  |
| 11 | `tnrCd` | 期限品种 | varchar(255) |  | YES |  |  |
| 12 | `usdCnyDlNumStr` | USD.CNY成交笔数 | varchar(255) |  | YES |  |  |
| 13 | `usdCnyNlegCnyAmntStr` | USD.CNY成交金额(亿元) | varchar(255) |  | YES |  |  |
| 14 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 15 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 16 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 17 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 18 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 19 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 43、 mtmondqtj
外汇交易中心统计月报-地区统计

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 更新时间 | varchar(255) |  | YES |  |  |
| 9 | `province` | 省/市 | varchar(255) |  | YES |  |  |
| 10 | `in` | 融入金额(亿元) | varchar(255) |  | YES |  |  |
| 11 | `in_per` | 融入占市场(%) | varchar(255) |  | YES |  |  |
| 12 | `out` | 融出金额(亿元) | varchar(255) |  | YES |  |  |
| 13 | `put_per` | 融出占市场(%) | varchar(255) |  | YES |  |  |
| 14 | `month` | 统计月份 | varchar(255) |  | YES |  |  |
| 15 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 16 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 17 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 18 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 19 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 20 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 44、 nafmii_org_cn
银行间交易商协会

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 日期 | datetime |  | YES |  |  |
| 9 | `class` | 分类 | varchar(255) |  | YES |  |  |
| 10 | `deadline` | 期限 | varchar(255) |  | YES |  |  |
| 11 | `valuation` | 估值 | varchar(255) |  | YES |  |  |
| 12 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 13 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 14 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 15 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 16 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 17 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 45、 nafmii_org_cn_detailshowframe
银行间交易商协会各估值机构原始报价

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 日期 | datetime |  | YES |  |  |
| 9 | `bank` | 银行 | varchar(255) |  | YES |  |  |
| 10 | `class` | 分类 | varchar(255) |  | YES |  |  |
| 11 | `deadline` | 期限 | varchar(255) |  | YES |  |  |
| 12 | `valuation` | 估值 | varchar(255) |  | YES |  |  |
| 13 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 14 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 15 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 16 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 17 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 18 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 46、 news_attachment_a
附件A资讯网站

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` |  | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `news_type` | 新闻类型（资讯，公告，纰漏） | varchar(255) |  | YES |  |  |
| 3 | `title` | 标题 | varchar(255) | MUL | YES |  |  |
| 4 | `content` | 新闻详情 | longtext |  | YES |  |  |
| 5 | `content_html` | 新闻详情带html标签 | longtext |  | YES |  |  |
| 6 | `content_md5` | 新闻详情内容md5 | varchar(255) | MUL | YES |  |  |
| 7 | `abstract` | 新闻摘要 | text |  | YES |  |  |
| 8 | `tag` | 标签 | varchar(255) |  | YES |  |  |
| 9 | `language` | 新闻语言 | varchar(10) |  | YES |  |  |
| 10 | `opinion_tag` | 舆情标签 | varchar(255) |  | YES |  |  |
| 11 | `risk_type` | 一级风险标签 | varchar(255) |  | YES |  |  |
| 12 | `risk_score` | 风险分数 | varchar(255) |  | YES |  |  |
| 13 | `risk_tag` | 风险标签 | varchar(512) |  | YES |  |  |
| 14 | `publish_org` | 新闻发布来源 | varchar(255) |  | YES |  |  |
| 15 | `publish_time` | 新闻发布时间 | datetime | MUL | YES |  |  |
| 16 | `positive_org` | 正面舆情公司名 | varchar(255) |  | YES |  |  |
| 17 | `positive_org_score` | 正面舆情公司分数 | varchar(255) |  | YES |  |  |
| 18 | `negative_org` | 负面舆情公司名 | varchar(255) |  | YES |  |  |
| 19 | `neutra_org` | 中性舆情公司名 | text |  | YES |  |  |
| 20 | `neutra_org_score` | 中性舆情公司分数 | varchar(255) |  | YES |  |  |
| 21 | `negative_org_score` | 负面舆情公司分数 | varchar(255) |  | YES |  |  |
| 22 | `article_file_name` | 附件名称 | text |  | YES |  |  |
| 23 | `article_file_url` | 附件地址 | text |  | YES |  |  |
| 24 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 25 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 26 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  | 0 |
| 27 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  | 0 |
| 28 | `author` | 作者 | varchar(255) |  | YES |  |  |
| 29 | `author_info` | 作者简介 | varchar(255) |  | YES |  |  |
| 30 | `company` | 新闻涉及公司 | text |  | YES |  |  |
| 31 | `web_site` | 来源网站，如财经网 | varchar(255) | MUL | YES |  |  |
| 32 | `event_tag` | 事件标签 | varchar(255) |  | YES |  |  |
| 33 | `emotion_tag` | 情感标签 | varchar(255) |  | YES |  |  |
| 34 | `region_tag` | 地区标签 | varchar(255) |  | YES |  |  |
| 35 | `likes` | 点赞数 | int(11) |  | YES |  |  |
| 36 | `hits` | 点击量访问量 | int(11) |  | YES |  |  |
| 37 | `web_site_url` | 来源网站地址 | varchar(255) |  | YES |  |  |
| 38 | `content_url` | 正文详情url | varchar(1000) |  | YES |  |  |
| 39 | `office_account` | 公众号 | varchar(255) |  | YES |  |  |
| 40 | `office_account_info` | 公众号简介 | varchar(255) |  | YES |  |  |
| 41 | `replies` | 评论数 | int(11) |  | YES |  |  |
| 42 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 43 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 44 | `is_company` | 0不是公司资讯1是公司资讯 | int(11) |  | YES |  |  |
| 45 | `emotion` | 资讯情感 | varchar(255) |  | YES |  |  |
| 46 | `emotion_score` | 情感分数 | varchar(255) |  | YES |  |  |
| 47 | `company_id` | 对应的公司id | varchar(255) |  | YES |  |  |
| 48 | `extra` | 附加数据，json格式 | text |  | YES |  |  |
| 49 | `local_article_file_url` | 本地附件存放地址 | text |  | YES |  |  |
| 50 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 51 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 52 | `product_tag` | 产品标签 | varchar(1024) |  | YES |  |  |
| 53 | `industry_tag` | 行业标签 | varchar(1024) |  | YES |  |  |


#### 47、 sbv_gov_vn
越南央行

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 日期 | varchar(255) |  | YES |  |  |
| 9 | `name` | 表头名称 | varchar(255) |  | YES |  |  |
| 10 | `average` | 中间价 | varchar(255) |  | YES |  |  |
| 11 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 12 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 13 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 14 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 15 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 16 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 48、 shclearing_dqsylqx
上海清算所债券收益率曲线

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `curvedate` | 曲线日期 | varchar(255) |  | YES |  |  |
| 9 | `curveName` | 曲线名称 | varchar(255) |  | YES |  |  |
| 10 | `standardterm` | 曲线标准期限 | varchar(255) |  | YES |  |  |
| 11 | `yield` | 收益率 | varchar(255) |  | YES |  |  |
| 12 | `nyearValue` | N值 | varchar(255) |  | YES |  |  |
| 13 | `kyearValue` | K值 | varchar(255) |  | YES |  |  |
| 14 | `termdesc` | 期限描述 | varchar(255) |  | YES |  |  |
| 15 | `webCurveType` | 曲线类型 | varchar(255) |  | YES |  |  |
| 16 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 17 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 18 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 19 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 20 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 21 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 49、 shclearing_zqgz
上海清算所债券估值

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `bondcode` | 债券代码 | varchar(255) |  | YES |  |  |
| 9 | `bondAbbr` | 债券简称 | varchar(255) |  | YES |  |  |
| 10 | `vdate` | 估值日期 | varchar(255) |  | YES |  |  |
| 11 | `circulationplace` | 流通场所 | varchar(255) |  | YES |  |  |
| 12 | `claimperiod` | 待偿期 | varchar(255) |  | YES |  |  |
| 13 | `vfullprice` | 日间估价全价 | varchar(255) |  | YES |  |  |
| 14 | `dayaccruedinterest` | 日间应计利息 | varchar(255) |  | YES |  |  |
| 15 | `estimatenetprice` | 估价净价 | varchar(255) |  | YES |  |  |
| 16 | `estimateyield` | 估价收益率 | varchar(255) |  | YES |  |  |
| 17 | `vfixedduration` | 估价修正久期 | varchar(255) |  | YES |  |  |
| 18 | `vconvexity` | 估价凸性 | varchar(255) |  | YES |  |  |
| 19 | `vbasispointvalue` | 估价基点价值 | varchar(255) |  | YES |  |  |
| 20 | `vcarrylongperiod` | 估价利差久期 | varchar(255) |  | YES |  |  |
| 21 | `vspreadsconvexity` | 估价利差凸性 | varchar(255) |  | YES |  |  |
| 22 | `realfullprice` | 真实全价 | varchar(255) |  | YES |  |  |
| 23 | `realnetprice` | 真实净价 | varchar(255) |  | YES |  |  |
| 24 | `realyield` | 真实收益率 | varchar(255) |  | YES |  |  |
| 25 | `realfixedduration` | 真实修正久期 | varchar(255) |  | YES |  |  |
| 26 | `realconvexity` | 真实凸性 | varchar(255) |  | YES |  |  |
| 27 | `rbasispointvalue` | 真实基点价值 | varchar(255) |  | YES |  |  |
| 28 | `rcarrylongperiod` | 真实利差久期 | varchar(255) |  | YES |  |  |
| 29 | `rspreadsconvexity` | 真实利差凸性 | varchar(255) |  | YES |  |  |
| 30 | `credibility` | 可信度 | varchar(255) |  | YES |  |  |
| 31 | `vratelongperiod` | 估价利率久期 | varchar(255) |  | YES |  |  |
| 32 | `vrateconvexity` | 估价利率凸性 | varchar(255) |  | YES |  |  |
| 33 | `rratelongperiod` | 真实利率久期 | varchar(255) |  | YES |  |  |
| 34 | `rrateconvexity` | 真实利率凸性 | varchar(255) |  | YES |  |  |
| 35 | `edayfullprice` | 日终估价全价 | varchar(255) |  | YES |  |  |
| 36 | `edayaccruedinterest` | 日终应计利息 | varchar(255) |  | YES |  |  |
| 37 | `remainingprincipal` | 剩余本金 | varchar(255) |  | YES |  |  |
| 38 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 39 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 40 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 41 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 42 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 43 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 50、 shclearing_zshq
上海清算所债券指数

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `indexdate` | 指数日期 | varchar(255) |  | YES |  |  |
| 9 | `indexCode` | 指数代码 | varchar(255) |  | YES |  |  |
| 10 | `indexNameChs` | 指数名称（中文） | varchar(255) |  | YES |  |  |
| 11 | `indexNameEng` | 指数名称（英文） | varchar(255) |  | YES |  |  |
| 12 | `indexAbbr` | 指数简称 | varchar(255) |  | YES |  |  |
| 13 | `indexType` | 指数类型 | varchar(255) |  | YES |  |  |
| 14 | `baseValue` | 基数 | varchar(255) |  | YES |  |  |
| 15 | `divisor` | 最新除数 | varchar(255) |  | YES |  |  |
| 16 | `indexValue` | 指数数值 | varchar(255) |  | YES |  |  |
| 17 | `indexExtent` | 指数涨跌幅(%) | varchar(255) |  | YES |  |  |
| 18 | `indexQuantity` | 指数样本数量 | varchar(255) |  | YES |  |  |
| 19 | `indexTotalValue` | 指数总市值(亿元) | varchar(255) |  | YES |  |  |
| 20 | `reinvestTotalValue` | 再投资总市值(亿元) | varchar(255) |  | YES |  |  |
| 21 | `indexAverageYield` | 指数平均收益率(%) | varchar(255) |  | YES |  |  |
| 22 | `indexAverageCycle` | 指数平均修正久期 | varchar(255) |  | YES |  |  |
| 23 | `indexAverageConvexity` | 指数平均凸性 | varchar(255) |  | YES |  |  |
| 24 | `indexAverageBaseValue` | 指数平均基点价值 | varchar(255) |  | YES |  |  |
| 25 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 26 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 27 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 28 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 29 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 30 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 51、 wh_bank_whpj
外汇交易中心部分-银行外汇牌价

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `hbmc` | 货币名称 | varchar(255) |  | YES |  |  |
| 9 | `xhmrj` | 现汇买入价 | varchar(255) |  | YES |  |  |
| 10 | `xcmrj` | 现钞买入价 | varchar(255) |  | YES |  |  |
| 11 | `xhmcj` | 现汇卖出价 | varchar(255) |  | YES |  |  |
| 12 | `xcmcj` | 现钞卖出价 | varchar(255) |  | YES |  |  |
| 13 | `zsj` | 折算价 | varchar(255) |  | YES |  |  |
| 14 | `publish_time` | 发布日期 | date |  | YES |  |  |
| 15 | `time` | 发布时间 | time |  | YES |  |  |
| 16 | `publish_org` | 来源 | varchar(255) |  | YES |  |  |
| 17 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 18 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 19 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 20 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 21 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 22 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 52、 wh_bank_xgwbckll
外汇交易中心部分-银行小额外币存款利率

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 时间 | datetime |  | YES |  |  |
| 9 | `hb_name` | 货币 | varchar(255) |  | YES |  |  |
| 10 | `hq` | 活期 | varchar(255) |  | YES |  |  |
| 11 | `qttz` | 七天通知 | varchar(255) |  | YES |  |  |
| 12 | `one_month` | 一个月 | varchar(255) |  | YES |  |  |
| 13 | `three_month` | 三个月 | varchar(255) |  | YES |  |  |
| 14 | `six_month` | 六个月 | varchar(255) |  | YES |  |  |
| 15 | `one_year` | 一年 | varchar(255) |  | YES |  |  |
| 16 | `two_year` | 两年 | varchar(255) |  | YES |  |  |
| 17 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 18 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 19 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 20 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 21 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 22 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 53、 wh_rmbpjhl
外汇交易中心人民币(月/年)平均汇率

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 时间 | varchar(255) |  | YES |  |  |
| 9 | `hbd` | 货币对 | varchar(255) |  | YES |  |  |
| 10 | `pj` | 月平均/年平均 | varchar(255) |  | YES |  |  |
| 11 | `zd` | 涨跌 | varchar(255) |  | YES |  |  |
| 12 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 13 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 14 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 15 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 16 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 17 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 54、 wh_tjyb_hyzqtj
外汇交易中心统计月报-活跃债券统计(成交前十位债券交易情况)

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | xxx注意修改类型 | datetime |  | YES |  |  |
| 9 | `mc` | 名次 | varchar(255) |  | YES |  |  |
| 10 | `zqjc` | 债券简称 | varchar(255) |  | YES |  |  |
| 11 | `cjje` | 成交金额（亿元） | varchar(255) |  | YES |  |  |
| 12 | `bs` | 笔数 | varchar(255) |  | YES |  |  |
| 13 | `dqsyl` | 到期收益率（%） | varchar(255) |  | YES |  |  |
| 14 | `tjyf` | 统计月份 | varchar(255) |  | YES |  |  |
| 15 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 16 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 17 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 18 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 19 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 20 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 55、 wh_tjyb_mysjyl
外汇交易中心统计月报-每月数据一览

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 时间 | datetime |  | YES |  |  |
| 9 | `title` | 标题 | varchar(255) |  | YES |  |  |
| 10 | `content_url` | 链接 | varchar(255) |  | YES |  |  |
| 11 | `file_url` | PDF文件链接 | varchar(255) |  | YES |  |  |
| 12 | `file_name` | PDF文件名 | varchar(255) |  | YES |  |  |
| 13 | `tjyf` | 统计月份 | varchar(255) |  | YES |  |  |
| 14 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 15 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 16 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 17 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 18 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 19 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


#### 56、 zdscxx
农产品批发价格200指数

| 序号 | 名称 | 描述 | 类型 | 键 | 为空 | 额外 | 默认值 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 1 | `id` | 主键id | bigint(11) unsigned | PRI | NO | auto_increment |  |
| 2 | `create_time` | 入库时间 | datetime | MUL | YES |  | CURRENT_TIMESTAMP |
| 3 | `update_time` | 更新时间 | datetime |  | YES | on update CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |
| 4 | `is_delete` | 0未删除 1已删除 | int(11) |  | YES |  |  |
| 5 | `status` | 0未清洗 1已清洗 | int(11) |  | YES |  |  |
| 6 | `web_site` | 来源网站，如知乎 | varchar(255) | MUL | YES |  |  |
| 7 | `web_site_url` | 来源网站url | varchar(255) |  | YES |  |  |
| 8 | `publish_time` | 时间 | varchar(255) |  | YES |  |  |
| 9 | `product` | 品类 | varchar(255) |  | YES |  |  |
| 10 | `item` | 指标名称 | varchar(255) |  | YES |  |  |
| 11 | `value` | 指标数值 | varchar(255) |  | YES |  |  |
| 12 | `source_type` | 资讯来源分类（1. 网站/2. 微信号/3. 微博/4. 论坛） | int(11) |  | YES |  | 1 |
| 13 | `copyright` | 0:不存在版权问题，1存在版权问题 | int(11) |  | YES |  | 0 |
| 14 | `content_md5` | 内容md5 | varchar(40) | MUL | YES |  |  |
| 15 | `batch_date` | 批次时间 | date | MUL | YES |  |  |
| 16 | `run_id` | 采集系统内置的run_id | bigint(20) | MUL | YES |  |  |
| 17 | `extra` | 附加数据，json格式 | text |  | YES |  |  |


