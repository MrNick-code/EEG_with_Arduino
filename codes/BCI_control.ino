#include <arduinoFFT.h>
#include <Wire.h>

const int analogPin = A0;           // AD620 to Arduino analog port
const int muxControlPin = 2;        // MUX control pin
const int numChannels = 2;         // Number of channel in each MUX
const int samples = 64;            // Number of samples for Fast Fourier Transform (64, 128 or 256)
const double samplingFrequency = 256.0;  // Sampling frequence (adjust as needed)

ArduinoFFT<double> FFT = ArduinoFFT<double>(); // double tipo for FFT instance

double vReal[samples];              // Real values Array
double vImag[samples];              // Imaginary values Array (start: 0)

void setup() {
  Serial.begin(9600);

  pinMode(muxControlPin, OUTPUT); // Define MUX control pins as output
}

void loop() {
  for (int channel = 0; channel < numChannels; channel++) {
    selectChannel(channel); // Select deired MUX channel

    // Colect samples for FFT
    for (int i = 0; i < samples; i++) {
      vReal[i] = analogRead(analogPin);
      vImag[i] = 0;
      delay(1000 / samplingFrequency); // Sampling rate
    }

    FFT.windowing(vReal, samples, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
    FFT.compute(vReal, vImag, samples, FFT_FORWARD);
    FFT.complexToMagnitude(vReal, vImag, samples);

    // Finds dominant frequency
    double dominantFrequency = FFT.majorPeak(vReal, samples, samplingFrequency);

    // Classifies the brain wave based on dominant freqeuncy
    String waveType = classifyWave(dominantFrequency);

    Serial.print("Canal: ");
    Serial.print(channel);
    Serial.print(" | Frequência dominante: ");
    Serial.print(dominantFrequency);
    Serial.print(" Hz | Tipo de onda: ");
    Serial.println(waveType);

    delay(100);  // Delay between signal's read
  }
}

// Function to select MUX channel
void selectChannel(int channel) {
  digitalWrite(muxControlPin, channel); // Define as high or low based on the channel
}

// Function to classify the brain wave
String classifyWave(double frequency) {
  if (frequency >= 0.5 && frequency < 4.0) {
    return "Delta (0.5-4 Hz)";
  } else if (frequency >= 4.0 && frequency < 8.0) {
    return "Theta (4-8 Hz)";
  } else if (frequency >= 8.0 && frequency < 13.0) {
    return "Alpha (8-13 Hz)";
  } else if (frequency >= 13.0 && frequency < 30.0) {
    return "Beta (13-30 Hz)";
  } else {
    return "Gamma (>30 Hz)";
  }
}
