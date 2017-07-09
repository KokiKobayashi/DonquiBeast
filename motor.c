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
#define AROUND 5

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
    struct timespec reqleft, reqright;

    left.front = 24;
    left.back = 23;
    right.front = 22;
    right.back = 21;

    reqleft.tv_sec = 0;
    reqleft.tv_nsec = 580000000;
    reqright.tv_sec = 0;
    reqright.tv_nsec = 579000000;

//printf("%d", decode(argv[1]));

    switch (atoi(argv[1])) {
    case STOP:
        printf("stop\n");
        Stop(left, right);
        break;
    case FORWARD:
        printf("front\n");
        MoveFront(left, right);
        sleep(5);
        Stop(left, right);
        break;
    case BACKWARD:
        printf("back\n");
        MoveBack(left, right);
        sleep(5);
        Stop(left, right);
        break;
    case LEFT:
        printf("turn left\n");
        TurnLeft(left, right);
        nanosleep(&reqleft, NULL);
        Stop(left, right);
        break;
    case RIGHT:
        printf("turn right\n");
        TurnRight(left, right);
        nanosleep(&reqright, NULL);
        Stop(left, right);
        break;
    case AROUND:
        printf("turn around\n");
        TurnRight(left, right);
        nanosleep(&reqright, NULL);
        nanosleep(&reqleft, NULL);
        Stop(left, right);
        break;
    default:
        printf("default\n");
        break;
    }

    return 0;
}

int decode (char *str) {
    if (str == "stop")
        return STOP;
    else if (str == "forward")
        return FORWARD;
    else if (str == "backward")
        return BACKWARD;
    else if (str == "left")
        return LEFT;
    else if (str == "right")
        return RIGHT;
    else
        return -1;
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
