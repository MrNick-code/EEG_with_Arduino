# EEG with Arduino - version 1.0
Home made EEG utilizing basic electronic components and an Arduino.

!["First time testing the first version"](images/metest1.jpg)

## Introduction
This project aims to developing an eletroencefalogram (EEG) utilizing simple eletronic and microeletronic components. The longer I get through my engineering course, the more I see how important is the "Cheapening Engineering" for the science development. So many projects that we found out so amazing and greatefull just takes really long or can't go any further because lack of investiment. Also, sometimes, several studies and tests does not require a very precise equipment, people usually look first for either prototypes or simpler versions of the device in question. Here, I'm trying to bring an alternative for those who looks to make some basic reseach in the area of brain computer interface (BCI), and also you can take that as an inspiration to build your own EEG or similar and even look for possible upgrades, fixes and so on. 

## Extra
If you either want to suggest changes, discuss or anything else, feel free to contact me: [LinkedIn](https://www.linkedin.com/in/matheus-capelin-a398a9289/), or just use github issue if you prefer. Please, I'd love to hear your opnion!

## How does the circuit works

The circuit is basically composed of an Arduino UNO as microcontroler, an amplifier, AgCl electrodes, an high and low pass filters, and a some multiplexers. I'll cover the use of them in more detail in the following subsections. To summarize, The filters will be used together as a band pass filter, so we get the output closest to only the frequencies emited by the brain. Those EEG's sign are of the order of microvolts, so we want to amplify them (of course with the amplifier) to get a better reading of 'em. The electrodes, attached to our head, will be used to collect the brain waves. In this case, we first need 3 electrodes. One will be used as ground, so we usually want to put at somewhere with no brain waves emission (like th ear), and the other two set what we call a channel. The more channels we have, the more measuresments we get, but we can't just connect the channels in series or parallel. For this to work, I found that using multiplexers could be a solution. They basically will constantly alternate between which channel the measures are made. Lastly, the Arduino is used for real time measures of this filtered and amplified sign and then we can do any needed analyses with any programming language. For this work, we're only focus on the arduino set up with C++ and python for the data analysis, but other could've be used. 

### Amplifier (AMP)

The AMP used is an [AD620](https://shopee.com.br/Ad620-MV-3-12V-DC-Módulo-Amplificador-De-Tensão-Microvolt-i.569260546.24929264617), which can be powered by a single +5V source and a common ground point. This is an operational AMP, that means, it amplifies the difference between two input signals. We connect the MUX+ to the S+ pin and the MUX- to the S-. Both Vneg and GND pin is going to be connected to the circuit common ground, Vin is connected to Arduino's +5V and Vout will continue to the filters. The AD620 gain is adjusted with an external resistor, and is given by, $G = 49.4 \cdot (1+\dfrac{49.4 k\Omega}{R_{ext}})$.

### Band-pass Filter (BPF)

An BPF can be made with an High-pass Filter (HPF) togheter with a Low-pass Filter (LPF). An HPF removes frequencies below an certain limit, allowing just the highest frequences to get through. For EEG's device, the cutoff frequency is usually between 0.5 and 1Hz, to remove frequences related to moviments (for this first approach, I'm just interested in evaluating the device capacity/accuracy). On the other hand, the LPF removes the frequencies above an certain limit. For EEG's device, usually the cutoff frequency is arround 30 to 50Hz, to eliminate the high frequency noise, including eletrical grid interferencies (60Hz). The cutoff frequency can be calculated by, $f_c = \dfrac{1}{2\pi RC}$. The filters are made of an resistor and capacitor (for each filter) direct connected right in between the AMP ouput (Vout) and the Arduino. For a 0.5-50Hz range frequency and, for both filters, an 330k$\Omega$ resistor, we finish it with capacitors of 3kF and 22mF to, respectively, the HPF and the LPF.

## Building the device



## Analysis



## Conclusion



## Licence
This project is licensed under the MIT license - See [LICENSE](LICENSE) for more details.
