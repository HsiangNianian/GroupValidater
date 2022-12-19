import OlivOS
import GroupValidater
from draw import drawing

class Event(object):
    def init(plugin_event, Proc):
      pass

    def private_message(plugin_event, Proc):
        drawing(plugin_event, Proc)

    def init_after(plugin_event, Proc):
       pass

    def group_message(plugin_event, Proc):
        drawing(plugin_event, Proc)

    def poke(plugin_event, Proc):
        pass

    def save(plugin_event, Proc):
        pass

    def menu(plugin_event, Proc):
        if plugin_event.data.namespace == 'GroupValidater':  # type: ignore
            if plugin_event.data.event == 'GroupValidater_Menu_Config':  # type: ignore
                logg("有笨蛋打开了配置")
            elif plugin_event.data.event == 'GroupValidater_Menu_About':  # type: ignore
                pass
              
