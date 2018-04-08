import os,re
#pc电脑路径
apkPath=r'D:\bao\kaimen.apk'
#直接获取设备名称
deviceName=re.findall('(.+?)\t',os.popen('adb devices').readlines()[1])[0]
#获取安卓版本号
platformVersion=''.join(re.findall('(.+?)',os.popen('adb shell getprop ro.build.version.release').readlines()[0]))
#获取安卓包名
appPackage=re.findall('name=\'(.+?)\'',os.popen('aapt dump badging '+apkPath).readline())[0]
#获取appActivity
#appActivity=re.findall('launchable-activity: name=\'(.+?)\'',os.popen('aapt dump badging '+apkPath+'|findstr "activity"').readline())[0]
global config
config = {}
config['appiumPort']='4723'
config['bootStrapPort']=''
config['seldnroidPort']=''
config['chromiumPort']=''
config['platformName'] = 'Android'
config['platformVersion'] = platformVersion
config['deviceName'] = deviceName
config['appPackage'] = appPackage
#config['appActivity']=appActivity
config['appActivity']='com.lekelian.lkkm.activity.WelComeActivity'
config['noReset'] = True
config['unicodeKeyboard'] = True
config['resetKeyboard'] = True
config['automationName']= 'Uiautomator2'
config['app'] = apkPath
config['newCommandTimeout'] = '400'

'''主按钮'''
global bottom
bottom = {}

bottom['开门id']='com.lekelian.lkkm:id/llt_tab1'
bottom['小区id']='com.lekelian.lkkm:id/llt_tab2'
bottom['我的id']='com.lekelian.lkkm:id/llt_tab3'
bottom['客服id']='com.lekelian.lkkm:id/img_home_goserve'
bottom['请选择小区id']='com.lekelian.lkkm:id/view_home_select'
bottom['登录按钮id'] ='com.lekelian.lkkm:id/iv_apply_key'
bottom['小区公告id']='com.lekelian.lkkm:id/img_home_notice'


'''登录页面action'''
global login
login = {}
login['账号id']='com.lekelian.lkkm:id/ed_user_phone'
login['获取验证码id']='com.lekelian.lkkm:id/tv_send_code'
login['输入验证码id']='com.lekelian.lkkm:id/ed_user_captcha'
login['登录id']='com.lekelian.lkkm:id/view_login_layout'
login['跳过id']='com.lekelian.lkkm:id/exlogin_button2'
login['客服反馈id']='com.lekelian.lkkm:id/img_title_right'


'''小区'''
global hous
hous = {}
hous['报修处理id']='com.lekelian.lkkm:id/view_block_repair'
hous['分享钥匙id']='com.lekelian.lkkm:id/view_block_sharekey'
hous['意见反馈id'] ='com.lekelian.lkkm:id/view_block_feedback'
hous['发放公告']='com.lekelian.lkkm:id/view_block_notice'
hous['加装门禁']='com.lekelian.lkkm:id/view_block_addguard'
hous['住户授权']='com.lekelian.lkkm:id/view_block_accredit'
hous['小区论坛id'] ='com.lekelian.lkkm:id/view_block_forum'
hous['小区成员id'] ='com.lekelian.lkkm:id/view_block_member'

'''报修、公告'''
global repairs
repairs={}
repairs['报修处理id']='com.lekelian.lkkm:id/tv_inbox'
repairs['发送通告id']='com.lekelian.lkkm:id/tv_notices'
repairs['处理xpath']='//android.widget.TextView[@text="处理"]'
repairs['待处理xpath']='//android.widget.TextView[@text="待处理"]'
repairs['以处理xpath']='//android.widget.TextView[@text="以处理"]'
repairs['输入公告内容xpath'] ='//android.widget.EditText[@text="有什么重要的广告要告诉大家，请认真编写吧~"]'
repairs['发公告id']='com.lekelian.lkkm:id/view_serve_layout'

'''选择小区'''
global choosehous
choosehous={}
choosehous['点击搜索小区id']='com.lekelian.lkkm:id/ed_select_site'
choosehous['返回id'] = 'com.lekelian.lkkm:id/img_title_left'









'''少用'''
global flash
flash = {}
flash['页面返回id']='com.lekelian.lkkm:id/img_title_left'
flash['跳过广告id']='com.lekelian.lkkm:id/img_welcome_jump'
flash['确定xpath']='//android.widget.TextView[@test=\"确定\"]'

'''我的'''
global my
my = {}
my['我的小区id']= 'com.lekelian.lkkm:id/view_my_block'
my['我的钥匙id']='com.lekelian.lkkm:id/view_my_key'
my['如何使用id']='com.lekelian.lkkm:id/view_course'
my['设置id']='com.lekelian.lkkm:id/view_setting'



'''设置'''
global setting
setting = {}
setting['个人信息id']='com.lekelian.lkkm:id/view_user_onclick'
setting['退出登录id']='com.lekelian.lkkm:id/view_off_login'