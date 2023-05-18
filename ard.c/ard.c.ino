#include <Servo.h>
#define MOTOR_X_PORT 12
#define MOTOR_Y_PORT 13

//#define MOTOR_X_ESQUERDA 12
//#define MOTOR_X_DIREITA 13
//#define MOTOR_Y_BAIXO 7
//#define MOTOR_Y_CIMA 8
 
int quadrante;
char rc[2] = {'0','\0'};
Servo motor_x, motor_y;
int angulo_x, angulo_y;

void setup() {
  // put your setup code here, to run once:
  angulo_x = 0; angulo_y = 0;
  
  motor_x.attach(MOTOR_X_PORT);
  motor_y.attach(MOTOR_Y_PORT);
  
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0)
  {
    rc[0] = Serial.read();
    quadrante = atoi(rc);
    switch (quadrante)
    {
      case 1:
        angulo_x = angulo_x - 10;
        motor_x.write(angulo_x);
          Serial.println("ESQUERDA");
        angulo_y = angulo_y + 10;
        motor_y.write(angulo_y);
          Serial.println("CIMA");
        break;
      case 2:
        angulo_x = angulo_x + 10;
        motor_x.write(angulo_x);
        angulo_y = angulo_y + 10;
        motor_y.write(angulo_y);
        break;
      case 3:
        angulo_x = angulo_x + 10;
        motor_x.write(angulo_x);
        angulo_y = angulo_y - 10;
        motor_y.write(angulo_y);
        break;
      case 4:
        angulo_x = angulo_x - 10;
        motor_x.write(angulo_x);
        angulo_y = angulo_y - 10;
        motor_y.write(angulo_y);
        break;
      default:
        break;
    }
  }
  else Serial.println("Fail");
  quadrante = -1;
  delay(500);  // a cada segundo será checado
}
