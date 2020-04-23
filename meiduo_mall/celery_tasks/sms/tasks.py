from celery_tasks.sms import constants
from meiduo_mall.libs.yuntongxun.sms import CCP

from celery_tasks.main import app

@app.task(bind=True,name='send_sms',retry_backoff=0)
def send_sms(self,mobile,sms_code):
    # 将耗时的代码封装在一个方法中
    ccp=CCP()
    ret=ccp.send_template_sms(mobile,[sms_code,constants.SMS_CODE_EXPIRES/60],1)
    if ret!=0:#等于0表示发送成功
        raise self.retry(exc=Exception('发送短信失败'),max_retries=0)
    return ret