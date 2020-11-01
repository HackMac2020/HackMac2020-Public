// #AUTHOR : TINOTENDA SLY KUNESU

#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>
#include <signal.h>

extern FILE *infile;
extern char input_strings[80];
char message[18];

static void sig_handler(int sig)
{
    (void)sig;
    printf("\nYOU THINK YOU CAN JUST CTRL-C ME, HAHA LETS SEE\n");
    sleep(3);
    printf("Well...\n");
    fflush(stdout);
    sleep(1);
    printf("YOU WIN THIS TIME, ILL GET YOU NEXT TIME\n");
    exit(18);
}

void bomb_setup(void)
{
    printf("SETUP SUCCESSFULLY COMPLETED, BOMB DETONATION IMMINENT!\n");
    signal(SIGINT, sig_handler);
}

int space_handler(char *tmpr)
{
    if (tmpr[0] == '\0')
    {
        return 1;
    }
    for (;;)
    {
        int c = *tmpr;
        tmpr++;
        if (isspace(c))
        {
            if (*tmpr == '\0')
            {
                return 1;
            }
        }
        else
        {
            return 0;
        }
    }
}

char *jump(void)
{

    char *tmp = fgets(input_strings, 50, infile);

    do
    {
        if (tmp == NULL)
        {
            break;
        }
    } while (space_handler(tmp));
    return tmp;
}

void BOOOM(void)
{
    printf("\n !!!BOOM BOOM POW!!!\n");
    printf("TRY HARDER OR JUST QUIT\n");
    exit(8);
}

char *reader(void)
{
    char *input;

    input = jump();

    if (input == NULL)
    {
        if (infile == stdin)
        {
            printf("Error: Premature EOF on stdin\n");
            BOOOM();
        }

        infile = stdin;
        input = jump();
        if (input == NULL)
        {
            printf("Error: Premature EOF on stdin\n");
            BOOOM();
        }
    }
    size_t strlength = strlen(input) + 1;
    if (strlength >= 0x31)
    {
        printf("Error: Input line too long\n");
        BOOOM();
    }
    return input;
}

int string_length(char *Str)
{
    int length;
    char *ptr;

    ptr = Str;
    length = 0;

    while (*ptr != 0 && *ptr != 0x0a)
    {
        length++;
        ptr++;
    }
    return length;
}

int strings_not_equal(char *s1, char *s2)
{
    char *p, *q;

    if (string_length(s1) != string_length(s2))
    {
        return 1;
    }

    p = s1;
    q = s2;

    while (*p != 0)
    {
        if (*p != *q)
            return 1;
        p++;
        q++;
    }
    return 0;
}

void stage2_helper(char *input, int *stage2_input)
{
    int stage2_nums_read = sscanf(input, "%d %d %d", &stage2_input[0], &stage2_input[1], &stage2_input[2]);
    if (stage2_nums_read != 3)
    {
        BOOOM();
    }
}

void *cc(void)
{

    char ch;
    int key = 5;
    strcpy(message, "mrKunesu's_work!\n");

    for (int i = 0; message[i] != '\n'; ++i)
    {
        ch = message[i];

        if (ch >= 'a' && ch <= 'z')
        {
            ch = ch + key;

            if (ch > 'z')
            {
                ch = ch - 'z' + 'a' - 1;
            }

            message[i] = ch;
        }
        else if (ch >= 'A' && ch <= 'Z')
        {
            ch = ch + key;

            if (ch > 'Z')
            {
                ch = ch - 'Z' + 'A' - 1;
            }

            message[i] = ch;
        }
    }
}

void secret_stage()
{ //Secret Stage hidden in setup
    char *input;

    printf("\n\n");
    printf("CONGRATULATIONS, YOU HAVE FOUND THE SECRET HIDDEN STAGE\n");
    printf("HOWEVER, FINDING AND SOLVING IT ARE TWO DIFFERERENT THINGS\n");
    printf("LETS SEE IF YOU CAN SOLVE IT AND FINALLY DEFUSE THE BOMB\n");
    printf("WHAT IS MY ENCRYPTED PASSPHRASE?\n");
    printf("\n\n");
    sleep(3);
    input = reader();
    cc();

    if (strings_not_equal(input, message) != 0)
    {
        printf("\n\n");
        printf("THAT IS INCORRECT, MAYBE QUIT WHILE YOU ARE AHEAD!\n");
        BOOOM();
    }
    else
    {
        printf("\n\n");
        printf("CONGRATULATIONS, YOU BEASTED THROUGH THIS CTF CHALLENGE!\n");
        printf("!!!BOMB HAS BEEN SUCESSFULLY DETONATED!!!\n");
        sleep(3);
        exit(18);
    }
}

void finish()
{

    sleep(3);
    printf("\n\n");
    printf("BUT WAIT...\n");
    sleep(2);
    printf("AREN'T YOU MISSING SOMETHING ELSE??\n");
    sleep(2);
    printf("MAYBE A SECRET HIDDEN STAGE MUAHAHAHAHAHAHA\n");
    sleep(1);
    printf("SECRETCODE NEEDED TO ACCESS SECRET STAGE\n");
    sleep(1);
    printf("ENTER SECRETCODE NOW!!\n");
    printf("\n\n");

    char *input = reader();

    if (strings_not_equal(input, "01-04-1998\n") == 0)
    {
        secret_stage();
    }
    else
    {
        printf("ERROR!, WRONG PASSCODE\n");
        printf("BOMB IS EXITING!!!\n");
        sleep(3);
        exit(18);
    }
}