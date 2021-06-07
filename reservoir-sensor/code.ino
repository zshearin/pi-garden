const int trigPin = 9;
const int echoPin = 10;
const int delaySeconds = 5;
long duration;
int distance;

void setup() {

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration*0.034/2)/2.54;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" in.");
  //Delay delaySeconds seconds
  delay(delaySeconds*1000);
  
}

