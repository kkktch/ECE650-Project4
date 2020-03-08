#include <iostream>
#include <string>
#include <pqxx/pqxx>

//#include "exerciser.h"

using namespace std;
using namespace pqxx;

std::string CreatePlayer() {
    std::string ans = "CREATE TABLE PLAYER (​" \
                      "PLAYER_ID   INT         NOT NULL," \
                      "TEAM_ID     INT         NOT NULL," \
                      "UNIFORM_NUM INT         NOT NULL," \
                      "FIRST_NAME  VARCHAR(20) NOT NULL," \
                      "LAST_NAME   VARCHAR(20) NOT NULL," \
                      "MPG         INT," \
                      "PPG         INT," \
                      "RPG         INT," \
                      "APG         INT," \
                      "SPG         DOUBLE," \
                      "BPG         DOUBLE," \
                      "PRIMARY KEY (PLAYER_ID));";
    return ans;
}

std::string CreateTeam() {
    std::string ans = "CREATE TABLE TEAM (​" \
                      "TEAM_ID   INT          NOT NULL," \
                      "NAME      VARCHAR(128) NOT NULL," \
                      "STATE_ID  INT          NOT NULL," \
                      "COLOR_ID  INT          NOT NULL," \
                      "WINS      INT          NOT NULL," \
                      "LOSSES    INT          NOT NULL," \
                      "PRIMARY KEY (TEAM_ID));";
    return ans;
}

std::string CreateState() {
    std::string ans = "CREATE TABLE STATE (​" \
                      "STATE_ID  INT          NOT NULL," \
                      "NAME      VARCHAR(2)   NOT NULL," \
                      "PRIMARY KEY (STATE_ID));";
    return ans;
}

std::string CreateColor() {
    std::string ans = "CREATE TABLE COLOR (" \
                      "COLOR_ID  INT          NOT NULL," \
                      "NAME      VARCHAR(20)  NOT NULL," \
                      "PRIMARY KEY (COLOR_ID));"
    return ans;
    
}

int main (int argc, char *argv[])
{

  //Allocate & initialize a Postgres connection object
  connection *C;

  try{
    //Establish a connection to the database
    //Parameters: database name, user name, user password
    C = new connection("dbname=ACC_BBALL user=postgres password=abc123");
    if (C->is_open()) {
      cout << "Opened database successfully: " << C->dbname() << endl;
        work W(C);
        std::string sql = CreatePlayer();
        W.exec(sql);
        W.commit();
    } else {
      cout << "Can't open database" << endl;
      return 1;
    }
  } catch (const std::exception &e){
    cerr << e.what() << std::endl;
    return 1;
  }


  //TODO: create PLAYER, TEAM, STATE, and COLOR tables in the ACC_BBALL database
  //      load each table with rows from the provided source txt files


  exercise(C);


  //Close database connection
  C->disconnect();

  return 0;
}


