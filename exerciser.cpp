#include "exerciser.h"

void exercise(connection *C)
{
    add_state(C, "test_state");
    add_color(C, "test_color");
    add_team(C, "test_team", 0, 0, 0, 0);
    query1(C, 1, 10, 38, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    query1(C, 0, 10, 38, 1, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    query1(C, 0, 10, 38, 0, 0, 20, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    query1(C, 0, 10, 38, 0, 0, 20, 0, 0, 5, 1, 0, 5, 0, 0, 0, 0, 0, 0);
    query1(C, 0, 10, 38, 0, 0, 20, 0, 0, 5, 0, 0, 5, 1, 0, 5, 0, 0, 0);
    query1(C, 0, 10, 38, 0, 0, 20, 0, 0, 5, 0, 0, 5, 0, 0, 5, 1, 0, 5);
    query1(C, 0, 10, 38, 1, 0, 20, 0, 0, 5, 0, 0, 5, 0, 0, 5, 1, 0, 5);
    query1(C, 0, 10, 38, 0, 0, 20, 1, 0, 5, 0, 0, 5, 1, 0, 5, 1, 0, 5);
    add_player(C, 1, 1, "first_test", "last_test", 0, 0, 0, 0, 0, 3);
    query1(C, 0, 10, 38, 0, 0, 20, 1, 0, 5, 0, 0, 5, 1, 0, 5, 1, 0, 5);
    query1(C, 1, 10, 38, 1, 0, 20, 1, 0, 5, 1, 0, 5, 1, 0, 5, 1, 0, 5);
    query2(C, "Gold");
    query2(C, "Red");
    query2(C, "Green");
    query2(C, "NoExist");
    query3(C, "GeorgiaTech");
    query3(C, "NoExist");
    query4(C, "FL", "Gold");
    query4(C, "NC", "DarkBlue");
    query5(C, 12);
    query5(C, 10);
    query5(C, 50);
}
