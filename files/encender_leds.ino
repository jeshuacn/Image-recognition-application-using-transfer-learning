int ld1 = 8;
int ld2 = 7;
int option;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ld1,OUTPUT);
  pinMode(ld2,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    option = Serial.read();
    Serial.println(option);
    if( option == 'p'){
       digitalWrite(ld1,HIGH);
       digitalWrite(ld2,LOW);
  
    }
    if( option == 'n'){
      digitalWrite(ld1,LOW);
      digitalWrite(ld2,HIGH);
    }
    if( option == 'e'){
      digitalWrite(ld1,LOW);
      digitalWrite(ld2,LOW);
    }
  }
  
}
