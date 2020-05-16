import numpy as np


def WinFn(Win_Fn, freq, Bands, Gains, data):
    stp = freq[3] - freq[2]

    if Win_Fn == 'Rectangular':
        Win_data = Rec_Fn(data, freq, Bands, Gains, stp)
    elif Win_Fn == 'Hamming':
        Win_data = Ham_Fn(data, freq, Bands, Gains, stp)
    elif Win_Fn == 'Hanning':
        Win_data = Han_Fn(data, freq, Bands, Gains, stp)

    return Win_data


def indxl(low, stp, len_freq):
    indx = int(low // stp)
    if indx < len_freq:
        return indx
    if indx > len_freq:
        return len_freq


def indxh(high, stp, len_freq):
    indx = int(high // stp)
    if indx < len_freq:
        return indx
    if indx > len_freq:
        return len_freq


def Rec_Fn(data, freq, Bands, Gains, stp):
    len_freq = int(len(freq) / 2)
    Win = np.zeros(0, dtype=complex)
    Win_data = np.zeros(len(freq), dtype=complex)
    itr_outer = 0
    while itr_outer < 10:
        low = indxl(Bands[itr_outer][0], stp, len_freq) - 1
        high = indxh(Bands[itr_outer][1], stp, len_freq) - 1
        BW = high - low
        Shaper_Arr_Size = 2 * (len_freq - high)
        if Shaper_Arr_Size > 0:
            Shaper_Arr = np.zeros((Shaper_Arr_Size), dtype=complex)
            Win = np.multiply(np.ones(BW), Gains[itr_outer])
            Win_Fn_Arr = np.concatenate((np.zeros(
                (low), dtype=complex), Win, Shaper_Arr, Win,
                                         np.zeros((low), dtype=complex)),
                                        axis=0)
        else:
            BW = len_freq - low
            Win = np.multiply(np.ones(BW), Gains[itr_outer])
            Win_Fn_Arr = np.concatenate((np.zeros(
                (low), dtype=complex), Win, Win, np.zeros(
                    (low), dtype=complex)),
                                        axis=0)
        Win_data += Win_Fn_Arr * data
        itr_outer += 1
    return Win_data


def Ham_Fn(data, freq, Bands, Gains, stp):
    len_freq = len(freq) / 2
    Win_data = np.zeros(len(freq), dtype=complex)
    itr_outer = 0
    while itr_outer < 10:
        low = indxl(Bands[itr_outer][0], stp, len_freq) - 1
        high = indxh(Bands[itr_outer][1], stp, len_freq) - 1
        Hamm_Arr_Size = int(2 * (high - low))
        Offset = abs(int((low - ((0.25) * Hamm_Arr_Size))))
        Shaper_Arr = np.zeros(0, dtype=complex)
        Shaper_Arr_Size = int(2 * (len_freq - Hamm_Arr_Size - Offset))
        Win = np.multiply(np.hamming(Hamm_Arr_Size), Gains[itr_outer])
        if Shaper_Arr_Size > 0:
            Shaper_Arr = np.zeros(Shaper_Arr_Size, dtype=complex)
            Hamm_Fn_Arr = np.concatenate(
                (np.zeros(Offset, dtype=complex), Win, Shaper_Arr, Win,
                 np.zeros(Offset, dtype=complex)),
                axis=0)
        else:
            Shaper_indx = int(len_freq - Offset)
            Hamm_Fn_Arr = np.concatenate(
                (np.zeros(Offset), Win[:Shaper_indx], np.flip(
                    Win[:Shaper_indx]), np.zeros(Offset)),
                axis=0)
        Win_data += data * Hamm_Fn_Arr
        itr_outer += 1
    return Win_data


def Han_Fn(data, freq, Bands, Gains, stp):
    len_freq = len(freq) / 2
    Win_data = np.zeros(len(freq), dtype=complex)
    itr_outer = 0
    while itr_outer < 10:
        low = indxl(Bands[itr_outer][0], stp, len_freq) - 1
        high = indxh(Bands[itr_outer][1], stp, len_freq) - 1
        Hann_Arr_Size = int(2 * (high - low))
        Offset = abs(int((low - ((0.25) * Hann_Arr_Size))))
        Shaper_Arr = np.zeros(0, dtype=complex)
        Shaper_Arr_Size = int(2 * (len_freq - Hann_Arr_Size - Offset))
        Win = np.multiply(np.hanning(Hann_Arr_Size), Gains[itr_outer])
        if Shaper_Arr_Size > 0:
            Shaper_Arr = np.zeros(Shaper_Arr_Size, dtype=complex)
            Hann_Fn_Arr = np.concatenate(
                (np.zeros(Offset, dtype=complex), Win, Shaper_Arr, Win,
                 np.zeros(Offset, dtype=complex)),
                axis=0)
        else:
            Shaper_indx = int(len_freq - Offset)
            Hann_Fn_Arr = np.concatenate(
                (np.zeros(Offset), Win[:Shaper_indx], np.flip(
                    Win[:Shaper_indx]), np.zeros(Offset)),
                axis=0)
        Win_data += data * Hann_Fn_Arr
        itr_outer += 1
    return Win_data


"""
Bass:
Deep Bass 20-40 Hz
Low Bass 40-80 Hz
Mid Bass 80-160 Hz
Upper Bass 160-300 Hz

Midrange:
Lower Midrange 300-600 Hz
Middle Midrange 600-1.2K Hz
Upper Midrange 1.2K-2.4K Hz
Presence Range 2.4K-5K Hz

High End:
High End 5K-10K Hz
Extremely High End 10K-20K Hz
"""