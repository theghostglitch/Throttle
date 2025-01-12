import logging
import subprocess

import pwnagotchi
import pwnagotchi.plugins as plugins
import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.components import LabeledValue
from pwnagotchi.ui.view import BLACK

class throttle(plugins.Plugin):
	__author__ = 'https://github.com/TheGhostGlitch'
	__version__ = '1.0.0'
	__license__ = 'GPL3'
	__description__ = 'Throttle status for pwnagotchi'

	def on_loaded(self):
		logging.info("Pwnagotchi Throttle Plugin loaded.")

	def on_ui_setup(self, ui):
		ui.add_element('Throttle', LabeledValue(color=BLACK, label='', value='Start',
			position=(int(self.options["throttle_x_coord"]),
			int(self.options["throttle_y_coord"])),
			label_font=fonts.Small, text_font=fonts.Small))
	
	def on_unload(self, ui):
		with ui._lock:
			ui.remove_element('throttle')
	
	def on_ui_update(self, ui):
		ui.set('Throttle', "%s" % self.check_low_power())
	
	def check_low_power(self):
		try:
			output = subprocess.check_output(["vcgencmd", "get_throttled"])
			throttled_value = int(output.decode('utf-8').split('=')[1], 16)
  			
			value = ''
			if throttled_value & 1 != 0:
				value = "Volt"
			elif throttled_value & 2 != 0:
				value = "Freq"
			elif throttled_value & 4 != 0:
				value = "Temp"
			else:
				value = "Clear"
			return value
  		
		except subprocess.CalledProcessError:
			logging.info("Error checking power status.")
			return "Error"
      	
