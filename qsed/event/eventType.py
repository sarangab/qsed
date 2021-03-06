# copy from vnpy/vnpy/event/

'''
本文件仅用于存放对于事件类型常量的定义。
由于python中不存在真正的常量概念，因此选择使用全大写的变量名来代替常量。
这里设计的命名规则以EVENT_前缀开头。
常量的内容通常选择一个能够代表真实意义的字符串（便于理解）。
建议将所有的常量定义放在该文件中，便于检查是否存在重复的现象。
'''

#
# EVENT_TIMER = 'eTimer'  # 计时器事件，每隔1秒发送一次
#
#
# # 系统相关
# EVENT_TIMER = 'eTimer'                  # 计时器事件，每隔1秒发送一次
# EVENT_LOG = 'eLog'                      # 日志事件，全局通用
#
# # Gateway相关
# EVENT_TICK = 'eTick.'                   # TICK行情事件，可后接具体的vtSymbol
# EVENT_TRADE = 'eTrade.'                 # 成交回报事件
# EVENT_ORDER = 'eOrder.'                 # 报单回报事件
# EVENT_POSITION = 'ePosition.'           # 持仓回报事件
# EVENT_ACCOUNT = 'eAccount.'             # 账户回报事件
# EVENT_CONTRACT = 'eContract.'           # 合约基础信息回报事件
# EVENT_ERROR = 'eError.'                 # 错误回报事件


# todo: move some events to CTA module, eg. bar_event, target_position_event

# 市场行情相关

EVENT_MARKET = 'eMarket'          # 通用市场行情事件

EVENT_ORDERBOOK = 'eOrderbook_%s'    # ORDERBOOK行情事件
EVENT_TICK = 'eTick_%s'              # TICK行情事件
EVENT_SNAPSHOT = 'eSnapshot'      # 快照行情事件，500ms切片
EVENT_BAR_OPEN = 'eBarOpen_%s_%s'       # BAR_OPEN + symbol + bar_type
EVENT_BAR_CLOSE = 'eBarClose_%s_%s'     # BAR_CLOSE + symbol + bar_type


# 策略信号相关
EVENT_SIGNAL = 'eSignal'          # 策略信号事件

# 交易相关

EVENT_TARGET_POSITION = 'eTargetPosition'   # 目标仓位事件

