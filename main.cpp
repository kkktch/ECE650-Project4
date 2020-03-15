#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <pqxx/pqxx>

#include "query_funcs.h"
#include "exerciser.h"

using namespace std;
using namespace pqxx;

vector<string> split(string input)
{
  vector<string> ans;
  string str = input;
  while (str.find(" ") != string::npos)
  {
    int found = str.find(" ");
    ans.push_back(str.substr(0, found));
    str = str.substr(found + 1);
  }
  ans.push_back(str);
  return ans;
}

string CreatePlayer()
{
  string ans = "CREATE TABLE PLAYER (​"
               "PLAYER_ID   SERIAL PRIMARY KEY  NOT NULL,"
               "TEAM_ID     INT                 NOT NULL,"
               "UNIFORM_NUM INT                 NOT NULL,"
               "FIRST_NAME  VARCHAR(256)        NOT NULL,"
               "LAST_NAME   VARCHAR(256)        NOT NULL,"
               "MPG         INT                 NOT NULL,"
               "PPG         INT                 NOT NULL,"
               "RPG         INT                 NOT NULL,"
               "APG         INT                 NOT NULL,"
               "SPG         DOUBLE PRECISION    NOT NULL,"
               "BPG         DOUBLE PRECISION    NOT NULL,"
               "FOREIGN KEY (TEAM_ID) REFERENCES TEAM(TEAM_ID) ON DELETE SET NULL ON UPDATE CASCADE);";
  return ans;
}

string CreateTeam()
{
  string ans = "CREATE TABLE TEAM ("
               "TEAM_ID   SERIAL PRIMARY KEY  NOT NULL,"
               "NAME      VARCHAR(256)        NOT NULL,"
               "STATE_ID  INT                 NOT NULL,"
               "COLOR_ID  INT                 NOT NULL,"
               "WINS      INT                 NOT NULL,"
               "LOSSES    INT                 NOT NULL,"
               "FOREIGN KEY (STATE_ID) REFERENCES STATE(STATE_ID) ON DELETE SET NULL ON UPDATE CASCADE,"
               "FOREIGN KEY (COLOR_ID) REFERENCES COLOR(COLOR_ID) ON DELETE SET NULL ON UPDATE CASCADE);";
  return ans;
}

string CreateState()
{
  string ans = "CREATE TABLE STATE ("
               "STATE_ID SERIAL PRIMARY KEY NOT NULL,"
               "NAME     VARCHAR(256)       NOT NULL);";
  return ans;
}

string CreateColor()
{
  string ans = "CREATE TABLE COLOR ("
               "COLOR_ID SERIAL PRIMARY KEY NOT NULL,"
               "NAME     VARCHAR(256)       NOT NULL);";
  return ans;
}

void initColor(connection *C)
{
  work W(*C);
  string sql = CreateColor();
  W.exec(sql);
  W.commit();

  int id;
  string content;
  ifstream read_file;
  read_file.open("color.txt", ios::binary);
  while (getline(read_file, content))
  {
    vector<string> contents = split(content);
    add_color(C, contents[1]);
  }
  read_file.close();
}

void initState(connection *C)
{
  work W(*C);
  string sql = CreateState();
  W.exec(sql);
  W.commit();

  int id;
  string content;
  ifstream read_file;
  read_file.open("state.txt", ios::binary);
  while (getline(read_file, content))
  {
    vector<string> contents = split(content);
    add_state(C, contents[1]);
  }
  read_file.close();
}

void initTeam(connection *C)
{
  work W(*C);
  string sql = CreateTeam();
  W.exec(sql);
  W.commit();

  string content;
  ifstream read_file;
  read_file.open("team.txt", ios::binary);
  while (getline(read_file, content))
  {
    vector<string> contents = split(content);
    add_team(C, contents[1], stoi(contents[2]), stoi(contents[3]), stoi(contents[4]), stoi(contents[5]));
  }
  read_file.close();
}

void initPlayer(connection *C)
{
  work W(*C);
  string sql = CreatePlayer();
  W.exec(sql);
  W.commit();

  string content;
  ifstream read_file;
  read_file.open("player.txt", ios::binary);
  while (getline(read_file, content))
  {
    vector<string> contents = split(content);
    add_player(C, stoi(contents[1]), stoi(contents[2]), contents[3], contents[4], stoi(contents[5]), stoi(contents[6]), stoi(contents[7]), stoi(contents[8]), stod(contents[9]), stod(contents[10]));
  }
  read_file.close();
}

int main(int argc, char *argv[])
{
  try
  {
    connection *C = new connection("dbname=ACC_BBALL user=postgres password=passw0rd hostaddr = 127.0.0.1 port = 5432");
    if (C->is_open())
    {
      work Drop(*C);
      string dropCMD = "DROP TABLE IF EXISTS player, team, state, color CASCADE;";
      Drop.exec(dropCMD);
      Drop.commit();
      initColor(C);
      initState(C);
      initTeam(C);
      initPlayer(C);
      //Close database connection
      C->disconnect();
      exercise(C);
    }
    else
    {
      return 1;
    }
  }
  catch (const std::exception &e)
  {
    cerr << e.what() << std::endl;
    return 1;
  }

  return 0;
}
