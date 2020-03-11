#include "exerciser.h"

void exercise(connection *C)
{
    query1(C, 1, 35, 40, 0, 0, 0, 0, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    query1(C, 0, 35, 40, 0, 0, 0, 1, 5, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    query1(C, 0, 35, 40, 1, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    query1(C, 0, 35, 40, 0, 0, 0, 0, 0, 0, 1, 0, 10, 0, 0, 0, 0, 0, 0);
    query1(C, 0, 35, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5, 0, 0, 0);
    query1(C, 0, 35, 40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5);
    query2(C, "Gold");
    query2(C, "NoExist");
    query3(C, "GeorgiaTech");
    query3(C, "NoExist");
    query4(C, "FL", "Gold");
    query4(C, "NC", "DarkBlue");
    query5(C, 12);
}
