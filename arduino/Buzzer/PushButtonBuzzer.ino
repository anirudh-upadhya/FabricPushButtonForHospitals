const int buttonPin = 2;     // the number of the pushbutton pin
const int buzzerPin =  13;      // the number of the Buzzer pin
int buttonState;            // variable for reading the pushbutton status


void setup() {
 // initialize the LED pin as an output:
//Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
pinMode(buzzerPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
 
buttonState = digitalRead(buttonPin);

if (buttonState == HIGH) {
    // turn buzzer on:
    digitalWrite(buzzerPin, HIGH);
    
  } else {
    // turn buzzer off:
    digitalWrite(buzzerPin, LOW);
  }
//Serial.print(buttonPin);
//Serial.print("\t");
}
