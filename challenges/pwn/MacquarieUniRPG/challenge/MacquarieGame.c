#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
struct staff
{
    void (*PrintStaff)(struct staff *);
    char boolean;
    char health;
    char damage;
    char regen;
};
struct player
{
    void (*PrintPlayer)(struct player *);
    char boolean;
    char health;
    char mana;
};
int GetChoice()
{
    int choice;
    scanf("%d", &choice);
    return choice;
}
void PrintPlayerInfo(struct player *p)
{
    if (p->boolean == 0)
    {
        printf("[ A+ Student ] %d HP / %d Mana\n", p->health, p->mana);
    }
    else
    {
        printf("[ F- Student ] %d HP / %d Mana\n", p->health, p->mana);
    }
}
void PrintStaffInfo(struct staff *a)
{
    if (a->boolean == 0)
    {
        printf("[ Lesley Legend ] %d HP / %d Damage / +%d Life Regeneration.\n", a->health, a->damage, a->regen);
    }
    else
    {
        printf("[ Brucy Boi ] %d HP / %d Damage / +%d Life Regeneration.\n", a->health, a->damage, a->regen);
    }
}
int FMinusStudentAttack(struct player *p, struct staff *d)
{
    int AttChoice;
    do
    {
        d->PrintStaff(d);
        p->PrintPlayer(p);
        puts("\t[ 1 ] Contest Grades [ Cost : 10 MP ]\n\t\tDeals 20 Damage.\n\t[ 2 ] Hit the UBAR [ Cost : 0 MP]\n\t\tRefreses All Mana.\n\t[ 3 ] Submit a Complaint to HR [ Cost : 25 MP]\n\t\tYou Become Temporarily Invincible.");
        AttChoice = GetChoice();
        switch (AttChoice)
        {
        case 1:
            if (p->mana <= 9)
            {
                puts("Not Enough Mana!\n");
            }
            else
            {
                printf("Contest Grades deals %d damage to the Staff member!\n", 20);
                d->health -= 20;
                p->mana -= 10;
                printf("But the Staff member deals %d damage to your self esteem!\n", d->damage);
                p->health -= d->damage;
                printf("And the staff member regenerates %d HP!\n", d->regen);
                d->health += d->regen;
            }
            break;
        case 2:
            puts("That beer sure hit the spot! Your Mana Has Been Refreshed");
            p->mana = 50;
            printf("But the staff deal %d damage to your future career options!\n", d->damage);
            p->health -= d->damage;
            printf("The staff are envigorated by your tears and heal %d HP!\n", d->regen);
            d->health += d->regen;
            break;
        case 3:
            if (p->mana <= 24)
            {
                puts("Not Enough Mana!");
            }
            else
            {
                puts("Complaint submitted! You Are Temporarily Invincible...");
                p->mana -= 25;
                printf("But the Staff Member Heals %d HP!\n", d->regen);
                d->health += d->regen;
            }
            break;
        }
        if (p->health <= 0)
        {
            free(d);
            return 0;
        }
    } while (d->health > 0);
    free(d);
    return 1;
}
int APlusStudentAttack(struct player *p, struct staff *d)
{
    int AttChoice;
    do
    {
        d->PrintStaff(d);
        p->PrintPlayer(p);
        puts("\t[ 1 ] Revise Responsibly!\n\t\tDeals 20 Damage.\n\t[ 2 ] Pull 5 Consecutive All Nighters!\n\t\tDeals 40 Damage, But You Lose 20 HP");
        AttChoice = GetChoice();
        switch (AttChoice)
        {
        case 1:
            printf("Your revision deals %d damage to the staff member!\n", 20);
            d->health -= 20;
            printf("But the Staff Member deals %d damage to you!\n", d->damage);
            p->health -= d->damage;
            printf("And The Staff Member Heals %d HP!\n", d->regen);
            d->health += d->regen;
            break;
        case 2:
            printf("The all nighters deal %d damage the staff!\nBut you also lose %d HP...\n", 40, 20);
            d->health -= 40;
            p->health -= 20;
            printf("But The Staff Member deals %d damage to you!\n", d->damage);
            p->health -= d->damage;
            printf("And the Staff Member heals %d HP\n", d->regen);
            d->health += d->regen;
            break;
        }
        if (p->health <= 0)
        {
            free(d);
            return 0;
        }
    } while (d->health > 0);
    free(d);
    return 1;
}
void StaffFight(int a)
{
    void *v2;
    struct staff *Staff = malloc(sizeof(struct staff));
    struct player *Player = malloc(sizeof(struct player));
    printf("You have arrived Macquarie University\n");
    static int c;
    int v3;
    if (c & 1)
    {

        Staff->boolean = 1;
        Staff->health = 80;
        Staff->damage = 10;
        Staff->regen = 4;
        Staff->PrintStaff = &PrintStaffInfo;
        puts("The Chancellor himself has descended from the heavens! Bruce Dowton stares you down!");
    }
    else
    {
        Staff->boolean = 0;
        Staff->health = 50;
        Staff->damage = 30;
        Staff->regen = 5;
        Staff->PrintStaff = &PrintStaffInfo;
        puts("The legendary lecturer Les Bell has appeared! This is going to be a tough semester!");
    }
    if (a == 1)
    {
        Player->boolean = 1;
        Player->health = 42;
        Player->mana = 50;
        Player->PrintPlayer = &PrintPlayerInfo;
        v3 = FMinusStudentAttack(Player, Staff);
    }
    else
    {
        Player->boolean = 0;
        Player->health = 50;
        Player->mana = 0;
        Player->PrintPlayer = &PrintPlayerInfo;
        v3 = APlusStudentAttack(Player, Staff);
    }
    if (v3)
    {
        puts("Well Done! You defeated the Uni's toughest!");
        puts("The World Will Remember you!:");
        v2 = malloc(sizeof(struct staff));
        scanf("%16s", v2);
        puts("And the boss you have defeated was called: ");
        Staff->PrintStaff(Staff);
    }
    else
    {
        puts("You Have Been Defeated!");
    }
    free(Player);
    c++;
}

unsigned int SecretLevel()
{
    // char s1[10];
    // printf("Welcome to Secret Level\nInput Password: ");
    // scanf("%10s", &s1);
    // if (strcmp(s1, "Super Strong Password That You can never guess"))
    // {
    //     puts("Wrong!\n");
    //     exit(-1);
    // }
    system("/bin/sh");
    return 0;
}

int PlayGame()
{
    int result;
    while (1)
    {
        while (1)
        {
            puts("What kind of student would you be ?\n[ 1 ] F- Student\n[ 2 ] A+ Student");
            result = GetChoice();
            if (result != 1 && result != 2)
                break;
            StaffFight(result);
        }
        if (result != 3)
            break;
    }

    return result;
}
int main()
{
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);

    puts("Welcome to Macquarie, Naive Student. Fight for your GRADES!");
    PlayGame();
    return 0;
}
