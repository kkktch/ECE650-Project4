#include <iostream>
#include <string>
#include <pqxx/pqxx>

//#include "exerciser.h"

using namespace std;
using namespace pqxx;

string CreatePlayer() {
    std::string ans = "CREATE TABLE PLAYER (​" \
                      "PLAYER_ID INT PRIMARY KEY  NOT NULL," \
                      "TEAM_ID     INT            NOT NULL," \
                      "UNIFORM_NUM INT            NOT NULL," \
                      "FIRST_NAME  VARCHAR(20)    NOT NULL," \
                      "LAST_NAME   VARCHAR(20)    NOT NULL," \
                      "MPG         INT," \
                      "PPG         INT," \
                      "RPG         INT," \
                      "APG         INT," \
                      "SPG         DOUBLE PRECISION," \
                      "BPG         DOUBLE PRECISION);";
    return ans;
}

string CreateTeam() {
    std::string ans = "CREATE TABLE TEAM (​" \
                      "TEAM_ID INT PRIMARY KEY  NOT NULL," \
                      "NAME      VARCHAR(128) NOT NULL," \
                      "STATE_ID  INT          NOT NULL," \
                      "COLOR_ID  INT          NOT NULL," \
                      "WINS      INT          NOT NULL," \
                      "LOSSES    INT          NOT NULL);";
    return ans;
}

string CreateState() {
    std::string ans = "CREATE TABLE STATE (​" \
                      "STATE_ID INT PRIMARY KEY NOT NULL," \
                      "NAME      VARCHAR(2)   NOT NULL);";
    return ans;
}

string CreateColor() {
    std::string ans = "CREATE TABLE COLOR (" \
                      "COLOR_ID INT PRIMARY KEY NOT NULL," \
                      "NAME      VARCHAR(20)  NOT NULL);";
    return ans;
    
}

void ReCreateDB() {
  connection *temp = = new connection("dbname=postgres user=postgres password=passw0rd hostaddr = 127.0.0.1 port = 5432");
  if (temp->is_open()) {
    pqxx::nontransaction W_t(*temp);
    string recreate = "drop database if exists \"ACC_BBALL\";";
    W_t.exec(recreate);
    recreate = "create database \"ACC_BBALL\";";
    W_t.exec(recreate);
    W_t.commit();
    temp->disconnect();
  } else {
    cerr << "Fail to connect to database\n";
    return;
  }
}

int main (int argc, char *argv[])
{


  try{
    //Establish a connection to the database
    //Parameters: database name, user name, user password

      //Allocate & initialize a Postgres connection object
    ReCreateDB();
    connection *C = new connection("dbname=ACC_BBALL user=postgres password=passw0rd hostaddr = 127.0.0.1 port = 5432");
    if (C->is_open()) {
      cout << "Opened database successfully: " << C->dbname() << endl;
        work W(*C);
        string dropCMD = "DROP TABLE IF EXISTS player, team, state, color;";
        W.exec(dropCMD);
        string sql = CreatePlayer();
        W.exec(sql);
        sql = CreateTeam();
        W.exec(sql);
        sql = CreateColor();
        W.exec(sql);
        sql = CreateState();
        W.exec(sql);
        W.commit();
        //Close database connection
        C->disconnect();
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


  //exercise(C);



  return 0;
}


