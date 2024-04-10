# Simple Sim Wheel Package
Support for the Logitech G923 (Xbox Version) Gaming Wheel & Pedals for driving in a Simple Sim environment.

## Usage

This package requires the IGVC Simple Sim environment, available [here](https://github.com/LTU-Actor/igvc_python_simulator).<br>

The wheel requires an initial message to be sent whenever the device is plugged into your computer: <br>

```
sudo ./g923_wheel_setup.sh
```

<br>

This command needs usbmodeswitch to be installed. It usually is already installed in Ubuntu 20.04, but if not run this command:<br>

```
sudo apt install usb-modeswitch usb-modeswitch-data
```

<br>

### Launch Steps
1. Launch the Simple Sim simulator: `roslaunch simple_sim_igvc sim_base.launch`
2. Ensure the wheel is connected to your computer by running the setup command.
3. Launch this package: `roslaunch simple_sim_wheel_pkg sim_wheel.launch`
4. Once both programs are running, you may need to press the brake in once to get the vehicle moving. This issue is caused by the wheel's firmware along with usbmodeswitch.
5. The control is ready when the vehicle starts idling forward.


