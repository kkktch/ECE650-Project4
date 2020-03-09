#include "exerciser.h"

void exercise(connection *C)
{
    query2(C, "Gold");
    query2(C, "NoExist");
}
