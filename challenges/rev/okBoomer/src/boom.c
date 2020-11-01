// #AUTHOR : TINOTENDA SLY KUNESU

#include <stdio.h>
#include <stdlib.h>
#include "stages.h"
#include "setup.h"

FILE *infile;
char input_strings[80];

int main(int argc, char *argv[]){
    char *input = NULL;
     
    //File IO
    if (argc == 1){
        infile = stdin;
    }

    else if (argc == 2){
        infile = fopen(argv[1], "r");
        if (infile == NULL){
            printf("Error: Couldn't open given file");
            exit(8);
        }
    }
    else{
        printf("Successful open\n");
        exit(8);
    }//END FILE IO

    //secret bomb setup lol.
    bomb_setup();

    //JUST A BIT OF BANTER
    printf("GET READY TO SPECTACULARLY FAIL THE UPCOMING 4 STAGES!\n");
    printf("BUT FIRST WE START OF WITH AN EASY ONE\n");
    printf("\n\n");

    //STAGES START HERE
    //STAGE 1 --- WHAT IS MY PASSWORD AGAIN? GOOD LUCK.
    printf("WHAT IS MY PASSWORD?\n");
    input = reader();
    stage1(input);

    //SUCCESS FOR STAGE1
    printf("\n\n");
    printf("I SEE YOU SOLVED THAT ONE LETS IF YOU CAN GET THIS ONE\n");
    printf("ACTIVATING HARDER STAGE NOW\n");
    printf("\n\n");

    //STAGE 2 --- WHAT IS TO THE POWER AGAIN?
    printf("STAGE 2\n");
    printf("LETS SEE YOUR MATH SKILLS\n");
    printf("LETS SEE IF YOU CAN FIGURE OUT MY 3 NUMBER PASSCODE\n");
    input = reader();
    stage2(input);

    //SUCCESS FOR STAGE2
    printf("WELL WELL WELL, YOU'RE NOT TOO BAD AFTER ALL!\n");
    printf("THATS 2 DOWN 2 MORE TO GO!!!");
    printf("\n\n");

    //STAGE 3 --- LETS SEE IF YOU CAN SUSS OUT THE DECOYS MUAHAHAHAHA.
    printf("STAGE 3\n");
    printf("LETS SEE IF YOU CAN FIGURE OUT THE RIGHT COMBINATION OF 3 CHARACTERS THAN PRODUCE THE FLAG\n");
    input = reader();
    stage3(input);

    //SUCCESS FOR STAGE3
    printf("GREAT JOB, THAT'S 3/4 DOWN NOW\n");
    printf("KEEP GOING!");
    printf("\n\n");

    //STAGE 4 --- LETS SEE IF YOU CAN FIND MY ENCRYPTED PASSWORD HIDDEN IN SOME BUFFER OVERFLOW MUAHAHAHA
    printf("STAGE 4\n");
    printf("LETS SEE IF YOU CAN FIND MY ENCRYPTED PASSWORD HIDDEN IN SOME BUFFER OVERFLOW MUAHAHAHA\n");
    input = reader();
    stage4(input);

    //SUCCESS FOR STAGE4
    printf("WELL DONE THAT IS 4/4\n");
    printf("\n\n");

    //FINALISE BOMB DEFUSION
    printf("CONGRATULATIONS YOU HAVE .....\n");
    finish();
}