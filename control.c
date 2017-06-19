#include <stdio.h>
#include <stdlib.h>

#include <time.h>
#include <sys/time.h>

#include <wiringPi.h>

#define STOP 0
#define FORWARD 1
#define BACKWARD 2
#define LEFT 3
#define RIGHT 4

typedef struct gp{
    int front;
    int back;
} gpio;


int main (int argc, char *argv[]) {
    if (argc < 2){
        puts("error");
        return -1;
    }

    gpio left, right;

    left.front = 21;
    left.back = 22;
    right.front = 23;
    right.back = 24;

    switch (atoi(argv[1])) {
    case STOP:
        printf("stop\n");
        Stop(left, right);
        break;
    case FORWARD:
        printf("front\n");
        MoveFront(left, right);
        break;
    case BACKWARD:
        printf("back\n");
        MoveBack(left, right);
        break;
    case LEFT:
        printf("turn left\n");
        TurnLeft(left, right);
        break;
    case RIGHT:
        printf("turn right\n");
        TurnRight(left, right);
        break;
    default:
        printf("default\n");
        break;
    }

    return 0;
}


// pinMode( wiringPi#, OUTPUT );
// digitalWrite( wiringPi#, 0/1 );
int Stop (gpio left, gpio right) {
    if (wiringPiSetup() == -1)
        return -1;

    pinMode(left.front, OUTPUT);
    digitalWrite(left.front, 0);
    pinMode(left.back, OUTPUT);
    digitalWrite(left.back, 0);
    pinMode(right.front, OUTPUT);
    digitalWrite(right.front, 0);
    pinMode(right.back, OUTPUT);
    digitalWrite(right.back, 0);

    return 0;
}

int MoveFront(gpio left, gpio right) {
    if (wiringPiSetup() == -1)
        return -1;

    pinMode(left.front, OUTPUT);
    digitalWrite(left.front, 1);
    pinMode(left.back, OUTPUT);
    digitalWrite(left.back, 0);
    pinMode(right.front, OUTPUT);
    digitalWrite(right.front, 1);
    pinMode(right.back, OUTPUT);
    digitalWrite(right.back, 0);

    return 0;
}

int MoveBack(gpio left, gpio right) {
    if (wiringPiSetup() == -1)
        return -1;

    pinMode(left.front, OUTPUT);
    digitalWrite(left.front, 0);
    pinMode(left.back, OUTPUT);
    digitalWrite(left.back, 1);
    pinMode(right.front, OUTPUT);
    digitalWrite(right.front, 0);
    pinMode(right.back, OUTPUT);
    digitalWrite(right.back, 1);

    return 0;
}

int TurnLeft(gpio left, gpio right) {
    if (wiringPiSetup() == -1)
        return -1;

    pinMode(left.front, OUTPUT);
    digitalWrite(left.front, 0);
    pinMode(left.back, OUTPUT);
    digitalWrite(left.back, 1);
    pinMode(right.front, OUTPUT);
    digitalWrite(right.front, 1);
    pinMode(right.back, OUTPUT);
    digitalWrite(right.back, 0);

    return 0;
}

int TurnRight(gpio left, gpio right) {
    if (wiringPiSetup() == -1)
        return -1;

    pinMode(left.front, OUTPUT);
    digitalWrite(left.front, 1);
    pinMode(left.back, OUTPUT);
    digitalWrite(left.back, 0);
    pinMode(right.front, OUTPUT);
    digitalWrite(right.front, 0);
    pinMode(right.back, OUTPUT);
    digitalWrite(right.back, 1);

    return 0;
}
