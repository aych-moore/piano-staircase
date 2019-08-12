// pins numbers
#define trigPin 2
byte echoPins[8] = {3,4,5,6,7,8,9,10};

byte mode = 0;

// defines variables
long duration;

int distances[8] = {0,0,0,0,0,0,0,0};

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  
  for(byte i = 0; i < 8; i++){
    pinMode(echoPins[i], INPUT); // Sets the echoPin as an Input
  }
  
  Serial.begin(9600); // Starts the serial communication
}

void loop() {
  for(byte echoPinNum = 0; echoPinNum < 8; echoPinNum++){
    digitalWrite(trigPin, LOW); // Clears the trigPin
    delayMicroseconds(2);
    
    digitalWrite(trigPin, HIGH); // Sets the trigPin on HIGH state for 10 micro seconds
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    distances[echoPinNum] = pulseIn(echoPins[echoPinNum], HIGH, 10000UL)*0.034/2; // Reads the echoPin, returns the sound wave travel time in microseconds then converts to distance

  }


  /* OUTPUT FORMAT:
   *     mode,distance,distance,distance,distance,distance,distance,distance
   *  eg 1,14,0,167,23,0,0,0,99
   *  mode: int 0, room for expansion eg 0-10 modes
   *  distance: int
   */

  Serial.print(String(mode));
  for(byte i = 0; i < 8; i++){
    Serial.print(',');
    Serial.print(distances[i]);
    
  }
  Serial.println();
}
