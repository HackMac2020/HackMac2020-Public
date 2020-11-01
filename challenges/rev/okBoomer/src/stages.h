// #AUTHOR : TINOTENDA SLY KUNESU

#pragma once
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "setup.h"

char *scode;

void stage1(char *input)
{

    char *str = ("VAr2T9Zn%X6h3&2E-but-is this strong enough??\n");
    char *defaul_t = ("COVID-2020_is_coming\n");

    if (strings_not_equal(input, defaul_t) == 0)
    {
        scode = "01-04-1998\n";
        printf("Hmmmmm MAYBE WRITE THIS DOWN FOR NOW, YOU MIGHT NEED IT LATER ON MUAHAHAHA: %s\n", scode);
        sleep(5);

        printf("WHAT IS MY PASSWORD AGAIN?\n");
        input = reader();

        if (strings_not_equal(input, str) != 0)
        {
            BOOOM();
        }
    }
    else if (strings_not_equal(input, str) != 0)
    {
        BOOOM();
    }
}

void stage2(char *input)
{
    int stage2_input[3];
    int i;
    int calc;

    stage2_helper(input, stage2_input);
    if (stage2_input[0] != 19)
    {
        printf("First Input is wrong lad/lass lol, need to remove this to make it harder haha\n");
        BOOOM();
    }

    for (i = 1; i < 4; ++i)
    {
        calc = pow(i, i) * 19;

        if (stage2_input[i - 1] != calc)
        {
            printf("input number %d is wrong lad/lass lol, need to remove this to make it harder haha\n", i);
            BOOOM();
        }
    }
}

void stage3(char *input)
{
    int a, c, d = 0;
    char b;

    ssize_t read = sscanf(input, "%d %c %d", &a, &b, &c);
    if (read != 3)
    {
        BOOOM();
    }

    if (a > 4 || a < 0)
    {
        BOOOM();
    }

    switch (a)
    {
    case 0:
        d = 0x67A;
        if (b != 'c')
        {
            BOOOM();
        }
        break;
    case 2:
        d = 0xfff;
        if (b != '<')
        {
            BOOOM();
        }
        break;
    case 3:
        d = 0b1111111111;
        if (b != '@')
        {
            BOOOM();
        }
        break;
    case 4:
        d = 0b10110101010;
        if (b != '.')
        {
            BOOOM();
        }
        break;
    default:
        BOOOM();
    }
    if (c != d)
    {
        BOOOM();
    }

    if (a != 3)
    {
        printf("HAHAHA WELL TRIED, YOU STILL HAVEN'T FOUND THE FLAG THOUGH!\n");
        printf("TRY AGAIN\n");
        printf("IM GOING TO EXPLODE NOW\n");
        sleep(4);
        BOOOM();
    }
}

void stage4(char *input)
{
    char buf[9];

    if (string_length(input) != 8)
    {
        BOOOM();
    }

    for (int i = 0; i < 8; i++)
    {
        if (i < 4)
        {
            buf[i] = "esupvmaZQs g!i\n"[input[i] & 0xa];
        }
        else
        {
            buf[i] = "opevas mQuig!Z\n"[input[i] & 0x5];
        }
    }
    buf[8] = ('\0');

    if (strings_not_equal(buf, "Que paso") != 0)
    {
        printf("buf: ");
        printf("%s", buf);
        BOOOM();
    }
}
