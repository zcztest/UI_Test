# AutoTestPOM 自动化测试框架
## _Python3 + UnitTest + DDT + HtmlTestRunner_
### Web -- _Selenium 3_

1、采用POM模式，封装常用关键字
```python
# 自定义关键字或者符合实际项目的方法（例子）
def select_element(self, loc, val):
    eles = self.find_elements(*loc)
    if val.find('-') > 0:
        for i in val.split('-'):
            self.select_element(loc, i)
    for ele in eles:
        if ele.text == val:
            ele.click()
            break
```
2、YAML管理元素对象
```yaml
# 新增客户页面元素对象（例子）
新增客户:
    客户名称: name # id
    客户级别选项: //*[@id="main-wrap"]/div/div[2]/div[2]/form/div[1]/div[2]/div[1]/div[2]/div
    客户级别内容: ant-select-dropdown-menu-item # class
    默认发货仓库选项: //*[@id="main-wrap"]/div/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/div
    默认发货仓库内容: ant-select-dropdown-menu-item # class
    所在部门选项: //*[@id="main-wrap"]/div/div[2]/div[2]/form/div[1]/div[1]/div[3]/div[1]/div/div[2]
    所在部门内容: ant-select-tree-title # class
    姓名: contactor # id
    手机: mobile # id
    保存: //*[@id="main-wrap"]/div/div[2]/div[3]/div/button[2]
    取消: //*[@id="main-wrap"]/div/div[2]/div[3]/div/button[1]
    弹框确定: /html/body/div[9]/div/div[2]/div/div[1]/div/div/div[2]/button[2]/span
    弹框取消: /html/body/div[9]/div/div[2]/div/div[1]/div/div/div[2]/button[1]/span
```
3、Excel管理测试数据
![Web](数据管理.png)

4、支持Chrome、Firefox（其他浏览器可自定义拓展）

5、测试报告

默认打开展示：
![默认](测试报告默认展示.png)

测试用例详细描述：
![详细描述](测试用例详细情况描述.png)

测试过程截图：
![测试截图](测试截图.png)

## 运行环境
_Windows 10+ 或 MacOS_

### 安装依赖
```bash
pip install -r requirements.txt
```

### 安装浏览器驱动
Chrome驱动：http://npm.taobao.org/mirrors/chromedriver/

Firefox驱动：https://github.com/mozilla/geckodriver/releases

## 操作说明
1、配置环境

2、安装完成后直接运行run.py

3、在result查看测试报告

4、在logs查看日志

##  更新记录
### version 0.1
1、新增
