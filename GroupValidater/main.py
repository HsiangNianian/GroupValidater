import OlivOS
import random
import GroupValidater
from PIL import Image, ImageDraw, ImageFont

TMP_PATH = 'plugin/data/GroupValidater/tmp.jpg'

def draw():
  def random_color():
      return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


  def random_color2():
      return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


  def random_char():
      return chr(random.randint(65, 90))


  # 创建图像，默认为黑色，可以修改参数color=(r, g, b)的值来赋予颜色
  img = Image.new('RGB', (240, 60))
  # 创建字体，使用系统自带的ttf字体文件
  img_font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 40)
  # 生成ImageDraw对象，能对图像进行注释，修描等操作
  draw = ImageDraw.Draw(img)
  for x in range(240):
      for y in range(60):
          draw.point((x, y), fill=random_color())

  for k in range(4):
      draw.text((60 * k + 10, 10), random_char(), font=img_font, fill=random_color2())

#   img.show()
  img.save(TMP_PATH)

    
class Event(object):
    def init(self, Proc):
      pass
    
    def group_member_increase(self, Proc):
      drawing()
      self.reply(
          f'欢迎[CQ:at,qq={str(self.data.user_id)}]，你有1分钟时间输入以下验证码进行验证：[CQ:image,file=///{TMP_PATH}]'
      )

    def save(self, Proc):
      pass

    def menu(self, Proc):
      if self.data.namespace == 'GroupValidater':# type: ignore
        if self.data.event == 'GroupValidater_Menu_Config':  # type: ignore
          logg("有笨蛋打开了配置")
              
