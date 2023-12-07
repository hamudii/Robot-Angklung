int relay1 = 2; // Sesuaikan dengan pin yang Anda gunakan pada Arduino
int relay2 = 3;
int relay3 = 4;
int relay4 = 5;
int relay5 = 6;
int relay6 = 7;
int relay7 = 8;
int relay8 = 9;

void setup() {
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  pinMode(relay5, OUTPUT);
  pinMode(relay6, OUTPUT);
  pinMode(relay7, OUTPUT);
  pinMode(relay8, OUTPUT);
  Serial.begin(9600);
}

void SwitchON(int relay){
  for (int x = 0; x < 1;x++){
    digitalWrite(relay, HIGH); 
    delay(300); 
    digitalWrite(relay, LOW); 
    delay(300);
  }  
}

void loop() {
  // SwitchON(relay1);
  if (Serial.available()>0) {
    // String command = Serial.readStringUntil('\n');
    char command = Serial.read();
    // if(command == '10000\n'){
    //   SwitchON(relay1);
    // }else if(command == '11000'){
    //   SwitchON(relay2);
    // }else if(command == '11100'){
    //   SwitchON(relay3);
    // }else if(command == '11110'){
    //   SwitchON(relay4);
    // }else if(command == '11111'){
    //   SwitchON(relay5);
    // }else if(command == '01111'){
    //   SwitchON(relay6);
    // }else if(command == '00111'){
    //   SwitchON(relay7);
    // }else if(command == '00011'){
    //   SwitchON(relay8);
    // }else{} 
    if(command == '1'){
      SwitchON(relay1);
    }else if(command == '2'){
      SwitchON(relay2);
    }else if(command == '3'){
      SwitchON(relay3);
    }else if(command == '4'){
      SwitchON(relay4);
    }else if(command == '5'){
      SwitchON(relay5);
    }else if(command == '6'){
      SwitchON(relay6);
    }else if(command == '7'){
      SwitchON(relay7);
    }else if(command == '8'){
      SwitchON(relay8);
    }else{}     
  }

}


