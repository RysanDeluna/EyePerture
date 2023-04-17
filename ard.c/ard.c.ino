// #include <Servo.h>
// #define MOTOR_X 12
// #define MOTOR_Y 13

#define MOTOR_X_ESQUERDA 12
#define MOTOR_X_DIREITA 13
#define MOTOR_Y_BAIXO 7
#define MOTOR_Y_CIMA 8

int quadrante;

void setup() {
  // put your setup code here, to run once:
  pinMode(MOTOR_X_ESQUERDA, OUTPUT);
  pinMode(MOTOR_Y_CIMA, OUTPUT);
  pinMode(MOTOR_X_DIREITA, OUTPUT);
  pinMode(MOTOR_Y_BAIXO, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    quadrante = Serial.read();
    printf("%d", quadrante);
    switch (quadrante)
    {
      case 1:
        // MOTOR_X.write(angulo_de_giro);
        // MOTOR_Y.write(angulo_de_giro);
        
        digitalWrite(MOTOR_X_ESQUERDA, HIGH);  // move primeiro para esquerda;
        Serial.println("ESQUERDA");
        delay(250); digitalWrite(MOTOR_X_ESQUERDA, LOW); // simula a situção de que o motor está realizando o movimento
        digitalWrite(MOTOR_Y_CIMA, HIGH); Serial.println("CIMA");
        delay(250); digitalWrite(MOTOR_Y_CIMA, LOW);
        break;
      case 2:
        digitalWrite(MOTOR_X_DIREITA, HIGH); Serial.println("DIREITA");
        delay(250); digitalWrite(MOTOR_X_DIREITA, LOW); 
        digitalWrite(MOTOR_Y_CIMA, HIGH); Serial.println("CIMA");
        delay(250); digitalWrite(MOTOR_Y_CIMA, LOW); 
        break;
      case 3:
        digitalWrite(MOTOR_X_ESQUERDA, HIGH); Serial.println("ESQUERDA");
        delay(250); digitalWrite(MOTOR_X_ESQUERDA, LOW);
        digitalWrite(MOTOR_Y_BAIXO, HIGH); Serial.println("BAIXO");
        delay(250); digitalWrite(MOTOR_Y_BAIXO, LOW); 
        break;
      case 4:
        digitalWrite(MOTOR_X_DIREITA, HIGH); Serial.println("DIREITA");
        delay(250); digitalWrite(MOTOR_X_DIREITA, LOW);
        digitalWrite(MOTOR_Y_BAIXO, HIGH); Serial.println("BAIXO");
        delay(250); digitalWrite(MOTOR_Y_BAIXO, LOW);
        break;
      default:
        break;
    }
  }
  quadrante = -1;
  delay(1000);  // a cada segundo será checado
}
