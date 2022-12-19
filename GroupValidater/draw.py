from PIL import Image, ImageDraw, ImageFont
import random
import OlivOS
import GroupValidater
 
def draw(plugin_event,Proc):
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

  img.show()
  return img
 
