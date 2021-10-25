WINDOW_SIZE = 16384 # samples per frame
SAMPLERATE = 44100 # samples per sec
MIDI_PITCH_AMOUNT = 128

# считаем, что нота прозвучала во время фрейма, только если количество 
# семплов проигрывающих данную ноту в этой фрейме превышает MIN_SAMPLES_PRESENT
MIN_SAMPLES_PRESENT = 0.1 * SAMPLERATE / 2
REL_PATH = 'ENSTDkCl'
# midi_statistics = np.zeros(MIDI_PITCH_AMOUNT)
