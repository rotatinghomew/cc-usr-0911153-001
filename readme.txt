果品智能分选质量闭环平台

复检与出库基线：可通过 Application.receive_inspection 记录人工复检凭据，
包括果批、产地、分选线、相机批次、机判级别、复检级别、抽样缘由及时间；
同一凭据重放不重复入库，冲突凭据会被拒绝。Application.dispatch 只给已放行
果批分配一次出库目的地，优先采用最新人工复检，否则沿用机器判级，
已有出库分配不会被后续证据静默改写。记录可通过仓储的 inspection_rows
和 queue_rows 读取，均使用运行命令的同一数据库。本功能不包含复检偏差评估、
候选标定、标定启用、按批次固定标定版本或历史标定复核。

运行验收：
python3 -m orchard_grade run --fixture fixtures/acceptance.json --database /tmp/orchard_grade.sqlite3 --output /tmp/orchard_grade-output

核验：
python3 -m orchard_grade verify --database /tmp/orchard_grade.sqlite3 --output /tmp/orchard_grade-output

全量测试：
python3 -m unittest discover -s tests -v

按模块测试：
python3 -m unittest tests.grading.test_decision_table -v

构建检查：
python3 -m compileall -q orchard_grade tests
