import os
import numpy
import lal 
import pycbc.types


def gen_my_waveform(**params): 

    """Generate a simple analytic time-domain waveform (hp, hc).
    Replace this  block with your function """

    delta_t = params.get('delta_t', 1.0 / 4096.0)
    duration = params.get('duration', 4.0)
    f_lower = params.get('f_lower', 20.0)
    f_final = params.get('f_final', 4.0 * f_lower)
    amplitude = params.get('amplitude', 1e-21)

    t = numpy.arange(0.0, duration, delta_t)
    if len(t) == 0:
        t = numpy.array([0.0])

    chirp_rate = (f_final - f_lower) / max(duration, delta_t)
    phase = 2.0 * numpy.pi * (f_lower * t + 0.5 * chirp_rate * t**2)

    # Smooth turn-on to reduce edge effects
    taper_duration = min(0.1, duration)
    n_taper = max(1, int(taper_duration / delta_t))
    window = numpy.ones_like(t)
    if n_taper > 1:
        ramp = 0.5 * (1.0 - numpy.cos(numpy.linspace(0.0, numpy.pi, n_taper)))
        window[:n_taper] = ramp

    hp_arr = amplitude * window * numpy.cos(phase)
    hc_arr = amplitude * window * numpy.sin(phase)

    hp = pycbc.types.TimeSeries(hp_arr, delta_t=delta_t, epoch=0.0)
    hc = pycbc.types.TimeSeries(hc_arr, delta_t=delta_t, epoch=0.0)
    return hp, hc