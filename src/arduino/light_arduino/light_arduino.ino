int light1 = 8;
int light2 = 9;
int light3 = 10;

void setup() {
  pinMode(light1, OUTPUT);
  pinMode(light2, OUTPUT);
  pinMode(light3, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(light1, HIGH);
    }
    else if (command == '2') {
      digitalWrite(light2, HIGH);
    }
    else if (command == '3') {
      digitalWrite(light3, HIGH);
    }
    else if (command == '4') {
      digitalWrite(light1, LOW);
    }
    else if (command == '5') {
      digitalWrite(light2, LOW);
    }
    else if (command == '6') {
      digitalWrite(light3, LOW);
    }
  }
}
