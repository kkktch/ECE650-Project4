#include "exerciser.h"

void exercise(connection *C)
{
    query2(C, "Gold");
    query2(C, "NoExist");
    query3(C, "GeorgiaTech");
    query3(C, "NoExist");
}
