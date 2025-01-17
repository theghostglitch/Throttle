# Throttle
Pwnagotchi Plugin that checks PI's throttle status.

## Setup:
To install, first set your directory for custom plugins in your config file.  
Find or add `main.custom_plugins = "/custom/plugin/directory"` Initially, it may be empty.

After that, add `throttle.py` to that folder.
Finally, enable it in your config.toml by adding the following line:

```toml
main.plugins.throttle.enabled = true
main.plugins.throttle.prefix = ''
main.plugins.throttle.throttle_x_coord = 0
main.plugins.throttle.throttle_y_coord = 0
```

Change your X and Y coords to where you want it to display on your screen.
Add a prefix if you need it. Ex: 'Throttle:'
