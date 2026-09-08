# PyCBC plugin for generic waveform 

This repository is for designing and implementing custom waveforms in PyCBC.

The plugin provides a simple framework for developing a custom waveform and making it accessible within PyCBC. Users can define waveforms in waveform/waveform_plugin.py.

### Installation 
Clone the repository:
```
git clone https://github.com/Kanchan-05/waveform_plugin.git
cd waveform_plugin
pip install -e .
```

### Usage 
 To call your waveform model, 
 ```
from pycbc.waveform import get_td_waveform

hp, hc = get_td_waveform(
    approximant="mywaveform",
    delta_t=1.0 / 4096,
    duration=4.0,
    f_lower=20.0
)
```

NOTE: Replace `mywaveform` with your model name 
