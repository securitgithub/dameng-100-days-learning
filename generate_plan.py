#!/usr/bin/env python3
# 达梦数据库100天学习计划生成脚本

# 定义100天学习计划内容
learning_plan = {
    1: {"title": "达梦数据库概述与环境准备", "category": "快速上手", "topics": ["达梦数据库简介", "国产数据库发展历程", "DM8版本特性", "学习路线规划"], "tasks": ["了解达梦数据库公司背景", "认识国产数据库生态", "安装准备：检查系统要求"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    2: {"title": "DM8版本介绍与获取", "category": "快速上手", "topics": ["DM8各版本区别", "开发版/标准版/企业版/安全版对比", "版本获取途径"], "tasks": ["理解不同版本适用场景", "下载适合的DM8版本", "获取授权文件"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "1.5小时"},
    3: {"title": "Windows环境安装DM8", "category": "快速上手", "topics": ["安装前准备", "图形化安装流程", "静默安装方式", "安装目录结构"], "tasks": ["检查Windows系统要求", "完成DM8图形化安装", "熟悉安装目录结构"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    4: {"title": "Linux环境安装DM8", "category": "快速上手", "topics": ["Linux系统要求", "命令行安装", "依赖包检查", "用户和组创建"], "tasks": ["准备Linux环境", "安装依赖包", "创建dmdba用户", "完成命令行安装"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2.5小时"},
    5: {"title": "配置数据库实例", "category": "快速上手", "topics": ["实例配置参数", "数据库初始化", "字符集选择", "页大小设置"], "tasks": ["使用dbca配置实例", "理解关键参数含义", "完成实例初始化"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    6: {"title": "启动与停止数据库服务", "category": "快速上手", "topics": ["服务注册", "启动模式", "停止方式", "服务状态检查"], "tasks": ["注册数据库服务", "练习启动/停止数据库", "检查服务状态"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "1.5小时"},
    7: {"title": "DM管理工具入门", "category": "快速上手", "topics": ["DM Manager界面", "连接数据库", "基本操作导航", "常用功能介绍"], "tasks": ["安装DM管理工具", "连接本地数据库", "熟悉界面布局"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    8: {"title": "DM数据迁移工具使用", "category": "快速上手", "topics": ["DTS工具介绍", "迁移项目创建", "数据源配置", "迁移执行"], "tasks": ["熟悉DTS工具界面", "创建简单迁移项目", "执行测试迁移"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    9: {"title": "SQL交互式查询工具", "category": "快速上手", "topics": ["DIsql工具介绍", "命令行操作", "脚本执行", "常用命令"], "tasks": ["练习DIsql基本命令", "执行SQL脚本", "掌握输出格式化"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "1.5小时"},
    10: {"title": "创建表空间", "category": "快速上手", "topics": ["表空间概念", "表空间类型", "创建语法", "表空间管理"], "tasks": ["理解表空间作用", "创建不同类型表空间", "设置表空间属性"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    11: {"title": "用户与权限管理", "category": "快速上手", "topics": ["用户创建", "角色管理", "权限授予", "用户与模式关系"], "tasks": ["创建数据库用户", "授予系统权限", "授予对象权限", "理解用户模式概念"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    12: {"title": "创建数据库对象", "category": "快速上手", "topics": ["表创建", "索引创建", "视图创建", "序列创建"], "tasks": ["创建基本表结构", "添加约束", "创建索引", "创建视图"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    13: {"title": "从Oracle迁移到DM", "category": "快速上手", "topics": ["Oracle迁移方案", "数据类型映射", "SQL兼容性", "迁移验证"], "tasks": ["分析Oracle源库结构", "配置迁移项目", "执行数据迁移", "验证迁移结果"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "3小时"},
    14: {"title": "从MySQL迁移到DM", "category": "快速上手", "topics": ["MySQL迁移方案", "语法差异处理", "数据类型转换", "迁移工具使用"], "tasks": ["准备MySQL源数据", "配置迁移参数", "执行迁移", "数据校验"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2.5小时"},
    15: {"title": "从其他数据库迁移", "category": "快速上手", "topics": ["PostgreSQL迁移", "SQL Server迁移", "DB2迁移", "迁移最佳实践"], "tasks": ["了解不同数据库迁移特点", "选择合适迁移方案", "处理兼容性问题"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    16: {"title": "SQL基础：单表查询", "category": "SQL开发", "topics": ["SELECT语句", "WHERE条件", "运算符使用", "NULL处理"], "tasks": ["编写基本SELECT语句", "使用各种条件表达式", "处理NULL值"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    17: {"title": "SQL基础：查询结果排序", "category": "SQL开发", "topics": ["ORDER BY子句", "多列排序", "NULL排序处理", "排序优化"], "tasks": ["使用ORDER BY排序", "实现多字段排序", "处理NULL排序"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "1.5小时"},
    18: {"title": "SQL基础：多表联合检索", "category": "SQL开发", "topics": ["内连接", "外连接", "交叉连接", "自连接"], "tasks": ["编写各种JOIN语句", "理解连接原理", "处理多表关联"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    19: {"title": "SQL基础：数据插入", "category": "SQL开发", "topics": ["INSERT语句", "批量插入", "INSERT SELECT", "默认值处理"], "tasks": ["编写单行插入", "实现批量插入", "使用INSERT SELECT"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    20: {"title": "SQL基础：数据更新与删除", "category": "SQL开发", "topics": ["UPDATE语句", "DELETE语句", "TRUNCATE", "事务控制"], "tasks": ["编写更新语句", "编写删除语句", "理解事务边界"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    21: {"title": "SQL基础：字符串函数", "category": "SQL开发", "topics": ["字符串拼接", "子串提取", "字符串转换", "正则表达式"], "tasks": ["使用常用字符串函数", "处理字符串格式", "应用正则匹配"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    22: {"title": "SQL基础：数值函数", "category": "SQL开发", "topics": ["数学运算函数", "取整函数", "随机数", "聚合函数"], "tasks": ["使用数值计算函数", "实现数值处理", "应用聚合统计"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    23: {"title": "SQL基础：日期函数", "category": "SQL开发", "topics": ["日期获取", "日期计算", "日期格式化", "日期比较"], "tasks": ["使用日期函数", "计算日期差值", "格式化日期输出"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    24: {"title": "SQL基础：日期操作进阶", "category": "SQL开发", "topics": ["时间戳处理", "时区转换", "日期范围查询", "日期边界"], "tasks": ["处理时间戳数据", "实现时区转换", "编写范围查询"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    25: {"title": "SQL基础：范围处理", "category": "SQL开发", "topics": ["BETWEEN操作", "IN操作", "EXISTS子查询", "范围优化"], "tasks": ["使用BETWEEN条件", "使用IN列表", "编写EXISTS子查询"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "1.5小时"},
    26: {"title": "SQL基础：聚合与分组", "category": "SQL开发", "topics": ["GROUP BY子句", "HAVING条件", "分组函数", "ROLLUP/CUBE"], "tasks": ["编写分组查询", "使用HAVING过滤", "实现多级分组"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    27: {"title": "SQL基础：子查询", "category": "SQL开发", "topics": ["标量子查询", "列子查询", "行子查询", "表子查询"], "tasks": ["编写各种子查询", "理解子查询执行顺序", "优化子查询性能"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    28: {"title": "SQL基础：视图创建与使用", "category": "SQL开发", "topics": ["视图概念", "创建视图", "可更新视图", "视图优化"], "tasks": ["创建简单视图", "创建复杂视图", "通过视图更新数据"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    29: {"title": "SQL基础：同义词使用", "category": "SQL开发", "topics": ["同义词概念", "创建同义词", "公共同义词", "私有同义词"], "tasks": ["创建私有同义词", "创建公共同义词", "管理同义词"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "1.5小时"},
    30: {"title": "SQL进阶：触发器基础", "category": "SQL开发", "topics": ["触发器类型", "触发时机", "触发事件", "触发器管理"], "tasks": ["创建DML触发器", "创建语句级触发器", "管理触发器"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    31: {"title": "SQL进阶：闪回查询", "category": "SQL开发", "topics": ["闪回概念", "闪回查询语法", "时间点查询", "版本查询"], "tasks": ["使用闪回查询", "查询历史数据", "恢复误删数据"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    32: {"title": "SQL进阶：物化视图", "category": "SQL开发", "topics": ["物化视图概念", "创建物化视图", "刷新策略", "查询重写"], "tasks": ["创建物化视图", "配置刷新策略", "测试查询重写"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    33: {"title": "SQL进阶：DBLINK使用", "category": "SQL开发", "topics": ["DBLINK概念", "创建DBLINK", "远程查询", "分布式事务"], "tasks": ["创建DBLINK连接", "执行远程查询", "处理分布式数据"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    34: {"title": "SQL进阶：存储过程基础", "category": "SQL开发", "topics": ["存储过程概念", "创建存储过程", "参数传递", "变量声明"], "tasks": ["创建简单存储过程", "使用输入参数", "使用输出参数"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    35: {"title": "SQL进阶：函数创建与使用", "category": "SQL开发", "topics": ["函数概念", "创建函数", "返回值处理", "函数调用"], "tasks": ["创建标量函数", "创建表值函数", "在SQL中调用函数"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    36: {"title": "SQL高级：分区表基础", "category": "SQL开发", "topics": ["分区概念", "范围分区", "列表分区", "哈希分区"], "tasks": ["创建范围分区表", "创建列表分区表", "管理分区"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    37: {"title": "SQL高级：复合分区与分区管理", "category": "SQL开发", "topics": ["复合分区", "分区维护", "分区索引", "分区裁剪"], "tasks": ["创建复合分区表", "添加/删除分区", "创建分区索引"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    38: {"title": "SQL高级：层次查询", "category": "SQL开发", "topics": ["层次结构", "START WITH", "CONNECT BY", "层级函数"], "tasks": ["编写层次查询", "处理树形数据", "使用层级函数"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    39: {"title": "DMSQL：数据类型详解", "category": "SQL开发", "topics": ["标量类型", "复合类型", "LOB类型", "类型转换"], "tasks": ["掌握各种数据类型", "处理类型转换", "使用LOB类型"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2小时"},
    40: {"title": "DMSQL：异常处理", "category": "SQL开发", "topics": ["异常概念", "预定义异常", "自定义异常", "异常传播"], "tasks": ["编写异常处理块", "定义自定义异常", "处理异常传播"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    41: {"title": "DMSQL：记录与集合", "category": "SQL开发", "topics": ["记录类型", "集合类型", "批量操作", "FORALL语句"], "tasks": ["定义记录类型", "使用集合类型", "实现批量操作"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    42: {"title": "DMSQL：包与嵌套子程序", "category": "SQL开发", "topics": ["包的概念", "创建包", "包体实现", "嵌套子程序"], "tasks": ["创建包规范", "实现包体", "调用包中子程序"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "2.5小时"},
    43: {"title": "SQL优化：执行计划分析", "category": "SQL开发", "topics": ["执行计划概念", "查看执行计划", "计划解读", "成本估算"], "tasks": ["获取执行计划", "分析执行计划", "识别性能瓶颈"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    44: {"title": "SQL优化：索引优化", "category": "SQL开发", "topics": ["索引类型", "索引选择", "索引失效", "索引维护"], "tasks": ["选择合适索引类型", "分析索引使用情况", "优化索引设计"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    45: {"title": "SQL优化：统计信息管理", "category": "SQL开发", "topics": ["统计信息概念", "收集统计信息", "统计信息维护", "直方图"], "tasks": ["收集表统计信息", "收集索引统计信息", "分析统计信息"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    46: {"title": "SQL优化：查询重写", "category": "SQL开发", "topics": ["查询重写规则", "谓词推入", "子查询展开", "连接优化"], "tasks": ["理解查询重写原理", "优化子查询", "优化连接查询"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    47: {"title": "SQL优化：并行查询", "category": "SQL开发", "topics": ["并行概念", "并行度设置", "并行执行计划", "并行限制"], "tasks": ["启用并行查询", "设置并行度", "分析并行执行"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    48: {"title": "SQL优化：内存优化", "category": "SQL开发", "topics": ["内存参数", "缓冲区配置", "排序内存", "哈希内存"], "tasks": ["理解内存参数", "调整缓冲区大小", "优化内存使用"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    49: {"title": "SQL优化：锁与并发控制", "category": "SQL开发", "topics": ["锁类型", "锁等待", "死锁检测", "并发优化"], "tasks": ["理解锁机制", "分析锁等待", "处理死锁问题"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    50: {"title": "SQL综合实战练习", "category": "SQL开发", "topics": ["综合SQL编写", "性能调优实战", "复杂查询设计"], "tasks": ["完成综合练习题", "优化复杂查询", "总结SQL技巧"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/sql-dev/"], "duration": "3小时"},
    51: {"title": "运维基础：安装前准备", "category": "运维管理", "topics": ["系统要求检查", "内核参数配置", "资源限制设置", "目录规划"], "tasks": ["检查系统配置", "调整内核参数", "规划安装目录"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    52: {"title": "运维基础：单机部署最佳实践", "category": "运维管理", "topics": ["规范化安装", "目录结构规划", "参数优化", "服务管理"], "tasks": ["完成规范化安装", "配置系统参数", "注册系统服务"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    53: {"title": "运维基础：系统资源监控", "category": "运维管理", "topics": ["CPU监控", "内存监控", "磁盘IO监控", "网络监控"], "tasks": ["配置资源监控", "分析监控数据", "设置告警阈值"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    54: {"title": "运维基础：实例状态监控", "category": "运维管理", "topics": ["会话监控", "事务监控", "锁监控", "等待事件"], "tasks": ["监控数据库会话", "分析事务状态", "处理锁问题"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    55: {"title": "运维基础：运维监控工具", "category": "运维管理", "topics": ["DEM工具", "性能监视器", "告警配置", "报表生成"], "tasks": ["部署DEM平台", "配置监控告警", "生成运维报表"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    56: {"title": "运维基础：系统健康检查", "category": "运维管理", "topics": ["检查项目清单", "检查脚本", "检查报告", "问题处理"], "tasks": ["执行健康检查", "分析检查结果", "处理发现问题"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    57: {"title": "运维基础：实例健康检查", "category": "运维管理", "topics": ["数据库参数检查", "表空间检查", "对象检查", "日志检查"], "tasks": ["检查数据库参数", "检查空间使用", "检查对象完整性"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    58: {"title": "备份恢复：物理备份基础", "category": "运维管理", "topics": ["备份概念", "完全备份", "增量备份", "备份策略"], "tasks": ["执行完全备份", "执行增量备份", "制定备份策略"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    59: {"title": "备份恢复：物理还原实战", "category": "运维管理", "topics": ["还原概念", "完全还原", "时间点恢复", "表空间恢复"], "tasks": ["执行完全还原", "执行时间点恢复", "恢复表空间"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    60: {"title": "备份恢复：逻辑备份", "category": "运维管理", "topics": ["dexp工具", "导出模式", "导出表", "导出用户"], "tasks": ["使用dexp导出数据", "配置导出参数", "执行全量导出"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    61: {"title": "备份恢复：逻辑还原", "category": "运维管理", "topics": ["dimp工具", "导入模式", "导入表", "数据校验"], "tasks": ["使用dimp导入数据", "处理导入冲突", "校验导入数据"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    62: {"title": "备份恢复：实战案例", "category": "运维管理", "topics": ["误删恢复", "数据迁移", "跨平台迁移", "灾难恢复"], "tasks": ["模拟误删场景并恢复", "跨平台数据迁移", "制定灾难恢复方案"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    63: {"title": "性能诊断：性能问题定位", "category": "运维管理", "topics": ["性能问题分类", "诊断方法论", "常用诊断工具", "性能视图"], "tasks": ["识别性能问题", "使用诊断工具", "分析性能视图"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    64: {"title": "性能诊断：AWR报告分析", "category": "运维管理", "topics": ["AWR报告生成", "报告解读", "性能指标分析", "优化建议"], "tasks": ["生成AWR报告", "分析报告内容", "提出优化建议"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    65: {"title": "性能优化：数据库参数优化", "category": "运维管理", "topics": ["内存参数", "IO参数", "连接参数", "优化原则"], "tasks": ["优化内存参数", "优化IO参数", "优化连接参数"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    66: {"title": "性能优化：SQL调优实战", "category": "运维管理", "topics": ["慢SQL识别", "SQL调优方法", "调优案例", "调优工具"], "tasks": ["识别慢SQL", "分析执行计划", "优化问题SQL"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    67: {"title": "故障诊断：SQL类故障", "category": "运维管理", "topics": ["语法错误", "权限错误", "空间不足", "超时问题"], "tasks": ["诊断SQL错误", "处理权限问题", "解决空间问题"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2小时"},
    68: {"title": "故障诊断：实例故障", "category": "运维管理", "topics": ["启动失败", "异常宕机", "性能问题", "连接问题"], "tasks": ["分析启动失败原因", "处理异常宕机", "诊断性能问题"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    69: {"title": "故障诊断：人为操作故障", "category": "运维管理", "topics": ["误删数据", "误删对象", "配置错误", "恢复方法"], "tasks": ["使用闪回恢复", "使用备份恢复", "处理配置错误"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    70: {"title": "运维综合实战", "category": "运维管理", "topics": ["运维流程设计", "自动化运维", "监控体系", "应急预案"], "tasks": ["设计运维流程", "编写运维脚本", "制定应急预案"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    71: {"title": "开发基础：JDBC连接", "category": "应用开发", "topics": ["JDBC驱动", "连接字符串", "连接池配置", "基本操作"], "tasks": ["配置JDBC驱动", "建立数据库连接", "执行CRUD操作"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2.5小时"},
    72: {"title": "开发基础：Python连接", "category": "应用开发", "topics": ["dmPython驱动", "连接配置", "基本操作", "批量处理"], "tasks": ["安装dmPython", "连接数据库", "执行数据操作"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2小时"},
    73: {"title": "开发基础：.NET连接", "category": "应用开发", "topics": ["DmProvider", "连接字符串", "EF Core", "Dapper"], "tasks": ["配置.NET驱动", "使用EF Core", "使用Dapper"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2.5小时"},
    74: {"title": "开发基础：Go连接", "category": "应用开发", "topics": ["Go驱动", "GORM框架", "连接配置", "数据操作"], "tasks": ["配置Go驱动", "使用GORM连接", "实现数据操作"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2小时"},
    75: {"title": "开发基础：ODBC连接", "category": "应用开发", "topics": ["ODBC驱动配置", "DSN配置", "连接测试", "应用集成"], "tasks": ["安装ODBC驱动", "配置数据源", "测试连接"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2小时"},
    76: {"title": "框架集成：MyBatis", "category": "应用开发", "topics": ["MyBatis配置", "映射文件", "动态SQL", "分页查询"], "tasks": ["配置MyBatis连接DM", "编写Mapper文件", "实现动态SQL"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2.5小时"},
    77: {"title": "框架集成：Spring Boot", "category": "应用开发", "topics": ["Spring Boot集成", "数据源配置", "事务管理", "多数据源"], "tasks": ["集成Spring Boot", "配置数据源", "实现事务管理"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2.5小时"},
    78: {"title": "框架集成：Hibernate/JPA", "category": "应用开发", "topics": ["Hibernate配置", "方言设置", "实体映射", "HQL查询"], "tasks": ["配置Hibernate连接DM", "定义实体类", "使用HQL查询"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2.5小时"},
    79: {"title": "框架集成：Django", "category": "应用开发", "topics": ["Django配置", "模型定义", "ORM操作", "迁移管理"], "tasks": ["配置Django连接DM", "定义数据模型", "执行数据迁移"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2.5小时"},
    80: {"title": "框架集成：SQLAlchemy", "category": "应用开发", "topics": ["SQLAlchemy配置", "引擎创建", "会话管理", "ORM操作"], "tasks": ["配置SQLAlchemy连接DM", "使用ORM操作数据", "处理会话"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2小时"},
    81: {"title": "开发进阶：大字段处理", "category": "应用开发", "topics": ["BLOB操作", "CLOB操作", "文件存取", "流式处理"], "tasks": ["处理BLOB数据", "处理CLOB数据", "实现文件存储"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2.5小时"},
    82: {"title": "开发进阶：事务控制", "category": "应用开发", "topics": ["事务隔离级别", "锁机制", "并发控制", "分布式事务"], "tasks": ["理解事务隔离级别", "处理并发问题", "实现分布式事务"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2.5小时"},
    83: {"title": "开发进阶：批量操作", "category": "应用开发", "topics": ["批量插入", "批量更新", "批量删除", "性能优化"], "tasks": ["实现批量插入", "优化批量操作性能", "处理大批量数据"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2小时"},
    84: {"title": "开发进阶：连接池优化", "category": "应用开发", "topics": ["连接池原理", "参数配置", "监控管理", "最佳实践"], "tasks": ["配置连接池参数", "监控连接池状态", "优化连接池"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "2小时"},
    85: {"title": "开发综合实战", "category": "应用开发", "topics": ["项目实战", "性能优化", "最佳实践"], "tasks": ["完成项目实战练习", "优化应用性能", "总结开发经验"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/app-dev/"], "duration": "3小时"},
    86: {"title": "高可用：数据守护概述", "category": "高可用", "topics": ["数据守护概念", "架构原理", "主备切换", "数据同步"], "tasks": ["理解数据守护架构", "掌握主备切换原理", "了解数据同步机制"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2小时"},
    87: {"title": "高可用：数据守护搭建", "category": "高可用", "topics": ["环境准备", "主库配置", "备库配置", "守护进程配置"], "tasks": ["准备搭建环境", "配置主备库", "启动守护进程"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    88: {"title": "高可用：读写分离集群", "category": "高可用", "topics": ["读写分离原理", "集群配置", "负载均衡", "故障切换"], "tasks": ["搭建读写分离集群", "配置负载均衡", "测试故障切换"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    89: {"title": "高可用：共享存储集群DSC", "category": "高可用", "topics": ["DSC概念", "共享存储配置", "集群管理", "负载均衡"], "tasks": ["理解DSC架构", "配置共享存储", "管理DSC集群"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    90: {"title": "高可用：分布式集群DMDPC", "category": "高可用", "topics": ["DMDPC概念", "分布式架构", "数据分布", "查询优化"], "tasks": ["理解分布式架构", "配置DMDPC", "管理分布式集群"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    91: {"title": "高可用：集群健康检查", "category": "高可用", "topics": ["集群监控", "健康检查脚本", "告警配置", "日志分析"], "tasks": ["执行集群健康检查", "配置监控告警", "分析集群日志"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    92: {"title": "高可用：主备切换实战", "category": "高可用", "topics": ["计划内切换", "故障切换", "切换验证", "数据校验"], "tasks": ["执行计划内切换", "模拟故障切换", "验证切换结果"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    93: {"title": "高可用：数据复制DMDRS", "category": "高可用", "topics": ["DMDRS概念", "复制配置", "数据同步", "冲突处理"], "tasks": ["配置数据复制", "管理同步任务", "处理复制冲突"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/start/"], "duration": "2.5小时"},
    94: {"title": "高可用：备份策略设计", "category": "高可用", "topics": ["备份策略制定", "异地备份", "备份验证", "恢复演练"], "tasks": ["制定备份策略", "配置异地备份", "执行恢复演练"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "2.5小时"},
    95: {"title": "高可用：容灾方案设计", "category": "高可用", "topics": ["容灾架构", "双活部署", "灾备切换", "容灾演练"], "tasks": ["设计容灾方案", "配置灾备环境", "执行容灾演练"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    96: {"title": "综合实践：项目实战", "category": "综合实践", "topics": ["项目需求分析", "架构设计", "数据库设计", "实施部署"], "tasks": ["分析项目需求", "设计数据库架构", "完成项目实施"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/"], "duration": "3小时"},
    97: {"title": "综合实践：性能调优实战", "category": "综合实践", "topics": ["性能问题诊断", "优化方案设计", "优化实施", "效果验证"], "tasks": ["诊断性能问题", "制定优化方案", "验证优化效果"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    98: {"title": "综合实践：问题排查实战", "category": "综合实践", "topics": ["问题分析", "日志分析", "问题定位", "解决方案"], "tasks": ["分析实际问题", "定位问题原因", "实施解决方案"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/ops/"], "duration": "3小时"},
    99: {"title": "综合实践：最佳实践总结", "category": "综合实践", "topics": ["开发最佳实践", "运维最佳实践", "性能最佳实践", "安全最佳实践"], "tasks": ["总结开发经验", "总结运维经验", "整理最佳实践"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/"], "duration": "2.5小时"},
    100: {"title": "学习总结与进阶规划", "category": "综合实践", "topics": ["知识回顾", "技能评估", "认证规划", "持续学习"], "tasks": ["回顾100天学习内容", "评估技能掌握程度", "规划进阶学习路径"], "resources": ["https://eco.dameng.com/document/dm/zh-cn/"], "duration": "2小时"},
}

def create_day_file(day_num, content):
    filename = f"day{day_num:03d}.md"
    filepath = f"/workspace/dameng-100-days-learning/{filename}"
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# Day {day_num}: {content['title']}\n\n")
        f.write(f"**学习分类**: {content['category']}\n\n")
        f.write(f"**预计时长**: {content['duration']}\n\n")
        f.write("---\n\n")
        f.write("## 学习目标\n\n")
        for topic in content['topics']:
            f.write(f"- {topic}\n")
        f.write("\n## 学习任务\n\n")
        for i, task in enumerate(content['tasks'], 1):
            f.write(f"{i}. {task}\n")
        f.write("\n## 学习资源\n\n")
        for resource in content['resources']:
            f.write(f"- [{resource}]({resource})\n")
        f.write("\n## 学习笔记\n\n")
        f.write("<!-- 在这里记录你的学习笔记 -->\n\n")
        f.write("## 实践记录\n\n")
        f.write("<!-- 记录实践过程中遇到的问题和解决方案 -->\n\n")
        f.write("---\n\n")
        f.write(f"*第{day_num}天学习完成日期: ____年____月____日*\n")
    return filepath

def main():
    for day_num, content in learning_plan.items():
        filepath = create_day_file(day_num, content)
        print(f"已创建: {filepath}")
    print(f"\n总计创建 {len(learning_plan)} 个学习计划文件")

if __name__ == "__main__":
    main()
