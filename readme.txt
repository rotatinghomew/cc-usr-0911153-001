果品智能分选质量闭环平台

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
