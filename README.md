# InteractiveSystems2020

# Fabric Push Button for Hospitals

The impact of Coronavirus in the world is unimaginable. During these times we need to come up with a system that would greatly increase the efficiency of the hospitals. The smart gown is one of the ideas which would help in this. The fabric button is embedded in the hospital’s patient gown. So, with the touch of the patient, it can invoke a sound and we can extend to have a centralized system that tells which device has requested using TCP/IP.

This is more necessary for patients who have an emergency in the washroom or any other place where there is no direct visibility to the nurse or the doctor.

There can be 2 variants for this project. One can be just a ringer to notify that the patient is in trouble. The other variant is to maintain a centralized system of every patient wearing this gown and their unique number. Whenever there is a request, along with the sound the data is sent to the server via TCP/IP and it is then logged.

The fabric pressure sensor is stitched on to the hospital gown acts as a push-button. The layout is a basic conductive fabric separated by spacer material setup which is on the gown. This is then connected to Arduino’s analog input pin. The Arduino’s output pins are connected to the speaker which would buzz based on the Fabric Push Button status. The controller is used to Actuate the speaker and also send data to the server using HTTP POST. The sensed value from the patient is visualized using the sound and on to the server’s display.

## Getting Started

The basic circuit diagram is done on Fritzing. Source code is written for it and then simulated in Tinkercad.

The push-button is connected to digital pin 2 and the buzzer is controlled using pin 8 of the Arduino UNO board. The pins are configured and coded in such a way that when a button is pressed the buzzer will buzz. The Circuit diagram, schematics, and source code are available at https://bit.ly/2YoubVX.  

Tinkercad:  "https://www.tinkercad.com/things/himwlsarHmG" can be found here.


### Prerequisites

There are certain set of materials you need to have before starting the project.

1. Conductive fabric sheet - 8×8cm. Pieces required are 2.
  ```It is required for the fabric push button.```

2. Normal fabric sheet - 8×8cm. Pieces required are 2.
   ```The material can be neoprene or any other fabric for the outer cover of the push-button sensor.```

3. Spacer material - 8×8cm. Pieces required are 2.
   ```It is used to place between 2 conductive fabric sheets.```

4. Arduino UNO Wifi Rev2
   ```It used to sense values from fabric push-button sensor and actuate the buzzer and to transmit data to the server.```

5. Piezo Buzzer
   ```It is the actuator we are using to indicate the button press```

6. LED
   ```This is for testing the fabric push-button sensor.```

7. Battery 5V
   ```Used to power the Arduino```

8. Battery holder
   ```Used to hold the battery```

9. Resistors - 100Ω(2) and 1kΩ(2)
   ```Used for buzzer and push-button circuit.```

10. Hospital gown/Shirt
    ```It is required as the fabric push button is sewed on to this.```

11. Sewing needle and thread
    ```It is required for all fabric related operations```

12. Jumper wires
    ```To connect between various components.```

13. Copper wires
    ```To solder from conductive fabric.```

14. Soldering gun and lead
    ```To solder the wires to the conductive fabric.```


### Installing

Since this is a hardware oriented project there is a very less developemnt with respect to software.

The only software tool required is Arduino IDE.
This software can be downlaoded from their official website arduino.cc
After installation it needs to be configured for the UNO which is the hardware for this project.
Once it is configured, we can directly code and flash the software to the microcontroller.


## Running the tests

Tests are done physically using the microcontroller.

In the next phase after the simulation, the circuit is implemented using Arduino UNO and breadboard. Due to lack of buzzer at this point of development I used LED to indicate the output.

The Arduino’s PWM pin 13 is connected to LED and pin 2 is connected to push button. It is coded in such a way that whenever button is pressed the LED glows. Which is the underlying principle for the fabric push button and actuation of buzzer.

### Break down into end to end tests

During the course of development, the tests can be broken down to many phases.
1. Simulation using Tinkercad.[Tinkercad](https://www.tinkercad.com/things/himwlsarHmG/)
2. Basic circuit using LED and Arduino.[PushButtonLED](https://github.com/anirudh-upadhya/InteractiveSystems2020/tree/master/tests/PushButtonLED/)
3. Pressure sensor sensitivity checks.
4. Fabric Push button and LED.
5. Fabric Push button and Buzzer.

### And coding style tests

The coding is done using embedded C language as we are using Arduino as microcontroller.

## Deployment

This project can be deployed in all hospitals. It can be integrated to their systems.

## Built With

* [Arduino](https://www.arduino.cc/en/Main/Software/) - The IDE for development used
* 

## Contributing

Please read [CONTRIBUTING.md](https://github.com/anirudh-upadhya/InteractiveSystems2020/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Anirudh Upadhya** - [anirudh-upadhya](https://github.com/anirudh-upadhya)

## License

This project is licensed under the Saarland University - see the [LICENSE.md](https://github.com/anirudh-upadhya/InteractiveSystems2020/blob/master/LICENSE.md) file for details

## Acknowledgments

* This project was inspired by the current Covid-19 situation around the world

